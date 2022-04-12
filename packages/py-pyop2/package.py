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

    depends_on('py-setuptools', type='build')
    depends_on('py-pytest', type='build')
    depends_on('py-flake8', type='build')
    depends_on('py-decorator@4.4.2')
    depends_on('py-cython')
    depends_on('py-numpy')
    depends_on('py-mpi4py')

    depends_on('firedrake.petsc')
    depends_on('firedrake.py-petsc4py')
    depends_on('firedrake.py-coffee')
    depends_on('firedrake.py-loopy')

    def install(self, spec, prefix):
        # Set CC to an MPI compiler
        if self.spec.satisfies('%intel'):
            mpi_prefix = Path(self.spec['mpi'].mpicc).parent
            env['CC'] = mpi_prefix.joinpath('mpiicc')
        else:
            env['CC'] = spec['mpi'].mpicc
        super().install(spec, prefix)

    def setup_run_environment(self, env):
        if self.spec.satisfies('%intel'):
            mpi_prefix = Path(self.spec['mpi'].mpicc).parent
            env.set('PYOP2_CC', str(mpi_prefix.joinpath('mpiicc')))
            env.set('PYOP2_CXX', str(mpi_prefix.joinpath('mpiicpc')))
        if self.spec.satisfies('%clang'):
            env.set('PYOP2_CC', str(self.spec['mpi'].mpicc))
            env.set('PYOP2_CXX', str(self.spec['mpi'].mpicxx))
            env.set('PYOP2_LD', 'ld.lld')

    def setup_dependent_run_environment(self, env, dependent_spec):
        super().setup_dependent_run_environment(env, dependent_spec)
        self.setup_run_environment(env)
