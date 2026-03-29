# Screenshot Workflow

This file records how the documentation screenshots are generated so we can
refresh them quickly after GUI changes.

## Purpose

The analysis-tab screenshots in `docs/source/img/` are generated from the real
Qt GUI, not captured manually. This keeps the images consistent across pages
and makes them easy to refresh after layout changes.

## Script

The generator script is:

- `docs/scripts/generate_analysis_tab_screenshots.py`

It creates these files:

- `docs/source/img/main_window_tab_TAF.png`
- `docs/source/img/main_window_tab_FrameCompliance.png`
- `docs/source/img/main_window_tab_HE.png`
- `docs/source/img/main_window_tab_Creep.png`
- `docs/source/img/main_window_tab_TipRadius.png`
- `docs/source/img/main_window_tab_PopIn.png`
- `docs/source/img/main_window_tab_Classification.png`

## Recommended update flow

1. Use the same Python environment that launches `indentationGUI`.
2. From the repository root, regenerate the screenshots:

   ```bash
   python docs/scripts/generate_analysis_tab_screenshots.py
   ```

   Or from the `docs` folder:

   ```bash
   make screenshots
   ```

3. Rebuild the documentation:

   ```bash
   cd docs
   make html
   ```

4. Review the generated pages in `docs/build/html/`.

## Notes

- On Linux, the script defaults to `QT_QPA_PLATFORM=offscreen` so it can run
  without a visible desktop window.
- If the active Python environment is not the GUI environment, the script will
  fail during import. In that case, rerun it with the environment used for the
  application itself.
- If the tab structure changes in the GUI, update `TAB_SCREENSHOTS` in
  `docs/scripts/generate_analysis_tab_screenshots.py`.
