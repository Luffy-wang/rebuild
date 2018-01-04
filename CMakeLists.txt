cmake_minimum_required(VERISON 2.6)
project(judger c)


set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/output)
set(CMAKE_C_FLAGS "-g -Wall -Werror -O3 -std=c99 -pie -fPIC")

file(GLOB SOURCE "src/*.c" "src/rules/*.c")
add_executable(libjudger.so ${SOURCE})

target_link_libraries(libjudger.so pthread seccomp)

install(FILE output/libjudger.so DESTITATION /usr/lib/judger 
			PERMISSIONS OWNER_EXECUTE OWNER_READ)