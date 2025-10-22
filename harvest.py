def tree_carrot_check_pattern(x, y):
	if (x + y) % 2 == 0:
		plant(Entities.Carrot)
	else:
		plant(Entities.Tree)


def basic_soil_harvest():
	if can_harvest():
		harvest()

	if get_ground_type() != Grounds.Soil:
		till()


def hydrate_if_needed():
	needs_water = get_water() < 0.5
	has_water = num_items(Items.Water) > 0
	if needs_water and has_water:
		use_item(Items.Water)
