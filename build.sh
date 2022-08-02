#!/bin/bash
if [[ "$(docker image inspect achlys-ubuntu --format="success")" == "success" ]]
then
  
  echo Found Achlys Docker image.
  echo Building Achlys-UQ...
  
  docker build -t achlys-uq docker/achlys-uq/

else
  
  echo Did not find Achlys Docker image.
  echo Building Achlys...
  
  git clone https://github.com/aurora-multiphysics/achlys.git
  cd achlys
  docker build -t achlys-ubuntu --build-arg compile_cores=4 --build-arg build_git_sha=master docker/achlys-ubuntu/
  
  echo Building Achlys-UQ...
  
  docker build -t achlys-uq docker/achlys-uq/

fi
