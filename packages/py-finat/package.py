# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyFinat(PythonPackage):
    '''A smarter library of finite elements'''

    homepage = 'https://firedrakeproject.org/'
    url      = 'https://github.com/FInAT/FInAT'
    git      = 'https://github.com/FInAT/FInAT'
   
    version('develop', branch='master')

    depends_on('py-numpy', type=('build','run'))
    depends_on('py-sympy', type=('build','run'))
