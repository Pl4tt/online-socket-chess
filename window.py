import pygame

from client import Client
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SERVER_ADDR, FONT, WHITE, CAPTION, BLACK


def menu_screen(window: pygame.Surface, name: str) -> None:
    window.fill(BLACK)  # TODO: load bg image

    font = pygame.font.SysFont(FONT, SCREEN_HEIGHT//10)
    text1 = font.render("Press any key", True, WHITE)
    text2 = font.render("to enter a game", True, WHITE)
    text3 = font.render(name, True, WHITE)
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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                client = Client(name, SERVER_ADDR)
                chess_game(window, client)

def chess_game(window: pygame.Surface, client: Client) -> None:
    board = client.board

    board.draw(window)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        pygame.display.update()


def main() -> None:
    pygame.init()

    name = input("Enter your name: ")

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    # TODO: set icon

    menu_screen(window, name)


if __name__ == "__main__": main()