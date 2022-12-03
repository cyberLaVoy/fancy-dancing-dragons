import pygame
import sys
import math
from pygame.locals import *

# Initialize PyGame
pygame.init()

# Load the dragon image and create a surface for it
dragon_image = pygame.image.load("fancy_dragon.jpeg")
dragon_surface = pygame.Surface(dragon_image.get_size())
dragon_surface.blit(dragon_image, (0, 0))

# Create the screen with the same size as the dragon image
width, height = dragon_image.get_size()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyGame Dragon Animation")


# Set the metronome frequency
metronome_frequency = .01

# Set the frame rate
fps = 60
frame = 0

# Define the animation function
def animate_dragon(frame, time):
    # Calculate the position of the dragon based on the metronome pulse
    x = width / 2 + math.sin(frame * metronome_frequency) * width / 16
    y = height / 2 + math.cos(frame * metronome_frequency) * height / 16
    # Calculate the angle of the dragon
    angle = math.sin(math.tan(time * metronome_frequency)) * 360

    return (x, y, angle)


# Run the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Calculate the position and angle of the dragon
    frame += 1
    time = frame / fps
    x, y, angle = animate_dragon(frame, time)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the dragon
    rotated_dragon = pygame.transform.rotate(dragon_surface, angle)
    rect = rotated_dragon.get_rect()
    rect.center = (x, y)
    screen.blit(rotated_dragon, rect)

    # Update the display
    pygame.display.update()
