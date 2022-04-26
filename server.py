import socket
import pickle
from threading import Thread

from constants import SERVER_ADDR
from board import Board


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDR)
server_socket.listen()

boards = []
connection_sockets = []


def client_thread(client_socket: socket.socket, board: Board, connection_number: int) -> None:
    client_socket.send(pickle.dumps(board))


if __name__ == "__main__":
    print("[WAITING] for incoming connections")

    while True:
        client_socket, addr = server_socket.accept()
        connection_sockets.append(client_socket)

        print(f"[CONNECTION] total: {len(connection_sockets)}")
        print(connection_sockets, boards)
        if (len(connection_sockets)-1)//2 >= len(boards):
            boards.append(Board())
            print(f"[CREATED] new board, total: {len(boards)}")
        
        thread = Thread(target=client_thread, args=(client_socket, boards[-1], len(connection_sockets)))
        thread.start()
        
