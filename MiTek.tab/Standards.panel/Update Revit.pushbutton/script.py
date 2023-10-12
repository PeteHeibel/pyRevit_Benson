"""Check to see if you are running the latest version of Revit."""

import subprocess
from pyrevit import coreutils, HOST_APP, forms

import sys
sys.path.append(r"%appdata%\pyRevit\Extensions\MiTek.extension")
from mitek import latest_version 

revit_version = HOST_APP.version
revit_subversion = HOST_APP.subversion
forms.toaster.get_toaster()
sharePoint_site = 'https://mitek.sharepoint.com/sites/CustomCurtainwallTraining/SitePages/Revit-Training/001_Revit-Installation-Configuration.aspx'
revit_icon = r"%appdata%\pyRevit\Extensions\MiTek.extension\images\Revit Icon.png"
    
if revit_subversion == latest_version(revit_version):
    message = 'You are running the latest version of Revit: ' + revit_subversion
    forms.toaster.send_toast(message, title='No Action Required', appid='Autodesk Revit', icon=revit_icon)
else:
    forms.toaster.send_toast(latest_version(revit_version), title='Please Update Revit', appid='Autodesk Revit', icon=revit_icon, click=sharePoint_site)
    subprocess.call("C:\Program Files\Autodesk\AdODIS\V1\Setup\AdskAccessCore.exe")

# troubleshooting
#print(revit_subversion)