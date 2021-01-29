This repository demonstrate how to integrate conan with cmake with xcode.

From conan it uses zeromq library as package.
It has cmake project zmqWrapLib which needs zeromq library to work.
And it has TestConan.xcodeproj xcode project which uses zmqWrapLib

If you want to build it download the repo. In zmqWrapLib call [`boot.sh`](zmqWrapLib/boot.sh).
Open the TestConan/TestConan.xcodeproj and build. You will be able to switch
build to simulator or ios device. Can test it with "any ios device" target.

This repository contains also custom conan generator in
[zmqWrapLib/xcode_multiarch/conanfile.py](zmqWrapLib/xcode_multiarch/conanfile.py).
It creates conanbuildinfo_multi.xcconfig file which has references to
correct builds for each architecture in the conan cache.