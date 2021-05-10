import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Menu:

    def __init__(self, controller) -> None:
        self.root = tk.Tk()
        self.controller = controller

        self.container = tk.Frame(self.root)
        self.container.pack()

        self.createPesquisar()
        self.createAdicionar()
        self.createRemover()

        self.framePesquisar.grid(row=0, column=0, sticky='nsew')
        self.frameAdicionar.grid(row=0, column=0, sticky='nsew')
        self.frameRemover.grid(row=0, column=0, sticky='nsew')

        self.show_main_menu()
        self.root.mainloop()


    # def print_item(self, text: str) -> None:
    #     """
    #     Imprime um item do menu
    #     :param text: string
    #     """
    #
    #     print('| {:<47s}|'.format(text))

    def print_alert(self, text: str) -> None:
        tk.messagebox.showinfo(title='AVISO', message=text)


    def print_message(self, text: str) -> None:
        tk.messagebox.showinfo(message=text)

    # def _continue(self) -> None:
    #     """
    #     Aguarda uma tecla e volta para o menu principal
    #     """
    #
    #     input('Digite uma tecla para continuar')
    #     self.show_main_menu()

    def salvar(self) -> None:
        self.controller.add_contact(self.nome.get(),
                                    self.telefone.get(),
                                    self.email.get(),
                                    self.grupo.get(),
                                    self.endereco.get(),
                                    self.favorito.get())

    def showFramePesquisar(self):
        self.framePesquisar.tkraise()

    def showFrameaAdicionar(self):
        self.frameAdicionar.tkraise()

    def showFrameaRemover(self):
        self.frameRemover.tkraise()

    def show_main_menu(self) -> None:
        container = tk.Frame(self.root)
        container.pack()

        labelMenu = tk.Label(container, width=20, text='___ MENU ___')
        labelMenu.grid(column=0, row=0, padx=5, pady=5)

        labelPesquisar = tk.Button(container, width=20, text='1. Pesquisar', command=self.showFramePesquisar)
        labelPesquisar.grid(column=0, row=1, padx=5, pady=5)

        labelAdicionar = tk.Button(container, width=20, text='2. Adicionar', command=self.showFrameaAdicionar)
        labelAdicionar.grid(column=0, row=2, padx=5, pady=5)

        labelRemover = tk.Button(container, width=20, text='3. Remover', command=self.showFrameaRemover)
        labelRemover.grid(column=0, row=3, padx=5, pady=5)

        labelSair = tk.Button(container, width=20, text='4. Sair', command=container.quit)
        labelSair.grid(column=0, row=4, padx=5, pady=5)

    # def createPesquisar(self) -> None:
    # container = tk.Frame(self.root)
    # container.pack()
    #
    # self.opc = tk.Entry(container, width=20)
    # self.opc.grid(column=1, row=0, padx=5, pady=5)
    #
    #
    # if self.opc == '1':
    #     self.show_search_menu()
    # elif self.opc == '2':
    #     self.show_add_menu()
    # elif self.opc == '3':
    #     self.show_remove_menu()
    # elif self.opc == '4':
    #     self.exit()
    # else:
    #     self.show_main_menu()
    #
    # opc = input('Digite sua opção: ')
    #
    # if opc == '1':
    #     self.show_search_menu()
    # elif opc == '2':
    #     self.show_add_menu()
    # elif opc == '3':
    #     self.show_remove_menu()
    # elif opc == '4':
    #     self.exit()
    # else:
    #     self.show_main_menu()

    def createPesquisar(self) -> None:
        self.framePesquisar = tk.Frame(self.container)

        labelTitulo = tk.Label(self.framePesquisar, width=20, text='PESQUISAR ')
        labelTitulo.grid(column=2, row=0, padx=5, pady=5)

        labelNome = tk.Label(self.framePesquisar, width=20, text='Nome: ')
        labelNome.grid(column=0, row=1, padx=5, pady=5)

        nome = tk.Entry(self.framePesquisar, width=20)
        nome.grid(column=2, row=1, padx=5, pady=5)

        # name = input('Nome: ')

        # self.controller.search_contact(nome)
        #
        # self._continue()

    #
    def createAdicionar(self):
        self.frameAdicionar = tk.Frame(self.container)

        labelTitulo = tk.Label(self.frameAdicionar, width=20, text='ADICIONAR ')
        labelTitulo.grid(column=1, row=0, padx=5, pady=5)

        labelNome = tk.Label(self.frameAdicionar, width=20, text='Nome: ')
        labelNome.grid(column=0, row=1, padx=5, pady=5)

        self.nome = tk.Entry(self.frameAdicionar, width=20)
        self.nome.grid(column=1, row=1, padx=5, pady=5)

        # --------------#

        labelTelefone = tk.Label(self.frameAdicionar, width=20, text='Telefone: ')
        labelTelefone.grid(column=0, row=2, padx=5, pady=5)

        self.telefone = tk.Entry(self.frameAdicionar, width=20)
        self.telefone.grid(column=1, row=2, padx=5, pady=5)

        # --------------#

        labelEmail = tk.Label(self.frameAdicionar, width=20, text='Email: ')
        labelEmail.grid(column=0, row=3, padx=5, pady=5)

        self.email = tk.Entry(self.frameAdicionar, width=20)
        self.email.grid(column=1, row=3, padx=5, pady=5)

        # --------------#

        labelGrupo = tk.Label(self.frameAdicionar, width=20, text='Grupo: ')
        labelGrupo.grid(column=0, row=5, padx=5, pady=5)

        self.grupo = tk.Entry(self.frameAdicionar, width=20)
        self.grupo.grid(column=1, row=5, padx=5, pady=5)

        # --------------#

        labelEndereco = tk.Label(self.frameAdicionar, width=20, text='Endereço: ')
        labelEndereco.grid(column=0, row=6, padx=5, pady=5)

        self.endereco = tk.Entry(self.frameAdicionar, width=20)
        self.endereco.grid(column=1, row=6, padx=5, pady=5)

        # --------------#

        labelFavorito = tk.Label(self.frameAdicionar, width=20, text='Favorito: ')
        labelFavorito.grid(column=0, row=7, padx=5, pady=5)

        self.favorito = tk.BooleanVar()

        chkBttn = tk.Checkbutton(self.frameAdicionar, text='Favorito', width=20,
                                 variable=self.favorito, anchor=tk.W)

        chkBttn.grid(column=1, row=7, padx=5, pady=5)

        botao = tk.Button(self.frameAdicionar, width=20, text='Salvar', command=self.salvar)
        botao.grid(column=0, row=8, padx=5, pady=5)

    def createRemover(self):
        self.frameRemover = tk.Frame(self.container)

        labelTitulo = tk.Label(self.frameRemover, width=20, text='REMOVER ')
        labelTitulo.grid(column=1, row=0, padx=5, pady=5)

        labelNome = tk.Label(self.frameRemover, width=20, text='Nome: ')
        labelNome.grid(column=0, row=1, padx=5, pady=5)

        nome = tk.Entry(self.frameRemover, width=20)
        nome.grid(column=1, row=1, padx=5, pady=5)

    #     name = input('Nome: ')
    #
    #     self.controller.remove_contact(name)
    #
    #     self._continue()
    #
    # def print_contact(self, nome, info) -> None:
    #     """
    #     Imprime informações de um contato
    #
    #     :param nome: string
    #         Nome do conato
    #     :param info: dict
    #         Dados do contato
    #     """
    #
    #     print('\tNome: ', nome)
    #     print('\tTelefone: ', info['telefone'])
    #     print('\tEmail: ', info['email'])
    #     print('\tGrupo: ', info['grupo'])
    #     print('\tEndereço: ', info['endereco'])
    #     print('\tFavoritos: ', info['favoritos'])
    #     print('')

    def exit(self) -> None:
        self.root.quit()
