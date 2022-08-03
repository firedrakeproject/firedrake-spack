# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyTinyasm(EditablePythonPackage):
    '''TinyASM: A simple implementation of PETSc's ASM preconditioner that
    is focussed on the case of small matrices. We avoid the overhead of
    KSP and PC objects for each block and just use the dense inverse.'''

    homepage = 'https://github.com/florianwechsung/TinyASM.git'
    url      = 'https://github.com/florianwechsung/TinyASM.git'
    git      = 'https://github.com/florianwechsung/TinyASM.git'

    version('develop', branch='master', submodules=True)

    depends_on('cmake', type=('build',))
    depends_on('petsc', type=('build', 'run'))
    depends_on('py-firedrake', type=('build', 'run'))
    depends_on('py-petsc4py', type=('build', 'run'))
    depends_on('py-pybind11', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
