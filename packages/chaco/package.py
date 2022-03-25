# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from pathlib import Path
import subprocess

from spack import *


class Chaco(MakefilePackage):
    """Chaco: Software for Partitioning Graphs

    Chaco contains a wide variety of algorithms and options, many of
    which were invented by the authors. Some of the algorithms exploit
    the geometry of the mesh, others its local connectivity or its global
    structure as captured by eigenvectors of a related matrix. These
    methods can be mixed and matched in several ways, and combinations
    often prove to be more effective than any single technique in
    isolation. All these algorithms are accessed via a simple user
    interface, or a call from other software. Innovations in Chaco
    include
    - Development of multilevel graph partitioning. This widely
    imitated approach has become the premiere algorithm combining very
    high quality with short calculation times.
    - Extension of spectral partitioning to enable the use of 2 or 3
    Laplacian eigenvectors to quadrisect of octasect a graph.
    # Highly efficient and robust eigensolvers for use with spectral
    graph algorithms.
    - Generalization of the Kernighan-Lin/Fiduccia-Mattheyses algorithm
    to handle weighted graphs, arbitrary number of sets and lazy
    initiation.
    - Development of skewed partitioning to improve the mapping of a
    graph onto a target parallel architecture.
    - Various post-processing options to improve partitions in a number
    of ways.
    """

    homepage = "https://www3.cs.stonybrook.edu/~algorith/implement/chaco/implement.shtml"
    url      = "https://www3.cs.stonybrook.edu/~algorith/implement/chaco/distrib/Chaco-2.2.tar.gz"

    maintainers = ['connorjward']

    version('petsc', git='https://bitbucket.org/petsc/pkg-chaco.git', branch='master')
    version('2.2', sha256='e7c1ab187b2dbd4b682da3dbb99097143b773f6b68b39be989442c176e9bcee1')

    build_directory = 'code'

    def edit(self, spec, prefix):
        cflags = ['-O2', self.compiler.cc_pic_flag]

        makefile = FileFilter('{}/Makefile'.format(self.build_directory))
        makefile.filter(r'^DEST\s*=.*', 'DEST=../bin/chaco')

        if self.spec.version == Version('petsc'):
            with open('make.inc', 'w') as inc:
                inc.write('CC={}\n'.format(spack_cc))
                inc.write('CFLAGS={}\n'.format(' '.join(cflags)))
                inc.write('OFLAGS={}\n'.format(' '.join(cflags)))
        else:
            makefile.filter(r'^CC\s*=.*', 'CC={}'.format(spack_cc))
            makefile.filter(r'^CFLAGS\s*=.*', 'CFLAGS={}'.format(cflags))
            makefile.filter(r'^OFLAGS\s*=.*', 'OFLAGS={}'.format(cflags))

    def build(self, spec, prefix):
        with working_dir('code'):
            mkdirp('../bin')
            make()

            if self.spec.version == Version('petsc'):
                # See https://gitlab.com/petsc/petsc/-/blob/main/config/BuildSystem/config/packages/Chaco.py
                mkdirp('../lib')
                cwd = Path()
                object_list = [str(ofile.relative_to(cwd.absolute()))
                               for ofile in cwd.cwd().glob('*/*.o')]
                subprocess.run(['ar', 'cr', 'libchaco.a', *object_list], check=True)
                subprocess.run(['ranlib', 'libchaco.a'], check=True)
                subprocess.run(['cp', 'libchaco.a', '../lib/'], check=True)

    def install(self, spec, prefix):
        install_tree('bin', prefix.bin)
        if self.spec.version == Version('petsc'):
            install_tree('lib', prefix.lib)
