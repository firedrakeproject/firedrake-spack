# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyLoopy(PythonPackage):
    '''A code generator for array-based code on CPUs and GPUs'''

    homepage = 'http://mathema.tician.de/software/loopy'
    url      = 'https://github.com/firedrakeproject/loopy'
    git      = 'https://github.com/firedrakeproject/loopy'

    version('develop', branch='main', submodules=True, no_cache=True)
     
    depends_on('py-setuptools', type='build')
    depends_on('py-pymbolic')
    depends_on('py-cgen')
    depends_on('py-genpy')
    depends_on('py-codepy')
    depends_on('py-mako')
    depends_on('py-islpy')
    depends_on('py-pyrsistent')
    depends_on('py-ply')

    depends_on('firedrake.py-pytools')
