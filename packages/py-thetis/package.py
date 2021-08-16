# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyThetis(PythonPackage):
    '''Finite element flow solver for simulating coastal and estuarine flows.'''

    homepage = 'https://thetisproject.org/'
    url      = 'https://github.com/thetisproject/thetis'
    git      = 'https://github.com/thetisproject/thetis'
    
    version('develop', branch='master')

    depends_on('py-setuptools', type='build')

    depends_on('py-firedrake')
    depends_on('py-netcdf4')
    depends_on('py-pyproj')
    depends_on('py-pytz')
    depends_on('py-scipy')
    depends_on('py-uptide')  # TODO
