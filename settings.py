
class Settings:
    # do not change
    size = 20 # standart turtle size
    # main
    screen_width = 600
    screen_height = 600
    relational_direction = False
    game_pace = 0.6 #saniye
    count_to_speed_up = 10 # speed up after every {speed_up}
    # snake
    starting_length = 3
    # scoreboard
    alignment = "center"
    font_family = 'Arial'
    font_size = 18
    font_set = 'normal'

    def speed_up(self):
        self.game_pace /= 1.5


s = Settings()