# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyLoopy(PythonPackage):
    """loopy"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/firedrakeproject/loopy"
    url      = "https://github.com/firedrakeproject/loopy"
    git = "https://github.com/firedrakeproject/loopy"

    version('firedrake', branch='firedrake' , submodules=True )
     
    depends_on('py-setuptools', type='build')
    depends_on('py-pytools')
    depends_on('py-pymbolic')
    depends_on('py-cgen')
    depends_on('py-genpy')
    depends_on('py-codepy')
    depends_on('py-mako')
    #depends_on('py-f2py')
    #depends_on('py-pyopencl')
    depends_on('py-islpy')

    depends_on('py-ply')
