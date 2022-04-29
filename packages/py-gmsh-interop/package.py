# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGmshInterop(PythonPackage):
    '''Interoperability with Gmsh for Python'''

    homepage = 'https://github.com/inducer/gmsh_interop'
    pypi     = 'gmsh_interop/gmsh_interop-2021.1.tar.gz'

    version('2021.1', sha256='15cb626ee782d67cffc931bb0b16063ab60c40bb5b49353730314f7fc2b52fd8')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-pytools', type=('build', 'run'))
    depends_on('py-setuptools', , type=('build', 'run'))
