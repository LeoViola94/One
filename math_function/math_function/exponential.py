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

