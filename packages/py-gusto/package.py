# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGusto(PythonPackage):
    '''Three dimensional atmospheric dynamical core using the Gung Ho numerics.'''

    homepage = 'http://firedrakeproject.org/gusto/'
    url      = 'https://github.com/firedrakeproject/gusto'
    git      = 'https://github.com/firedrakeproject/gusto'
    
    version('develop', branch='master')

    depends_on('py-setuptools', type='build')

    depends_on('py-firedrake')
    depends_on('py-netcdf4')
