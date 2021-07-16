# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyUfl(PythonPackage):
    '''UFL - Unified Form Language'''

    homepage = 'https://fenicsproject.org/'
    url      = 'https://github.com/firedrakeproject/ufl'
    git      = 'https://github.com/firedrakeproject/ufl'

    version('develop', branch='master', no_cache=True)
    
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy', type=('build','run'))
    depends_on('py-six', type=('build','run'))
