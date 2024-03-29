# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCgen(PythonPackage):
    """C/C++ source generation from an AST"""

    homepage = "https://github.com/inducer/cgen"
    url = "https://github.com/inducer/cgen"
    git = "https://github.com/inducer/cgen"

    version("develop", branch="main", no_cache=True)

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-pytools", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-appdirs", type=("build", "run"))
    depends_on("py-decorator", type=("build", "run"))
