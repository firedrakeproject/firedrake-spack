from spack import *
from spack.pkg.builtin.slepc import Slepc as OrigSlepc


class Slepc(OrigSlepc):
    homepage = "https://github.com/firedrakeproject/slepc.git"
    git = "https://github.com/firedrakeproject/slepc.git"

    version("develop", branch="firedrake", no_cache=True)

    depends_on("firedrake.petsc@develop", when="@develop")

    # Some spack bug: https://github.com/spack/spack/issues/27508
    @run_before("install")
    def fixup_bug(self):
        spack.pkg.builtin.slepc.python = python
