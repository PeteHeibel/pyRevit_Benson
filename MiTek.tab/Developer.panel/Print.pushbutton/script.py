import os
from pyrevit import revit

doc = revit.doc

# Get and set the "File Size" project parameter
#file_size_parameter = doc.ProjectInformation.LookupParameter("File Size")
file_path = doc.PathName
file_size_bytes = float(os.path.getsize(file_path))
file_size_mb = round((file_size_bytes / 1024**2), 2)

print("File Path: " + file_path)
print("File Size: "+ str(file_size_mb) + "mb")