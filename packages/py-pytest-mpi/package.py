# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyPytestMpi(EditablePythonPackage):
    """Pytest plugin that lets you run tests in parallel with MPI."""

    homepage = "https://github.com/firedrakeproject/pytest-mpi"
    url = "https://github.com/firedrakeproject/pytest-mpi"
    git = "https://github.com/firedrakeproject/pytest-mpi"

    version("develop", branch="main", get_full_repo=True, no_cache=True)

    phases = ["install"]

    depends_on("mpi")

    depends_on("py-hatchling", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run", "test"))
    depends_on("py-mpi4py", type=("build", "run"))

    def install(self, spec, prefix):
        # Set CC to an MPI compiler
        if self.spec.satisfies("^intel-oneapi-mpi") or self.spec.satisfies("^intel-mpi"):
            mpi_prefix = Path(self.spec["mpi"].mpicc).parent
            env["CC"] = str(mpi_prefix.joinpath("mpiicc"))
        else:
            env["CC"] = spec["mpi"].mpicc
        super().install(spec, prefix)
