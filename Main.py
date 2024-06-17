import pygame

pygame.init()
clock = pygame.time.Clock()

screen_high = 600
screen_width = 1000
screen = pygame.display.set_mode((screen_width, screen_high))
pygame.display.set_caption("Character walking")


class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image


# Load sprite sheet
sprite_sheet = pygame.image.load("dino.png").convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet)
BLACK = (0, 0, 0)
# Create animation list
animation_list = []
animation_steps = [4, 6, 3, 4]  # animation: 4 frames - standing, 6 - running, etc
action = 0  # what action dino is doing(jumping, running, etc
last_update = pygame.time.get_ticks()  # time for animation
animation_cooldown = 100  # 75 miliseconds
frame = 0
step_counter = 0
for animation in animation_steps:
    temp_image_list = []
    for _ in range(animation):
        temp_image_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))  # x - frame(1,2,3
        step_counter += 1
    animation_list.append(temp_image_list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                print("pridedu faila")
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0

    # Clear the screen
    screen.fill((0, 255, 0))

    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0
    screen.blit(animation_list[action][frame], (0, 0))
    # Update the display
    pygame.display.flip()
    clock.tick(60)
