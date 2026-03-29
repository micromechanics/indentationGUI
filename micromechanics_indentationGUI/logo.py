"""Generate logo assets for the GUI."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


ROW = COLUMN = 3
HARDNESS_0 = 10
HARDNESS_DECREASE = 0.2
LINE_WIDTH = 10
GRID_WIDTH = 5
OUTPUT_DIR = Path(__file__).resolve().parent / "pic" / "logo"


def build_hardness_map():
  """Create the tiled background used by the icon."""
  hardness = np.ones((ROW, COLUMN))
  for i in range(ROW):
    for j in range(i, COLUMN):
      hardness[i, j] = hardness[j, i] = HARDNESS_0 - (j + i) / 2 + HARDNESS_DECREASE
  return hardness


def draw_logo():
  """Draw the standard blue logo and return the figure."""
  hardness = build_hardness_map()
  plt.style.use("_mpl-gallery-nogrid")
  fig, ax = plt.subplots()
  ax.imshow(
    hardness,
    cmap="Blues",
    vmin=np.min(hardness) - 0.1 * HARDNESS_0,
    vmax=np.max(hardness),
  )

  line_color = "white"

  x_values = np.arange(-0.5, 0, 0.01)
  y_values = np.ones(len(x_values)) * (ROW - 0.5)
  ax.plot(x_values, y_values, linewidth=LINE_WIDTH, color=line_color)

  x_values = np.arange(0, ROW - 0.55 + 0.01, 0.01)
  curvature = ROW / (ROW - 0.55) ** 2
  y_values = -curvature * x_values ** 2 + ROW - 0.5
  ax.plot(x_values, y_values, linewidth=LINE_WIDTH, color=line_color)

  x_values = np.arange(ROW - 0.55, ROW - 0.5, 0.0001)
  y_values = np.ones(len(x_values)) * -0.5
  ax.plot(x_values, y_values, linewidth=LINE_WIDTH, color=line_color)

  alpha = 5
  hf = ROW - 0.5 - (ROW / alpha) ** (1 / 1.25)
  x_values = np.arange(hf, ROW - 0.5, 0.0001)
  y_values = -alpha * (x_values - hf) ** 1.25 + ROW - 0.5
  ax.plot(x_values, y_values, linewidth=LINE_WIDTH, color=line_color)

  x_values = np.arange(0, hf, 0.01)
  y_values = np.ones(len(x_values)) * (ROW - 0.5)
  ax.plot(x_values, y_values, linewidth=LINE_WIDTH, color=line_color)

  for i in range(ROW - 1):
    ax.axvline(i + 0.5, color=line_color, linewidth=GRID_WIDTH)
    ax.axhline(i + 0.5, color=line_color, linewidth=GRID_WIDTH)

  ax.spines["top"].set_visible(False)
  ax.spines["right"].set_visible(False)
  ax.spines["bottom"].set_visible(False)
  ax.spines["left"].set_visible(False)
  ax.get_xaxis().set_ticks([])
  ax.get_yaxis().set_ticks([])
  return fig


def save_standard_logo_set(fig):
  """Save the standard icon sizes."""
  output_map = {
    "logo.png": 1000,
    "logo_16x16.png": 8,
    "logo_24x24.png": 12,
    "logo_32x32.png": 16,
    "logo_48x48.png": 24,
    "logo_256x256.png": 128,
  }
  for filename, dpi in output_map.items():
    fig.savefig(OUTPUT_DIR / filename, dpi=dpi, bbox_inches="tight", pad_inches=0)


def save_white_logo_set():
  """Create white transparent variants from the standard logo."""
  source = OUTPUT_DIR / "logo.png"
  source_img = Image.open(source).convert("RGBA")
  pixels = np.asarray(source_img, dtype=np.uint8)
  transparent = np.zeros_like(pixels)

  # Keep the original blue shading as varying alpha on a white logo.
  # Pure white pixels remain transparent so the indentation curve/grid
  # and outer background still show through the docs header color.
  non_white_mask = np.any(pixels[:, :, :3] < 245, axis=2)
  transparent[:, :, :3] = 255
  transparent[:, :, 3] = np.where(non_white_mask, pixels[:, :, 2], 0)

  white_logo = Image.fromarray(transparent, mode="RGBA")
  output_map = {
    "logo_white.png": white_logo.size,
    "logo_white_16x16.png": (16, 16),
    "logo_white_24x24.png": (24, 24),
    "logo_white_32x32.png": (32, 32),
    "logo_white_48x48.png": (48, 48),
    "logo_white_256x256.png": (256, 256),
  }

  for filename, size in output_map.items():
    image = white_logo if size == white_logo.size else white_logo.resize(size, Image.LANCZOS)
    image.save(OUTPUT_DIR / filename)


def main():
  """Generate the standard and white logo assets."""
  OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
  fig = draw_logo()
  save_standard_logo_set(fig)
  plt.close(fig)
  save_white_logo_set()


if __name__ == "__main__":
  main()
