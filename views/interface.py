import os
import time
from controllers.tarefacontroller import TarefaController as TController

class MainView:

    def __init__(self):
        self.tela_atual = None
        self.mudar_tela(TelaInicial())

    def mudar_tela(self, tela):
        if self.tela_atual:
            os.system('clear')
        self.tela_atual = tela

class TelaInicial(MainView):

    def __init__(self):        
        self.print_menu()

    def print_menu(self):

        print('=== Menu ===')
        print('1 - Cadastrar nova tarefa'),
        print('2 - Alterar tarefa existente'),
        print('3 - Remover tarefa existente'),
        print('4 - Listar tarefas'),
        print('0 - Sair')
        print('============')

        self.option = int(input('Digite a opção desejada: '))
        self.get_option(self.option)

    def get_option(self, option):
        if option == 1:
            self.mudar_tela(CadastrarTarefa())
        elif option == 2:
            self.mudar_tela(AlterarTarefa())
        elif option == 3:
            self.mudar_tela(RemoverTarefa())
        elif option == 4:
            self.mudar_tela(ListarTarefas())
        elif option == 0:
            self.mudar_tela(TelaFinal()) 
        else:
            print('Opção inválida, tente novamente.')
            time.sleep(5)
            self.mudar_tela(TelaInicial())

class CadastrarTarefa(MainView):
    
        def __init__(self):            
            self.print_cadastro_form()
            self.cadastro_tarefa()
    
        def print_cadastro_form(self):
            print('=== Cadastro de tarefa ===')
            self.titulo = input('Digite o título da tarefa: ')
            self.descricao = input('Digite a descrição da tarefa: ')
            self.status = input('Digite o status da tarefa: ')
            
        def cadastro_tarefa(self):
            try:
                if TController().criar_tarefa(self.titulo, self.descricao, self.status):
                    print('Tarefa cadastrada com sucesso!')
                else:
                    print('Erro ao cadastrar tarefa, tente novamente.')
                time.sleep(5)
                self.mudar_tela(TelaInicial())
            except Exception as e:
                print('Erro ao cadastrar tarefa, tente novamente.', e)
                time.sleep(5)
                self.mudar_tela(TelaInicial())

class AlterarTarefa(MainView):
    
    def __init__(self):        
        self.print_alterar_form()
        self.alterar_tarefa()
    
    def print_alterar_form(self):
        print('=== Alterar tarefa ===')
        self.id = int(input('Digite o ID da tarefa que deseja alterar: '))
        self.titulo = input('Digite o novo título da tarefa: ')
        self.descricao = input('Digite a nova descrição da tarefa: ')
        self.status = input('Digite o novo status da tarefa: ')
    
    def alterar_tarefa(self):
        try:
            TController().atualizar_tarefa(self.id, self.titulo, self.descricao, self.status)
            print('Tarefa alterada com sucesso!')
            time.sleep(5)
            self.mudar_tela(TelaInicial())
        except Exception as e:
            print('Erro ao alterar tarefa, tente novamente.', e)
            time.sleep(5)
            self.mudar_tela(TelaInicial())

class RemoverTarefa(MainView):
    
    def __init__(self):        
        self.print_remover_form()
        self.remover_tarefa()
    
    def print_remover_form(self):
        print('=== Remover tarefa ===')
        self.id = int(input('Digite o ID da tarefa que deseja remover: '))
    
    def remover_tarefa(self):
        try:
            TController().deletar_tarefa(self.id)
            print('Tarefa removida com sucesso!')
            time.sleep(5)
            self.mudar_tela(TelaInicial())
        except Exception as e:
            print('Erro ao remover tarefa, tente novamente.', e)
            time.sleep(5)
            self.mudar_tela(TelaInicial())

class ListarTarefas(MainView):
        
        def __init__(self):
            self.listar_tarefas()
        
        def listar_tarefas(self):
            try:
                tarefas = TController().listar_tarefas()
                print('=== Lista de tarefas ===')
                for tarefa in tarefas:
                    print(f'ID: {tarefa["id"]}')
                    print(f'Título: {tarefa["titulo"]}')
                    print(f'Descrição: {tarefa["descricao"]}')
                    print(f'Status: {tarefa["status"]}')
                    print('=========================')
                time.sleep(5)
                self.mudar_tela(TelaInicial())
            except Exception as e:
                print('Erro ao listar tarefas, tente novamente.', e)
                time.sleep(5)
                self.mudar_tela(TelaInicial())

class TelaFinal(MainView):
    
    def __init__(self):
        print('Volte sempre!')
        time.sleep(1)
        exit()