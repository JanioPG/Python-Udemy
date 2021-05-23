class Entrada:

    def __init__(self, question, *args):
        self.question: str = question
        self.args = args

    def num_inteiro(self):
        """-> Aceita um número inteiro.

        Returns:
            int: numero inteiro inserido pelo usuário.
        """
        while True:
            try:
                num = int(input(f"{self.question}"))
            except:
                print('Desculpe. Digite um número inteiro válido.')
                continue
            else:
                if len(self.args) == 0:
                    pass
                elif num not in self.args:
                    print(f"Opção inválida. Tente novamente com {self.args}")
                    continue
                return num


    def caractere(self):
        """Aceita um conjunto de caracteres.

        Raises:
            ValueError: Usuario nao pode inserir somente espacos ou resposta vazia.

        Returns:
            str: caracteres inserido pelo usuario
        """
        while True:
            try:
                resp = str(input(f"{self.question}")).strip()
                if len(resp) == 0:
                    raise ValueError
            except:
                print('Desculpe. Tente novamente.')
                continue
            else:
                if len(self.args) == 0:
                    pass
                elif resp not in [str(x) for x in self.args]:
                    print(f"Opção inválida. Tente novamente com {self.args}")
                    continue
                return resp

    def __str__(self):
        return f'Pergunta: {self.question}\nResposta exigida:  {self.args}'