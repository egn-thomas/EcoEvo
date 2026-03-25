cmake_minimum_required(VERSION 3.10)
project(EcoEvo)

set(CMAKE_CXX_STANDARD 17)

# Trouve SFML sur le système
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)

# Inclut le dossier des headers (.hpp)
include_directories(include)

# Ajoute tous tes fichiers sources
add_executable(EcoEvo 
    src/main.cpp 
    src/Creature.cpp 
    src/World.cpp
)

# Lie l'exécutable aux bibliothèques SFML
target_link_libraries(EcoEvo sfml-graphics sfml-window sfml-system)