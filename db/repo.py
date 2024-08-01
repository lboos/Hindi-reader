import abc

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list:
        raise NotImplementedError

    def add_term(self, word_1: str, word_2: str):
        raise NotImplementedError