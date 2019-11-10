from typing import Tuple, Dict, List


class RSA:
    def __init__(self, message, p = None, q = None, e = None):
        self.message = message
        self.p = p
        self.q = q
        self.e = e

    @staticmethod
    def letter_numerating() -> Tuple[Dict[chr, int], Dict[int, chr]]:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.-'

        alphabet_letters_numbers = {ch: i for i, ch in enumerate(alphabet, 1)}
        alphabet_numbers_letters = {i: ch for i, ch in enumerate(alphabet, 1)}

        return alphabet_letters_numbers, alphabet_numbers_letters

    def get_secret_key(self, euler_num: int) -> int:
        d = 0
        while (1 > 0):
            if (d * self.e) % euler_num == 1:
                break
            d += 1

        return d

    def encrypt(self, public_key) -> Tuple[List[str], Dict[int, chr]]:
        alphabet_for_encryption, alphabet_for_decryption = RSA.letter_numerating()

        crypto_string = list()

        for ch in self.message:
            crypto_string.append(alphabet_for_encryption[ch] ** public_key[0] % public_key[1])

        return crypto_string, alphabet_for_decryption

    @staticmethod
    def decrypt(secret_key, alphabet, encrypte_message, n) -> str:
        position_decrypt = [i ** secret_key % n for i in encrypte_message]

        message_decrypt = ''.join(alphabet[i] for i in position_decrypt)

        return message_decrypt

    def result_print(self, encrypt_message, decrypt_message):
        print(f'Изначальное сообщение -> {self.message}')
        print(f'Зашифрованное сообщение -> {encrypt_message}')
        print(f'Расшифрованное сообщение -> {decrypt_message}')
        print(['Расшифрованное сообщение совпадает с исходным текстом' if decrypt_message == self.message else
               'Расшифрованное сообщение НЕ совпадает с исходным текстом'])

    def start(self):
        n = self.p * self.q

        euler_num = (self.p - 1) * (self.q - 1)
        public_key = [self.e, n]

        encrypt_message, alphabet_for_decrypt = RSA.encrypt(self, public_key)
        secret_key = RSA.get_secret_key(self, euler_num)
        decrypt_message = RSA.decrypt(secret_key, alphabet_for_decrypt, encrypt_message, public_key[1])

        RSA.result_print(self, encrypt_message, decrypt_message)


if __name__ == "__main__":
    message = "Иванов Иван Иванович"
    p = 7
    q = 17
    e = 29

    RSA(message=message, p=p, q=q, e=e).start()