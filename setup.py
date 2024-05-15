from setuptools import setup
from setuptools.command.install import install
import os
import platform
import commit
import sys


class PostInstallCommand(install):
  """Post-installation for installation mode."""
  def run(self):
    install.run(self)
    if platform.system() == "Linux" and ('generic' in platform.platform()):
        self.create_desktop_file()

  def create_desktop_file(self):
    """create .desktop file for Linux-Ubuntu user"""
    pythonVersion = sys.version[:3]
    installation_path = os.path.join(sys.prefix, 'lib', f"python{pythonVersion}", 'site-packages')
    desktop_file_content = f"""
    [Desktop Entry]
    Type=Application
    Name=indentationGUI
    Exec={os.path.join(sys.prefix, 'bin', 'indentationGUI')}
    Icon={os.path.join(installation_path, 'micromechanics_indentationGUI', 'pic', 'indentationGUI.png')}
    Terminal=false
    """
    desktop_file_path = os.path.expanduser("~/.local/share/applications/indentationGUI.desktop")
    with open(desktop_file_path, "w") as desktop_file:
        desktop_file.write(desktop_file_content)

if __name__ == '__main__':
  setup(
        name='micromechanics-indentationGUI',
        version=commit.get_version()[1:],
        cmdclass ={'install':PostInstallCommand}
        )
