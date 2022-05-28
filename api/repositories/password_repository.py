import re
import string
from random import choice


class PasswodRepository:
    def __init__(self, size):
        self.size = size

    def password_is_valid(self, random_string):
        """
        Faz a validacao de uma string randomica para verificar se corresponde a todos os criterios de uma senha segura.

        :param random_string:
        :return: Boolean
        """
        has_minimun = len(random_string) >= 8
        has_maximun = len(random_string) <= 50
        has_lower = re.findall('[a-z]', random_string)
        has_upper = re.findall('[A-Z]', random_string)
        has_number = re.findall('[0-9]', random_string)
        has_special_characteres = re.findall('[!-/:-?]', random_string)

        if has_lower and has_upper and has_number and has_special_characteres and has_minimun and has_maximun:
            return True
        else:
            return False

    def generate_random_string(self):
        """
        Gera uma string com caracteres aleatorios. Utilizamos uma string especifica para caracteres especiais ao inves
        do 'string.punctuation', pois sabemos que alguns deses podem retornar problemas dependendo da validacao feita.
        Para uma acao mais assertiva seria necessario fazer testes no sistema para o qual as senhas sao geradas.

        :return: String com caracteres aleatorios.
        """
        random_string = ''
        characters = string.digits + string.ascii_letters + '!#$%&*+->@_'

        for i in range(self.size):
            random_string += choice(characters)

        return random_string

    def generate_password(self):
        """
        Repete o teste ate obter uma string que corresponda a uma senha segura.

        :return: String de uma senha segura validada.
        """
        while True:
            random_string = self.generate_random_string()
            if self.password_is_valid(random_string):
                return random_string
