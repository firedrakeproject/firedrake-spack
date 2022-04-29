# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import inspect
import os

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage
from pathlib import Path


class PyPyop2(EditablePythonPackage):
    '''Framework for performance-portable parallel computations on unstructured meshes'''

    homepage = 'https://op2.github.io/PyOP2'
    url      = 'https://github.com/OP2/PyOP2'
    git      = 'https://github.com/OP2/PyOP2'

    version('develop', branch='master', get_full_repo=True, no_cache=True)

    phases = ['install']

    depends_on('mpi')

    depends_on('py-setuptools', , type=('build', 'run'))
    depends_on('py-pytest', type=('build', 'run', 'test'))
    depends_on('py-flake8', type=('build', 'run', 'test'))
    depends_on('py-decorator@4.4.2', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-mpi4py', type=('build', 'run'))

    depends_on('firedrake.petsc', type=('build', 'link', 'run'))
    depends_on('firedrake.py-petsc4py', type=('build', 'run'))
    depends_on('firedrake.py-coffee', type=('build', 'run'))
    depends_on('firedrake.py-loopy', type=('build', 'run'))

    def install(self, spec, prefix):
        # Set CC to an MPI compiler
        if self.spec.satisfies('^intel-oneapi-mpi') or \
            self.spec.satisfies('^intel-mpi'):
            mpi_prefix = Path(self.spec['mpi'].mpicc).parent
            env['CC'] = mpi_prefix.joinpath('mpiicc')
        else:
            env['CC'] = spec['mpi'].mpicc
        super().install(spec, prefix)

    def setup_run_environment(self, env):
        super().setup_run_environment(env)
        if self.spec.satisfies('%intel') and \
            self.spec.satisfies('^intel-mpi'):
            mpi_prefix = Path(self.spec['mpi'].mpicc).parent
            env.set('PYOP2_CC', str(mpi_prefix.joinpath('mpiicc')))
            env.set('PYOP2_CXX', str(mpi_prefix.joinpath('mpiicpc')))
        if self.spec.satisfies('%clang') or \
            self.spec.satisfies('%aocc'):
            env.set('PYOP2_CC', str(self.spec['mpi'].mpicc))
            env.set('PYOP2_CXX', str(self.spec['mpi'].mpicxx))
            env.set('PYOP2_LD', 'ld.lld')

    def setup_dependent_run_environment(self, env, dependent_spec):
        super().setup_dependent_run_environment(env, dependent_spec)
        self.setup_run_environment(env)
