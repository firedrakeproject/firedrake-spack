#!/bin/bash

RETURN_TO_DIR=`pwd`

if [ -n "$SPACK_ENV" ]
then
  SPACK_ENV2=$SPACK_ENV
  cd $SPACK_ENV

  # Run git pull in each component directory
  for DIR in $SPACK_ENV/libsupermesh/ $SPACK_ENV/petsc/ $SPACK_ENV/py-*/
    do
    cd $DIR
    git pull 2>&1 > /dev/null
    cd ..
  done

  # Reconcretize (in case dependencies have changed) and reinstall to update
  spack concretize -f 2>&1 | tee $SPACK_ENV/spack-firedrake-reconc.log
  spack install --fail-fast --show-log-on-error --log-format cdash --log-file $SPACK_ENV/spack-firedrake-update.log
  cd $RETURN_TO_DIR

  spack env deactivate
  spack env activate -p $SPACK_ENV2
else
  echo Must be run in an activated Spack environment
fi
