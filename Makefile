# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/kk123/Desktop/rebuild judger"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/kk123/Desktop/rebuild judger"

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target install
install: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Install the project..."
	/usr/bin/cmake -P cmake_install.cmake
.PHONY : install

# Special rule for the target install
install/fast: preinstall/fast
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Install the project..."
	/usr/bin/cmake -P cmake_install.cmake
.PHONY : install/fast

# Special rule for the target list_install_components
list_install_components:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Available install components are: \"Unspecified\""
.PHONY : list_install_components

# Special rule for the target list_install_components
list_install_components/fast: list_install_components

.PHONY : list_install_components/fast

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/usr/bin/cmake -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target install/strip
install/strip: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Installing the project stripped..."
	/usr/bin/cmake -DCMAKE_INSTALL_DO_STRIP=1 -P cmake_install.cmake
.PHONY : install/strip

# Special rule for the target install/strip
install/strip/fast: install/strip

.PHONY : install/strip/fast

# Special rule for the target install/local
install/local: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Installing only the local directory..."
	/usr/bin/cmake -DCMAKE_INSTALL_LOCAL_ONLY=1 -P cmake_install.cmake
.PHONY : install/local

# Special rule for the target install/local
install/local/fast: install/local

.PHONY : install/local/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "No interactive CMake dialog available..."
	/usr/bin/cmake -E echo No\ interactive\ CMake\ dialog\ available.
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start "/home/kk123/Desktop/rebuild judger/CMakeFiles" "/home/kk123/Desktop/rebuild judger/CMakeFiles/progress.marks"
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start "/home/kk123/Desktop/rebuild judger/CMakeFiles" 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named libjudger.so

# Build rule for target.
libjudger.so: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 libjudger.so
.PHONY : libjudger.so

# fast build rule for target.
libjudger.so/fast:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/build
.PHONY : libjudger.so/fast

judger/argtable3.o: judger/argtable3.c.o

.PHONY : judger/argtable3.o

# target to build an object file
judger/argtable3.c.o:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/argtable3.c.o
.PHONY : judger/argtable3.c.o

judger/argtable3.i: judger/argtable3.c.i

.PHONY : judger/argtable3.i

# target to preprocess a source file
judger/argtable3.c.i:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/argtable3.c.i
.PHONY : judger/argtable3.c.i

judger/argtable3.s: judger/argtable3.c.s

.PHONY : judger/argtable3.s

# target to generate assembly for a file
judger/argtable3.c.s:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/argtable3.c.s
.PHONY : judger/argtable3.c.s

judger/child.o: judger/child.c.o

.PHONY : judger/child.o

# target to build an object file
judger/child.c.o:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/child.c.o
.PHONY : judger/child.c.o

judger/child.i: judger/child.c.i

.PHONY : judger/child.i

# target to preprocess a source file
judger/child.c.i:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/child.c.i
.PHONY : judger/child.c.i

judger/child.s: judger/child.c.s

.PHONY : judger/child.s

# target to generate assembly for a file
judger/child.c.s:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/child.c.s
.PHONY : judger/child.c.s

judger/killer.o: judger/killer.c.o

.PHONY : judger/killer.o

# target to build an object file
judger/killer.c.o:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/killer.c.o
.PHONY : judger/killer.c.o

judger/killer.i: judger/killer.c.i

.PHONY : judger/killer.i

# target to preprocess a source file
judger/killer.c.i:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/killer.c.i
.PHONY : judger/killer.c.i

judger/killer.s: judger/killer.c.s

.PHONY : judger/killer.s

# target to generate assembly for a file
judger/killer.c.s:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/killer.c.s
.PHONY : judger/killer.c.s

judger/logger.o: judger/logger.c.o

.PHONY : judger/logger.o

# target to build an object file
judger/logger.c.o:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/logger.c.o
.PHONY : judger/logger.c.o

judger/logger.i: judger/logger.c.i

.PHONY : judger/logger.i

# target to preprocess a source file
judger/logger.c.i:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/logger.c.i
.PHONY : judger/logger.c.i

judger/logger.s: judger/logger.c.s

.PHONY : judger/logger.s

# target to generate assembly for a file
judger/logger.c.s:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/logger.c.s
.PHONY : judger/logger.c.s

judger/main.o: judger/main.c.o

.PHONY : judger/main.o

# target to build an object file
judger/main.c.o:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/main.c.o
.PHONY : judger/main.c.o

judger/main.i: judger/main.c.i

.PHONY : judger/main.i

# target to preprocess a source file
judger/main.c.i:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/main.c.i
.PHONY : judger/main.c.i

judger/main.s: judger/main.c.s

.PHONY : judger/main.s

# target to generate assembly for a file
judger/main.c.s:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/main.c.s
.PHONY : judger/main.c.s

judger/rules/c_cpp.o: judger/rules/c_cpp.c.o

.PHONY : judger/rules/c_cpp.o

# target to build an object file
judger/rules/c_cpp.c.o:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/rules/c_cpp.c.o
.PHONY : judger/rules/c_cpp.c.o

judger/rules/c_cpp.i: judger/rules/c_cpp.c.i

.PHONY : judger/rules/c_cpp.i

# target to preprocess a source file
judger/rules/c_cpp.c.i:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/rules/c_cpp.c.i
.PHONY : judger/rules/c_cpp.c.i

judger/rules/c_cpp.s: judger/rules/c_cpp.c.s

.PHONY : judger/rules/c_cpp.s

# target to generate assembly for a file
judger/rules/c_cpp.c.s:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/rules/c_cpp.c.s
.PHONY : judger/rules/c_cpp.c.s

judger/rules/general.o: judger/rules/general.c.o

.PHONY : judger/rules/general.o

# target to build an object file
judger/rules/general.c.o:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/rules/general.c.o
.PHONY : judger/rules/general.c.o

judger/rules/general.i: judger/rules/general.c.i

.PHONY : judger/rules/general.i

# target to preprocess a source file
judger/rules/general.c.i:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/rules/general.c.i
.PHONY : judger/rules/general.c.i

judger/rules/general.s: judger/rules/general.c.s

.PHONY : judger/rules/general.s

# target to generate assembly for a file
judger/rules/general.c.s:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/rules/general.c.s
.PHONY : judger/rules/general.c.s

judger/runner.o: judger/runner.c.o

.PHONY : judger/runner.o

# target to build an object file
judger/runner.c.o:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/runner.c.o
.PHONY : judger/runner.c.o

judger/runner.i: judger/runner.c.i

.PHONY : judger/runner.i

# target to preprocess a source file
judger/runner.c.i:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/runner.c.i
.PHONY : judger/runner.c.i

judger/runner.s: judger/runner.c.s

.PHONY : judger/runner.s

# target to generate assembly for a file
judger/runner.c.s:
	$(MAKE) -f CMakeFiles/libjudger.so.dir/build.make CMakeFiles/libjudger.so.dir/judger/runner.c.s
.PHONY : judger/runner.c.s

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... install"
	@echo "... list_install_components"
	@echo "... rebuild_cache"
	@echo "... libjudger.so"
	@echo "... install/strip"
	@echo "... install/local"
	@echo "... edit_cache"
	@echo "... judger/argtable3.o"
	@echo "... judger/argtable3.i"
	@echo "... judger/argtable3.s"
	@echo "... judger/child.o"
	@echo "... judger/child.i"
	@echo "... judger/child.s"
	@echo "... judger/killer.o"
	@echo "... judger/killer.i"
	@echo "... judger/killer.s"
	@echo "... judger/logger.o"
	@echo "... judger/logger.i"
	@echo "... judger/logger.s"
	@echo "... judger/main.o"
	@echo "... judger/main.i"
	@echo "... judger/main.s"
	@echo "... judger/rules/c_cpp.o"
	@echo "... judger/rules/c_cpp.i"
	@echo "... judger/rules/c_cpp.s"
	@echo "... judger/rules/general.o"
	@echo "... judger/rules/general.i"
	@echo "... judger/rules/general.s"
	@echo "... judger/runner.o"
	@echo "... judger/runner.i"
	@echo "... judger/runner.s"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system
