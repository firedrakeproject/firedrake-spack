# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyVtk(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "/home/jbetteridge/scratch/workspace/vtk_build/dist/"
    #https://github.com/firedrakeproject/VTKPythonPackage/releases/download/firedrake_20210613/vtk-9.0.1-cp38-cp38-linux_aarch64.whl

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions here.
    # version('1.2.4')
    version(
        '9.0.1',
        url="file:///scratch/opt/spack/wheels/vtk-9.0.1-cp38-cp38-linux_aarch64.whl",
        expand=False,
        md5='5a162fee46eaaf5066a803ec5577abf7'
    )

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-pip', type='build')

    def install(self, spec, prefix):
        pip = which('pip')
        pip('install', self.stage.archive_file, '--prefix={0}'.format(prefix))

