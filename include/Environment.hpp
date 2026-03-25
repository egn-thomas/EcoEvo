#ifndef ENVIRONMENT_HPP
#define ENVIRONMENT_HPP

struct Environment {
    float gravity = 9.81f;
    float friction = 0.98f; // Pour ralentir les créatures
    float temperature = 20.0f;
    
    // On pourrait ajouter des fonctions ici :
    // float getEnergyLossFactor() { return temperature * 0.01f; }
};

#endif