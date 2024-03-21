"""Opens the Dynamo 'Scripts' folder in File Explorer"""

from pyrevit import coreutils

try:
    coreutils.open_folder_in_explorer("K:\Revit Standards\Dynamo\Scripts")
except OSError:
    pyrevit.forms.alert("K: drive not connected. Folder could not be opened.", "Error")