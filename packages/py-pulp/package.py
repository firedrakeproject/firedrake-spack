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
    
    version('2.4',   sha256='d52d52b6078ea2c503b33814738866902d661cfe60d7a76251d50423e4af3ad0')
    version('2.3.1', sha256='e06660f384382a128ccf3af97458f67d48b412fc0051bddd66ae28eaabc0853e')
    version('2.3',   sha256='fcb2246faf8377b806073ce12aa182f91702a2c8c8a53594a2baed59d0ebc77c')
    version('2.2',   sha256='f5d2d10244fc4f1bb6d4fa0ff10db2605e557ef203bfa01c24f60758bef0c5ed')

    depends_on('py-setuptools', type='build')
