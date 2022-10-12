# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.builtin.petsc import Petsc as OrigPetsc


class Petsc(OrigPetsc):
    homepage = "https://github.com/firedrakeproject/petsc.git"
    git = "https://github.com/firedrakeproject/petsc.git"

    version("develop", branch="firedrake", no_cache=True)

    # Desired variants:
    # [Alphabetical]
    # --flags:
    #   --with-c2html=0
    #   --with-cxx-dialect=C++11
    #   --with-debugging=0
    #   --with-fortran-bindings=0
    #   --with-shared-libraries=1
    # --minimal:
    #   --download-blas + lapack (!)
    #   --download-chaco (32bit)
    #   --download-eigen=/path/eigen-3.3.3.tgz (*)
    #   --download-hdf5
    #   --download-hypre (REAL)
    #   --download-mpich
    #   --download-mumps (32bit)
    #   --download-ptscotch
    #   --download-scalapack (32bit)
    #   --download-superlu_dist
    # --full: (additionally)
    #   --download-hwloc
    #   --download-metis
    #   --download-ml (32bit)(REAL)
    #   --download-netcdf
    #   --download-pastix
    #   --download-pnetcdf
    #   --download-suitesparse
    #   --download-zlib
    # --parmetis:
    #   --download-parmetis
    # --complex:
    #   --with-scalar-type=complex
    # --64bit-indices:
    #   --with-64-bit-indices
    #

    variant("chaco", default=False, description="Activates support for chaco")
    variant("eigen", default=True, description="Activates support for eigen")
    variant("netcdf-c", default=False, description="Activates support for netcdf")
    variant("parallel-netcdf", default=False, description="Activates support for pnetcdf")
    depends_on("firedrake.chaco@petsc", when="+chaco")
    depends_on("eigen", when="+eigen")
    depends_on("netcdf-c+mpi", when="+netcdf-c")
    depends_on("parallel-netcdf", when="+parallel-netcdf")

    def configure_options(self):
        options = super().configure_options()
        if "+chaco" in self.spec:
            options += ["--with-chaco=1", "--with-chaco-dir={}".format(self.spec["chaco"].prefix)]
        if "+eigen" in self.spec:
            options += ["--with-eigen=1", "--with-eigen-dir={}".format(self.spec["eigen"].prefix)]
        # If 'cflags', 'fflags', and/or 'cxxflags' are set by the compiler
        # remove them from the PETSc configure options. Certain flags
        # cannot be duplicated eg: --eliminate-similar-expr
        remove_option = ["CFLAGS", "CXXFLAGS", "FFLAGS"]
        new_options = []
        for opt in options:
            if not any(opt.startswith(rem) for rem in remove_option):
                new_options.append(opt)
        options = new_options
        return options

    # Some spack bug: https://github.com/spack/spack/issues/27508
    @run_before("configure")
    def fixup_bug(self):
        spack.pkg.builtin.petsc.python = python

    def setup_dependent_run_environment(self, env, dependent_spec):
        self.setup_run_environment(env)

    #def setup_dependent_build_environment(self, env, dependent_spec):
    #    env.set("FFTW_INCLUDE_DIR", self.prefix.inc)
    #    env.set("FFTW_LIBRARY_DIR", self.prefix.lib)
