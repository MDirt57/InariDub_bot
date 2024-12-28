from abc import ABC, abstractmethod


class TitleRepository(ABC):
    @abstractmethod
    def get_all_titles(self):
        pass

