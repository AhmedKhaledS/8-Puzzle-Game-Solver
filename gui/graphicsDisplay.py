import pygame as pg
from gui import tile

WINDOW_WIDTH, WINDOW_HEIGHT = 480, 480
TILE_WIDTH = WINDOW_WIDTH / 3
TILE_HEIGHT = WINDOW_HEIGHT / 3

class GraphicsPuzzle:

    def __init__(self):
        self.game = "8-puzzle"

    def initialize_game(self):
        pg.init()
        window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption("8-Puzzle-Game")
        return window

    def prepare_tiles(self, gameState):
        x, y = 0, 0
        tiles = []
        for i in range(9):
            tiles.append(tile.Tile(x, y, TILE_WIDTH, TILE_HEIGHT, gameState.get_state_stream()[i]))
            x = (x + TILE_WIDTH + 3 if x + TILE_WIDTH < WINDOW_WIDTH else 0)
            if (i+1) % 3 == 0:
                y = (y + TILE_HEIGHT + 3 if y + TILE_HEIGHT < WINDOW_HEIGHT else 0)
        return tiles

    def draw_tiles(self, window, tiles):
        font = pg.font.SysFont('Comic Sans MS', 120)
        for i in range(9):
            if tiles[i].number == 0:
                pg.draw.rect(window, (215, 225, 242),
                         (tiles[i].pos_x, tiles[i].pos_y, tiles[i].width, tiles[i].height))
            else:
                pg.draw.rect(window, (87, 89, 91),
                         (tiles[i].pos_x, tiles[i].pos_y, tiles[i].width, tiles[i].height))
                text_tile = font.render(str(tiles[i].number), False, (16, 39, 76))
                window.blit(text_tile, (tiles[i].pos_x + TILE_WIDTH / 3, tiles[i].pos_y + TILE_HEIGHT / 4))
        pg.display.update()

    def show(self, gameSolution):
        solution_states = gameSolution.path
        print(len(solution_states))
        state_count = 0
        window = self.initialize_game()
        run = True
        while run:
            pg.time.delay(1000)
            print(state_count)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            tiles = self.prepare_tiles(solution_states[state_count])
            state_count += (1 if state_count + 1 < len(solution_states) else 0)
            self.draw_tiles(window, tiles)

        pg.quit()
