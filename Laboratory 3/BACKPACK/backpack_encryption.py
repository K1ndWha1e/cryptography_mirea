from typing import Dict, Tuple


class Backpack:
    def __init__(self, message=None, secret_key=None, m=None, n=None):
        self.message = message
        self.secret_key = secret_key
        self.m = m
        self.n = n

    @staticmethod
    def alphabet_code_bin() -> Tuple[Dict[str, int], Dict[int, str]]:
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя "

        alphabet_letter_bin = {ch: int(str(bin(code_a))[2:]) for code_a, ch in enumerate(alphabet, 192)}
        alphabet_bin_letter = {int(str(bin(code_a))[2:]): ch for code_a, ch in enumerate(alphabet, 192)}

        return alphabet_letter_bin, alphabet_bin_letter

    def get_inverse_number_n(self) -> int:
        inverse_number_n = 0
        while 1 > 0:
            if (inverse_number_n * self.n) % self.m == 1:
                break
            inverse_number_n += 1

        return inverse_number_n

    def summary_weight(self, inverse_number_n: int, cipher_text) -> int:
        summ_weight = cipher_text * inverse_number_n % self.m

        return summ_weight

    def get_public_key(self) -> list:
        public_key = [self.secret_key[i] * self.n % self.m for i in range(len(self.secret_key))]

        return public_key

    def encryption(self, alphabet_bin: dict, public_key: list) -> list:
        cipher_text = list()

        for i in range(len(self.message)):
            string_num = str(alphabet_bin[self.message[i]])
            summ = 0

            for ch in range(len(string_num)):
                summ += int(string_num[ch]) * public_key[ch]

            cipher_text.append(summ)

        return cipher_text

    def decryption(self, alphabet_letter_bin, alphabet_bin_letter, secret_key, weight_summ) -> str:
        finals_weight = list()
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя "

        for count in range(len(weight_summ)):
            for i in range(len(alphabet)):
                string_num = str(alphabet_letter_bin[alphabet[i]])
                summ = 0

                for ch in range(len(string_num)):
                    summ += int(string_num[ch]) * int(secret_key[ch])

                if summ == weight_summ[count]:
                    finals_weight.append(alphabet_letter_bin.get(alphabet[i]))

        original_text = ''.join(alphabet_bin_letter[finals_weight[i]] for i in range(len(self.message)))

        return original_text

    def result_print(self, public_key, weight_summ, cipher_text, decrypted_message):
        print(f"Открытый ключ -> {public_key}")
        print(f'Сумма весов -> {weight_summ}')
        print(f'Шифр текст -> {cipher_text}')
        print(f'Расшифрованное сообщение -> {decrypted_message}')
        print(['Расшифрованное сообщение совпадает с исходным текстом' if decrypted_message == self.message else
               'Расшифрованное сообщение НЕ совпадает с исходным текстом'])

    def start(self):
        alphabet_for_encryption, alphabet_for_decryption = Backpack.alphabet_code_bin()

        public_key = Backpack.get_public_key(self)

        cipher_text = Backpack.encryption(self, alphabet_for_encryption, public_key)

        inverse_number_n = Backpack.get_inverse_number_n(self)

        weight_summ = [Backpack.summary_weight(self, inverse_number_n, cipher_text[i]) for i in range(len(cipher_text))]

        decrypted_message = Backpack.decryption(self, alphabet_for_encryption, alphabet_for_decryption, secret_key, weight_summ)

        Backpack.result_print(self, public_key, weight_summ, cipher_text, decrypted_message)


if __name__ == "__main__":
    message = 'Иванов Иван Иванович'.lower()
    secret_key = [2, 3, 6, 13, 27, 52, 105, 210]
    number_m = 420
    number_n = 31

    print(f'Исходное сообщение -> {message}')
    Backpack(message=message, secret_key=secret_key, m=number_m, n=number_n).start()