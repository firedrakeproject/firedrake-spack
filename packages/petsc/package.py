# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Petsc(Package):
    git = 'https://github.com/firedrakeproject/petsc.git'

    version('develop', branch='firedrake', no_cache=True)

    depends_on('blas')
    depends_on('chaco+petsc')
    depends_on('lapack')
    depends_on('mpi')
    depends_on('mumps+mpi~openmp')
    depends_on('python@3.4:', type='build')
    depends_on('scalapack')
    depends_on('hdf5+hl+mpi')
    depends_on('zlib')

    phases = ['configure', 'build', 'install']

    def configure_args(self):
        args = ['--with-cc={}'.format(self.spec['mpi'].mpicc),
                '--with-cxx={}'.format(self.spec['mpi'].mpicxx),
                '--with-fc={}'.format(self.spec['mpi'].mpifc)]

        args += ['CFLAGS={}'.format(' '.join(self.spec.compiler_flags['cflags'])),
                 'FFLAGS={}'.format(' '.join(self.spec.compiler_flags['fflags'])),
                 'CXXFLAGS={}'.format(' '.join(self.spec.compiler_flags['cxxflags']))]

        args += ['--with-shared-libraries',
                 '--with-debugging=0',
                 '--with-blas-lib={}'.format(self.spec['blas'].libs),
                 '--with-lapack-lib={}'.format(self.spec['lapack'].libs)]

        args += ['--with-chaco=1',
                 '--with-chaco-dir={}'.format(self.spec['chaco'].prefix),
                 '--with-mumps=1',
                 '--with-mumps-dir={}'.format(self.spec['mumps'].prefix),
                 '--with-scalapack=1',
                 '--with-scalapack-lib={}'.format(self.spec['scalapack'].libs.joined()),
                 '--with-hdf5=1',
                 '--with-hdf5-include={}'.format(self.spec['hdf5'].prefix.include),
                 '--with-hdf5-lib={}'.format(self.spec['hdf5:hl,fortran'].libs.joined())]
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
