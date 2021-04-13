# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libsupermesh(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://bitbucket.org/libsupermesh/libsupermesh"
    url      = "https://bitbucket.org/libsupermesh/libsupermesh/downloads/libsupermesh-1.0.1.tar.gz"
    git      = "https://bitbucket.org/libsupermesh/libsupermesh"

    version('master', branch='master')
    
    depends_on('mpi')

    def cmake_args(self):
        return [
            "-DBUILD_SHARED_LIBS:BOOL=ON",
            "-DMPI_C_COMPILER={}".format(self.spec['mpi'].mpicc),
            "-DMPI_CXX_COMPILER={}".format(self.spec['mpi'].mpicxx),
            "-DMPI_Fortran_COMPILER={}".format(self.spec['mpi'].mpifc)
        ]
