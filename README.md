# grepdl

A simple command line interface to grep live text stream of docker logs

### Install

```console
git clone https://git.metodogroup.it/andrea.tedeschi/grepdl.git
cd grepdl
python3 -m pip install .
```
N.B. If you have not python3-pip installed, last command is:

```console
python3 setup.py install
```

N.B. A deb and an rpm will be provided soon

### Usage

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
