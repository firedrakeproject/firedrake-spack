# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json

from spack import *

class FiredrakeConfiguration(dict):
    """A dictionary extended to facilitate the storage of Firedrake
    configuration information."""
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

class PyFiredrake(PythonPackage):
    '''Firedrake is an automated system for the portable solution of partial
    differential equations using the finite element method (FEM)'''

    homepage = 'https://firedrakeproject.org'
    git      = 'https://github.com/firedrakeproject/firedrake.git'

    maintainers = ['connorjward', 'JDBetteridge']

    version('develop', branch='master', get_full_repo=True, no_cache=True)

    # Variants
    # ~ variant('slepc', default=False,
            # ~ description='Install SLEPc along with PETSc')
    variant('mpich', default=True, description='Use MPICH as MPI provider')

    # Compatible Python versions
    depends_on('python@3.6:3.10')

    # External dependencies
    depends_on('eigen@3.3.3')
    depends_on('mpi')
    # depends_on('mpich', when='+mpich')
    depends_on('py-pip', type=('build', 'run'))
    depends_on('py-cachetools')
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-h5py')
    depends_on('py-matplotlib')
    depends_on('py-mpi4py')
    depends_on('py-numpy ^openblas@:0.3.13')
    depends_on('py-pkgconfig')
    depends_on('py-requests')
    depends_on('py-scipy')
    depends_on('py-setuptools')
    depends_on('py-sympy')

    # Optional external dependencies
    # ~ depends_on('slepc', when='+slepc')
    # ~ depends_on('py-slepc4py', when='+slepc')

    # Future external dependencies
    # (These should be pushed to Spack)
    depends_on('libsupermesh ^mpich')
    depends_on('firedrake.py-islpy')

    # Internal dependencies
    depends_on('firedrake.libspatialindex')
    depends_on('firedrake.py-fiat')
    depends_on('firedrake.py-finat')
    depends_on('firedrake.petsc')
    depends_on('firedrake.py-petsc4py')
    depends_on('firedrake.py-pyadjoint')
    depends_on('firedrake.py-pyop2')
    depends_on('firedrake.py-tsfc')
    depends_on('firedrake.py-ufl')
    # VTK is a pain to build in Spack so we just use the wheel ~on PyPI~ locally
    depends_on('firedrake.py-vtk')

    # Test dependencies
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-xdist', type='test')

    # Make Firedrake configuration not depend on firedrake-install
    # ~ patch('config.patch')

    phases = ['install']

    def install(self, spec, prefix):
        print('INSTALL')
        print('prefix:', prefix)
        try:
            print('spec.devpath', spec.devpath)
        except:
            pass
        # Do an editable install if `spack develop firedrake` has been run.
        with working_dir(self.build_directory):
            python = which('python')
            if 'dev_path' in self.spec.variants:
                python('setup.py', 'develop', '--prefix={}'.format(prefix))
            else:
                python('setup.py', 'install', '--prefix={}'.format(prefix))

    @run_before('install')
    def generate_config_file(self):
        print('BEFORE INSTALL')
        config = FiredrakeConfiguration()
        config['options'] = {
            'cache_dir':          '{}/.cache'.format(self.prefix),
            'complex':            False,
            'disable_ssh':        False,
            'honour_petsc_dir':   True,
            'honour_pythonpath':  False,
            'minimal_petsc':      False,
            'mpicc':              '{}/mpicc'.format(self.spec['mpi'].prefix.bin),
            'mpicxx':             '{}/mpicxx'.format(self.spec['mpi'].prefix.bin),
            'mpiexec':            '{}/mpiexec'.format(self.spec['mpi'].prefix.bin),
            'mpif90':             '{}/mpif90'.format(self.spec['mpi'].prefix.bin),
            'opencascade':        False,
            'package_manager':    False,
            'packages':           [],
            'petsc_int_type':     'int32',
            'remove_build_files': False,
            'slepc':              False,
            'tinyasm':            False,
            'with_blas':          None,
            'with_parmetis':      False
        }
        print('self.prefix:', self.prefix)
        print('self.spec.prefix:', self.spec.prefix)
        print(self.spec.variants)
        print('self.spec.variants[\'dev_path\'].value:', self.spec.variants['dev_path'].value)
        if 'dev_path' in self.spec.variants:
            config_file = '{}/firedrake_configuration/configuration.json'.format(self.spec.variants['dev_path'].value)
        else:
            config_file = '{}/firedrake_configuration/configuration.json'.format(self.prefix)
        with open(config_file, 'w') as fh:
            from pprint import pprint
            pprint(json.dumps(config))
            json.dump(config, fh)

    def setup_run_environment(self, env):
        env.set('OMP_NUM_THREADS', 1)
        env.set('OPENBLAS_NUM_THREADS', 1)
