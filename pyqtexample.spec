# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['example1.py'],
             pathex=['E:\\py_code\\pyqt_exec1'],
             binaries=[('bb.ico', '.'),('loding.gif', '.')],
             datas=[],
             hiddenimports=['bb.ico'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='pyqtexample',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='bb.ico')
