C++ Project Template
====================

This is a simple project template that uses [CMake](https://cmake.org/), the package manager [Conan](https://conan.io/), and the test library [Catch](https://github.com/catchorg/Catch2).

Its main purpose is to provide a project structure that is ready to go with only minimal adjustments depending on the project itself.

The default structure is configured for building a library, as well as providing an app that uses it.

The folders break down as follows:

```
project
├── CMakeLists.txt
│
├── apps
│   ├── CMakeLists.txt
│   └── main.cpp
│
├── include
│   └── libname 
│       └── hello_world.h
├── src
│   ├── CMakeLists.txt
│   └── hello_world.cpp
│
└── tests
    ├── CMakeLists.txt
    ├── example_test.cpp
    └── main.cpp
```

## Setup instructions

This project depends on CMake and Conan, which need to be installed prior to using this template.
* [CMake installation instructions](https://cmake.org/install/)
* [Conan installation instructions](http://docs.conan.io/en/latest/installation.html)

The folder structure can be copied and used directly with only a few minor adjustments.

1. Modify the name of the project in the root `CMakeLists.txt`.

## Recommended build instructions

### Unix/MacOS

From the root of the project:

1. `mkdir build && cd build`
2. `conan install .. && cmake .. && cmake --build .`
3. Run tests with `ctest -V`

### Windows

Coming soon™
