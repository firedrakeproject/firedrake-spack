# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGenpy(PythonPackage):
    """An AST for Python code generation, in Python"""

    homepage = "https://github.com/inducer/genpy"
    url = "https://github.com/inducer/genpy"
    git = "https://github.com/inducer/genpy"

    version("develop", branch="main")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-pytools", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
