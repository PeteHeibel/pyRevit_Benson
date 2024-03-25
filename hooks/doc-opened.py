from pyrevit import revit, DB, HOST_APP, forms
import os

import sys
import os
sys.path.append(os.path.expandvars("%appdata%\pyRevit\Extensions\Benson.extension"))
from benson import latest_version 

revit_version = HOST_APP.version
revit_subversion = HOST_APP.subversion

# Get the active Revit document
doc = revit.doc

# Check if the project contains a sheet titled "Home"
sheets = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Sheets).ToElements()
hasHomeView = False
for sheet in sheets:
    if sheet.Name == "Home":
        hasHomeView = True
        break

# If the project contains a sheet titled "Home" and the project is hosted in the cloud, run the script
if hasHomeView and doc.IsModelInCloud:
    trans = DB.Transaction(doc)
    trans.Start("Write Home Data")

    # Get and set the "Revit Version" project parameter
    revit_version_parameter = doc.ProjectInformation.LookupParameter("Revit Version")
    revit_version_parameter.Set(revit_subversion)

    # Get Revit version and local cache path
    revit_version = str(HOST_APP.version)
    local_app_data = os.getenv('LOCALAPPDATA')
    collaboration_cache_path = os.path.join(local_app_data, "Autodesk\Revit\Autodesk Revit " + revit_version + "\CollaborationCache")

    # Extract cloud model path information
    cloud_file_path = doc.GetCloudModelPath()
    account_guid = "CFP2XTS6R29ZTP5B"
    project_guid = cloud_file_path.GetProjectGUID()
    model_guid = cloud_file_path.GetModelGUID()

    # Construct collaboration cache file path efficiently
    collaboration_cache_project_path = os.path.join(collaboration_cache_path, account_guid, str(project_guid))
    cloud_file_cache_path = os.path.join(collaboration_cache_project_path, str(model_guid) + ".rvt")

    # Get and set the "File Size" project parameter
    file_size_parameter = doc.ProjectInformation.LookupParameter("File Size")

    file_size_bytes = float(os.path.getsize(cloud_file_cache_path))
    file_size_mb = file_size_bytes / 1024**2
    file_size_parameter.Set(file_size_mb)

    # set the value of the "MTK - Home" titleblock's "Update" parameter
    titleblock = DB.ElementId(74651769)
    update_parameter = doc.GetElement(titleblock).LookupParameter("Update")
    update_parameter.Set(0) if revit_subversion == latest_version(revit_version) else update_parameter.Set(1)

    # additional parameter writing here

    trans.Commit()

else:
    # Do nothing
    pass