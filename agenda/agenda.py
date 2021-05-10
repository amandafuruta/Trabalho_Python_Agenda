
from .persistencia import Persistencia


class Agenda:
    """
    Classe responsável por manipular a agenda e seus contatos

    Attributes
    ----------
    persistencia : Persistencia()
        Classe que salva/carrega agenda do disco
    contact_dict: dict
        dicionário contendo os contatos da agenda

    Methods
    -------
    adicionar_contato()
        Adiciona um contato à agenda
    remover_contato()
        Remove um contato da agenda
    buscar_contato()
        Busca um contato na agenda
    """

    def __init__(self) -> None:
        """
        Construtor da agenda
            carrega a agenda do disco para a memória
            na variável contact_dict que é um dicionário
        """

        self.persistencia = Persistencia()
        self.contact_dict = self.persistencia.contact_data

    def sair(self) -> None:
        """
        Encerra a agenda gravando as alterações
        """

        self.persistencia.gravar_agenda()

    def adicionar_contato(self,
                          nome: str,
                          telefone: str,
                          email: str,
                          grupo: str,
                          endereco: str,
                          favoritos: bool) -> None:
        """
        Adiciona um contato à agenda

        Parameters
        ----------
        nome: string
            nome do contato
        telefone: string
            telefone do contato
        email: string
            email do contato
        grupo: string
            grupo do contato - trabalho, família, amigos, comercial
        endereco: string
            endereço do contato
        favoritos: bool
            se o contato está na categoria favoritos

        Raises
        ------
        ValueError
            Caso o contato já exista
        """

        if nome in self.contact_dict:
            raise ValueError('Contato já existente.')
        else:
            info = {
                'telefone': telefone,
                'email': email,
                'grupo': grupo,
                'endereco': endereco,
                'favoritos': favoritos
            }
            self.contact_dict[nome] = info

    def remover_contato(self, nome: str) -> None:
        """
        Remove um contato da agenda

        Parameters
        ----------
        nome: string
            nome do contato

        Raises
        ------
        ValueError
            Caso o contato não exista
        """

        try:
            del self.contact_dict[nome]
        except KeyError:
            raise ValueError('Contato não encontrado.')

    def buscar_contato(self, nome: str) -> tuple:
        """
        Busca um contato na agenda

        Parameters
        ----------
        nome: string
            nome do contato

        Returns
        -------
        tuple (name, info: dict)
            Caso o contato exista retorna o nome e telefone

        Raises
        ------
        ValueError
            Caso o contato não exista
        """

        if nome not in self.contact_dict:
            raise ValueError('Contato não encontrado.')
        else:
            return nome, self.contact_dict[nome]
