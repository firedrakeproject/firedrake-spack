# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyIslpy(PythonPackage):
    '''Python wrapper for isl, an integer set library'''

    homepage = 'https://github.com/inducer/islpy'
    url      = 'https://github.com/inducer/islpy'
    git      = 'https://github.com/inducer/islpy'

    version('develop', branch='main', submodules=True)

    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-pytest', type=('build', 'run'))
    depends_on('py-cffi', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
