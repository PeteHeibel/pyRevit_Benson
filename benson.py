"""list of functions used in Benson Revit addins"""

def latest_version(revit_version):
    if revit_version == '2021':
        return '2021.2'
    elif revit_version == '2022':
        return '2022.1.6'
    elif revit_version == '2023':
        return '2023.1.40'
    elif revit_version == '2024':
        return '2024.2.10'
    # elif revit_version == '2025':
    #     return '2025.1'
    else:
        warning = 'Revit {} is not supported at Benson. Please upgrade.'.format(revit_version)
        return warning