from pygame.image import load

def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/elon.jpg"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()
