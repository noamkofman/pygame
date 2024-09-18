import pygame

# Initialize Pygame

# Create a surface with the original dimensions
original_surface = pygame.Surface((1468, 200))

# Scale the surface
scaled_surface = pygame.transform.scale_by(original_surface, 240 / 1468)

# Print the dimensions of the scaled surface
print(scaled_surface.get_size())  # Should print (240, ...) if the scaling is correct

# Quit Pygame
pygame.quit()
