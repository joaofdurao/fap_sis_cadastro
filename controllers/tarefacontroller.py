from models.tarefa import Tarefa
from repositories.tarefarepository import TarefaRepository as TRepo

class TarefaController:

    def __init__(self):
        self.t_repo = TRepo()
        self.tarefa = Tarefa()

    def criar_tarefa(self, titulo_tarefa, descricao_tarefa, status_tarefa):
        self.tarefa = Tarefa(titulo = titulo_tarefa, descricao = descricao_tarefa, status = status_tarefa)
        
        try: 
            self.t_repo.create_tarefa(self.tarefa)
            return True  
        except Exception as e:
            print('Erro ao cadastrar tarefa, tente novamente.', e)
            return False

    def encontrar_tarefa(self, tarefa_id):
        try:
            self.tarefa = self.t_repo.find_tarefa_by_id(tarefa_id)
            tarefa_dict = self.tarefa.__dict__
            return tarefa_dict
        except Exception:
            return False

    def listar_tarefas(self):
        try:
            tarefas = self.t_repo.list_tarefas()
            print(tarefas)
            tarefas_dict = []
            for i in tarefas:
                print('testeee')
                tarefas_dict.append(i.__dict__)
            return tarefas_dict
        except Exception:
            return False

    def atualizar_tarefa(self, id_tarefa, titulo_tarefa = None, descricao_tarefa = None, status_tarefa = None):
        try:
            self.tarefa = Tarefa(id = id_tarefa, titulo = titulo_tarefa, descricao = descricao_tarefa, status = status_tarefa)
            self.t_repo.update_tarefa(self.tarefa)
            return True
        except Exception:
            return False

    def deletar_tarefa(self, id_tarefa):
        try:
            self.t_repo.delete_tarefa(id_tarefa)
            return True
        except Exception:
            return False