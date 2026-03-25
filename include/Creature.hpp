#ifndef CREATURE_HPP
#define CREATURE_HPP

#include <SFML/Graphics.hpp>
#include <vector>

// Structure pour l'évolution des caractéristiques physiques
struct GenomeStats {
    float maxSpeed = 5.0f;
    float size = 6.0f;
    float detectionRange = 100.0f;
};

class Creature {
public:
    Creature(float x, float y);
    
    // La méthode centrale : décide et bouge
    void update(const std::vector<double>& neuralOutputs, float deltaTime);
    void draw(sf::RenderWindow& window);

    // Getters pour la simulation
    sf::Vector2f getPosition() const { return position; }
    float getFitness() const { return fitness; }
    void addFitness(float value) { fitness += value; }

private:
    sf::Vector2f position;
    GenomeStats stats;
    float fitness = 0.0f;
    sf::CircleShape shape; // Représentation visuelle SFML
};

#endif