import random

# Define adjacency probabilities
terrain_adjacencies = {
    "plain": [("plain", 0.6), ("forest", 0.15), ("hills", 0.1), ("marsh", 0.1), ("pond", 0.05)],
    "scrub": [("scrub", 0.6), ("desert", 0.2), ("plain", 0.1), ("hills", 0.05), ("forest", 0.05)],
    "forest": [("forest", 0.6), ("plain", 0.2), ("hills", 0.1), ("marsh", 0.05), ("pond", 0.05)],
    "rough": [("rough", 0.7), ("hills", 0.2), ("mountains", 0.05), ("forest", 0.05)],
    "desert": [("desert", 0.6), ("scrub", 0.2), ("plain", 0.1), ("mountains", 0.1)],
    "hills": [("hills", 0.6), ("mountains", 0.2), ("plain", 0.1), ("forest", 0.05), ("depression", 0.05)],
    "mountains": [("mountains", 0.6), ("hills", 0.2), ("rough", 0.1), ("forest", 0.1)],
    "marsh": [("marsh", 0.6), ("pond", 0.2), ("plain", 0.1), ("forest", 0.1)],
    "pond": [("pond", 0.6), ("marsh", 0.2), ("plain", 0.1), ("forest", 0.1)],
    "depression": [("depression", 0.6), ("plain", 0.2), ("hills", 0.1), ("mountains", 0.1)]
}

def get_adjacent_terrain(current_terrain):
    """Predicts the terrain type of an adjacent hex based on the current terrain type."""
    # Get the possible adjacencies and their probabilities
    adjacencies = terrain_adjacencies[current_terrain]
    terrains, probabilities = zip(*adjacencies)
    
    # Choose an adjacent terrain type based on the probabilities
    return random.choices(terrains, probabilities)[0]

def path(input_tuple):
    current_terrain, current_index = input_tuple
    # Calculate indices and corresponding probabilities
    indices = [(current_index + i) % 6 for i in range(6)]
    probabilities = [0.05, 0.15, 0.2, 0.25, 0.2, 0.15]
    # Rotate probabilities list to align it with indices list
    probabilities = probabilities[-current_index:] + probabilities[:-current_index]
    # Choose a new index based on the defined probabilities
    new_index = random.choices(indices, probabilities, k=1)[0]
    return (current_terrain, new_index)

#print(test_get_adjacent_terrain("plain", 1000))

input_tuple = ("King's road", 2)
print(path(input_tuple))
