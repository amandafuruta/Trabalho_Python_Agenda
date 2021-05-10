
import os
import pickle


class Persistencia:
    """
    Classe responsável por persistir a agenda usando a biblioteca Pickle

    Attributes
    ----------
    file_name : string
        Arquivo no qual será salva a agenda
    contact_data: dict
        Dicionário que contém as informações do contato

    Methods
    -------
    carregar_agenda()
        carrega a agenda do disco
    gravar_agenda()
        salva a agenda no disco
    """

    def __init__(self) -> None:
        """
        Construtor da classe - carrega a agenda automaticamente

        See Also
        --------
        file_name : string
            Arquivo em que a agenda será salva
        contact_data : dict
            Dicionário contendo as informações dos contatos
        """

        self.file_name = 'contatos.pkl'
        self.contact_data = {}

        self.carregar_agenda()

    def carregar_agenda(self) -> None:
        """
        Carrega a agenda do arquivo em disco

        Abre o arquivo em modo 'rb' - Leitura Binária e
        usa a biblioteca picke para carregar o arquivo em um dicionário

        Caso o arquivo não exista, cria e salva um dicionário vazio
        """
        if not os.path.isfile(self.file_name):
            self.gravar_agenda()

        with open(self.file_name, 'rb') as file:
            self.contact_data = pickle.load(file)

    def gravar_agenda(self) -> None:
        """
        Salva a agenda do dicionário em um arquivo em disco

        Abre o arquivo em modo 'wb' - escrita Binária e
        usa a biblioteca picke para salvar o dicionário em disco
        """

        with open(self.file_name, 'wb') as file:
            pickle.dump(self.contact_data, file)
