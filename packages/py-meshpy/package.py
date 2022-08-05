# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMeshpy(PythonPackage):
    """2D/3D simplicial mesh generator interface for Python (Triangle, TetGen, gmsh)"""

    homepage = "https://documen.tician.de/meshpy/"
    pypi = "MeshPy/MeshPy-2020.1.tar.gz"

    version("2020.1", sha256="7b14eef33ccfb7974c058cea04672bfcd66e57dfcfa6a65cf01943b08964e879")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-gmsh-interop", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-pytools@2011.2:", type=("build", "run"))
