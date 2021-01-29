pushd xcode_multiarch
conan export . test/test
popd

rm -rf build
mkdir build
pushd build

conan install .. -s os=iOS -s os.version=9.0 -s arch=x86_64 --build missing
conan install .. -s os=iOS -s os.version=9.0 -s arch=armv8 --build missing
#cp conanbuildinfo.xcconfig conanbuildinfo_arm64.xcconfig
#sed -i'.org' 's/ = /[arch=arm64] = /g' conanbuildinfo_arm64.xcconfig

cmake .. -GXcode -DDEPLOYMENT_TARGET="13.0" -DARCHS="\$(ARCHS_STANDARD)"

popd