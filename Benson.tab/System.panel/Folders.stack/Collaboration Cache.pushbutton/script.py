# -*- coding: utf-8 -*-
# script metadata
__title__   = 'Collaboration Cache'
__doc__     = "Opens the Revit 'Collaboration Cache' folder in File Explorer"
__author__  = 'Pete Heibel'
__min_revit_ver__  = 2021
__max_revit_ver__  = 2024
__context__ = 'zero-doc'

# imports
import os
from pyrevit import revit, coreutils, HOST_APP, forms

# variables
doc = revit.doc
local_app_data = os.getenv('LOCALAPPDATA')
revit_version = str(HOST_APP.version)
collaboration_cache_path = local_app_data + "\Autodesk\Revit\Autodesk Revit " + revit_version + "\CollaborationCache"

# main
try:
    # if the active document is saved in the cloud, open the project guid folder
    cloud_file_path = doc.GetCloudModelPath()
    project_guid = cloud_file_path.GetProjectGUID()
    account_guid = "CFP2XTS6R29ZTP5B"
    collaboration_cache_project_path = os.path.join(collaboration_cache_path, account_guid, str(project_guid))

    coreutils.open_folder_in_explorer(collaboration_cache_project_path)
    
except:
    # if there is no project guid folder, do one of the following 
    if os.path.exists(collaboration_cache_path):
            coreutils.open_folder_in_explorer(collaboration_cache_path)
    else:
        message = "Looks like you haven't opened a cloud model yet in Revit " + revit_version + ". Open a Revit cloud model first to generate a 'Collaboration Cache' folder."
        forms.alert(message, warn_icon=False)