from abc import ABC, abstractmethod
import math

class FunzioneMatematica(ABC):
    @abstractmethod
    def calcola(self, x):
        pass

class FunzioneEsponenziale(FunzioneMatematica):
    def __init__(self, base):
        self.base = base

    def calcola(self, x):
        return self.base ** x

if __name__ == '__main__':
    x = input("inserisci i valori da sommare separati da virgola: ")
    checked=check(x)
    print("vuoi sommare questi numeri", checked)
    ris=somma(checked)
    print(f' Facile! fa {ris}')