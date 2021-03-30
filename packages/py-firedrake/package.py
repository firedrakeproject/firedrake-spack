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
    #depends_on('firedrake.petsc')

    def install(self, spec, prefix):
        # import pdb; pdb.set_trace()
        #print(type(spec))
        # print(type(spec["py-firedrake"]))
        # print(dir(spec["py-firedrake"]))
        if "dev_path" in spec["py-firedrake"].variants:
            self.setup_py("develop")
        else:
            self.setup_py("install")
        # print(spec["py-firedrake"].extra_attributes)
        #print(spec.to_dict())
        #print(spec.to_dict()["spec"][0]["py-firedrake"]["parameters"]["dev_path"])#["py-firedrake"]["parameters"])
        #print("dev_path" in spec)
        #print(repr(spec))
        
