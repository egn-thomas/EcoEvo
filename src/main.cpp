#include <SFML/Graphics.hpp>
#include "World.hpp"

int main() {
    // Création de la fenêtre
    sf::RenderWindow window(sf::VideoMode(800, 600), "EcoEvo Studio C++");
    window.setFramerateLimit(60);

    World world;
    sf::Clock clock;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Temps écoulé entre deux images (important pour la physique)
        float dt = clock.restart().asSeconds();

        // 1. Logique
        world.step(dt);

        // 2. Rendu
        window.clear(sf::Color(20, 20, 30));
        world.draw(window);
        window.display();
    }

    return 0;
}