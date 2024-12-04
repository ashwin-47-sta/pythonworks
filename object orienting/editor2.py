from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):

        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def debug(self):

        pass

    @abstractmethod
    def execute(self):
        pass


class vscode(Editor):

    def open(self):

        print("vscode open method")

vscode_instance=vscode()

vscode_instance.open()

