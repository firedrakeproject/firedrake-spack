# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPygmsh(PythonPackage):
    '''Gmsh for Python'''

    homepage = 'https://github.com/nschloe/pygmsh'
    pypi     = 'pygmsh/pygmsh-7.1.11.tar.gz'

    version('7.1.11', sha256='852e17fb32c324595f82a2fb1efe29cec9ef823b5e60d00553913c97dd67dce4')

    depends_on('py-setuptools', type=('build', 'run'))
