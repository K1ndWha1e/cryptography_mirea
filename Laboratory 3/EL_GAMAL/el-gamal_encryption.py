from typing import Tuple, Dict
import random


class El_Gamal:
    def __init__(self, message=None, p_number=None, g_number=None, x_number=None):
        self.p_number = p_number
        self.g_number = g_number
        self.x_number = x_number
        self.message = message
        self.public_key = self.g_number ** self.x_number % self.p_number
        #1 < K < P - 1
        self.k_number = random.randint(2, self.p_number - 2)

    @staticmethod
    def letter_numerating() -> Tuple[Dict[chr, int], Dict[int, chr]]:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.'

        alphabet_letters_numbers = {ch: i for i, ch in enumerate(alphabet, 1)}
        alphabet_numbers_letters = {i: ch for i, ch in enumerate(alphabet, 1)}

        return alphabet_letters_numbers, alphabet_numbers_letters

    def get_position_for_letter_in_message(self, alphabet_letters_numbers: dict) -> list:
        num_for_letter_in_message = [alphabet_letters_numbers[ch] for ch in self.message]

        return num_for_letter_in_message

    def first_part_encryption(self) -> int:
        #a = gˆk mod(p)
        a_part_encryption = (self.g_number ** self.k_number) % p_number

        return a_part_encryption

    def second_part_encryption(self, public_key: int, letter_position_in_message: list):
        #b = (yˆk * T) mod p
        b_part_encruption = list()

        for i in range(len(self.message)):
            b_part_encruption.append(((int(public_key) ** self.k_number) * int(letter_position_in_message[i])) % p_number)

        return b_part_encruption

    def decryption(self, a_part_encryption: int, b_part_encryption: list) -> list:
        #T = (b(aˆx)ˆ-1)mod(p)
        decrypt = list()

        for i in range(len(self.message)):
            decrypt.append((b_part_encryption[i] * (a_part_encryption ** (self.p_number - 1 - self.x_number))) % p_number)

        return decrypt

    @staticmethod
    def get_decrypted_message(decrypt: list, alphabet_numbers_letters: dict) -> str:
        decrypted_message = ''.join(alphabet_numbers_letters[i] for i in decrypt)

        return decrypted_message

    def result_print(self, a_part_encryption, b_part_encruption, decrypted_message):
        print(f'Исходное сообщение -> {self.message}')
        print(f'Первая часть шифрования = {a_part_encryption}')
        print(f'Вторая часть шифрования = {b_part_encruption}')
        print(f'Расшифрованное сообщение - > {decrypted_message}')
        print(['Расшифрованное сообщение совпадает с исходным текстом' if decrypted_message == self.message else
               'Расшифрованное сообщение НЕ совпадает с исходным текстом'])

    def start(self):
        alphabet_for_encryption, alphabet_for_decryption = El_Gamal.letter_numerating()
        a_part_encryption = El_Gamal.first_part_encryption(self)

        letter_position_in_message = El_Gamal.get_position_for_letter_in_message(self, alphabet_for_encryption)

        b_part_encruption = El_Gamal.second_part_encryption(self, self.public_key, letter_position_in_message)

        decrypt = El_Gamal.decryption(self, a_part_encryption, b_part_encruption)

        decrypted_message = El_Gamal.get_decrypted_message(decrypt, alphabet_for_decryption)

        El_Gamal.result_print(self, a_part_encryption, b_part_encruption, decrypted_message)


if __name__ == "__main__":
    message = "Иванов Иван Иванович".lower()
    p_number = 37
    g_number = 2
    x_number = 5

    El_Gamal(message=message, p_number=p_number, g_number=g_number, x_number=x_number).start()