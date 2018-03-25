set(TEST_APP_NAME "${LIBRARY_NAME}-test")

include(ParseAndAddCatchTests)

set(TEST_MODULE_PATH "${PROJECT_SOURCE_DIR}/tests")
set(TEST_SRC_PATH "${TEST_MODULE_PATH}/src")

include_directories(${LIBRARY_INCLUDE_PATH})

file (GLOB_RECURSE TEST_SOURCE_FILES "${TEST_SRC_PATH}/*.cpp")

add_executable(${TEST_APP_NAME} ${TEST_SOURCE_FILES})

target_link_libraries(${TEST_APP_NAME} ${LIBRARY_NAME} ${CONAN_LIBS})

enable_testing()
ParseAndAddCatchTests(${TEST_APP_NAME})
