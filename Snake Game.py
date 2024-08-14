import pygame
import random
import time
import math
import os


# import pygame_gui


class Snake:
    """
       A class to represent the snake in the game.

       Attributes:
       ----------
       x : int
           The x-coordinate of the snake's position.
       y : int
           The y-coordinate of the snake's position.
       size : int
           The size of the snake's body.
       red_color : pygame.Color
           The color of the snake (red).
       dir_x : int
           The direction of movement along the x-axis.
       dir_y : int
           The direction of movement along the y-axis.
       direction : str
           The current direction of the snake ('RIGHT', 'LEFT', 'UP', 'DOWN').
       snake_list : list
           The list representing the snake's body segments.
       snake_length : int
           The initial length of the snake.
       score : int
           The player's current score.

       Methods:
       -------
       change_direction(user_dir):
           Changes the direction of the snake based on user input.
       move_snake(speed):
           Moves the snake in the current direction with the given speed.
       check_boarder():
           Checks and updates the snake's position when it crosses the screen borders.
       """
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.red_color = pygame.color.Color('red')
        self.dir_x = 0
        self.dir_y = 0
        self.direction = "RIGHT"
        self.snake_list = []
        self.snake_length = 8
        self.score = 0

    def change_direction(self, user_dir):
        if user_dir == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        if user_dir == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if user_dir == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if user_dir == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

    def move_snake(self, speed):
        if self.direction == "RIGHT":
            self.dir_x = 0
            self.dir_y = 0
            self.dir_x = self.dir_x + speed
        elif self.direction == "LEFT":
            self.dir_x = 0
            self.dir_y = 0
            self.dir_x = self.dir_x - speed
        elif self.direction == "DOWN":
            self.dir_x = 0
            self.dir_y = 0
            self.dir_y = self.dir_y + speed
        elif self.direction == "UP":
            self.dir_x = 0
            self.dir_y = 0
            self.dir_y = self.dir_y - speed

    def check_boarder(self):
        if self.x > screen_width - 1:
            self.x = 0
        elif self.x < 1:
            self.x = screen_width
        elif self.y > screen_height - 1:
            self.y = 0
        elif self.y < 1:
            self.y = screen_height


class Food:
    """
       A class to represent the food for the snake in the game.

       Attributes:
       ----------
       x : int
           The x-coordinate of the food's position.
       y : int
           The y-coordinate of the food's position.
       size : int
           The size of the food.
       green_color : pygame.Color
           The color of the food (green).

       Methods:
       -------
       No methods.
       """
    def __init__(self, size):
        self.x = random.randint(10, screen_width - 10)
        self.y = random.randint(10, screen_height - 10)
        self.size = size
        self.green_color = pygame.Color('green')


class BonusFood:
    """
        A class to represent the bonus food in the game.

        Attributes:
        ----------
        x : int
            The x-coordinate of the bonus food's position.
        y : int
            The y-coordinate of the bonus food's position.
        size : int
            The size of the bonus food.
        trans_yellow_color : tuple
            The transparent yellow color for the bonus food.
        yellow_color : tuple
            The opaque yellow color for the bonus food.

        Methods:
        -------
        No methods.
        """
    def __init__(self, size):
        self.x = random.randint(10, screen_width - 10)
        self.y = random.randint(10, screen_height - 10)
        # self.height = height
        # self.width = width
        self.size = size
        # self.yellow_color = pygame.Color('yellow')
        self.trans_yellow_color = (255, 255, 0, 0)
        self.yellow_color = (255, 255, 0, 255)

    # def bonus_circle(self, screen, color):
    #     # surface_circle = screen.convert_alpha()
    #     # surface_circle.fill((0,0,0,0))
    #     surface_circle = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)   
    #     bonus_food_circle = pygame.draw.circle(surface_circle, color, (self.size, self.size), self.size)
    #     screen.blit(surface_circle, (self.x-self.size, self.y-self.size))
    #     return bonus_food_circle


def update_text(screen, font_type, font_name, text, size, color, antialias, pos, bold):
    """
        Updates the text on the game screen.

        Parameters:
        ----------
        screen : pygame.Surface
            The surface on which to draw the text.
        font_type : str
            The type of font to use ('sys' for system font, 'custom' for custom font).
        font_name : str
            The name of the font.
        text : str
            The text to display.
        size : int
            The font size.
        color : pygame.Color
            The color of the text.
        antialias : bool
            Whether to apply antialiasing to the text.
        pos : tuple
            The (x, y) position of the text on the screen.
        bold : bool
            Whether to make the text bold.
        """
    if font_type == "sys":
        font = pygame.font.SysFont(font_name, size, bold)
    elif font_type == "custom":
        font = pygame.font.Font(my_font_path, size)
    font_text = font.render(text, antialias, color)
    screen.blit(font_text, pos)


def get_coordinates_in_circle(x, y, radius):
    """
        Generates a list of coordinates within a circle.

        Parameters:
        ----------
        x : int
            The x-coordinate of the circle's center.
        y : int
            The y-coordinate of the circle's center.
        radius : int
            The radius of the circle.

        Returns:
        -------
        list
            A list of coordinates within the circle.
        """
    coordinates = []
    for i in range(x - 1 - radius, x + radius + 2):
        for j in range(y - 1 - radius, y + radius + 2):
            distance = math.sqrt((i - x) ** 2 + (j - y) ** 2)
            if distance <= radius:
                coordinates.append([i, j])
    return coordinates


class InputTextBox:
    """
        A class to represent a text input box.

        Attributes:
        ----------
        x : int
            The x-coordinate of the input box.
        y : int
            The y-coordinate of the input box.
        w : int
            The width of the input box.
        h : int
            The height of the input box.
        active_color : pygame.Color
            The color of the input box when active.
        inactive_color : pygame.Color
            The color of the input box when inactive.
        color : pygame.Color
            The current color of the input box.
        active : bool
            Whether the input box is active or not.

        Methods:
        -------
        No methods.
        """
    def __init__(self, x, y, width, height, active_color, inactive_color) -> None:
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.color = self.inactive_color
        self.active = False


def start_screen():
    """
        Displays the start screen and handles user input for starting the game.

        The user can input the snake's speed and start the game by clicking the "START" button.
        """
    text = ''
    start_screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("Snake Game by Haja")
    # manager = pygame_gui.UIManager((500, 300))
    clock = pygame.time.Clock()
    # button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(185, 160, 100, 50), text='Start')
    input_box = InputTextBox(260, 123, 25, 22, pygame.Color((0, 0, 50)), pygame.Color('lightskyblue3'))
    input_rect = pygame.Rect(input_box.x, input_box.y, input_box.w, input_box.h)
    button_box = InputTextBox(185, 160, 100, 30, (180, 180, 180), (110, 110, 110))
    button_rect = pygame.Rect(button_box.x, button_box.y, button_box.w, button_box.h)

    is_showing = True
    while is_showing:
        # clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_showing = False
            # manager.process_events(event)
            # if event.type  == pygame_gui.UI_BUTTON_PRESSED:
            #     if event.ui_element == button:
            #             if len(text ) != 0:
            #                 is_showing = False
            #                 play_snake(int(text))
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    input_box.active = not input_box.active
                else:
                    input_box.active = False
                # Change the current color of the input box.
                input_box.color = input_box.active_color if input_box.active else input_box.inactive_color

                if button_rect.collidepoint(event.pos):
                    if len(text) != 0 and text.isnumeric():
                        is_showing = False
                        play_snake(int(text))

            if event.type == pygame.KEYDOWN:
                if input_box.active:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if len(text) != 0 and text.isnumeric():
                            is_showing = False
                            play_snake(int(text))
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) <= 1:
                            text += str(event.unicode).strip()

        if len(text) > 0 and text.isnumeric():
            if int(text) > 10:
                text = str(10)
        mx, my = pygame.mouse.get_pos()
        # print(mx, my, button_box.x, button_box.x + button_box.w)
        if (button_box.x <= mx <= button_box.x + button_box.w) and (button_box.y <= my <= button_box.y + button_box.h):
            # Toggle the active variable.
            button_box.active = True
        else:
            button_box.active = False
            # Change the current color of the input box.
        # manager.update(time_delta)
        start_screen.fill(pygame.Color(0, 102, 102))
        button_box.color = button_box.active_color if button_box.active else button_box.inactive_color
        # Snake Game Text
        update_text(start_screen, "sys", "Impact", "S N A K E   G A M E", 50, pygame.Color(200, 0, 0), True, (80, 50),
                    False)
        update_text(start_screen, "sys", "Georgia", "Speed  -", 20, pygame.Color('white'), True, (180, 120), False)
        update_text(start_screen, "sys", "Arial", text, 15, input_box.color, True, (input_box.x + 4, input_box.y + 2),
                    True)
        pygame.draw.rect(start_screen, input_box.color, input_rect, 2)
        pygame.draw.rect(start_screen, button_box.color, button_rect)
        update_text(start_screen, "sys", "Courier New", "START", 25, pygame.Color('black'), True,
                    (button_box.x + 12, button_box.y + 2), True)
        # manager.draw_ui(start_screen)
        pygame.display.update()  # update the entire screen


def play_snake(speed):
    """
       The main function to run the snake game.

       Parameters:
       ----------
       speed : int
           The speed of the snake as input by the user.
       """
    food_count = 0
    food_eat_sound = pygame.mixer.Sound(my_path + r"\eat_food_sound.wav")
    game_over_sound = pygame.mixer.Sound(my_path + r"\game_over_sound.wav")
    bonus_food_sound = pygame.mixer.Sound(my_path + r"\bonus_food_sound.wav")
    snake_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game by Haja")
    snake = Snake(50, 100, 7)
    food = Food(5)
    bonus_food = BonusFood(15)
    clock = pygame.time.Clock()
    cyan = (20, 100, 120)
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        snake_screen.fill(pygame.Color('black'))
        for x, y in snake.snake_list:
            # food_box = pygame.draw.rect(screen, food.green_color, (food.x, food.y, food.height, food.width),0,8)
            snake_box = pygame.draw.circle(snake_screen, snake.red_color, (x, y), snake.size)
            food_box = pygame.draw.circle(snake_screen, food.green_color, (food.x, food.y), food.size)
            if snake_box.colliderect(food_box):
                coord_list = get_coordinates_in_circle(x, y, (food.size + snake.size))

                if [food.x, food.y] in coord_list:
                    food_eat_sound.play()
                    snake.snake_length += 5
                    snake.score += 1
                    if food_count == 10:
                        food_count = 0
                    food_count += 1
                    food = Food(5)

            # if food_count == 0 or food_count % 3 != 0:
            #     bonus_food_box = pygame.draw.circle(snake_screen, pygame.color.Color('black'), (screen_width + 50, screen_height + 50), 5)
            if food_count == 10:
                bonus_food_box = pygame.draw.circle(snake_screen, pygame.color.Color('yellow'),
                                                    (bonus_food.x, bonus_food.y), bonus_food.size)
                if snake_box.colliderect(bonus_food_box):
                    bonus_food_sound.play()
                    food_count = 0
                    snake.score += 5
                    bonus_food = BonusFood(15)
                    # bonus_food_box = pygame.draw.circle(snake_screen, pygame.color.Color('black'), (screen_width + 50, screen_height + 50), 5)
                # elif snake_box.colliderect(food_box):
                #     bonus_food_box = pygame.draw.circle(snake_screen, pygame.color.Color('black'), (screen_width + 50, screen_height + 50), 5)

        snake.snake_list.append([snake.x, snake.y])
        if len(snake.snake_list) >= snake.snake_length:
            snake.snake_list.pop(0)
        if snake.snake_list[-1] in snake.snake_list[:-1]:
            game_over_sound.play()
            # print(snake.snake_list[-1])
            # print(snake.snake_list[:-1])
            snake_screen.fill(cyan)
            # Game Over Text
            update_text(snake_screen, "custom", "", "GAME OVER", 100, pygame.Color('white'), True, (120, 150), False)
            # End Score Text
            update_text(snake_screen, "sys", "comicsansms", f"Your Score - {snake.score}", 25, pygame.Color('white'),
                        True, (150, 200), False)
            # end_score_text = end_score_font.render(f"Your Score - {snake.score}", True, white)
            # game_ovr_text = game_ovr_font.render("GAME OVER", True, white)
            # screen.blit(game_ovr_text, (120, 150))
            # screen.blit(end_score_text, (120, 200))
            pygame.display.update()
            time.sleep(3)
            is_running = False
            start_screen()
            snake.snake_list.clear()
            snake.snake_length = 8
            snake.score = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            snake.change_direction("RIGHT")
        if keys[pygame.K_LEFT]:
            snake.change_direction("LEFT")
        if keys[pygame.K_UP]:
            snake.change_direction("UP")
        if keys[pygame.K_DOWN]:
            snake.change_direction("DOWN")

        snake.move_snake(speed)
        snake.check_boarder()
        snake.x = snake.x + snake.dir_x
        snake.y = snake.y + snake.dir_y
        # Score Text
        bonus_food_box = pygame.draw.circle(snake_screen, pygame.color.Color('black'),
                                            (screen_width + 50, screen_height + 50), 5)
        update_text(snake_screen, "sys", "Arial", f"Score - {snake.score}", 15, pygame.Color('white'), True, (10, 10),
                    True)
        # score_text = score_font.render(f"Score - {snake.score}", True, white)
        # screen.blit(score_text, (10, 10))
        pygame.display.update()  # update the entire screen
        clock.tick(50)
        # pygame.display.flip()


if __name__ == '__main__':
    screen_width = 490
    screen_height = 420
    my_path = os.path.dirname(os.path.abspath(__file__))
    my_font_path = my_path + r"\game_over.ttf"
    pygame.init()
    start_screen()
    pygame.quit()
    exit()
