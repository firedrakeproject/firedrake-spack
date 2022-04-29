# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyThetis(EditablePythonPackage):
    '''Finite element flow solver for simulating coastal and estuarine flows.'''

    homepage = 'https://thetisproject.org/'
    git      = 'https://github.com/thetisproject/thetis'

    version('develop', branch='master', no_cache=True)

    depends_on('py-firedrake', type=('build', 'run'))
    depends_on('py-netcdf4', type=('build', 'run'))
    depends_on('py-pyproj', type=('build', 'run'))
    depends_on('py-pytz', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-uptide', type=('build', 'run'))
