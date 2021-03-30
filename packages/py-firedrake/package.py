# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFiredrake(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = 'https://firedrakeproject.org'
    git      = 'https://github.com/firedrakeproject/firedrake.git'

    maintainers = ['connorjward', 'JDBetteridge']

    version('master', branch='master')

    depends_on('python@3.6:')
    depends_on('py-setuptools', type='build')
    depends_on('firedrake.petsc')
