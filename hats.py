def equip_random_hat_and_flip():
    available_hats = get_available_hats()
    # selected_hat = random.choice(available_hats)
    change_hat(available_hats[len(available_hats) - 1])
    do_a_flip()


def get_available_hats():
    return [
        Hats.Gray_Hat,
        Hats.Purple_Hat,
        Hats.Green_Hat,
        Hats.Brown_Hat,
        Hats.Tree_Hat,
    ]
