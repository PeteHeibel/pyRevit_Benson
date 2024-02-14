from pyrevit import revit, DB, HOST_APP
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

# If the project contains a sheet titled "Home", run the script
if hasHomeView:
    trans = DB.Transaction(doc)
    trans.Start("Write Home Data")

    # Get and set the "Revit Version" project parameter
    revit_version_parameter = doc.ProjectInformation.LookupParameter("Revit Version")
    revit_version_parameter.Set(revit_subversion)

    # Get and set the "File Size" project parameter
    file_size_parameter = doc.ProjectInformation.LookupParameter("File Size")
    file_path = doc.PathName
    file_size_bytes = float(os.path.getsize(file_path))
    file_size_mb = file_size_bytes / 1024**2
    file_size_parameter.Set(file_size_mb)

    # set the value of the "MTK - Home" titleblock's "Update" parameter
    titleblock = DB.ElementId(74651769)
    update_parameter = doc.GetElement(titleblock).LookupParameter("Update")
    update_parameter.Set(0) if revit_subversion == latest_version(revit_version) else update_parameter.Set(1)

    # additional parameter writing here

    trans.Commit()
