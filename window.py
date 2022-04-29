import os
import pickle
import pygame

from client import Client
from constants import BOARD_LENGTH, SCREEN_WIDTH, SCREEN_HEIGHT, SERVER_ADDR, FONT, TILE_LENGTH, WHITE, CAPTION, BLACK, RED


def draw_start_menu(window: pygame.Surface, name: str, connection_lost: bool=False, connection_refused: bool=False) -> None:
    window.fill(BLACK)  # TODO: load bg image

    font = pygame.font.SysFont(FONT, SCREEN_HEIGHT//10)
    text1 = font.render("Press space key", True, WHITE)
    text2 = font.render("to enter a game", True, WHITE)
    text3 = font.render(name, True, WHITE)

    if connection_refused:
        conn_text = font.render("(connection refused)", True, RED)
        conn_text_rect = conn_text.get_rect()
        conn_text_rect.centerx = SCREEN_WIDTH/2
        window.blit(conn_text, conn_text_rect)
    
    if connection_lost:
        conn_text = font.render("(connection lost)", True, RED)
        conn_text_rect = conn_text.get_rect()
        conn_text_rect.centerx = SCREEN_WIDTH/2
        window.blit(conn_text, conn_text_rect)

    text1_rect = text1.get_rect()
    text1_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - SCREEN_HEIGHT//10)
    text2_rect = text2.get_rect()
    text2_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    text3_rect = text3.get_rect()
    text3_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + SCREEN_HEIGHT//10)

    window.blit(text1, text1_rect)
    window.blit(text2, text2_rect)
    window.blit(text3, text3_rect)

    pygame.display.update()

def draw_waiting(window: pygame.Surface) -> None:
    window.fill(BLACK)

    font = pygame.font.SysFont(FONT, SCREEN_HEIGHT//10)
    text = font.render("Waiting for enemy...", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    window.blit(text, text_rect)
    pygame.display.update()

def menu_screen(window: pygame.Surface, name: str, connection_lost: bool=False) -> None:
    draw_start_menu(window, name, connection_lost)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw_waiting(window)
                    try:
                        client = Client(name, SERVER_ADDR)
                        chess_game(window, client)
                    except ConnectionRefusedError:
                        draw_start_menu(window, name, connection_refused=True)

def chess_game(window: pygame.Surface, client: Client) -> None:
    window.fill(BLACK)

    board = client.board

    board.draw(window)
    pygame.display.update()

    while True:
        if client.name != board.turn:
            try:
                command = client.receive(4096)  # wait for their move
                command["window"] = window
                board.command(command, window)
            except ConnectionResetError:  # connection closed
                menu_screen(window, client.name, connection_lost=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                client.disconnect()
                pygame.quit()
                exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = int((y - (SCREEN_HEIGHT - BOARD_LENGTH)/2)//TILE_LENGTH)
                col = int((x - (SCREEN_WIDTH - BOARD_LENGTH)/2)//TILE_LENGTH)
                
                if not 0 <= row <= 7 or not 0 <= col <= 7:
                    continue

                selected = board.selected

                if board.click(client.name, row, col, window):
                    client.send({
                        "command": "move",
                        "p_name": client.name,
                        "pos_before": selected,
                        "pos_after": (row, col),
                    })  # send your move

        pygame.display.update()


def main() -> None:
    pygame.init()

    name = input("Enter your name: ")

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "images", "window_icon.png")))

    menu_screen(window, name)


if __name__ == "__main__": main()