# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyPyop2(PythonPackage):
    '''Framework for performance-portable parallel computations on unstructured meshes'''

    homepage = 'https://op2.github.io/PyOP2'
    url      = 'https://github.com/OP2/PyOP2'
    git      = 'https://github.com/OP2/PyOP2'

    version('develop', branch='master', no_cache=True)

    phases = ['install']

    depends_on('py-setuptools', type='build')
    depends_on('py-pytest', type='build')
    depends_on('py-flake8', type='build')
    depends_on('py-decorator')
    depends_on('py-cython')
    depends_on('py-numpy')
    depends_on('py-mpi4py')

    depends_on('firedrake.petsc')
    depends_on('firedrake.py-petsc4py')
    depends_on('firedrake.py-coffee')
    depends_on('firedrake.py-loopy')

    def install(self, spec, prefix):
        # Do an editable install if `spack develop py-pyop2` has been run.
        with working_dir(self.build_directory):
            python = which('python')
            if 'dev_path' in self.spec.variants:
                python('setup.py', 'develop', '--prefix={}'.format(prefix))
            else:
                python('setup.py', 'install', '--prefix={}'.format(prefix))

    def setup_run_environment(self, env):
        # Needs upstream changes in PYOP2:
        if self.spec.satisfies('%intel'):
            mpi_prefix = Path(self.spec['mpi'].mpicc).parent
            env.set('PYOP2_BACKEND_COMPILER', str(mpi_prefix.joinpath(mpi.mpicc)))
            env.set('PYOP2_CC', str(mpi_prefix.joinpath(mpi.mpicc)))
            env.set('PYOP2_CXX', str(mpi_prefix.joinpath(mpi.mpicxx)))
        if self.spec.satisfies('%clang'):
            env.set('PYOP2_BACKEND_COMPILER', 'clang')
            env.set('PYOP2_CC', str(self.spec['mpi'].mpicc))
            env.set('PYOP2_CXX', str(self.spec['mpi'].mpicxx))
            env.set('PYOP2_LD', str(self.spec['llvm'].bin) + '/ld.lld')
