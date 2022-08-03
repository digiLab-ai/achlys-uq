#!/bin/bash
if [[ "$(docker image inspect achlys-ubuntu --format="success")" == "success" ]]
then
  echo Found Achlys Docker image.
else
  echo Did not find Achlys Docker image.
  echo Building Achlys...
  
  docker build -t achlys-ubuntu https://raw.githubusercontent.com/aurora-multiphysics/achlys/master/docker/achlys-ubuntu/Dockerfile
fi
echo Building Achlys-UQ...
  
docker build -t achlys-uq docker/achlys-uq/
