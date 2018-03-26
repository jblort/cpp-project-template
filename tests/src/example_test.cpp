#include <catch.hpp>

SCENARIO("Example scenario") {
    GIVEN("A C++ project template") {
        WHEN("I want to compile it") {
            THEN("It works!") {
                REQUIRE("Hello" != "World!");
            }
        }
    }
}
