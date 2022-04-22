import multiprocessing
import os
import time
from itertools import product
import string
from typing import Any
from zipfile import ZipFile
from threading import Thread


def locateFile(path: str, password: str) -> None:
    """
    Descompacta arquivo, se possuir senha, e esta for desconhecida, tenta a bruteforce
    :param path:
    :param password:
    :return:
    """
    zip_ = ZipFile(path, "r")
    length_of_directory = len(os.listdir("C:\\Users\\Marcu\\Desktop\\AtividadesEmPython\\"))
    now: int = 0
    with zip_ as f:  # gerenciador de contexto para evitar bo com os processos
        try:
            zip_.extractall(pwd=password.encode())
        except Exception:
            ...
        else:
            now = len(os.listdir("C:\\Users\\Marcu\\Desktop\\AtividadesEmPython\\"))
            if length_of_directory < now:
                print(f"Congratulations!!! ☻")
                print(f"Password was finded: {password}")


def howMuchTimeLonger(function) -> Any:
    """
    Decorator que calcula o tempo
    :param function:
    :return: function
    """
    def wrapper(*args):
        init = time.time()
        function(args[0])
        print(f"Executado em: {time.time() - init}")
    return wrapper


@howMuchTimeLonger
def findPass(pw_length=9) -> None:
    """
    tenta encontrar passwords
    :param pw_length: integer
    :return: None (void)
    """
    ascii: str = string.ascii_letters + string.digits + string.punctuation
    chars: list[chr] = [char for char in ascii]
    hits: int = 0
    secret: str = ""
    for items in range(1, pw_length):
        for item in product(chars, repeat=items): # generator
            secret = ''.join(item)
            print(f"Testando: {secret}")
            locateFile("C:\\Users\\Marcu\\Desktop\\AtividadesEmPython\\arquivo.zip", secret)
            hits += 1
    print(f"TENTATIVAS: {hits}")


def threadStart(**kwargs):
    """
    Inicia threads
    :param kwargs:
    :return:
    """
    core = multiprocessing.cpu_count()
    [Thread(target=kwargs['function'], args=(kwargs['parameter'], )).start() for n in range(core)]
    [Thread(target=kwargs['function'], args=(kwargs['parameter'],)).join() for n in range(core)]


if __name__ == '__main__':
    threadStart(function=findPass, parameter=9)
