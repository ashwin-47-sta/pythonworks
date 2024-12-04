
class editor:

    name:str

    vandor:str


    def __init__(self,name,vandor):

        self.name=name

        self.vandor=vandor

    def __str__(self):

        return self.name
    

editor_instance1=editor("pycharm","jebrains")
editor_instance2=editor("intellij","jetbrains")
editor_instance3=editor("vscode","microsoft")

print(editor_instance2)