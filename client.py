import socket
import pickle
from typing import Any


class Client:
    def __init__(self, name: str, server_addr: tuple[str, int]) -> None:
        self.name = name
        self.server_addr = server_addr
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.board = pickle.loads(self.connect())

    def connect(self) -> bytes:
        self.socket.connect(self.server_addr)
        return self.socket.recv(4096*8)

    def disconnect(self) -> None:
        self.socket.close()
    
    def send(self, content: Any, dump_pickle: bool=False) -> None:
        if dump_pickle:
            content = pickle.dumps(content)

        self.socket.send(content)

    def receive(self, bufsize: int, load_pickle: bool=False) -> Any:
        result = self.socket.recv(bufsize)

        if load_pickle:
            result = pickle.loads(result)

        return result