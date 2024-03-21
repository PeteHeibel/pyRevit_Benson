import pyrevit
from pyrevit import forms
import subprocess

try:
    subprocess.call([r'K:\Revit Standards\Dynamo\Dependencies\Download Dependencies.bat'])
    pyrevit.forms.alert("Beep boop beep... \n\nDynamo now has everything it needs to run smoothly.", "Result", warn_icon=False)
except OSError:
    pyrevit.forms.alert("K: drive not connected. Dependencies could not be downloaded.", "Error")