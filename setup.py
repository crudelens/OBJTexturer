from setuptools import setup

APP = ['main.py']
DATA_FILES = ['blendloc.txt','finalloc.txt','images.txt','objfile.txt','blendscript.py','qml','Images','Lovelo']
OPTIONS = {'argv_emulation': True,
            'packages': ['PySide2']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
