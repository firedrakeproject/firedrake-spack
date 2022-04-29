# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.firedrake.editable_install import EditablePythonPackage


class PyPyadjoint(EditablePythonPackage):
    '''The algorithmic differentation tool pyadjoint and add-ons.'''

    homepage = 'https://firedrakeproject.org'
    url      = 'https://github.com/dolfin-adjoint/pyadjoint.git'
    git      = 'https://github.com/dolfin-adjoint/pyadjoint.git'

    maintainers = ['connorjward', 'JDBetteridge']

    version('develop', branch='master', no_cache=True)

    depends_on('py-setuptools', type=('build', 'run'))
