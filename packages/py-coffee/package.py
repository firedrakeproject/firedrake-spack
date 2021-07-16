# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCoffee(PythonPackage):
    '''COFFEE - A COmpiler For Fast Expression Evaluation'''

    homepage = 'https://github.com/coneoproject/COFFEE'
    url      = 'https://github.com/coneoproject/COFFEE'
    git      = 'https://github.com/coneoproject/COFFEE'
    
    version('develop', branch='master')
    
    depends_on('py-setuptools', type='build')
    depends_on('py-pulp')
    depends_on('py-numpy')
    depends_on('py-networkx')
    depends_on('py-six')
