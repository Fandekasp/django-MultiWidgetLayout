"""
An enhanced class based on MultiWidget that lets you easily control the
rendering using a layout
"""

__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 0,
}


def get_version():
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    return ''.join(vers)

__version__ = get_version()
