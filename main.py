from hats import equip_random_hat_and_flip
from move import (
    go_to_position,
    traverse_grid,
    traverse_grid_reverse,
    traverse_grid_infinite,
)
from harvest import basic_soil_harvest, hydrate_if_needed, tree_carrot_check_pattern

clear()

# pet_the_piggy()
equip_random_hat_and_flip()

available_patterns = ["trees_and_carrots"]


def handle_cell(x, y, pattern):
    basic_soil_harvest()
    hydrate_if_needed()

    if pattern == "trees_and_carrots":
        tree_carrot_check_pattern(x, y)


def cell_handler(x, y):
    handle_cell(x, y, "trees_and_carrots")


while True:
    grid_size = get_world_size()
    # grid_size = 2
    start_position = (0, 0)

    traverse_grid_infinite(start_position, grid_size, cell_handler)
