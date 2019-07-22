# API wrapper for Rez

from rez.resolved_context import ResolvedContext as env
from rez.packages_ import iter_packages as find
from rez.package_copy import copy_package
from rez.package_filter import Rule, PackageFilterList
from rez.package_repository import package_repository_manager
from rez.packages_ import Package
from rez.utils.formatting import PackageRequest
from rez.config import config
from rez import __version__ as version
from rez.exceptions import (
    PackageFamilyNotFoundError,
    RexUndefinedVariableError,
    RexError,
    PackageCommandError,
    RezError,
)

try:
    from rez import project
except ImportError:
    # Vanilla Rez
    project = "rez"


__all__ = [
    "env",
    "find",
    "config",
    "version",
    "project",
    "copy_package",
    "package_repository_manager",

    # Classes
    "Package",
    "PackageRequest",

    # Exceptions
    "PackageFamilyNotFoundError",
    "RexUndefinedVariableError",
    "RexError",
    "PackageCommandError",
    "RezError",

    # Filters
    "Rule",
    "PackageFilterList",
]