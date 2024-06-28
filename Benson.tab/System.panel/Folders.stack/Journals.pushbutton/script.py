# -*- coding: utf-8 -*-
# script metadata
__title__   = 'Journals'
__doc__     = "Opens the Revit journals folder for current user"
__author__  = 'Pete Heibel'
__min_revit_ver__  = 2021
__max_revit_ver__  = 2024
__context__ = 'zero-doc'

# imports
from pyrevit import coreutils, revit

# variables
journals_folder = revit.get_journals_folder()

# main
coreutils.open_folder_in_explorer(journals_folder)