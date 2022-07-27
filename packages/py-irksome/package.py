# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyIrksome(EditablePythonPackage):
    '''Solvers for Implicit Runge Kutta methods'''

    homepage = 'https://firedrakeproject.github.io/Irksome/'
    git      = 'https://github.com/firedrakeproject/Irksome/'

    version('develop', branch='master', no_cache=True)

    depends_on('py-firedrake', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
