""" Module for tools for loading data """
from io import StringIO, TextIOWrapper
from zipfile import ZipFile
from pathlib import Path
import re
import pandas as pd
import numpy as np
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from scipy.ndimage import gaussian_filter1d

def Convert2inGUI(fileNameList):
  """
  Convert input files into the inGUI Excel format.

  Supported formats:
  - .zip → processed with DataTransformation_MicroMaterials
  - .smart500 → processed with DataTransformation_Surface_Smart_500
  - .xlsx → used directly

  If multiple files are provided, they are merged using merge_excels().

  Returns
  -------
  str
    Path to the resulting Excel file.
  """
  for i,file in enumerate(fileNameList):
    file_path = Path(file)
    OutputFileName = file_path.with_name(file_path.stem + "_inGUI.xlsx")
    if not OutputFileName.exists():
      if 'zip' in file:
        DataTransformation_MicroMaterials(fileName=file)
      elif '.smart500' in file:
        DataTransformation_Surface_Smart_500(fileName=file)
      elif '.xlsx' in file:
        OutputFileName = file_path
    fileNameList[i] = str(OutputFileName)
  if len(fileNameList)==1:
    fileName = fileNameList[0]
  else:
    fileName = merge_excels(fileNameList)
  return fileName

def merge_excels(files_list):
  """
  Merge multiple Excel files into one workbook.

  Rules:
  - "Results" comes FIRST:
    * Row 1 = header, Row 2 = units, Row 3+ = data.
    * Keep header and units once (from first file).
    * Append all data rows with 'Path' column.
  - Each non-Results sheet becomes "Test 1", "Test 2", ...
    * Same rule: header+units once, rest are data rows.
    * All data rows tagged with Path.
  - Output saved beside the first file as 'merged_all_inGUI.xlsx'.
  """
  files_list = [Path(p) for p in files_list]
  out_path = files_list[0].parent / "merged_all_inGUI.xlsx"

  def split_header_units_data(xls, sheet):
    """Read one sheet from an already-open ExcelFile."""
    df = xls.parse(sheet_name=sheet)
    cols = list(df.columns)
    if len(df) > 0:
      units = df.iloc[0]   # row1 = units
    else:
      units = pd.Series(index=cols, dtype=object)
    data = df.iloc[1:].copy()  # drop units
    return cols, units, data

  with pd.ExcelWriter(out_path, engine="openpyxl") as w: # pylint: disable=abstract-class-instantiated
    # ---- Results sheet (merged, first) ----
    first_cols, first_units, parts = None, None, []
    for i, f in enumerate(files_list, 1):
      try:
        xls = pd.ExcelFile(f)
        cols, units, data = split_header_units_data(xls, "Results")
      except Exception: #pylint: disable=broad-except
        continue
      if first_cols is None:
        first_cols, first_units = cols, units
      if not data.empty:
        data.insert(0, "Path", int(i))
        data = data.reindex(columns=["Path"] + first_cols)
        parts.append(data)
    if first_cols is not None:
      units_df = pd.DataFrame(
        [[""] + list(first_units)], columns=["Path"] + first_cols
      )
      pd.concat([units_df] + parts, ignore_index=True).to_excel(
        w, "Results", index=False
      )
    # ---- Test sheets (independent, renamed) ----
    t = 0
    for i, f in enumerate(files_list, 1):
      try:
        xls = pd.ExcelFile(f)
      except Exception: #pylint: disable=broad-except
        continue
      for s in xls.sheet_names:
        if s.strip().lower() == "results":
          continue
        try:
          cols, units, data = split_header_units_data(xls, s)
        except Exception: #pylint: disable=broad-except
          continue
        if len(cols) == 0:
          continue
        if not data.empty:
          data.insert(0, "Path", int(i))
          data = data.reindex(columns=["Path"] + cols)
        else:
          data = pd.DataFrame(columns=["Path"] + cols)
        # add one shared units row if this is the first file for this Test
        if t == 0 or s not in xls.sheet_names:
          pass
        units_df = pd.DataFrame([[""] + list(units)], columns=["Path"] + cols)
        t += 1
        pd.concat([units_df, data], ignore_index=True).to_excel(
          w, f"Test {t}", index=False
          )
  return str(out_path)


def read_file_list(tableWidget):
  """
  to obtain the file list from the table
  """
  fileNameList=[]
  for i in range(tableWidget.rowCount()):
    theItem0 = tableWidget.item(i,0)
    if theItem0.checkState() == Qt.Checked:
      fileNameList.append(theItem0.text())
  return fileNameList

def split_text_into_segments_by_blank_lines(text: str):
  """
  Splits a block of text into multiple segments separated by blank lines.
  A blank line means a line with no content or only whitespace.
  Each segment is returned as a string containing its lines joined by "\n".
  This is used to split the drift data file into one segment per test.
  """
  segments, buf = [], []
  for line in text.splitlines():
    if line.strip() == "":
      if buf:
        segments.append("\n".join(buf))
        buf = []
    else:
      buf.append(line)
  if buf:
    segments.append("\n".join(buf))  # Add the last segment if it exists
  return segments

def read_drift_segments(segments):
  """
  Parse each drift segment as a small DataFrame with columns:
    Time [s], Displacement [nm]
  (The source file’s second column is displacement in nm.)
  Ensures numeric types and drops non-numeric rows.
  Returns a list[pd.DataFrame].
  """
  drift_dfs = []
  for seg in segments:
    d = pd.read_csv(StringIO(seg), sep="\t", header=None,
                    names=["Time [s]", "Displacement [nm]"])
    d["Time [s]"] = pd.to_numeric(d["Time [s]"], errors="coerce")
    d["Displacement [nm]"] = pd.to_numeric(d["Displacement [nm]"], errors="coerce")
    d = d.dropna(subset=["Time [s]", "Displacement [nm]"]).sort_values("Time [s]").reset_index(drop=True)
    drift_dfs.append(d)
  return drift_dfs

def insert_drift_into_gap( #pylint: disable=missing-param-doc
  group: pd.DataFrame,
  drift_df: pd.DataFrame,
  gap_threshold_s: float,
  gap_strategy: str = "last",   # "largest", "first", or "last"
) -> pd.DataFrame:
  """
  For a single test (group):
    1) Detect an internal time jump > gap_threshold_s, chosen by `gap_strategy`.
    2) Build drift rows with times offset from the time *before* the gap:
          new_time = t_pre + drift_time   (only drift_time > 0)
        - displacement from drift_df["Displacement [nm]"]
        - load held constant at the *pre-gap* row
    3) Insert these rows strictly between the pre-gap row and the first post-gap row (t_pre < t < t_post).
  If no qualifying gap is detected, return the group unchanged.

  Parameters
  ----------
  group : pd.DataFrame
    Test data with columns ["Time [s]", "Displacement [nm]", "Load [mN]"].
  drift_df : pd.DataFrame
    Drift data with columns ["Time [s]", "Displacement [nm]"].
  gap_threshold_s : float
    Threshold in seconds above which a time jump is considered a gap.
  gap_strategy : {"largest", "first", "last"}, default="largest"
    Which qualifying gap to use.
  """
  print("insert_drift_into_gap")
  # ---- Validation: check required columns exist
  required_cols = {"Time [s]", "Displacement [nm]", "Load [mN]"}
  if not required_cols.issubset(group.columns):
    missing = required_cols - set(group.columns)
    raise ValueError(f"group is missing required columns: {sorted(missing)}")
  if not {"Time [s]", "Displacement [nm]"}.issubset(drift_df.columns):
    raise ValueError("drift_df must contain 'Time [s]' and 'Displacement [nm]'")

  # ---- Prepare group: ensure numeric dtypes, drop NaNs, sort by time
  g = group.copy()
  g["Time [s]"] = pd.to_numeric(g["Time [s]"], errors="coerce")
  g["Displacement [nm]"] = pd.to_numeric(g["Displacement [nm]"], errors="coerce")
  g["Load [mN]"] = pd.to_numeric(g["Load [mN]"], errors="coerce")
  g = g.dropna(subset=["Time [s]"]).sort_values("Time [s]").reset_index(drop=True)

  # ---- If too few rows, nothing to do
  times = g["Time [s]"].to_numpy(dtype=float)
  if times.size < 2:
    return g

  # ---- Compute time differences to detect internal gaps
  diffs = np.diff(times)
  candidate_idxs = np.where(diffs > float(gap_threshold_s))[0]  # idx = pre-gap row
  if candidate_idxs.size == 0:
    return g  # no gap above threshold

  # ---- Pick which gap to use depending on strategy
  if gap_strategy == "largest":
    rel = np.argmax(diffs[candidate_idxs])     # relative index of the largest gap
    pre_idx = int(candidate_idxs[rel])         # absolute pre-gap index
  elif gap_strategy == "first":
    pre_idx = int(candidate_idxs[0])           # first qualifying gap
  elif gap_strategy == "last":
    pre_idx = int(candidate_idxs[-1])          # last qualifying gap
  else:
    raise ValueError("gap_strategy must be 'largest', 'first', or 'last'")

  post_idx = pre_idx + 1                         # first row AFTER the gap
  t_pre = float(times[pre_idx])                  # pre-gap time
  t_post = float(times[post_idx])                # post-gap time
  load_pre = float(g.at[pre_idx, "Load [mN]"])   # keep load constant
  test_num = g.at[pre_idx, "Test number"] if "Test number" in g.columns else np.nan

  # ---- Prepare drift data: numeric, sorted, drop NaNs, only positive times
  d = drift_df.copy()
  d["Time [s]"] = pd.to_numeric(d["Time [s]"], errors="coerce")
  d["Displacement [nm]"] = pd.to_numeric(d["Displacement [nm]"], errors="coerce")
  d = d.dropna(subset=["Time [s]", "Displacement [nm]"]).sort_values("Time [s]")
  d = d[d["Time [s]"] > 0]                       # skip t=0 to avoid duplicate timestamp
  if d.empty:
    return g

  # ---- Shift drift times relative to pre-gap time
  insert_times = t_pre + d["Time [s]"].to_numpy(dtype=float)
  print(insert_times)
  # ---- Keep only drift times strictly inside the gap window
  inside = (insert_times > t_pre) & (insert_times < t_post)
  if not np.any(inside):
    return g  # all drift times fell outside the gap

  # ---- Build new drift rows to insert
  insert_rows = pd.DataFrame({
    "Test number": test_num,
    "Time [s]": insert_times[inside],
    "Displacement [nm]": d["Displacement [nm]"].to_numpy()[inside],
    "Load [mN]": load_pre
  })

  # ---- Concatenate: keep everything up to pre-gap row, add drift, then post-gap onward
  g_filled = pd.concat(
    [g.iloc[:post_idx], insert_rows, g.iloc[post_idx:]],
    ignore_index=True
    )
  print(g_filled)
  # ---- Restore tidy column order
  desired_order = ["Test number", "Time [s]", "Displacement [nm]", "Load [mN]"]
  cols = [c for c in desired_order if c in g_filled.columns] + \
          [c for c in g_filled.columns if c not in desired_order]
  return g_filled[cols]

def apply_two_row_header(df_simple: pd.DataFrame) -> pd.DataFrame:
  """
  Convert a 4-column simple DataFrame into a two-row header (name/unit) layout using a MultiIndex:
    Row 1 (names): ['Test number', 'Time', 'Displacement', 'Load']
    Row 2 (units): ['-',          's',    'nm',           'mN' ]
  """
  names = ["Test number", "Time", "Displacement", "Load"]
  units = ["-", "s", "nm", "mN"]
  df_out = df_simple.copy()
  df_out.columns = pd.MultiIndex.from_arrays([names, units])
  return df_out

def write_with_two_row_header(writer: pd.ExcelWriter, df_simple: pd.DataFrame, sheet_name: str):
  """
  Write a DataFrame with a manual two-row header:
    Row 1: names  (Test number | Time | Displacement | Load)
    Row 2: units  (-           | s    | nm           | mN )
  """
  # Two-row header content
  HEADER_NAMES = ["Test number", "Time", "Displacement", "Load"]
  HEADER_UNITS = ["-", "s", "nm", "mN"]
  # Write the two header rows by hand
  ws = writer.book.add_worksheet(sheet_name)
  writer.sheets[sheet_name] = ws
  ws.write_row(0, 0, HEADER_NAMES)
  ws.write_row(1, 0, HEADER_UNITS)
  # Then write the data starting at row 2 (zero-based)
  df_simple.to_excel(writer, sheet_name=sheet_name, startrow=2, index=False, header=False)

def obtainDrift_Micormaterials_default(drift_df):
  """
  Estimate the drift rate from MicroMaterials indentation data.

  The drift is calculated by performing a linear fit on the last 60% of
  the displacement-time data. MicroMaterials instruments typically use
  this region for drift correction.

  Parameters
  ----------
  drift_df : pandas.DataFrame
    DataFrame containing the drift measurement data. It must include
    the columns:
    - "Time [s]"
    - "Displacement [nm]"

  Returns
  -------
  float
    Estimated drift rate (slope of displacement vs time).
    Units: nm/s.
  """
  Time = drift_df["Time [s]"]
  Displacement = drift_df["Displacement [nm]"]
  # Displacement = gaussian_filter1d(Displacement, 3)
  Drift_Start = int(len(Time) * 0.4) # Micromaterials use the last 60% for drift correction by default.
  popt = np.polyfit(Time[Drift_Start:], Displacement[Drift_Start:], 1)
  Drift = popt[0]
  return Drift

def split_name_unit(col: str):
  """
  Split 'Name [unit]' into ('Name', '[unit]').
  If no unit is present, return ('Name', '').
  """
  if col is None:
    return "", ""
  s = str(col).strip()
  m = re.match(r"^(.*?)(\s*\[[^\]]*\])\s*$", s)
  if m:
    return m.group(1).strip(), m.group(2).strip()
  return s, ""

def dataframe_with_unit_row(df: pd.DataFrame) -> pd.DataFrame:
  """
  Convert a DataFrame whose columns are 'Name [unit]' into:
    - Excel row 1: column names (without units)
    - Excel row 2: units
    - Excel row 3+: data
  """
  base_names = []
  units = []
  for c in df.columns:
    name, unit = split_name_unit(c)
    base_names.append(name)
    units.append(unit)
  df2 = df.copy()
  df2.columns = base_names
  unit_row = pd.DataFrame([units], columns=base_names)
  return pd.concat([unit_row, df2], ignore_index=True)

def DataTransformation_Surface_Smart_500(fileName):
  """
  Extract and transform Surface Smart 500 data from a ZIP archive into an Excel file.

  The function:
  - Reads CSV files inside a ZIP archive
  - Identifies a Results file and multiple Test files
  - Filters and reformats relevant columns
  - Writes structured data into an Excel file with multiple sheets

  Parameters
  ----------
  fileName : str
    Path to the ZIP file containing Surface Smart 500 data.

  Returns
  -------
  str
    Path to the generated Excel file.
  """
  # Detect path separator
  slash = '/' if '/' in fileName else '\\'
  # Extract path and base filename
  index_path_end = fileName.rfind(slash)
  thePath = fileName[:index_path_end]
  theFile = fileName[index_path_end + 1:fileName.rfind('.')]
  zip_path = fileName
  output_excel = f"{thePath}{slash}{theFile}_inGUI.xlsx"
  KEEP_COLUMNS = [
    "Time on Sample",
    "Displacement into Surface",
    "Load on Sample",
    "Dynamic Contact Stiffness"
    ]
  test_pattern = re.compile(r"_(\d+)\.csv$", re.IGNORECASE)
  results_csv = None
  test_csvs = {}

  with ZipFile(zip_path, "r") as z:
    csv_files = [f for f in z.namelist() if f.lower().endswith(".csv")]
    # Classify CSV files
    for name in csv_files:
      if name.endswith("_Results.csv"):
        results_csv = name
        continue
      m = test_pattern.search(name)
      if m:
        test_csvs[int(m.group(1))] = name
    if results_csv is None:
      raise FileNotFoundError("No CSV ending with '_Results.csv' found")
    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
      # ---------- Results sheet ----------
      with z.open(results_csv) as f:
        df_results = pd.read_csv(
          TextIOWrapper(f, encoding="utf-8"),
          sep="\t"
        )
      df_results_out = dataframe_with_unit_row(df_results)
      # Overwrite first column with 1,2,3,...
      first_col = df_results_out.columns[0]
      df_results_out.loc[1:, first_col] = range(1, len(df_results_out))
      df_results_out.to_excel(writer, sheet_name="Results", index=False)
      # ---------- Test N sheets ----------
      for n in sorted(test_csvs):
        with z.open(test_csvs[n]) as f:
          df = pd.read_csv(
            TextIOWrapper(f, encoding="utf-8"),
            sep=";"
            ).fillna(0.0)
        # Build mapping: base_name -> (original_column, unit)
        base_to_orig = {}
        base_to_unit = {}
        for col in df.columns:
          base, unit = split_name_unit(col)
          if base not in base_to_orig:
            base_to_orig[base] = col
            base_to_unit[base] = unit
        # Keep only requested columns
        keep = [c for c in KEEP_COLUMNS if c in base_to_orig]
        df_filtered = df[[base_to_orig[c] for c in keep]].copy()
        df_filtered.columns = keep
        unit_row = pd.DataFrame(
          [[base_to_unit.get(c, "") for c in keep]],
          columns=keep
          )
        df_out = pd.concat([unit_row, df_filtered], ignore_index=True)
        df_out.to_excel(writer, sheet_name=f"Test {n}", index=False)
  return output_excel

def DataTransformation_MicroMaterials(fileName):
  """
  Transform MicroMaterials indentation data from a ZIP archive into an Excel file.

  The function:
  - Reads measurement data (load–displacement–time)
  - Extracts pre- and post-indent drift data
  - Optionally reads coordinates (X/Y positions)
  - Reconstructs raw displacement by reversing drift correction
  - Inserts drift segments into time gaps
  - Writes results into a structured Excel file (one sheet per test)

  Parameters
  ----------
  fileName : str
    Path to the ZIP file containing MicroMaterials data.
  """
  # Detect path separator
  slash = '/' if '/' in fileName else '\\'
  # Extract path and base filename
  index_path_end = fileName.rfind(slash)
  thePath = fileName[:index_path_end]
  theFile = fileName[index_path_end + 1:fileName.rfind('.')]
  # 1. Read both the measurement and drift data from the ZIP archive
  zip_path = fileName
  txt_filenames = ["load_depth.txt","l.txt"]
  drift_post_names = ["thermal_drift post indent drift data.txt","d post indent drift data.txt"]
  drift_pre_names = ["thermal_drift pre indent data.txt","d pre indent data.txt"]
  coordinates_names = ["coordinates.TXT","c.TXT"]  # file containing X/Y positions
  output_excel_path = f"{thePath}{slash}{theFile}_inGUI.xlsx"
  print(f"Excel file saved to: {output_excel_path}")
  # Threshold to detect the in-test gap (seconds)
  gap_threshold_s = 1.0 # [s]
  # Read the text file from the ZIP archive
  with ZipFile(zip_path, 'r') as z:
    # Load into a DataFrame, tab-separated, no header in the original file
    for name in txt_filenames:
      if name in z.namelist():
        with z.open(name) as f:
          df = pd.read_csv(
          f, sep="\t", header=None,
          names = ["Test number", "Cycle number", "Time [s]", "Displacement [nm]", "Load [mN]"]
          )
        print(f"Opened {name}")
        break
    # Group by "Test number" and write each group to a separate sheet in Excel
    df = df.drop(columns=["Cycle number"])
    # Load post-indent drift data (used to measure the gap duration)
    for name in drift_post_names:
      if name in z.namelist():
        try:
          with z.open(name) as f:
            drift_post_text = f.read().decode(errors="replace")
        except:
          test_to_drift_post_df = {}
        else:
          # 3. Split drift data into segments and compute durations
          segments_drift_post = split_text_into_segments_by_blank_lines(drift_post_text)
          drift_post_per_test = read_drift_segments(segments_drift_post)
          # 4. Map each drift duration to the corresponding test number
          test_ids = sorted(df["Test number"].dropna().unique())
          if len(drift_post_per_test) != len(test_ids):
            print(f"Warning: found {len(drift_post_per_test)} post drift segments for {len(test_ids)} tests. "
              f"Mapping in ascending order up to the shorter length.")
          map_len = min(len(drift_post_per_test), len(test_ids))
          test_to_drift_post_df = {test_ids[i]: drift_post_per_test[i] for i in range(map_len)}
    # Load pre-indent drift data (used to measure the gap duration)
    for name in drift_pre_names:
      if name in z.namelist():
        try:
          with z.open(name) as f:
            drift_pre_text = f.read().decode(errors="replace")
        except:
          test_to_drift_pre_df = {}
        else:
          # 3. Split drift data into segments and compute durations
          segments_drift_pre = split_text_into_segments_by_blank_lines(drift_pre_text)
          drift_pre_per_test = read_drift_segments(segments_drift_pre)
          # 4. Map each drift duration to the corresponding test number
          test_ids = sorted(df["Test number"].dropna().unique())
          if len(drift_pre_per_test) != len(test_ids):
            print(f"Warning: found {len(drift_pre_per_test)} pre drift segments for {len(test_ids)} tests. "
              f"Mapping in ascending order up to the shorter length.")
          map_len = min(len(drift_pre_per_test), len(test_ids))
          test_to_drift_pre_df = {test_ids[i]: drift_pre_per_test[i] for i in range(map_len)}
    for name in coordinates_names:
      if name in z.namelist():
        with z.open(name) as f:
          coords_df = pd.read_csv(f, sep="\t", header=None,
                                  names=["Test", "X_Position", "Y_Position"])
    # 5. Create an Excel file with one sheet per test, containing adjusted times
    with pd.ExcelWriter(output_excel_path) as writer:
      wb = writer.book
      # First sheet: Results
      ws_results = wb.add_worksheet("Results")
      writer.sheets["Results"] = ws_results
      # Header row 1: names
      ws_results.write_row(0, 0, ["Test", "X_Position", "Y_Position"])
      # Header row 2: units
      ws_results.write_row(1, 0, ["-", "µm", "µm"])
      for row_idx, row in enumerate(coords_df.itertuples(index=False), start=2):
        ws_results.write_row(row_idx, 0, row)
      # Other sheets: one per test
      for test_num, group in df.groupby("Test number"):
        drift_post_df = test_to_drift_post_df.get(test_num, None)
        drift_pre_df = test_to_drift_pre_df.get(test_num, None)
        defaultDrift = None
        if drift_post_df is None:
          drift_post = None
        else:
          drift_post = obtainDrift_Micormaterials_default(drift_post_df)
          defaultDrift = drift_post
        if drift_pre_df is None:
          drift_pre = None
        else:
          drift_pre = obtainDrift_Micormaterials_default(drift_pre_df)
          if defaultDrift is not None:
            defaultDrift = (defaultDrift + drift_pre)/2.
        print(drift_pre)
        print(drift_post)
        print(defaultDrift)
        if defaultDrift is None:
          defaultDrift = 0 #nm/s
        group = group.sort_values("Time [s]")[["Test number", "Time [s]", "Displacement [nm]", "Load [mN]"]]
        # Because the exported load depth was automatically corrected by the thermal drift, the following step is to obtain the raw load depth
        group["Displacement [nm]"] = group["Displacement [nm]"] + defaultDrift * group["Time [s]"]
        if drift_post_df is not None:
          group = insert_drift_into_gap(group, drift_post_df, gap_threshold_s, gap_strategy='last')
        if drift_pre_df is not None:
          group = insert_drift_into_gap(group, drift_pre_df, gap_threshold_s, gap_strategy='first')
        write_with_two_row_header(writer, group, sheet_name=f"Test {test_num}")
