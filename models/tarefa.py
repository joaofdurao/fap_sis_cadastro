class Tarefa:
    def __init__(self, id = None, titulo = None, descricao = None, status = None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def __str__(self):
        return f'{self.id} - {self.titulo} - {self.descricao} - {self.status}'