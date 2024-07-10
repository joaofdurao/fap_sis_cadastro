from models.tarefa import Tarefa
from repositories.tarefarepository import TarefaRepository as TRepo

class TarefaController:

    def criar_tarefa(self, titulo_tarefa, descricao_tarefa, status_tarefa):
        print('teste')
        tarefa = Tarefa(titulo = titulo_tarefa, descricao = descricao_tarefa, status = status_tarefa)
        
        try: 
            TRepo.create_tarefa(tarefa)
            return True  
        except Exception:
            raise Exception('Erro ao criar tarefa.')

    def encontrar_tarefa(self, tarefa_id):
        try:
            tarefa = TRepo.find_tarefa_by_id(tarefa_id)
            tarefa_dict = tarefa.__dict__
            return tarefa_dict
        except Exception:
            return False

    def listar_tarefas(self):
        try:
            tarefas = TRepo.list_tarefas()
            tarefas_dict = []
            for i in tarefas:
                tarefas_dict.append(i.__dict__)
            return tarefas_dict
        except Exception:
            return False

    def atualizar_tarefa(self, id_tarefa, titulo_tarefa = None, descricao_tarefa = None, status_tarefa = None):
        try:
            tarefa = Tarefa(id = id_tarefa, titulo = titulo_tarefa, descricao = descricao_tarefa, status = status_tarefa)
            TRepo.update_tarefa(tarefa)
            return True
        except Exception:
            return False

    def deletar_tarefa(self, id_tarefa):
        try:
            TRepo.delete_tarefa(id_tarefa)
            return True
        except Exception:
            return False