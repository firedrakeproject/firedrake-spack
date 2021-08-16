# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyIrksome(PythonPackage):
    '''Solvers for Implicit Runge Kutta methods'''

    homepage = 'https://firedrakeproject.github.io/Irksome/'
    url      = 'https://github.com/firedrakeproject/Irksome/'
    git      = 'https://github.com/firedrakeproject/Irksome/'
    
    version('develop', branch='master')

    depends_on('py-setuptools', type='build')
    depends_on('py-firedrake')
