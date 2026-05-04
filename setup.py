import shutil
import subprocess
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
        self.install_icons()
        self.create_desktop_file()

  def install_icons(self):
    """Copy logos into the user's hicolor icon theme so the .desktop's
    Icon=indentationGUI resolves on Wayland/GNOME (which ignores absolute
    icon paths for window/title-bar matching in newer Qt versions)."""
    pythonVersion = f"{sys.version_info.major}.{sys.version_info.minor}"
    installation_path = os.path.join(sys.prefix, 'lib', f"python{pythonVersion}", 'site-packages')
    logo_dir = os.path.join(installation_path, 'micromechanics_indentationGUI', 'pic', 'logo')
    hicolor = os.path.expanduser("~/.local/share/icons/hicolor")
    sizes = [(16, 'logo_16x16.png'), (24, 'logo_24x24.png'),
             (32, 'logo_32x32.png'), (48, 'logo_48x48.png'),
             (256, 'logo_256x256.png')]
    for px, fname in sizes:
        src = os.path.join(logo_dir, fname)
        if not os.path.exists(src):
            continue
        dst_dir = os.path.join(hicolor, f"{px}x{px}", "apps")
        os.makedirs(dst_dir, exist_ok=True)
        shutil.copyfile(src, os.path.join(dst_dir, "indentationGUI.png"))
    try:
        subprocess.run(["gtk-update-icon-cache", "-f", "-t", hicolor],
                       check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        pass

  def create_desktop_file(self):
    """create .desktop file for Linux-Ubuntu user.
    Note: lines must NOT be indented — the freedesktop spec rejects leading
    whitespace on keys, and some compositors silently drop the icon when the
    file is malformed."""
    desktop_file_content = (
        "[Desktop Entry]\n"
        "Type=Application\n"
        "Name=indentationGUI\n"
        f"Exec={os.path.join(sys.prefix, 'bin', 'indentationGUI')}\n"
        "Icon=indentationGUI\n"
        "Terminal=false\n"
        "StartupNotify=true\n"
        "StartupWMClass=indentationGUI\n"
    )
    apps_dir = os.path.expanduser("~/.local/share/applications")
    os.makedirs(apps_dir, exist_ok=True)
    desktop_file_path = os.path.join(apps_dir, "indentationGUI.desktop")
    with open(desktop_file_path, "w", encoding="utf-8") as desktop_file:
        desktop_file.write(desktop_file_content)
    try:
        subprocess.run(["update-desktop-database", apps_dir],
                       check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        pass

if __name__ == '__main__':
  setup(
        name='micromechanics-indentationGUI',
        version=commit.get_version()[1:],
        cmdclass ={'install':PostInstallCommand}
        )
