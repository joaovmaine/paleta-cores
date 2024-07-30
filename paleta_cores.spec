# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

a = Analysis(
    ['paleta_cores.py'],
    pathex=['C:\\Users\\USUARIO\\Desktop\\paleta-cores'],
    binaries=[],
    datas=[('favicon.ico', '.')],  # Inclui o arquivo de ícone
    hiddenimports=['pyperclip'],  # Adiciona pyperclip como importação oculta
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Paleta_de_Cores',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='favicon.ico',  # Define o ícone da janela
)
