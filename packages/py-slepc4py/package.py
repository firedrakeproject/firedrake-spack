# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class PySlepc4py(PythonPackage):
    """SLEPc Python bindings, Firedrake fork
    """

    homepage = "https://github.com/firedrakeproject/slepc"
    url = "https://github.com/firedrakeproject/slepc"
    git = "https://github.com/firedrakeproject/slepc"

    maintainers = ["JDBettereidge"]

    version("develop", branch="firedrake", no_cache=True)

    depends_on("py-cython", type=("build", "run"))
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))

    depends_on("firedrake.slepc")
    depends_on("firedrake.py-petsc4py", type=("build", "run"))

    @property
    def build_directory(self):
        return os.path.join(self.stage.source_path, "src", "binding", "slepc4py")
