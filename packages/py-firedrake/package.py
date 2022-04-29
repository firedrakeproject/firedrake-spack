# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json
import os

from collections import namedtuple
from pathlib import Path
from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage

fields = ['mpicc', 'mpicxx', 'mpif90', 'mpiexec']
MPI = namedtuple('MPI', fields)

class FiredrakeConfiguration(dict):
    '''A dictionary extended to facilitate the storage of Firedrake
    configuration information.'''
    def __init__(self, args=None):
        super(FiredrakeConfiguration, self).__init__()

        '''A record of the persistent options in force.'''
        self["options"] = {}
        '''Relevant environment variables.'''
        self["environment"] = {}
        '''Additional packages installed via the plugin interface.'''
        self["additions"] = []

        if args:
            for o in self._persistent_options:
                if o in args.__dict__.keys():
                    self["options"][o] = args.__dict__[o]

    _persistent_options = ["package_manager",
                           "minimal_petsc", "mpicc", "mpicxx", "mpif90", "mpiexec", "disable_ssh",
                           "honour_petsc_dir", "with_parmetis",
                           "slepc", "packages", "honour_pythonpath",
                           "opencascade", "tinyasm",
                           "petsc_int_type", "cache_dir", "complex", "remove_build_files", "with_blas"]


class PyFiredrake(EditablePythonPackage):
    '''Firedrake is an automated system for the portable solution of partial
    differential equations using the finite element method (FEM)'''

    homepage = 'https://firedrakeproject.org'
    git      = 'https://github.com/firedrakeproject/firedrake.git'

    maintainers = ['connorjward', 'JDBetteridge']

    version('develop', branch='master', get_full_repo=True, no_cache=True)

    # Variants
    variant(
        'minimal-petsc',
        default=False,
        description='Build PETSc with minimal packages for Firedrake',
    )
    variant(
        'complex',
        default=False,
        description='Install Firedrake in complex mode'
    )
    variant(
        '64-bit-indices',
        default=False,
        description='Install PETSc using 64bit indices'
    )
    variant(
        'slepc',
        default=False,
        description='Install SLEPc and slepc4py'
    )

    # Compatible Python versions
    depends_on('python@3.6:3.10', type=('build', 'link', 'run'))

    # External dependencies
    depends_on('eigen@3.3.3', type=('build', 'link', 'run'))
    depends_on('libspatialindex', type=('build', 'link', 'run'))
    depends_on('mpi', type=('build', 'link', 'run'))
    depends_on('py-pip', type=('build', 'run'))
    depends_on('py-cachetools', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-h5py', type=('build', 'run'))
    depends_on('py-matplotlib', type=('build', 'run'))
    depends_on('py-mpi4py', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-numpy ^openblas@:0.3.13', when='openblas', type=('build', 'run'))
    depends_on('py-pkgconfig', type=('build', 'run'))
    depends_on('py-requests', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    with when('%intel'):
        # Pythran cannot currently use intel compilers
        # https://github.com/serge-sans-paille/pythran/issues/892
        # The py-scipy package.py doesn't have a flag to turn this off either!
        os.environ['SCIPY_USE_PYTHRAN'] = '0'
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-sympy', type=('build', 'run'))

    # Optional external dependencies
    depends_on('slepc', when='+slepc', type=('build', 'link', 'run'))
    depends_on('py-slepc4py', when='+slepc', type=('build', 'run'))

    # Future external dependencies
    # (These should be pushed to Spack)
    depends_on('libsupermesh', type=('build', 'link', 'run'))
    depends_on('firedrake.py-islpy', type=('build', 'run'))

    # Internal dependencies
    # PETSc
    # BLAS, LAPACK, zlib (shared libraries) included by default
    # TODO:
    # --download-pastix missing for full
    # --download-ml missing for real_int32
    minimal = ' +shared +chaco +hdf5 +mpi +ptscotch +superlu-dist'
    full    = ' +hwloc +metis +netcdf-c +parallel-netcdf +suite-sparse'
    real    = ' +hypre'
    int32   = ' +mumps +scalapack'
    eigen   = ' ^eigen@3.3.3'

    depends_on('firedrake.petsc@develop' + minimal + eigen, type=('build', 'link', 'run'))  # (when='minimal-petsc')
    depends_on('firedrake.petsc@develop' + full, when='~minimal-petsc', type=('build', 'link', 'run'))
    depends_on('firedrake.petsc@develop' + real, when='~complex', type=('build', 'link', 'run'))
    depends_on('firedrake.petsc@develop' + int32, when='~64-bit-indices', type=('build', 'link', 'run'))

    depends_on('firedrake.py-fiat', type=('build', 'run'))
    depends_on('firedrake.py-finat', type=('build', 'run'))
    depends_on('firedrake.py-petsc4py', type=('build', 'run'))
    depends_on('firedrake.py-pyadjoint', type=('build', 'run'))
    depends_on('firedrake.py-pyop2', type=('build', 'run'))
    depends_on('firedrake.py-tsfc', type=('build', 'run'))
    depends_on('firedrake.py-ufl', type=('build', 'run'))
    # VTK is a pain to build in Spack so we build a minimal wheel locally
    depends_on('firedrake.py-vtk', type=('build', 'run'))

    # Test dependencies
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-xdist', type='test')
    # ~ depends_on('py-nbval', type='test')  # Package doesn't yet exist

    phases = ['install']

    def install(self, spec, prefix):
        # Set CC to an MPI compiler
        if self.spec.satisfies('%intel'):
            mpi_prefix = Path(self.spec['mpi'].mpicc).parent
            env['CC'] = mpi_prefix.joinpath('mpiicc')
        else:
            env['CC'] = spec['mpi'].mpicc
        super().install(spec, prefix)

    @run_before('install')
    def generate_config_file(self):
        config = FiredrakeConfiguration()
        if self.spec.satisfies('^intel-oneapi-mpi') or \
            self.spec.satisfies('^intel-mpi'):
            # It's difficult to pick out the Intel MPI compilers
            # We do it manually here
            mpi_prefix = Path(self.spec['mpi'].mpicc).parent
            mpi = MPI('mpiicc', 'mpiicpc', 'mpiifort')
        else:
            mpi_prefix = Path(self.spec['mpi'].prefix.bin)
            mpi = MPI(*fields)
        config['options'] = {
            'cache_dir':          '{}/.cache'.format(self.prefix),
            'complex':            '+complex' in self.spec,
            'disable_ssh':        False,
            'honour_petsc_dir':   True,
            'honour_pythonpath':  False,
            'minimal_petsc':      '+minimal-petsc' in self.spec,
            'mpicc':              str(mpi_prefix.joinpath(mpi.mpicc)),
            'mpicxx':             str(mpi_prefix.joinpath(mpi.mpicxx)),
            'mpiexec':            str(mpi_prefix.joinpath(mpi.mpiexec)),
            'mpif90':             str(mpi_prefix.joinpath(mpi.mpif90)),
            'opencascade':        False,
            'package_manager':    False,
            'packages':           [],
            'petsc_int_type':     ('int64' if '+int64' in self.spec['petsc'] else 'int32'),
            'remove_build_files': False,
            'slepc':              '+slepc' in self.spec,
            'tinyasm':            False,
            'with_blas':          self.spec['blas'].prefix.lib,
            'with_parmetis':      '+parmetis' in self.spec['petsc']
        }
        if 'dev_path' in self.spec.variants:
            config_file = '{}/firedrake_configuration/configuration.json'.format(self.spec.variants['dev_path'].value)
        else:
            config_file = '{}/firedrake_configuration/configuration.json'.format(self.prefix)
        with open(config_file, 'w') as fh:
            from pprint import pprint
            pprint(json.dumps(config))
            json.dump(config, fh)

    def setup_run_environment(self, env):
        super().setup_run_environment(env)
        env.set('OMP_NUM_THREADS', '1')
        env.set('OPENBLAS_NUM_THREADS', '1')

    def setup_dependent_run_environment(self, env, dependent_spec):
        super().setup_dependent_run_environment(env, dependent_spec)
        self.setup_run_environment(env)
