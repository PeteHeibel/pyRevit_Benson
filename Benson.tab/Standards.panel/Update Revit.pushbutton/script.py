"""Check to see if you are running the latest version of Revit."""

import subprocess
import webbrowser
from pyrevit import coreutils, HOST_APP, forms

import sys
import os
sys.path.append(os.path.expandvars("%appdata%\pyRevit\Extensions\Benson.extension"))
from benson import latest_version 

revit_version = HOST_APP.version
revit_subversion = HOST_APP.subversion
# forms.toaster.get_toaster()
# revit_icon = r"%appdata%\pyRevit\Extensions\Benson.extension\images\Revit Icon.png"
sharePoint_site = 'https://mitek.sharepoint.com/sites/CustomCurtainwallTraining/SitePages/Revit-Training/001_Revit-Installation-Configuration.aspx'
    
if revit_subversion == latest_version(revit_version):
    message = 'You are running the latest version of Revit: ' + revit_subversion
    # forms.toaster.send_toast(message, title='No Action Required', appid='Autodesk Revit', icon=revit_icon)
    forms.alert(message, title="No Action Required", warn_icon=False)
else:
    # forms.toaster.send_toast(latest_version(revit_version), title='Please Update Revit', appid='Autodesk Revit', icon=revit_icon, click=sharePoint_site)
    forms.alert("Please update Revit " + revit_version + " to the latest subversion: " + revit_subversion, title="Update Required")
    subprocess.call("C:\Program Files\Autodesk\AdODIS\V1\Access\AdskAccessCore.exe")
    webbrowser.open(sharePoint_site)