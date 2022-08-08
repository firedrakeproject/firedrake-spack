# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFolium(PythonPackage):
    """Python Data. Leaflet.js Maps."""

    homepage = "https://python-visualization.github.io/folium/"
    url = "https://github.com/python-visualization/folium/archive/refs/tags/v0.12.1.post1.tar.gz"
    git = "https://github.com/python-visualization/folium/"

    version("0.12.1", sha256="6b2e29d62ea6499c9b25150781e759924de1862d7c5c7dc0376cf1b43a8c71b8")

    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-branca", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
