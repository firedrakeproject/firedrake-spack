# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGeojson(PythonPackage):
    '''Python bindings and utilities for GeoJSON'''

    pypi = 'geojson/geojson-2.5.0.tar.gz'

    version('2.5.0', sha256='6e4bb7ace4226a45d9c8c8b1348b3fc43540658359f93c3f7e03efa9f15f658a')

    depends_on('python@3.6:3.9', type=('build', 'run'))
    depends_on('py-setuptools', , type=('build', 'run'))
