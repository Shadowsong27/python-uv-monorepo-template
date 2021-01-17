# python-standard-template

A personal flavoured template for Python 3 projects

I need this because there is no one strict way of 
defining one's project in the Python world.

I use the following CLI tools to manage any Python projects.

1. poetry - for dependency management
2. pyenv - for virutal environment management
3. pre-commit - for maintaining code standard
4. bumpversion - for maintaining project semantic versioning

There will be more stuff that comes later, such as the support of 
dockerization, RestAPI endpoints template etc.

# Installation Instruction

Before taking any further actions, you need to make
 sure you are not in any existing virtual environment. All these packages should
 be installed both in the global Python instead of the project environments

### poetry

Follow the installation Guide here

`https://python-poetry.org/docs/`

After successful installation, to allow command line usage of `poetry`, append
your PATH variable to make it available for CLI usage.

```
export PATH="$PATH:$HOME/.poetry/bin"
```

For windows user, the PATH will be different, please refer to the docs.

to your shell configuration file, as stated in the docs or in the `stdout` during installation

run `poetry` in a new shell to check:

```
poetry --version
```
It should return something like

```
Poetry version 1.0.5
```

### pyenv

`pyenv` makes it easy to install new versions of python, and switch between them.

`pyenv-virtualenv` is a plugin that allows you to switch virtual environment in python easily.

---

To install `pyenv` on Mac:

https://github.com/pyenv/pyenv

```
brew update
brew install pyenv
```

In case zlib is missing: 

(UPDATE: I am not sure whether this is solved in Big Sur, but it 
is a problem in Mojave.)

```
brew install zlib
export LDFLAGS="-L/usr/local/opt/zlib/lib"
export CPPFLAGS="-I/usr/local/opt/zlib/include"
export PKG_CONFIG_PATH="/usr/local/opt/zlib/lib/pkgconfig"
```

In case sqlite 3 does not install:

```
xcode-select --install
sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

If that does not solve the issue, look at the original GitHub for more details, it covers the common
installation problem easily.

---

To install `pyenv-virtualenv` on Mac:

```
brew install pyenv-virtualenv
```

Then add the following lines to your shell profile (e.g. `~/.zshrc`)

```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

For Windows user you will need to use a special version of pyenv, look here:

https://github.com/pyenv-win/pyenv-win

---

After installation, check

```
pyenv -v
```

It should return something like

```
pyenv 1.2.11
```

Once this is done, you can create a new virtual environment by running

```
pyenv install 3.7.6
```

To install python 3.7.6 in your computer.
Note: Python 3.8 will have some compatibility issue with some libraries.

Then create the virtual env by running

```
pyenv virtualenv 3.7.6
```

And start to build environment by running

```
poetry add
poetry install
```

### pre-commit

```
pip install pre-commit
```

and setup the `.pre-commit-config.yaml` file in your project

(This should be automatic once we enabled project template in GitLab)

Then you will need to install all pre commit hooks before actually using them

```
pre-commit install
```


### bumpversion

```
pip install bumpversion
```

and setup the `.bumpversion.cfg` config file

Note: this is an archived project / tool, there might be a better
 tool out there, I know Poetry has its own version bumping functionality
 but I did not further look into it as it is not that usable back then.
 
  
# Design Thoughts;

### Config

The config will be declared by the Environment Variable `PROJECT_ENV`. 

So to toggle the environment, just export a different environment name,
which should have the same name as the python files under the `src/config/environments`
folder.

The goal is use a the same names of any configurable variable across
environments, so we could achieve the switch of environments with 
just an export statement.

### Constants vs Config

Configs are supposed to be things that are configurable, common 
configs are placed in `src/config/environments/common.py`.

The constants on the other are some hardcoded values, like 
the parameter of the earth, the light speed etc. They are NOT
configurable.

### Customized Exceptions

In a small project we rarely need to define custom exceptions,
but it might come handy when you have a quite a few layers
in your system and then you might want to raise an exception
explicitly tied to a situation.

### manage.py file placement

I use this template mainly for Data projects, i.e. they are 
mostly a bunch of CLI commands executables, scheduled
or executed as a long running service. That's why the 
entry point is always from CLI. I might need to create
a template for building packages too, and FastAPI projects? 
Probably there are already some FastAPI projects template on
Github.

### LICENSE

Added the license because it's on Github. Free to delete
it when doing a private project.