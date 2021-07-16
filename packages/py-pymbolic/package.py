# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPymbolic(PythonPackage):
    '''A simple package to do symbolic math (focus on code gen and DSLs)'''

    homepage = 'http://mathema.tician.de/software/pymbolic'
    url      = 'https://github.com/inducer/pymbolic'
    git      = 'https://github.com/inducer/pymbolic'

    version('develop', branch='main', no_cache=True)
    version('2019.2', tag='v2019.2')
    version('2019.1', tag='v2019.1')
    version('2017.1', tag='v2017.1')

    depends_on('py-setuptools', type='build')
    depends_on('py-pytools')
    depends_on('py-six')
