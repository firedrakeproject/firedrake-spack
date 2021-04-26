# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Chaco(MakefilePackage):
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

    maintainers = ['connorjward']

    version('2.2', sha256='e7c1ab187b2dbd4b682da3dbb99097143b773f6b68b39be989442c176e9bcee1')

    build_directory = 'src'

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')

        # Use the Spack compiler wrapper
        makefile.filter(r'^CC\s*=.*', 'CC=cc')

        # Set install destination
        makefile.filter(r'^DEST\s*=.*', 'DEST={0}/libchaco.a'.format(prefix.lib))

        # Set appropriate compiler flags
        cflags = '-O2'
        # cflags.append(self.compiler.cc_pic_flag)
        # cflags.append('-fstack-protector') # ??? Is this generic

        makefile.filter(r'^CFLAGS\s*=.*', 'CFLAGS={0}'.format(cflags))
        makefile.filter(r'^OFLAGS\s*=.*', 'OFLAGS={0}'.format(cflags))
