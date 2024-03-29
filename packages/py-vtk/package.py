# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class PyVtk(CMakePackage):
    """Builds a minimal VTK and generated Python package from it"""

    homepage = "https://github.com/firedrakeproject/VTKPythonPackage"
    url = "http://www.vtk.org"
    git = "https://gitlab.kitware.com/vtk/vtk"
    maintainers = ["JDBetteridge"]

    version("9.1.0", tag="v9.1.0", preferred=True)
    version("9.0.3", tag="v9.0.3")
    version("9.0.1", tag="v9.0.1")
    version("9.0.0", tag="v9.0.0")
    version("8.2.0", tag="v8.2.0")
    version("8.1.2", tag="v8.1.2")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-setuptools@:62.0.0", type="build")
    depends_on("ninja", type="build")

    variant("build_type", default="Release", description="CMake build type")
    generator = "Ninja"

    def cmake_args(self):
        args = [
            self.define("BUILD_SHARED_LIBS", "ON"),
            self.define("BUILD_TESTING", "OFF"),
            self.define("VTK_PYTHON_VERSION", 3),
            self.define("VTK_WRAP_PYTHON", "ON"),
            self.define("VTK_WHEEL_BUILD", "ON"),
            self.define("VTK_GROUP_ENABLE_Imaging", "NO"),
            self.define("VTK_GROUP_ENABLE_MPI", "NO"),
            self.define("VTK_GROUP_ENABLE_Qt", "NO"),
            self.define("VTK_GROUP_ENABLE_StandAlone", "NO"),
            self.define("VTK_GROUP_ENABLE_Views", "NO"),
            self.define("VTK_GROUP_ENABLE_Web", "NO"),
            self.define("VTK_MODULE_ENABLE_VTK_CommonCore", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_CommonExecutionModel", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_CommonMath", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_CommonMisc", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_CommonSystem", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_CommonTransforms", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_IOCore", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_IOLegacy", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_IOParallelXML", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_IOXML", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_IOXMLParser", "YES"),
            self.define("VTK_MODULE_ENABLE_VTK_ParallelCore", "YES"),
        ]
        return args

    @run_after("install")
    def pip_install(self):
        with working_dir(self.build_directory):
            pip("install", "--prefix={}".format(prefix), ".")
