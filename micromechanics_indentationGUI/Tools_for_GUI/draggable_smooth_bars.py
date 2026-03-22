import numpy as np
import matplotlib.pyplot as plt


class DraggableSmoothBars:
    """Interactive draggable bar plot that can be embedded into an existing canvas."""

    def __init__(self, ax=None, n_bars=20, initial_height=5.0, influence_width=1.8,
                 x_values=None, heights=None, title=None, x_label=None, y_label=None):
        self.influence_width = influence_width
        self.dragging_index = None
        self.press_y = None
        self.heights_at_press = None
        self._cid_press = None
        self._cid_release = None
        self._cid_motion = None

        if x_values is None:
            self.x = np.arange(n_bars, dtype=float)
        else:
            self.x = np.asarray(x_values, dtype=float)
        if heights is None:
            self.heights = np.full(len(self.x), initial_height, dtype=float)
        else:
            self.heights = np.asarray(heights, dtype=float).copy()
        self.original_heights = self.heights.copy()
        self.n_bars = len(self.x)

        if ax is None:
            self.fig, self.ax = plt.subplots(figsize=(12, 6))
        else:
            self.ax = ax
            self.fig = ax.figure
            self.ax.cla()

        self.canvas = self.fig.canvas
        self.bar_width = self._compute_bar_width()
        self.bars = self.ax.bar(self.x, self.heights, width=self.bar_width, alpha=0.55, color='tab:blue')
        self.original_points, = self.ax.plot(
            self.x, self.original_heights, 'o', markersize=5,
            markerfacecolor='none', markeredgecolor='0.35', linestyle='None',
            label='original w'
        )
        self.points, = self.ax.plot(self.x, self.heights, 'o', markersize=6, color='tab:blue', label='dragged w')
        self.curve = None

        self.ax.set_title(title or 'Interactive weights for TAF fitting')
        self.ax.set_xlabel(x_label or 'Bar index')
        self.ax.set_ylabel(y_label or 'Value')
        self.ax.legend()
        self._set_x_limits()
        self.ax.set_ylim(0, max(1.0, np.max(self.heights) * 1.25))
        self.original_xlim = self.ax.get_xlim()
        self.original_ylim = self.ax.get_ylim()

        self.update_plot(preserve_limits=False)
        self._connect_events()

    def _compute_bar_width(self):
        if len(self.x) <= 1:
            return 0.8
        unique_x = np.unique(np.sort(self.x))
        if len(unique_x) <= 1:
            return 0.8
        return np.min(np.diff(unique_x)) * 0.8

    def _set_x_limits(self):
        if len(self.x) <= 1:
            self.ax.set_xlim(self.x[0] - 0.5, self.x[0] + 0.5)
            return
        margin = self.bar_width * 0.75
        self.ax.set_xlim(np.min(self.x) - margin, np.max(self.x) + margin)

    def _connect_events(self):
        self._cid_press = self.canvas.mpl_connect('button_press_event', self.on_press)
        self._cid_release = self.canvas.mpl_connect('button_release_event', self.on_release)
        self._cid_motion = self.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def disconnect(self):
        for cid in (self._cid_press, self._cid_release, self._cid_motion):
            if cid is not None:
                self.canvas.mpl_disconnect(cid)

    def neighbor_weights(self, center_index):
        dist = self.x - self.x[center_index]
        w = np.exp(-(dist ** 2) / (2 * self.influence_width ** 2))
        w[center_index] = 1.0
        return w

    def update_plot(self, preserve_limits=True):
        current_xlim = self.ax.get_xlim()
        current_ylim = self.ax.get_ylim()

        for rect, height in zip(self.bars, self.heights):
            rect.set_height(height)

        self.original_points.set_data(self.x, self.original_heights)
        self.points.set_data(self.x, self.heights)

        if preserve_limits:
            self.ax.set_xlim(current_xlim)
            self.ax.set_ylim(current_ylim)
        else:
            self._set_x_limits()
            ymax = max(1.0, np.max(np.maximum(self.heights, self.original_heights)) * 1.25)
            self.ax.set_ylim(0, ymax)
            self.original_xlim = self.ax.get_xlim()
            self.original_ylim = self.ax.get_ylim()
        self.canvas.draw_idle()

    def get_closest_point(self, event, max_pixel_distance=12):
        if event.xdata is None or event.ydata is None:
            return None

        closest = None
        best_dist = float('inf')
        for index, (x_val, y_val) in enumerate(zip(self.x, self.heights)):
            px, py = self.ax.transData.transform((x_val, y_val))
            distance = np.hypot(event.x - px, event.y - py)
            if distance < best_dist and distance <= max_pixel_distance:
                best_dist = distance
                closest = index
        return closest

    def on_press(self, event):
        if event.inaxes != self.ax or event.button != 1:
            return
        idx = self.get_closest_point(event)
        if idx is None:
            return
        self.dragging_index = idx
        self.press_y = event.ydata
        self.heights_at_press = self.heights.copy()

    def on_motion(self, event):
        if self.dragging_index is None or event.inaxes != self.ax or event.ydata is None:
            return
        delta = event.ydata - self.press_y
        weights = self.neighbor_weights(self.dragging_index)
        new_heights = self.heights_at_press + delta * weights
        self.heights = np.maximum(new_heights, 0.0)
        self.update_plot()

    def on_release(self, event):
        self.dragging_index = None
        self.press_y = None
        self.heights_at_press = None


if __name__ == '__main__':
    app = DraggableSmoothBars(
        n_bars=20,
        initial_height=5.0,
        influence_width=1.0,
    )
    plt.show()
