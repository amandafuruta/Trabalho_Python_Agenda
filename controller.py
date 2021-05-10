
from agenda import Agenda
from menu import Menu

class Controller:
    def __init__(self):

        self.agenda = Agenda()
        self.view = Menu(self)

        self.view.show_main_menu()



    def sair(self):
        self.agenda.sair()

    # def search_contact(self, name):
    #     try:
    #         nome, info = self.agenda.buscar_contato(name)
    #     except ValueError as err:
    #         self.view.print_alert(str(err))
    #     else:
    #         self.view.print_message('Contato encontrado')
    #         # self.view.print_contact(nome, info)
    #
    def add_contact(self,
                    name: str,
                    telefone: str,
                    email: str,
                    grupo: str,
                    endereco: str,
                    favorito: bool) -> None:
        try:
            self.agenda.adicionar_contato(name,
                                          telefone,
                                          email,
                                          grupo,
                                          endereco,
                                          favorito)
        except ValueError as err:
            self.view.print_alert(str(err))
        else:
            self.view.print_message('Contato inserido')
    #
    # def remove_contact(self, name) -> None:
    #     try:
    #         self.agenda.remover_contato(name)
    #     except ValueError as err:
    #         self.view.print_alert(str(err))
    #     else:
    #         self.view.print_message('Contato excluído')
