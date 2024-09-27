# Testing for Streamlit
# can't find files on relative path or absolute path
# probably libraries conflicts on different versions

import pathlib
import glob

import pathlib
import os
cwd = os.getcwd()

p = pathlib.Path('dataset.csv')
print(p)
