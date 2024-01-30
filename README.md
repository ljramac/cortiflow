## Prerequisites

Before you begin, make sure you have Node.js and Python installed on your system. This project requires the use of `pyenv` and `pipenv` to manage Python versions and environment dependencies.

### Installing Node.js

Visit [Node.js](https://nodejs.org/) and download and install the recommended version for your operating system.

### Installing pyenv

`pyenv` is a simple tool to manage multiple versions of Python. To install it, follow the instructions at [pyenv](https://github.com/pyenv/pyenv#installation).

### Installing pipenv

Once you have `pyenv` installed, you can install `pipenv`, which is a tool for creating and managing virtual environments in Python:

```bash
pip install pipenv
```

## Setting Up the Python Environment

Ensure that the `python` command is available in your terminal and that `pyenv` and `pipenv` are using the version of Python specified in the `python-version` file.

```bash
pyenv install $(cat python-version)
pyenv local $(cat python-version)
pipenv --python $(pyenv which python)
```

This will configure both `pyenv` and `pipenv` to use the Python version defined in your `python-version`.

## Installing Dependencies

With the Python environment set up, proceed to install the Node.js and Python dependencies of the project.

```bash
npm install
pipenv install
```

This will install all the necessary dependencies for the project contained in `package.json` and `Pipfile`, respectively.

## Running the Application

Once the dependencies are installed, you can start the application in two different ways:

### Using start.sh

To start the application without backend hot reloading:

```bash
./bin/start.sh
```

Make sure that `start.sh` has execution permissions. If not, grant them with:

```bash
chmod +x ./bin/start.sh
```

### Using dev.sh for Hot Reloading

If you want to start the application with backend hot reloading, use:

```bash
./bin/dev.sh
```

Again, check and grant execution permissions if necessary:

```bash
chmod +x ./bin/dev.sh
```

Both scripts will allow you to run the application in development mode.
