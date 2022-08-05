# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libsupermesh(CMakePackage):
    """libsupermesh parallel supermeshing library"""

    homepage = "https://bitbucket.org/libsupermesh/libsupermesh"
    url = "https://bitbucket.org/libsupermesh/libsupermesh"
    git = "https://bitbucket.org/libsupermesh/libsupermesh"

    version("develop", branch="master", no_cache=True)

    variant("shared", default=True, description="Enable shared library")

    depends_on("mpi")

    # It's not clear at what point the -s flag to the Cray compiler changed
    # if we can identify this we should add version specifiers to cce
    patch("crayftn.patch", when="%cce")

    def cmake_args(self):
        args = []
        if "+shared" in self.spec:
            args.append("-DBUILD_SHARED_LIBS=ON")
        return args
