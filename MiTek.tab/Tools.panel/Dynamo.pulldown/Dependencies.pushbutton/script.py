from pyrevit import revit, HOST_APP
import subprocess

source_directory = ""
destination_directory = ""

# create code that copies Dynamo packages from network to local machine
# replace version if already exists, but do not overwrite in case others have custom configurations
# include a try/except statement that checks if the K:/ drive exists (where scripts are stored)

# review for proper function:
# https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy







# _____________________________________________________________________________

# not sure I need to do this if I just copy all packages/folders at once
# even if they've never opened Dynamo, it should work to just have the folder waiting

# if HOST_APP.version == 2021:
#     pass
# elif HOST_APP.version == 2022:
#     pass
# elif HOST_APP.version == 2023:
#     pass
# elif HOST_APP.version == 2024:
#     pass