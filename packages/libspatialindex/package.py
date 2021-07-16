# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libspatialindex(CMakePackage):
    '''C++ implementation of R*-tree, an MVR-tree and a TPR-tree with C API'''

    homepage = 'http://libspatialindex.github.com/'
    url      = 'https://github.com/firedrakeproject/libspatialindex'
    git      = 'https://github.com/firedrakeproject/libspatialindex'

    version('develop', branch='master', no_cache=True)
