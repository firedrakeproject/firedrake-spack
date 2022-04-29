# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyCoffee(EditablePythonPackage):
    '''COFFEE - A COmpiler For Fast Expression Evaluation'''

    homepage = 'https://github.com/coneoproject/COFFEE'
    url      = 'https://github.com/coneoproject/COFFEE'
    git      = 'https://github.com/coneoproject/COFFEE'

    version('develop', branch='master')

    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-pulp', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-networkx', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
