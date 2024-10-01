from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class webserverRecipe(ConanFile):
    name = "webserver"
    version = "0.1"
    package_type = "static-library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of webserver package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"FOO": [None, "ANY"]}
    default_options = {"FOO": None}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        for option, value in self.options.items():
            if value is None:
                continue
            tc.preprocessor_definitions["FOO"] = value
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def requirements(self):
        self.requires("3rdparty/0.1")

    def config_options(self):
        self.options["3rdparty"].FOO = '"Foo"'

    def package_info(self):
        self.cpp_info.libs = ["webserver"]
        for option, value in self.options.items():
            if value is None:
                continue
            self.cpp_info.defines = [f"{option}={value}"]
