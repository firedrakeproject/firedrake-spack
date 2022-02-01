# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyFiat(PythonPackage):
    '''FIAT: FInite element Automatic Tabulator'''

    homepage = 'https://fenicsproject.org/'
    url      = 'https://github.com/firedrakeproject/fiat'
    git      = 'https://github.com/firedrakeproject/fiat'

    version('develop', branch='master')

    depends_on('py-setuptools', type='build')
    depends_on('py-numpy', type=('build','run'))
    depends_on('py-sympy', type=('build','run'))

    # See https://github.com/xianyi/OpenBLAS/issues/3225
    # ~ depends_on('openblas@:0.3.13', when='blas=openblas')
