"""Check to see if you are running the latest version of Revit."""

import subprocess
from pyrevit import HOST_APP, forms

import sys
import os
sys.path.append(os.path.expandvars("%appdata%\pyRevit\Extensions\Benson.extension"))
from benson import latest_version 

revit_version = HOST_APP.version
revit_subversion = HOST_APP.subversion
# forms.toaster.get_toaster()
# revit_icon = r"%appdata%\pyRevit\Extensions\Benson.extension\images\Revit Icon.png"
hyperlink = "<a href=\"https://mitek.sharepoint.com/sites/CustomCurtainwallTraining/SitePages/Revit-Training/001_Revit-Installation-Configuration.aspx#install-update-via-autodesk-access\">Revit Installation Help</a>"
 
if revit_subversion == latest_version(revit_version):
    # forms.toaster.send_toast(message, title='No Action Required', appid='Autodesk Revit', icon=revit_icon)
    forms.alert("You are running the latest version of Revit.", sub_msg="Revit " + revit_subversion, title="No Action Required", warn_icon=False)
    
else:
    # forms.toaster.send_toast(latest_version(revit_version), title='Please Update Revit', appid='Autodesk Revit', icon=revit_icon, click=sharePoint_site)
    forms.alert("Please update Revit to the latest subversion: " + revit_subversion, sub_msg="See the Help link below for more information.", title="Update Required",footer=hyperlink)
    
    # Launch Autodesk Access app after task dialog is closed
    exe_name = "AdskAccessCore.exe"
    root_directory = "C:\\Program Files\\Autodesk"
    for path, _, files in os.walk(root_directory):
        if exe_name in files:
            exe_path = os.path.join(path, exe_name)
            subprocess.call([exe_path])