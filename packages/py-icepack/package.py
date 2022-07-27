# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyIcepack(EditablePythonPackage):
    '''Finite element modeling of glaciers and ice sheets.'''

    homepage = 'https://icepack.github.io/'
    git      = 'https://github.com/icepack/icepack/'

    version('develop', branch='master', no_cache=True)

    depends_on('py-firedrake', type=('build', 'run'))
    depends_on('py-geojson', type=('build', 'run'))
    depends_on('py-pygmsh', type=('build', 'run'))
    depends_on('py-matplotlib', type=('build', 'run'))
    depends_on('py-meshio', type=('build', 'run'))
    depends_on('py-meshpy', type=('build', 'run'))
    depends_on('py-netcdf4', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-pooch', type=('build', 'run'))
    depends_on('py-rasterio@1.0.26:', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-shapely', type=('build', 'run'))
    depends_on('py-tqdm', type=('build', 'run'))
