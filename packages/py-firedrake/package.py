# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFiredrake(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = 'https://firedrakeproject.org'
    git      = 'https://github.com/firedrakeproject/firedrake.git'

    maintainers = ['connorjward', 'JDBetteridge']

    version('develop', branch='master')

    # Variants
    variant('slepc', default=False,
            description='Install SLEPc along with PETSc')

    # Compatible Python versions
    depends_on('python@3.6:3.9')

    # External dependencies
    depends_on('eigen')
    depends_on('mpi')
    depends_on('py-cachetools')
    depends_on('py-h5py')
    depends_on('py-matplotlib')
    depends_on('py-mpi4py')
    depends_on('py-numpy')
    depends_on('py-pkgconfig')
    depends_on('py-requests')
    depends_on('py-scipy')
    depends_on('py-setuptools')
    depends_on('py-sympy')
    # depends_on('vtk@9.0.1+python')  # llvm takes about 10 years to compile

    # Optional external dependencies
    depends_on('slepc', when='+slepc')
    depends_on('py-slepc4py', when='+slepc')

    # Future external dependencies
    # (These should be pushed to Spack)
    depends_on('firedrake.libsupermesh')
    depends_on('firedrake.py-islpy')

    # Internal dependencies
    depends_on('firedrake.petsc@main+hdf5+superlu-dist+hypre+mumps+ptscotch')  # missing chaco and eigen
    depends_on('firedrake.py-fiat')
    depends_on('firedrake.py-finat')
    depends_on('firedrake.py-petsc4py@main')
    depends_on('firedrake.py-pyadjoint')
    depends_on('firedrake.py-pyop2')
    depends_on('firedrake.py-tsfc')
    depends_on('firedrake.py-ufl')

    # Test dependencies
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-xdist', type='test')

    # Developer dependencies
    depends_on('py-pylint', when='@develop')

    def install(self, spec, prefix):
        # Do an editable install if `spack develop firedrake` has been run.
        if "dev_path" in spec["py-firedrake"].variants:
            self.setup_py("develop")
        else:
            self.setup_py("install")
