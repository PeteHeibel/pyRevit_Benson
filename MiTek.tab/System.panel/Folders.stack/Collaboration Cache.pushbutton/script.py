"""Opens the Revit 'Collaboration Cache' folder in File Explorer"""

import os
from pyrevit import coreutils, HOST_APP, forms

local_app_data = os.getenv('LOCALAPPDATA')
revit_version = str(HOST_APP.version)
collaboration_cache_path = local_app_data + "\Autodesk\Revit\Autodesk Revit " + revit_version + "\CollaborationCache"
#print(local_app_data, revit_version, collaboration_cache_path)

if os.path.exists(collaboration_cache_path):
    coreutils.open_folder_in_explorer(collaboration_cache_path)
else:
    message = "Looks like you haven't opened a cloud model yet in Revit " + revit_version + ". Open a Revit cloud model to generate a 'Collaboration Cache' folder."
    forms.alert(message, warn_icon=False)