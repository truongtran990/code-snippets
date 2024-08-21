import os
import sys
import time
import random

GAME_WIDTH = 20
GAME_HEIGHT = 20
DELAY = 1


pacman = (0, 0)
ghosts = [(5, 5), (10, 10)]
score = -10
is_game_over = False
dots = {(x, y) for x in range(GAME_WIDTH) for y in range(GAME_HEIGHT)}


def get_user_input() -> None:
    while True:
        global pacman, ghosts, is_game_over

        if is_game_over:
            sys.exit()

        user_input = input()
        if user_input == "q":
            is_game_over = True
            sys.exit()
        else:
            global pacman
            if user_input == "w":
                pacman = (pacman[0], pacman[1] - 1)
            elif user_input == "a":
                pacman = (pacman[0] - 1, pacman[1])
            elif user_input == "s":
                pacman = (pacman[0], pacman[1] + 1)
            elif user_input == "d":
                pacman = (pacman[0] + 1, pacman[1])
            else:
                pass


def compute_game_world():
    while True:
        global pacman, ghosts, is_game_over, score

        if is_game_over:
            sys.exit()

        for i, ghost in enumerate(ghosts):
            new_ghost_x = ghost[0] + random.choice([-1, 0, 1])
            new_ghost_y = ghost[1] + random.choice([-1, 0, 1])
            new_ghost_x = new_ghost_x if 0 <= new_ghost_x < GAME_WIDTH else ghost[0]
            new_ghost_y = new_ghost_y if 0 <= new_ghost_y < GAME_HEIGHT else ghost[1]
            ghosts[i] = (new_ghost_x, new_ghost_y)

        if pacman in ghosts:
            is_game_over = True
            sys.exit()

        if pacman in dots:
            dots.remove(pacman)
            score += 10

        if not dots:
            is_game_over = True
            sys.exit()

        time.sleep(DELAY)


def render_next_screen() -> None:
    while True:
        global pacman, ghosts, score, is_game_over, dots
        os.system("clear")

        if is_game_over:
            print("GAME OVER!")
            print(f"Your score: {score}. Press Enter")
            sys.exit()

        # Render the game world on the terminal
        game_world = []
        for y in range(GAME_HEIGHT):
            row = []
            for x in range(GAME_WIDTH):
                if (x, y) == pacman:
                    row.append("P")
                elif (x, y) in ghosts:
                    row.append("G")
                elif (x, y) in dots:
                    row.append(".")
                else:
                    row.append(" ")
            game_world.append(" ".join(row))

        print(f"Score:{score}. Press 'q' to quit")
        print("\n".join(game_world))
        # Sleep for a short time to avoid excessive CPU usage
        time.sleep(DELAY)
