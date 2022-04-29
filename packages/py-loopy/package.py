# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyLoopy(EditablePythonPackage):
    '''A code generator for array-based code on CPUs and GPUs'''

    homepage = 'http://mathema.tician.de/software/loopy'
    url      = 'https://github.com/firedrakeproject/loopy'
    git      = 'https://github.com/firedrakeproject/loopy'

    version('develop', branch='main', submodules=True, no_cache=True)

    depends_on('py-setuptools', , type=('build', 'run'))
    depends_on('py-pymbolic', type=('build', 'run'))
    depends_on('py-cgen', type=('build', 'run'))
    depends_on('py-genpy', type=('build', 'run'))
    depends_on('py-codepy', type=('build', 'run'))
    depends_on('py-mako', type=('build', 'run'))
    depends_on('py-islpy', type=('build', 'run'))
    depends_on('py-pyrsistent', type=('build', 'run'))
    depends_on('py-ply', type=('build', 'run'))

    depends_on('firedrake.py-pytools', type=('build', 'run'))

