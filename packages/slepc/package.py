from spack import *
from spack.pkg.builtin.slepc import Slepc as OrigSlepc


class Slepc(OrigSlepc):
    homepage = "https://github.com/firedrakeproject/slepc.git"
    git = "https://github.com/firedrakeproject/slepc.git"

    version("develop", branch="firedrake", no_cache=True)
