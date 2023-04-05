""" Graphical user interface includes all widgets """
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget # pylint: disable=no-name-in-module
from micromechanics.indentation import Indentation

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  """ Graphical user interface includes all widgets """
  def __init__(self):
    #global setting
    super().__init__()
    self.setWindowTitle("Indentation GUI")


##############
## Main function
def main():
  """ Main method and entry point for commands """
  app = QApplication()
  window = MainWindow()
  window.show()
  app.exec()
  return

# called by python3 -m micromechanics-IndentationGUI.main
if __name__ == '__main__':
  main()
