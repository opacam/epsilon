# -*- test-case-name: epsilon.test -*-
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from twisted.python import versions

def asTwistedVersion(packageName, versionString):
    return versions.Version(packageName, *map(int, versionString.split(".")))

version = asTwistedVersion("epsilon", __version__)
del versions

__all__ = ['__version__', 'version']
