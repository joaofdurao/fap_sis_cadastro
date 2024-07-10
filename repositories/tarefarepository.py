import os
import json

from models.tarefa import Tarefa

class TarefaRepository:
    TAREFA_JSON = os.curdir + '/repositories/tarefa_repo.json'

    def create_tarefa(self, tarefa):   
        new_tarefa = tarefa
        new_tarefa.id = self._generate_tarefa_id()

        try:
            with open(self.TAREFA_JSON, 'r+') as arquivo:
                try: 
                    tarefas = json.load(arquivo)
                except json.JSONDecodeError: 
                    print('Arquivo JSON em branco. Gerando primeira tarefa.')
                    tarefas = []
                    
                tarefas.append(new_tarefa.__dict__)
                arquivo.seek(0)
                json.dump(tarefas, arquivo, indent=4)
                arquivo.truncate()
                return True
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False

    def find_tarefa_by_id(self, id):
        try:
            with open(self.TAREFA_JSON, 'r') as arquivo:
                    tarefas = json.load(arquivo)
                    for tarefa in tarefas:
                        if tarefa['id'] == id:
                            tarefa_result = Tarefa(tarefa['id'], 
                                                     tarefa['titulo'], 
                                                     tarefa['descricao'], 
                                                     tarefa['status'])
                            return tarefa_result
    
                    raise ValueError('Tarefa não encontrada.')
        except json.decoder.JSONDecodeError:
            print('Arquivo JSON em branco.')
        except Exception as e:
            print(f'Erro no repositorio: {e}')

    def list_tarefas(self):
        try:
            with open(self.TAREFA_JSON, 'r') as arquivo:
                tarefas = json.load(arquivo)
                print('repoooo', tarefas)
                tarefas_list = []
                for tf in tarefas:
                    print('tarefa', tf)
                    tarefas_list.append(Tarefa(tf['id'], 
                                                 tf['titulo'], 
                                                 tf['descricao'], 
                                                 tf['status']))
                return tarefas_list

        except json.decoder.JSONDecodeError:
            print('Arquivo JSON em branco.')
        except Exception as e:
            print(f'Erro no repositorio: {e}')   

    def update_tarefa(self, tarefa):
        try:
            updated_tarefa = self.find_tarefa_by_id(tarefa.id)
            if updated_tarefa:
                updated_tarefa.titulo = tarefa.titulo
                updated_tarefa.descricao = tarefa.descricao
                updated_tarefa.status = tarefa.status

            else:
                return False

            with open(self.TAREFA_JSON, 'r+') as arquivo:
                tarefas = json.load(arquivo)
                for tf in tarefas:
                    if tf['id'] == tarefa.id:
                        tf['titulo'] = updated_tarefa.titulo
                        tf['descricao'] = updated_tarefa.descricao
                        tf['status'] = updated_tarefa.status
                        break

                arquivo.seek(0)
                json.dump(tarefas, arquivo, indent=4)
                arquivo.truncate()
                return True
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False
    
    def delete_tarefa(self, id):
        try:
            with open(self.TAREFA_JSON, 'r+') as arquivo:
                tarefas = json.load(arquivo)
                for tf in tarefas:
                    if tf['id'] == id:
                        tarefas.remove(tf)
                        arquivo.seek(0)
                        json.dump(tarefas, arquivo, indent=4)
                        arquivo.truncate()
                        print('Tarefa deletada com sucesso.')
                        return True
                return False
        except Exception as e:
            print(f'Erro no repositorio: {e}')
            return False
    
    def _generate_tarefa_id(self):
        try:
            with open(self.TAREFA_JSON, 'r') as arquivo:
                tarefas = json.load(arquivo)
                if len(tarefas) == 0:
                    return 1
                else:
                    return tarefas[-1]['id'] + 1
        except json.decoder.JSONDecodeError:
            return 1
        except Exception as e:
            print(f'Erro no repositorio: {e}')