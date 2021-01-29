find_package(ZeroMQ)

add_library(zmqwrap ZMQConnect.cpp)

target_link_libraries(zmqwrap PUBLIC ZeroMQ::ZeroMQ)

target_include_directories(zmqwrap PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
