import pygame

def load_image(image_path):
    try:
        image = pygame.image.load(image_path)
        return image
    except pygame.error as e:
        print(f"Cannot load image: {image_path}")
        raise SystemExit(e)

def play_sound(sound_path):
    try:
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
    except pygame.error as e:
        print(f"Cannot play sound: {sound_path}")
        raise SystemExit(e)