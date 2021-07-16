# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPulp(PythonPackage):
    '''A python Linear Programming API'''

    homepage = 'http://coin-or.github.io/pulp/'
    url      = 'https://github.com/coin-or/pulp/archive/refs/tags/2.4.tar.gz'
    git      = 'https://github.com/coin-or/pulp'
    
    version('1.6.7', tag='1.6.7')

    depends_on('py-setuptools', type='build')
