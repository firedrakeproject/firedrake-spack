# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install petsc-chaco
#
# You can edit this file again by typing:
#
#     spack edit petsc-chaco
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from pathlib import Path
from spack import *
from subprocess import run
import os



class PetscChaco(MakefilePackage):
    """# Chaco: Software for Partitioning Graphs

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
    git      = "https://bitbucket.org/petsc/pkg-chaco/src/master/"

    maintainers = ['anon']

    version('develop', branch='master', preferred=True)
    version('2.2', sha256='e7c1ab187b2dbd4b682da3dbb99097143b773f6b68b39be989442c176e9bcee1')

    def edit(self, spec, prefix):
        with open('make.inc', 'w') as fh:
            fh.writelines('CC=cc\n')
            cflags = ['-O3'] # ??? Do I want to specify optimisation here
            cflags.append(self.compiler.cc_pic_flag)
            cflags.append('-fstack-protector') # ??? Is this generic
            fh.writelines('CFLAGS=' + ' '.join(cflags) + '\n')
            fh.writelines('OFLAGS=' + ' '.join(cflags) + '\n')

    def build(self, spec, prefix):
        with working_dir('code'):
            make()
            mkdirp('../lib/')
            cwd = Path()
            object_list = [str(ofile.relative_to(cwd.absolute()))
                           for ofile in cwd.cwd().glob('*/*.o')]
            ar = ['ar', 'cr', 'libchaco.a', *object_list]
            run(ar, check=True)
            ranlib = ['ranlib', 'libchaco.a']
            run(ranlib, check=True)
            copylib = ['cp', 'libchaco.a', '../lib/']
            run(copylib, check=True)

    def install(self, spec, prefix):
        install_tree('.', prefix)
