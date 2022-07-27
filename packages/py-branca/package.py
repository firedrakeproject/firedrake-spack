# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyBranca(PythonPackage):
    '''This library is a spinoff from folium,
    that would host the non-map-specific features.'''

    pypi = 'branca/branca-0.4.2.tar.gz'

    version('0.4.2', sha256='c111453617b17ab2bda60a4cd71787d6f2b59c85cdf71ab160a737606ac66c31')

    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
