# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class PyPetsc4py(PythonPackage):
    """This package provides Python bindings for the PETSc package.
    """

    homepage = "https://gitlab.com/petsc/petsc4py"
    url      = "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc4py-3.15.0.tar.gz"
    git='https://github.com/firedrakeproject/petsc'

    maintainers = ['dalcinl', 'balay']

    version('develop', branch='firedrake', no_cache=True)

    patch('ldshared-dev.patch')

    depends_on('py-cython', type='build')
    depends_on('python@2.6:2.8,3.3:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-mpi4py', when='+mpi', type=('build', 'run'))

    depends_on('firedrake.petsc')

    @property
    def build_directory(self):
        return os.path.join(self.stage.source_path, 'src', 'binding', 'petsc4py')
