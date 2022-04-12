# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyTsfc(EditablePythonPackage):
    '''Two-stage form compiler'''

    homepage = 'https://firedrakeproject.org/'
    url      = 'https://github.com/firedrakeproject/tsfc'
    git      = 'https://github.com/firedrakeproject/tsfc'

    version('develop', branch='master', no_cache=True)

    depends_on('py-numpy')

    depends_on('firedrake.py-coffee')
    depends_on('firedrake.py-fiat')
    depends_on('firedrake.py-finat')
    depends_on('firedrake.py-ufl')

