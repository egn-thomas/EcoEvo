import pygame
import neat
import os
import random
from creature import Creature

# Configuration Globale
WIDTH, HEIGHT = 800, 600
FOOD_POS = (WIDTH // 2, 100)
START_POS = (WIDTH // 2, HEIGHT - 50)

# INITIALISATION UNIQUE
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 18)

def get_color_from_genome(genome):
    random.seed(genome.key)
    return (random.randint(50, 255), random.randint(50, 255), 255)

def eval_genomes(genomes, config):
    nets = []
    creatures = []
    ge = []

    obstacle_rect = pygame.Rect(WIDTH//4, HEIGHT//2 - 20, WIDTH//2, 30)

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        c = Creature(START_POS[0], START_POS[1], FOOD_POS[0], FOOD_POS[1])
        c.color = get_color_from_genome(genome)
        creatures.append(c)
        ge.append(genome)

    steps = 0
    MAX_STEPS = 300
    
    run = True
    while run and len(creatures) > 0:
        SCREEN.fill((10, 10, 20)) 
        steps += 1

        if steps > MAX_STEPS:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Dessin des éléments fixes
        pygame.draw.rect(SCREEN, (100, 100, 120), obstacle_rect) 
        pygame.draw.circle(SCREEN, (255, 50, 50), FOOD_POS, 10) 

        for i in range(len(creatures) - 1, -1, -1):
            creature = creatures[i]
            
            # Normalisation des entrées
            in_x = (creature.food_x - creature.x) / WIDTH
            in_y = (creature.food_y - creature.y) / HEIGHT
            
            output = nets[i].activate((in_x, in_y))
            creature.move(output)
            
            pygame.draw.circle(SCREEN, creature.color, (int(creature.x), int(creature.y)), 6)

            dist = creature.get_distance_to_food()
            c_rect = pygame.Rect(creature.x - 3, creature.y - 3, 6, 6)

            # Collisions et Fitness
            if obstacle_rect.colliderect(c_rect) or \
               creature.x < 0 or creature.x > WIDTH or \
               creature.y < 0 or creature.y > HEIGHT:
                ge[i].fitness -= 200
                remove_creature(i, creatures, nets, ge)
                continue

            if dist < 20:
                ge[i].fitness += 2000 + (MAX_STEPS - steps)
                remove_creature(i, creatures, nets, ge)
                continue

            # On garde le meilleur score de proximité
            current_fitness = 1000 - dist
            if current_fitness > ge[i].fitness:
                ge[i].fitness = current_fitness

        # --- LES LIGNES MANQUANTES ÉTAIENT ICI ---
        txt = FONT.render(f"Gen: {pop.generation} | Survivants: {len(creatures)} | Step: {steps}", True, (200, 200, 200))
        SCREEN.blit(txt, (10, 10))
        
        pygame.display.flip() # Affiche l'image calculée
        CLOCK.tick(120)       # Régle la vitesse (mets 60 pour voir, 0 pour turbo)

    # Nettoyage de sécurité pour éviter le crash au prochain spawn
    for i in range(len(creatures) - 1, -1, -1):
        remove_creature(i, creatures, nets, ge)

def remove_creature(index, creatures, nets, ge):
    creatures.pop(index)
    nets.pop(index)
    ge.pop(index)

def run_neat(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    
    global pop
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    pop.run(eval_genomes, 100)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run_neat(config_path)