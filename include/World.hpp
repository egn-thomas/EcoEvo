#ifndef WORLD_HPP
#define WORLD_HPP

#include "Creature.hpp"
#include "Environment.hpp"
#include <vector>

class World {
public:
    World();
    void step(float deltaTime); // Met à jour tout le monde
    void draw(sf::RenderWindow& window);

private:
    std::vector<Creature> population;
    sf::Vector2f foodPos;
    Environment currentEnv;
    
    void checkCollisions();
};

#endif