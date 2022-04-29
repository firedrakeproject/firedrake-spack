# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage

class PyFiat(EditablePythonPackage):
    '''FIAT: FInite element Automatic Tabulator'''

    homepage = 'https://fenicsproject.org/'
    url      = 'https://github.com/firedrakeproject/fiat'
    git      = 'https://github.com/firedrakeproject/fiat'

    version('develop', branch='master')

    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-numpy', type=('build','run'))
    depends_on('py-sympy', type=('build','run'))
