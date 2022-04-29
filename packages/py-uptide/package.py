# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyUptide(PythonPackage):
    '''python package for tidal calculations'''

    pypi = 'uptide/uptide-1.0.tar.gz'

    version('1.0', sha256='ded7fb23bb6daae74fbb2b2a393b73e07036b502ac24947a20f12e47812e1435')

    depends_on('py-setuptools', type=('build', 'run'))
