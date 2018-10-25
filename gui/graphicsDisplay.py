import pygame as pg
import tile

WINDOW_WIDTH, WINDOW_HEIGHT = 480, 480
TILE_WIDTH = WINDOW_WIDTH / 3
TILE_HEIGHT = WINDOW_HEIGHT / 3
x, y = 0, 0


def initialize_game():
    pg.init()
    window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption("8-Puzzle-Game")
    vel = 5
    return window


def prepare_tiles():
    x, y = 0, 0
    tiles = []
    for i in range(8):
        tiles.append(tile.Tile(x, y, TILE_WIDTH, TILE_HEIGHT, i + 1))
        x = (x + TILE_WIDTH + 3 if x + TILE_WIDTH < WINDOW_WIDTH else 0)
        if (i+1) % 3 == 0:
            y = (y + TILE_HEIGHT + 3 if y + TILE_HEIGHT < WINDOW_HEIGHT else 0)

    return tiles


def draw_tiles(window, tiles):
    font = pg.font.SysFont('Comic Sans MS', 120)
    for i in range(8):
        pg.draw.rect(window, (87, 89, 91),
                     (tiles[i].pos_x, tiles[i].pos_y, tiles[i].width, tiles[i].height))
        text_tile = font.render(str(tiles[i].number), False, (16, 39, 76))
        window.blit(text_tile, (tiles[i].pos_x + TILE_WIDTH / 3, tiles[i].pos_y + TILE_HEIGHT / 4))
    pg.display.update()


def main():
    window = initialize_game()
    run = True
    while run:
        pg.time.delay(100)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        tiles = prepare_tiles()
        draw_tiles(window, tiles)

    pg.quit()


if __name__ == '__main__':
    main()
