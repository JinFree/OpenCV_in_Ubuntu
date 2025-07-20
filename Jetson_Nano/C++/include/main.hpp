#ifndef MAIN_HPP
#define MAIN_HPP

#include <iostream>
#include <string>
#include <experimental/filesystem>
#include <utils.hpp>

using namespace std;
namespace fs = std::experimental::filesystem;

int main(int argc, char** argv);

void process_image(const std::string& save_path, const std::string& input_path);
void process_video(const std::string& save_path, const std::string& input_path);

bool is_image(const std::string& path);
bool is_video(const std::string& path);

#endif // MAIN_HPP
