import pygame

def main():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("360 Panorama Viewer")

    # Load image
    image = pygame.image.load("panorama.jpg")
    image_width, image_height = image.get_size()

    # Initial offset
    offset_x = 0
    offset_y = 0

    # Movement speed for keyboard
    scroll_speed = 5  

    # Dragging variables
    dragging = False
    mouse_start_x, mouse_start_y = 0, 0
    offset_start_x, offset_start_y = 0, 0

    # Game loop
    running = True
    while running:
        screen.fill((0, 0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Start dragging
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
                dragging = True
                mouse_start_x, mouse_start_y = pygame.mouse.get_pos()
                offset_start_x, offset_x = offset_x, offset_x
                offset_start_y, offset_y = offset_y, offset_y

            # Stop dragging
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False

        # Handle mouse dragging
        if dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            offset_x = offset_start_x + (mouse_x - mouse_start_x)
            offset_y = offset_start_y + (mouse_y - mouse_start_y)

        # Handle key presses for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            offset_x += scroll_speed
        if keys[pygame.K_RIGHT]:
            offset_x -= scroll_speed
        if keys[pygame.K_UP]:
            offset_y += scroll_speed
        if keys[pygame.K_DOWN]:
            offset_y -= scroll_speed

        # Wrap horizontally for 360 effect
        if offset_x > image_width:
            offset_x -= image_width
        elif offset_x < -image_width:
            offset_x += image_width



        # Blit images for smooth wrapping
        screen.blit(image, (offset_x, offset_y))
        screen.blit(image, (offset_x - image_width, offset_y))  # Left duplicate
        screen.blit(image, (offset_x + image_width, offset_y))  # Right duplicate

        # Update display
        pygame.display.flip()

    pygame.quit()
