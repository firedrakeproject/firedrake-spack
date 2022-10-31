# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class PyMpi4pyFft(PythonPackage):
    """The Python package mpi4py-fft is a tool primarily for working with Fast Fourier Transforms (FFTs) of (large) multidimensional arrays
    """

    homepage = "https://mpi4py-fft.readthedocs.io/en/latest/introduction.html"
    url = "https://github.com/mpi4py/mpi4py-fft"
    git = "https://github.com/mpi4py/mpi4py-fft.git"

    maintainers = ["JHopeCollins"]

    version("master", branch="master", no_cache=True)
    version("2.0.2", sha256="2331edd30ef7c903391e667bdf8ac079ddf4012d", no_cache=True)

    depends_on("python@3.3:", type=("build", "run"))
    depends_on("py-cython", type=("build"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))

    # really we depend on FFTW, but this is built with PETSc
    #   PETSc needs to set the environment variables FFTW_{INCLUDE,LIBRARY}_DIR
    depends_on("fftw", type=("build", "run"))

