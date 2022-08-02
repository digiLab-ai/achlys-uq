# Achlys-UQ
## Installation
First install the Achlys Docker image from [https://github.com/aurora-multiphysics/achlys](https://github.com/aurora-multiphysics/achlys).

Then clone this directory and run
```
docker build -t achlys-uq docker/achlys-uq/
```

## Usage
Achlys-UQ adds the script modify_input_file, which modifies an Achlys input file according to a JSON file listing the updated parameters and their updated values.
