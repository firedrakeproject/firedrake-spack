# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libspatialindex(CMakePackage):
    """libsupermesh parallel supermeshing library"""

    homepage = "https://github.com/firedrakeproject/libspatialindex"
    url      = "https://github.com/firedrakeproject/libspatialindex"
    git      = "https://github.com/firedrakeproject/libspatialindex"

    version('master', branch='master')
