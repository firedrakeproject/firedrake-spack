# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFolium(PythonPackage):
    """Python Data. Leaflet.js Maps."""

    homepage = "https://python-visualization.github.io/folium/"
    git = "https://github.com/python-visualization/folium/"

    version("0.12.1", sha256="3e0cb5bc1817db67ff216af3875a45b50b453c1ae9adf5c4b610413a91b3e1cc")

    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-branca", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
