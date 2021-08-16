# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyIcepack(PythonPackage):
    '''Finite element modeling of glaciers and ice sheets.'''

    homepage = 'https://icepack.github.io/'
    git      = 'https://github.com/icepack/icepack/'
    
    version('develop', branch='master', no_cache=True)

    depends_on('py-firedrake')
    depends_on('py-geojson')  # TODO
    depends_on('py-gmsh')  # TODO
    depends_on('py-matplotlib')
    depends_on('py-meshio')  # TODO
    depends_on('py-meshpy')  # TODO
    depends_on('py-netcdf4')
    depends_on('py-numpy')
    depends_on('py-pooch')
    depends_on('py-rasterio@1.0.26:')
    depends_on('py-scipy')
    depends_on('py-setuptools', type='build')
    depends_on('py-shapely')
    depends_on('py-tqdm')
