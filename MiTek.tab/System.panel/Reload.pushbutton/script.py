"""Reload pyRevit into new session."""

from pyrevit import script
from pyrevit.loader import sessionmgr
from pyrevit.loader import sessioninfo

import subprocess
subprocess.call(["echo", "Updating 'MiTek' Revit addin..."])
subprocess.call(["cmd", "/c", "pyrevit extensions update MiTek"])

res = True

if res:
    logger = script.get_logger()
    results = script.get_results()

    # re-load pyrevit session.
    logger.info('Reloading....')
    sessionmgr.reload_pyrevit()

    results.newsession = sessioninfo.get_session_uuid()