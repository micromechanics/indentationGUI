#!/usr/bin/env python3
"""Generate documentation screenshots for the analysis tabs."""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
IMAGE_DIR = REPO_ROOT / "docs" / "source" / "img"


if sys.platform.startswith("linux"):
  os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-indentationgui-docs")
sys.path.insert(0, str(REPO_ROOT))


@dataclass(frozen=True)
class TabScreenshot:
  """One documentation screenshot target."""

  output_name: str
  top_level_attr: str
  nested_tab_widget_attr: str | None = None
  nested_tab_attr: str | None = None


TAB_SCREENSHOTS = (
  TabScreenshot("main_window_tab_TAF.png", "tabTAF"),
  TabScreenshot(
    "main_window_tab_FrameCompliance.png",
    "tabHE_0",
    "tabWidget_HE",
    "tabHE_FrameStiffness",
  ),
  TabScreenshot(
    "main_window_tab_HE.png",
    "tabHE_0",
    "tabWidget_HE",
    "tabHE",
  ),
  TabScreenshot(
    "main_window_tab_Creep.png",
    "tabCreep",
    "tabWidget_Creep",
    "tabCreep1",
  ),
  TabScreenshot(
    "main_window_tab_TipRadius.png",
    "tabTipRadius_0",
    "tabWidget_TipRadius",
    "tabTipRadius",
  ),
  TabScreenshot(
    "main_window_tab_PopIn.png",
    "tabPopIn_0",
    "tabWidget_PopIn",
    "tabPopIn",
  ),
  TabScreenshot("main_window_tab_Classification.png", "tabClassification"),
)


def _import_gui_classes():
  """Import the GUI from the active project environment."""
  try:
    from PySide6.QtTest import QTest  # pylint: disable=import-outside-toplevel
    from PySide6.QtWidgets import QApplication, QLineEdit, QTableWidget, QTextEdit  # pylint: disable=import-outside-toplevel
    from micromechanics_indentationGUI.main import MainWindow  # pylint: disable=import-outside-toplevel
  except Exception as exc:  # pragma: no cover - friendly runtime guard
    raise SystemExit(
      "Could not import indentationGUI from the current Python environment.\n"
      "Run this script with the same environment that launches the GUI.\n"
      f"Original error: {exc}"
    ) from exc
  return QApplication, MainWindow, QTest, QLineEdit, QTableWidget, QTextEdit


def _select_tab(window, spec: TabScreenshot):
  """Show the requested top-level tab and nested analysis tab."""
  top_level_widget = getattr(window.ui, spec.top_level_attr)
  window.ui.tabAll.setCurrentWidget(top_level_widget)
  if spec.nested_tab_widget_attr and spec.nested_tab_attr:
    nested_tab_widget = getattr(window.ui, spec.nested_tab_widget_attr)
    nested_widget = getattr(window.ui, spec.nested_tab_attr)
    nested_tab_widget.setCurrentWidget(nested_widget)


def _scrub_personal_paths(window, qlineedit_cls, qtablewidget_cls, qtextedit_cls):
  """Remove local file paths before screenshots are saved."""
  for line_edit in window.findChildren(qlineedit_cls):
    object_name = line_edit.objectName()
    if "path_" in object_name.lower():
      line_edit.clear()

  for table_widget in window.findChildren(qtablewidget_cls):
    object_name = table_widget.objectName().lower()
    if "tablewidget_path_" in object_name:
      table_widget.clearContents()
      table_widget.setRowCount(0)

  for text_edit in window.findChildren(qtextedit_cls):
    object_name = text_edit.objectName().lower()
    if "files_tabclassification" in object_name:
      text_edit.clear()


def generate_screenshots():
  """Generate and save all configured screenshots."""
  QApplication, MainWindow, QTest, QLineEdit, QTableWidget, QTextEdit = _import_gui_classes()
  app = QApplication.instance() or QApplication([])
  window = MainWindow()
  window.setWindowTitle("indentationGUI")
  window.resize(max(window.width(), 1700), max(window.height(), 1100))
  _scrub_personal_paths(window, QLineEdit, QTableWidget, QTextEdit)
  window.show()
  window.activateWindow()
  window.raise_()

  generated_files: list[Path] = []
  for spec in TAB_SCREENSHOTS:
    _select_tab(window, spec)
    for _ in range(3):
      app.processEvents()
      QTest.qWait(80)
    output_path = IMAGE_DIR / spec.output_name
    pixmap = window.grab()
    if not pixmap.save(str(output_path)):
      raise RuntimeError(f"Failed to save screenshot to {output_path}")
    generated_files.append(output_path)
    print(f"Saved {output_path.relative_to(REPO_ROOT)}")

  window.close()
  app.quit()
  return generated_files


def main():
  """CLI entry point."""
  generated_files = generate_screenshots()
  print(f"Generated {len(generated_files)} screenshots.")


if __name__ == "__main__":
  main()
