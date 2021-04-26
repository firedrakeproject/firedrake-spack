# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyadjoint(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = 'https://firedrakeproject.org'
    git      = 'https://github.com/dolfin-adjoint/pyadjoint.git'

    maintainers = ['connorjward', 'JDBetteridge']

    version('master', branch='master')

    depends_on('py-setuptools', type='build')
