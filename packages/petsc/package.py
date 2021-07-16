# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Petsc(Package):
    homepage = 'https://github.com/firedrakeproject/petsc.git'
    git      = 'https://github.com/firedrakeproject/petsc.git'

    version('develop', branch='firedrake', no_cache=True)

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
    #   --download-suitesparse
    #   --download-zlib
    # --parmetis:
    #   --download-parmetis
    # --complex:
    #   --with-scalar-type=complex
    # --64bit-indices:
    #   --with-64-bit-indices
    #

    depends_on('python@3.4:', type='build')

    # Minimal
    depends_on('blas')
    #depends_on('chaco+lib')
    depends_on('lapack')
    depends_on('hdf5@1.12.0+hl+mpi')
    depends_on('hypre')
    depends_on('mpi')
    depends_on('mumps')
    depends_on('scalapack')
    depends_on('scotch') # Provides ptscotch
    depends_on('superlu-dist')

    # Full
    # ~ depends_on('hwloc')
    # ~ depends_on('metis')
    # ~ # Not sure how we get ML, perhaps "--download-ml"
    # ~ depends_on('netcdf-c')
    # ~ depends_on('parallel-netcdf')
    # ~ depends_on('pastix')
    # ~ depends_on('suite-sparse')
    # ~ # depends_on('zlib') only a dependency of scotch?

    # Parmetis
    # ~ depends_on('parmetis')

    phases = ['configure', 'build', 'install']

    def configure_args(self):
        # Compilers
        args = ['--with-cc={}'.format(self.spec['mpi'].mpicc),
                '--with-cxx={}'.format(self.spec['mpi'].mpicxx),
                '--with-fc={}'.format(self.spec['mpi'].mpifc)]
        args += ['CFLAGS={}'.format(' '.join(self.spec.compiler_flags['cflags'])),
                 'FFLAGS={}'.format(' '.join(self.spec.compiler_flags['fflags'])),
                 'CXXFLAGS={}'.format(' '.join(self.spec.compiler_flags['cxxflags']))]
        args += ["--COPTFLAGS=-O3 -march=native -mtune=native",
                 "--CXXOPTFLAGS=-O3 -march=native -mtune=native",
                 "--FOPTFLAGS=-O3 -march=native -mtune=native"]

        # Flags
        args += ['--with-c2html=0',
                 '--with-cxx-dialect=C++11',
                 '--with-debugging=0',
                 '--with-fortran-bindings=0',
                 '--with-shared-libraries=1',
                 '--with-x=0']

        # External dependencies
        args += ['--with-blas-lib={}'.format(self.spec['blas'].libs),
                 '--with-lapack-lib={}'.format(self.spec['lapack'].libs),
                 # ~ '--download-chaco',
                 #'--with-chaco=1',
                 #'--with-chaco-dir={}'.format(self.spec['chaco'].prefix),
                 '--with-hdf5=1',
                 '--with-hdf5-include={}'.format(self.spec['hdf5'].prefix.include),
                 '--with-hdf5-lib={}'.format(self.spec['hdf5:hl,fortran'].libs.joined()),
                 '--with-hypre=1',
                 '--with-hypre-dir={}'.format(self.spec['mumps'].prefix),
                 #mpi
                 '--with-mumps=1',
                 # ~ '--with-mumps-dir={}'.format(self.spec['mumps'].prefix),
                 '--with-mumps-include={}'.format(self.spec['mumps'].prefix.include),
                 '--with-mumps-lib={}'.format(self.spec['mumps'].libs.joined()),
                 '--with-ptscotch=1',
                 '--with-ptscotch-include={}'.format(self.spec['scotch'].prefix.include),
                 '--with-ptscotch-lib={}'.format(self.spec['scotch'].libs.joined()),
                 '--with-scalapack=1',
                 '--with-scalapack-lib={}'.format(self.spec['scalapack'].libs.joined()),
                 '--with-superlu_dist=1',
                 '--with-superlu_dist-include={}'.format(self.spec['superlu-dist'].prefix.include),
                 '--with-superlu_dist-lib={}'.format(join_path(self.spec['superlu-dist'].prefix.lib, 'libsuperlu_dist.a'))
                 ]

        return args

    def configure(self, spec, prefix):
        python('configure', '--prefix={}'.format(prefix), *self.configure_args())

    def build(self, spec, prefix):
        make('MAKE_NP={}'.format(make_jobs), parallel=False)

    def install(self, spec, prefix):
        make('install')

    def setup_build_environment(self, env):
        env.unset('PETSC_DIR')
        env.unset('PETSC_ARCH')

    def setup_run_environment(self, env):
        env.set('PETSC_DIR', self.prefix)
        env.unset('PETSC_ARCH')

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set('PETSC_DIR', self.prefix)
        env.unset('PETSC_ARCH')
