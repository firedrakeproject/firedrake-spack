# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libsupermesh(CMakePackage):
    """libsupermesh parallel supermeshing library"""

    homepage = "https://bitbucket.org/libsupermesh/libsupermesh"
    url      = "https://bitbucket.org/libsupermesh/libsupermesh"
    git      = "https://bitbucket.org/libsupermesh/libsupermesh"

    version('master', branch='master')

    depends_on('mpi')

    variant('shared', default=True, description='Enable shared library')

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS=ON']
        if '~shared' in self.spec:
            args.remove('-DBUILD_SHARED_LIBS=ON')
        return args
