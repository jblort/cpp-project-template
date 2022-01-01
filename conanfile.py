from conans import ConanFile, CMake


class ProjectNameConan(ConanFile):
    name = "Project"
    version = "0.1"
    license = "MIT"
    author = ""
    url = ""
    topics = ("cpp","utility")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "enable_tests": [True, False]}
    default_options = {"shared": True,
                       "enable_tests": True}

    generators = "cmake"
    exports_sources = "*"

    def requirements(self):
        if self.options.enable_tests:
            self.requires("catch2/2.13.7")

    def build(self):
        cmake_defs = {}
        cmake_defs["ENABLE_TESTS"] = True
        cmake_defs["CMAKE_EXPORT_COMPILE_COMMANDS"] = True
        cmake = CMake(self)
        cmake.configure(defs=cmake_defs)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["library_name"]

