# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMeshio(PythonPackage):
    '''input/output for many mesh formats'''

    homepage = 'https://github.com/nschloe/meshio'
    pypi     = 'meshio/meshio-5.0.0.tar.gz'

    version('5.0.0', sha256='f6327c06d6171d30e0991d3dcb048751035f9cfac1f19e2444971275fd971188')

    depends_on('py-setuptools', type='build')
