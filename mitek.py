"""list of functions used in MiTek Revit addins"""


def latest_version(revit_version):
    if revit_version == '2021':
        # actual version is 2021.1.90 but subversion reports the following
        return '2021.2'
    elif revit_version == '2022':
        return '2022.1.5'
    elif revit_version == '2023':
        return '2023.1.30'
    elif revit_version == '2024':
        return '2024.1.0'
    else:
        warning = 'Revit {} is not supported at MiTek. Please upgrade.'.format(revit_version)
        return warning