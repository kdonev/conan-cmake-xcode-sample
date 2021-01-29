cmake_minimum_required (VERSION 3.19)

# If conan is being used, configure CMake to use conan for dependencies.
include(${CMAKE_BINARY_DIR}/conan_paths.cmake OPTIONAL)

set(CMAKE_TOOLCHAIN_FILE ${CONAN_IOS-CMAKE_ROOT}/lib/cmake/ios-cmake/ios.toolchain.cmake)

project (ZMQWrapper)

add_subdirectory (src)