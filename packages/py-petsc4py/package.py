# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class PyPetsc4py(PythonPackage):
    """PETSc, pronounced PET-see (the S is silent), is a suite of data structures
    and routines for the scalable (parallel) solution of scientific applications
    modeled by partial differential equations.
    """

    homepage = "https://www.mcs.anl.gov/petsc/"
    url = "https://github.com/firedrakeproject/petsc"
    git = "https://github.com/firedrakeproject/petsc"

    maintainers = ["connorjward"]

    version("develop", branch="firedrake", no_cache=True)

    depends_on("py-cython", type=("build", "run"))
    depends_on("python@2.6:2.8,3.3:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))

    depends_on("firedrake.petsc")

    @property
    def build_directory(self):
        return os.path.join(self.stage.source_path, "src", "binding", "petsc4py")
