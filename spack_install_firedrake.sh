#!/bin/bash

# Usage:
# ./spack_install_script.sh directory_name spec_to_install

# Check for a spack command
which spack 2>&1 > /dev/null
if [ $? -ne 0 ] && [ -d spack ]
  then
  # Try and setup spack environment
  source ./spack/share/spack/setup-env.sh
fi

# Check for a spack command
which spack 2>&1 > /dev/null
if [ $? -ne 0 ]
then
  # Tell user to go and install spack
  echo Spack command not found, install and activate Spack by running:
  echo git clone git@github.com:spack/spack.git
  echo source spack/share/spack/setup-env.sh
  echo Read the docs for more info https://spack.readthedocs.io/en/latest/
  echo
  echo Then add the Firedrake Spack repo by running:
  echo git clone git@github.com:firedrakeproject/firedrake-spack.git
  echo spack repo add firedrake-spack
else
  # Setup spack environment
  SPACK_ENV=$1
  SPACK_ENV2=$SPACK_ENV
  echo Creating Spack environment in: $SPACK_ENV
  spack env create -d $SPACK_ENV
  spack env activate -p $SPACK_ENV

  shift 1
  echo Adding spec: $@
  spack add $@

  # All packages that need to be developed
  spack develop py-firedrake@develop
  spack develop libsupermesh@develop
  spack develop petsc@develop
  spack develop chaco@petsc
  spack develop py-fiat@develop
  spack develop py-finat@develop
  spack develop py-islpy@develop
  spack develop py-petsc4py@develop
  spack develop py-pyadjoint@develop
  spack develop py-pyop2@develop
  spack develop py-coffee@develop
  spack develop py-loopy@develop
  spack develop py-cgen@develop
  spack develop py-codepy@develop
  spack develop py-genpy@develop
  spack develop py-tsfc@develop
  spack develop py-ufl@develop

  # Install (and log)
  spack install --fail-fast 2>&1 | tee spack-firedrake-install.log

  # For some reason the environment needs deactivating
  # and activating before it is useable
  spack env deactivate
  spack env activate -p $SPACK_ENV2
fi

