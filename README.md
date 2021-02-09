[![Python 3.6|3.9](https://img.shields.io/badge/python-3.6|3.9-blue.svg)](https://www.python.org/) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-red.svg)](https://www.gnu.org/licenses/gpl-3.0) [![release 1.0](https://img.shields.io/badge/release-1.0-yellow.svg)](https://github.com/DontPanicO/grepdl/releases/tag/v1.0) [![pypi 1.0](https://img.shields.io/badge/pypi-1.0-purple.svg)](https://pypi.org/project/grepdl/)

# grepdl

A simple command line interface to grep live text stream of docker logs

## Installation

N.B. Installation cloning the repository should be done for development pourposes only.

#### Install with dpkg

```console
$ wget http://andreatedeschi.uno/grepdl/grepdl_1.0-1_all.deb
$ sudo dpkg --install grepdl_1.0-1_all.deb
```

#### Install with pip

```console
$ sudo python3 -m pip install grepdl
```

#### Install with rpm

```console
$ wget http://andreatedeschi.uno/grepdl/grepdl-1.0-1.noarch.rpm
$ sudo rpm --install grepdl-1.0-1.noarch.rpm
```

#### Install cloning the repo 

```console
git clone https://git.metodogroup.it/andrea.tedeschi/grepdl.git
cd grepdl
python3 -m pip install .
```
N.B. If you have not python3-pip installed, last command is:

```console
python3 setup.py install
```

## Usage

```console
grepdl  [options] <container> <search>
||=============================================||
||Examples:                                    ||
||grepdl '^thi.+ mine$' container --regex      ||
||grepdl 'hello world'  container --since 10m  ||
||=============================================||

A tool to scan recursively a directory and grep in the content of its files

positional arguments:
  container             The container id or name
  search                The text or the pattern to look for in files content

optional arguments:
  -h, --help            show this help message and exit
  -r, --regex           Search is regular expression
  -i, --case-insensitive
                        The script will acts case insensitive
  --since <timestamp>   Only logs since timestamps (YYYY-mm-ddThh:mm:ssZ) or relative (42m, 10h, etc)
  --until <timestamp>   Only logs until timestamps (YYYY-mm-ddThh:mm:ssZ) or relative (42m, 10h, etc)
```
