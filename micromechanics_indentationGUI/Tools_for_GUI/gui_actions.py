""" Module for tools for GUI """
import numpy as np
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem # pylint: disable=no-name-in-module

def Select_TypedTest(self,tabName=None): #pylint: disable=no-self-use
  "select the tests for calculation in one tab"
  if tabName is None:
    tableWidget = getattr(self.ui, "tableWidget")
    plainTextEdit = getattr(self.ui, "plainTextEdit_SelectTypedTest")
  else:
    tableWidget = getattr(self.ui, f"tableWidget_{tabName}")
    plainTextEdit = getattr(self.ui, f"plainTextEdit_SelectTypedTest_{tabName}")
  Text = plainTextEdit.toPlainText()
  TypedTests = Text.split(',')
  for k in range(tableWidget.rowCount()):
    try:
      tableWidget.item(k,0).setCheckState(Qt.Unchecked)
    except:
      pass
  for k, theTest in enumerate(TypedTests):
    if '-' in theTest:
      startNumber = int(theTest.split('-')[0])-1
      EndNumber = int(theTest.split('-')[1])-1
      for j in np.arange(startNumber, EndNumber+1, 1):
        try:
          tableWidget.item(j,0).setCheckState(Qt.Checked)
        except:
          pass
    else:
      try:
        tableWidget.item(int(theTest)-1,0).setCheckState(Qt.Checked)
      except:
        pass

def click_pushButton_SelectAll(self, tabName=None): #pylint: disable=no-self-use
  """ select/ unselect all tests in {tabName} """
  State = Qt.Checked
  if tabName is None:
    tableWidget = getattr(self.ui, "tableWidget")
  else:
    tableWidget = getattr(self.ui, f"tableWidget_{tabName}")
  if tableWidget.item(0,0).checkState() == Qt.Checked:
    State = Qt.Unchecked
  for k in range(tableWidget.rowCount()):
    try:
      tableWidget.item(k,0).setCheckState(State)
    except:
      pass


def addFile_tab(self,tabName):
  """ + "select" Button to select a file path for tab  """
  file = str(QFileDialog.getOpenFileName(self, "Select File")[0])
  if tabName is None:
    theTableWidget = getattr(self.ui, "tableWidget_path")
  else:
    theTableWidget = getattr(self.ui, f"tableWidget_path_{tabName}")
  theRowCount = theTableWidget.rowCount()
  if file != '':
    if theRowCount>0:
      if len(theTableWidget.item(theRowCount-1,0).text()) > 0:
        theRowCount+=1
    else:
      theRowCount=1
    theTableWidget.setRowCount(theRowCount)
    qtablewidgetitem = QTableWidgetItem(file)
    qtablewidgetitem.setCheckState(Qt.Checked)
    theTableWidget.setVerticalHeaderItem(theRowCount-1, QTableWidgetItem(f"Path{int(theRowCount)}"))
    theTableWidget.setItem(0,theRowCount-1,qtablewidgetitem)

def deleteFile_tab(self,tabName):
  """ click "-" Button to delete a file path for tab  """
  if tabName is None:
    theTableWidget = getattr(self.ui, "tableWidget_path")
  else:
    theTableWidget = getattr(self.ui, f"tableWidget_path_{tabName}")
  # get selected rows
  selected_items = theTableWidget.selectedItems()
  if not selected_items:
    return  # nothing selected
  # collect row indices (unique + sorted descending, so deleting doesn’t shift others)
  rows = sorted({item.row() for item in selected_items}, reverse=True)
  for row in rows:
    theTableWidget.removeRow(row)
  for i in range(theTableWidget.rowCount()):
    theTableWidget.setVerticalHeaderItem(i, QTableWidgetItem(f"Path{int(i+1)}"))

def MoveFileUp_tab(self,tabName):
  """ click "up" Button to move up a file path  """
  if tabName is None:
    theTableWidget = getattr(self.ui, "tableWidget_path")
  else:
    theTableWidget = getattr(self.ui, f"tableWidget_path_{tabName}")
  # rowCount = theTableWidget.rowCount()
  columnCount = theTableWidget.columnCount()
  # get selected rows
  selected_items = theTableWidget.selectedItems()
  if not selected_items:
    return  # nothing selected
  # collect row indices (unique + sorted descending, so deleting doesn’t shift others)
  rows = sorted({item.row() for item in selected_items}, reverse=True)
  if len(rows) == 1:
    row = rows[0]
    for i in range(columnCount):
      thisItemClone = theTableWidget.item(row,i).clone()
      upItem = theTableWidget.item(row-1,i)
      if upItem is not None:
        theTableWidget.setItem(row,i,upItem.clone())
        theTableWidget.setItem(row-1,i,thisItemClone)

def MoveFileDown_tab(self,tabName):
  """ click "down" Button to move down a file path  """
  if tabName is None:
    theTableWidget = getattr(self.ui, "tableWidget_path")
  else:
    theTableWidget = getattr(self.ui, f"tableWidget_path_{tabName}")
  # rowCount = theTableWidget.rowCount()
  columnCount = theTableWidget.columnCount()
  # get selected rows
  selected_items = theTableWidget.selectedItems()
  if not selected_items:
    return  # nothing selected
  # collect row indices (unique + sorted descending, so deleting doesn’t shift others)
  rows = sorted({item.row() for item in selected_items}, reverse=True)
  if len(rows) == 1:
    row = rows[0]
    for i in range(columnCount):
      thisItemClone = theTableWidget.item(row,i).clone()
      downItem = theTableWidget.item(row+1,i)
      if downItem is not None:
        theTableWidget.setItem(row,i,downItem.clone())
        theTableWidget.setItem(row+1,i,thisItemClone)

def changeFile_tab(self, tabName):
  """Click 'Change' Button to replace the selected file path in the table."""
  if tabName is None:
    theTableWidget = getattr(self.ui, "tableWidget_path")
  else:
    theTableWidget = getattr(self.ui, f"tableWidget_path_{tabName}")
  selected_items = theTableWidget.selectedItems()
  if not selected_items:
    return  # nothing selected
  # assume we only care about the first selected row
  row = selected_items[0].row()
  # open file dialog
  file, _ = QFileDialog.getOpenFileName(self, "Select File")
  if not file:
    return  # user canceled
  # set new file path in column 0 (adjust column index if needed)
  qtablewidgetitem = QTableWidgetItem(file)
  qtablewidgetitem.setCheckState(Qt.Checked)
  theTableWidget.setVerticalHeaderItem(row, QTableWidgetItem(f"Path{int(row+1)}"))
  theTableWidget.setItem(row, 0, qtablewidgetitem)

def FilesToDialog_tab(self):
  """ + "select" Button to select a file path for tab  """
  IsPath=False
  try:
    Widget = getattr(self.ui, "tableWidget_path")
  except:
    Widget = getattr(self.ui, "tableWidget")
  else:
    IsPath = True
  theTableWidget_INPUT = self.OriginalTableWidget
  rowCount = theTableWidget_INPUT.rowCount()
  columnCount = theTableWidget_INPUT.columnCount()
  Widget.setRowCount(rowCount)
  Widget.setColumnCount(columnCount)
  for i in range(rowCount):
    for j in range(columnCount):
      theItem = theTableWidget_INPUT.item(i,j)
      try:
        Widget.setItem(i,j,theItem.clone())
      except:
        Widget.setItem(i,j,None)
    if IsPath:
      Widget.setVerticalHeaderItem(i, QTableWidgetItem(f"Path{int(i+1)}"))
  # Copy horizontal header labels (if they exist)
  header_labels = []
  for j in range(columnCount):
    h_item = theTableWidget_INPUT.horizontalHeaderItem(j)
    header_labels.append(h_item.text() if h_item else "")
  Widget.setHorizontalHeaderLabels(header_labels)

def PlainTextToDialog_tab(self):
  """ + "select" Button to select a file path for tab  """
  Widget = getattr(self.ui, "plainTextEdit_SelectTypedTest")
  thePlainTextWidget_INPUT = self.OriginalPlainTextWidget
  if thePlainTextWidget_INPUT is not None:
    Text = thePlainTextWidget_INPUT.toPlainText()
    Widget.setPlainText(Text)

def PlainTextToMainWindow_tab(self):
  """ + "select" Button to select a file path for tab  """
  Widget = self.OriginalPlainTextWidget
  thePlainTextWidget_INPUT = getattr(self.ui, "plainTextEdit_SelectTypedTest")
  if thePlainTextWidget_INPUT is not None:
    Text = thePlainTextWidget_INPUT.toPlainText()
    Widget.setPlainText(Text)

def FilesToMainWindow_tab(self):
  """ + "select" Button to select a file path for tab  """
  Widget = self.OriginalTableWidget
  IsPath=False
  try:
    theTableWidget_INPUT = getattr(self.ui, "tableWidget_path")
  except:
    theTableWidget_INPUT = getattr(self.ui, "tableWidget")
  else:
    IsPath = True
  rowCount = theTableWidget_INPUT.rowCount()
  columnCount = theTableWidget_INPUT.columnCount()
  Widget.setRowCount(rowCount)
  Widget.setColumnCount(columnCount)
  for i in range(rowCount):
    for j in range(columnCount):
      theItem = theTableWidget_INPUT.item(i,j)
      if theItem is not None:
        Widget.setItem(i,j,theItem.clone())
    if IsPath:
      Widget.setVerticalHeaderItem(i, QTableWidgetItem(f"Path{int(i+1)}"))
  # Copy horizontal header labels (if they exist)
  header_labels = []
  for j in range(columnCount):
    h_item = theTableWidget_INPUT.horizontalHeaderItem(j)
    header_labels.append(h_item.text() if h_item else "")
  Widget.setHorizontalHeaderLabels(header_labels)
