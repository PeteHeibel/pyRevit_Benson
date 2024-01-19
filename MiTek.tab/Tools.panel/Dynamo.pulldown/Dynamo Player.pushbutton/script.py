from pyrevit import HOST_APP, UI

uiapp = HOST_APP.uiapp

uiapp.PostCommand(UI.RevitCommandId.LookupCommandId("ID_PLAYLIST_DYNAMO"))