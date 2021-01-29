from conans import ConanFile
from conans.model import Generator
from conans.client.generators import XCodeGenerator
from conans import tools
from conans.util.files import load
import os

class XCodeMultiarchGenerator(Generator):

    multi_file_name = "conanbuildinfo_multi.xcconfig"

    @property
    def content(self):
        arch = self.conanfile.settings.arch
        apple_arch = tools.to_apple_arch(arch)
        return {"conanbuildinfo_%s.xcconfig" % apple_arch: self._content_arch(apple_arch),
                self.multi_file_name: self._content_multi(apple_arch)}

    @property
    def filename(self):
        pass

    def _content_arch(self, apple_arch):
        xcodeGen = XCodeGenerator(self.conanfile)
        return xcodeGen.content.replace(" = ", "[arch=%s] = " % apple_arch)

    def _read_old_multi_content(self):
        multi_path = os.path.join(self.output_path, self.multi_file_name)
        content_multi = ""
        if os.path.isfile(multi_path):
            content_multi = load(multi_path)

        return content_multi

    def _content_multi(self, apple_arch):
        content = self._read_old_multi_content()
        additional_line = '#include "conanbuildinfo_%s.xcconfig"' % apple_arch
        if (content.find(additional_line) == -1):
            content = content + "\n" + additional_line

        return content

class XCodeMultiarchGeneratorPackage(ConanFile):
    name = "xcode_multiarch"
    description="Generate xcconfig files for multiple architectures."
    version = "1.0"
    url = "https://github.com/kdonev/conan-cmake-xcode-sample"
    license = "Public"