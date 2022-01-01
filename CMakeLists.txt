cmake_minimum_required(VERSION 3.9)

project("PROJECT_NAME" CXX)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake.modules/")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(src)
add_subdirectory(apps)

if (ENABLE_TESTS)
    add_subdirectory(tests)
    enable_testing()
endif()
