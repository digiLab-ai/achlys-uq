# Achlys-UQ

Achlys-UQ is an example of building a surrogate for Tritium desorption.

## Installation

You'll need a copy of `twinlab` next to `achlys-uq`:

```shell
git clone git@github.com:digiLab-ai/twinLab.git
git clone git@github.com:digiLab-ai/achlys-uq.git
```

Then set your current working directory as the top level folder of `achlys-uq`:

```shell
cd achlys-uq
```

And install the library and it's dependencies:

```shell
poetry install
```

You can then run the notebooks via:

```shell
poetry run jupyter notebook
```

After you've trained a surrogate, run the `Bokeh` app from the `achlys-uq/surrogate` directory:

```shell
cd achlys-uq/surrogate
poetry run python surrogate.py
```

## Installation

Run the build script `build.sh`.

## Usage

Spin up the achlys-uq Docker image.

Achlys-UQ adds the script modify_input_file, which modifies an Achlys input file according to a JSON file listing the updated parameters and their updated values.
