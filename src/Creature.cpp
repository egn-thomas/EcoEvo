#include "Creature.hpp"

Creature::Creature(float x, float y) : position(x, y) {
    shape.setRadius(stats.size);
    shape.setPosition(position);
    shape.setFillColor(sf::Color::White);
}

void Creature::update(const std::vector<double>& neuralOutputs, float deltaTime) {
    // Logique de mouvement à venir
}

void Creature::draw(sf::RenderWindow& window) {
    window.draw(shape);
}