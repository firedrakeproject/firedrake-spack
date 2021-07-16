# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPytools(PythonPackage):
    '''Pytools is a big bag of things that are 'missing' from the Python standard library.'''

    homepage = 'https://documen.tician.de/pytools/'
    url      = 'https://github.com/inducer/pytools'
    git      = 'https://github.com/inducer/pytools'

    version('develop', branch='main', no_cache=True)

    depends_on('py-setuptools', type='build')
    depends_on('py-appdirs')
    depends_on('py-numpy')
    depends_on('py-dataclasses', when='python@:3.6')
