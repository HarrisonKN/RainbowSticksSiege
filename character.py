import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, speed=5, frame_count=4):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()  # Load the sprite sheet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.speed = speed

        # Animation variables
        self.current_frame = 0
        self.animation_speed = 10  # Frame rate of the animation
        self.frames = self.load_animation_frames(image_path, frame_count)

    def load_animation_frames(self, image_path, frame_count):
        """Load the individual frames from the sprite sheet."""
        sprite_sheet = pygame.image.load(image_path).convert_alpha()
        frame_width = sprite_sheet.get_width() // frame_count  # Assuming frames are laid horizontally
        frames = []

        # Cut out individual frames from the sprite sheet
        for i in range(frame_count):
            frame = sprite_sheet.subsurface(i * frame_width, 0, frame_width, sprite_sheet.get_height())
            frames.append(frame)
        return frames

    def update(self, keys):
        """Update character movement and animation."""
        # Handle movement input
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
        else:
            self.vel_x = 0
        
        if keys[pygame.K_UP]:
            self.vel_y = -self.speed
        elif keys[pygame.K_DOWN]:
            self.vel_y = self.speed
        else:
            self.vel_y = 0

        # Update position
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Update animation
        self.animate()

    def animate(self):
        """Cycle through frames to animate the character."""
        self.current_frame += 1
        if self.current_frame >= self.animation_speed * len(self.frames):
            self.current_frame = 0
        frame_index = self.current_frame // self.animation_speed
        self.image = self.frames[frame_index]
