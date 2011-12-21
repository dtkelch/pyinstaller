from PyInstaller.hooks.hookutils import qt4_plugins_binaries


def hook(mod):
    mod.pyinstaller_binaries.extend(qt4_plugins_binaries('codecs', pyside=True))
    return mod
