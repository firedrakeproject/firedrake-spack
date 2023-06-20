from spack.pkg.builtin.py_setuptools import PySetuptools as OrigPySetuptools


class PyNewsetuptools(OrigPySetuptools):
    """This is a duplicate package to allow installing UFL which requires
    a very recent version of setuptools (65:), ut numpy requires a very
    old version (:59)."""
    pass
