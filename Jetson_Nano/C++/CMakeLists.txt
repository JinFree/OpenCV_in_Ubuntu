cmake_minimum_required(VERSION 3.5)
project(OpenCVCpp LANGUAGES CXX)

# —————————————————————————————
# 1) C++ 표준 설정
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# —————————————————————————————
# 2) OpenCV 찾기
find_package(OpenCV REQUIRED)

# —————————————————————————————
# 3) include 디렉터리 설정
#    모든 모듈이 include/ 하위 헤더를 참조하므로 PUBLIC으로 지정
#    main, utils 모두 경로를 상속받습니다.
set(PROJECT_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/include")
include_directories(${PROJECT_INCLUDE_DIR}
                    ${OpenCV_INCLUDE_DIRS})

# —————————————————————————————
# 4) utils 라이브러리 
add_library(utils STATIC
    src/utils.cpp
)
target_link_libraries(utils
    PUBLIC ${OpenCV_LIBS} 
)
target_include_directories(utils
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# —————————————————————————————
# 5) main 실행 파일
add_executable(main
    src/main.cpp
)
# utils → OpenCV 순으로 링크
target_link_libraries(main
    PRIVATE utils
    PUBLIC stdc++fs
)
target_include_directories(main
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# —————————————————————————————
# 6) (선택) 설정 확인용 메세지
message(STATUS "Include dirs: ${PROJECT_INCLUDE_DIR}")
message(STATUS "OpenCV includes: ${OpenCV_INCLUDE_DIRS}")
message(STATUS "OpenCV libs:     ${OpenCV_LIBS}")
