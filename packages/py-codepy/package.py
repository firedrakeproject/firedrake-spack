# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCodepy(PythonPackage):
    """Generate and execute native code at run time, from Python"""

    homepage = "http://mathema.tician.de/software/codepy"
    url = "https://github.com/inducer/codepy"
    git = "https://github.com/inducer/codepy"

    version("develop", branch="main")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-pytools", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-appdirs", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-cgen", type=("build", "run"))
