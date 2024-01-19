import pyrevit
from pyrevit import revit, DB

try:
    # Access the current Revit document
    doc = revit.doc

    # Get the Revit application
    app = doc.Application

    # Find the Dynamo Player command ID
    command_id = app.LookupCommandId("ID_PLAYLIST_DYNAMO")

    # Execute the command
    app.PostCommand(command_id)

except Exception as e:
    pyrevit.report_error("Error launching Dynamo Player:", e)  # Use PyRevit's error reporting