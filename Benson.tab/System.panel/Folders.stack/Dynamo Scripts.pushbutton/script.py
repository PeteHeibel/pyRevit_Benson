# -*- coding: utf-8 -*-
# script metadata
__title__   = 'Dynamo Scripts'
__doc__     = "Opens the Dynamo 'Scripts' folder in File Explorer"
__author__  = 'Pete Heibel'
__min_revit_year__  = 2021
__max_revit_year__  = 2024
__context__ = 'zero-doc'

# imports
import os
from pyrevit import coreutils, forms

# variables
path = "K:\Revit Standards\Dynamo\Scripts"

# main
if os.path.exists(path):
    coreutils.open_folder_in_explorer(path)
else:
    forms.alert("K: drive not connected. Folder could not be opened.", "Error")