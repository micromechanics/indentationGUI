from pathlib import Path
from types import SimpleNamespace

import pandas as pd

from micromechanics_indentationGUI.Export import _export_hdf5
from micromechanics_indentationGUI.Tools4hdf5 import convertXLSXtoHDF5


def test_agilent_xlsx_conversion_is_hdf5_readable(tmp_path):
  source_xlsx = (
    Path("micromechanics_indentationGUI/Examples/Example1/FusedSilica.xlsx")
  )
  working_xlsx = tmp_path / "FusedSilica.xlsx"
  working_xlsx.write_bytes(source_xlsx.read_bytes())

  convertXLSXtoHDF5(str(working_xlsx))

  hdf5_path = working_xlsx.with_suffix(".h5")
  with pd.HDFStore(str(hdf5_path), mode="r") as store:
    assert "/Results" in store.keys()
    assert store.get("Results").shape == (20, 6)
    assert "/Test 1" in store.keys()
    assert not store.get("Test 1").empty


def test_hdf5_export_helper_writes_results_and_per_test_data(tmp_path):
  output_path = tmp_path / "exported_results.h5"
  params = pd.DataFrame({" ": ["demo"]})
  win = SimpleNamespace(
    tabHE_testName_collect=["Test 1"],
    tabHE_hc_collect=[[1.0, 2.0]],
    tabHE_hmax_collect=[3.0],
    tabHE_Pmax_collect=[[4.0, 5.0]],
    tabHE_H_collect=[[6.0, 7.0]],
    tabHE_E_collect=[[8.0, 9.0]],
    tabHE_Er_collect=[[10.0, 11.0]],
    tabHE_Hmean_collect=[6.5],
    tabHE_Hstd_collect=[0.5],
    tabHE_Emean_collect=[8.5],
    tabHE_Estd_collect=[0.5],
    tabHE_Er_mean_collect=[10.5],
    tabHE_Er_std_collect=[0.5],
    tabHE_X_Position_collect=[None],
    tabHE_Y_Position_collect=[None],
  )

  _export_hdf5(str(output_path), 0, params, win)

  with pd.HDFStore(str(output_path), mode="r") as store:
    assert set(store.keys()) == {
      "/experimental_parameters",
      "/results",
      "/tests/Test 1",
    }
    assert store.get("/results").shape == (1, 12)
    assert store.get("/tests/Test 1").shape == (2, 9)
