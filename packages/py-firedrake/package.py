# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json

from spack import *


class PyFiredrake(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = 'https://firedrakeproject.org'
    git      = 'https://github.com/firedrakeproject/firedrake.git'

    maintainers = ['connorjward', 'JDBetteridge']

    version('develop', branch='spack-install-v2', no_cache=True)

    # Variants
    variant('slepc', default=False,
            description='Install SLEPc along with PETSc')
    variant('mpich', default=True, description='Use MPICH as MPI provider')

    # Compatible Python versions
    depends_on('python@3.6:3.8')

    # External dependencies
    depends_on('eigen')
    depends_on('mpi')
    # depends_on('mpich', when='+mpich')
    depends_on('py-cachetools')
    depends_on('py-h5py')
    depends_on('py-matplotlib')
    depends_on('py-mpi4py')
    depends_on('py-numpy')
    depends_on('py-pkgconfig')
    depends_on('py-pip', type='build')
    depends_on('py-requests')
    depends_on('py-scipy')
    depends_on('py-setuptools')
    depends_on('py-sympy')

    # Optional external dependencies
    depends_on('slepc', when='+slepc')
    depends_on('py-slepc4py', when='+slepc')

    # Future external dependencies
    # (These should be pushed to Spack)
    depends_on('libsupermesh')
    depends_on('firedrake.py-islpy')

    # Internal dependencies
    # depends_on('firedrake.petsc@main+hdf5+superlu-dist+hypre+mumps+ptscotch')  # missing chaco and eigen
    depends_on('firedrake.libspatialindex')
    depends_on('firedrake.petsc')
    depends_on('firedrake.py-fiat')
    depends_on('firedrake.py-finat')
    depends_on('firedrake.py-petsc4py')
    depends_on('firedrake.py-pyadjoint')
    depends_on('firedrake.py-pyop2')
    depends_on('firedrake.py-tsfc')
    depends_on('firedrake.py-ufl')

    # Test dependencies
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-xdist', type='test')

    # Developer dependencies
    depends_on('py-pylint', when='@develop')

    phases = ['install']

    def install(self, spec, prefix):
        # Do an editable install if `spack develop firedrake` has been run.
        if 'dev_path' in self.spec.variants:
            self.setup_py('develop', '--prefix={}'.format(prefix))
        else:
            self.setup_py('install', '--prefix={}'.format(prefix))

    #@run_before('install')
    def install_vtk(self):
        # VTK is a pain to build in Spack so we just use the wheel on PyPI
        pip = which('pip')
        pip('install', 'vtk', '--prefix={}'.format(prefix))

    @run_after('install')
    def generate_config_file(self):
        config = {
            'libraries': {
                'EIGEN_INCLUDE_DIR': self.spec['eigen'].prefix.include,
            },
            'options': {
                'complex': False,
                'install_mode': 'spack',
                'petsc_int_type': 'int32',
                'cache_dir': '{}/.cache'.format(self.prefix),
            }
        }
        with open('{}/.configuration.json'.format(self.prefix), "w") as f:
            json.dump(config, f)
