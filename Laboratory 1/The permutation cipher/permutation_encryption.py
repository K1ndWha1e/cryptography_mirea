import re
import numpy as np


def get_clean_string(encrypted_array):
    trash = {" ": "", "[": "", "]": "", "'": "", '"': "", "\n": ""}

    trash = dict((re.escape(k), v) for k, v in trash.items())
    pattern = re.compile("|".join(trash.keys()))
    clean_encrypted_line = pattern.sub(lambda m: trash[re.escape(m.group(0))], encrypted_array)

    return clean_encrypted_line


class Encoding:
    def __init__(self, original_text=None, key_length=None, key=None):
        self.original_text = original_text
        self.length_original_text = len(self.original_text)
        self.key_length = key_length
        self.key = key

    def formatting_original_text(self):
        remain = self.length_original_text % self.key_length
        empty_line = " "

        if remain == 0:
            self.original_text = self.original_text
        else:
            self.original_text += empty_line * (self.key_length - remain)

    def create_original_matrix(self):
        matrix_column_length = len(self.original_text) / self.key_length

        scrub_original_text = str(list(self.original_text.replace(" ", "_")))
        array_in_single_line = np.array(list(map(str, scrub_original_text.split(','))))

        array_in_single_line.shape = (self.key_length, int(matrix_column_length))
        array_original = array_in_single_line.transpose()

        return array_original, matrix_column_length

    def matrix_encode(self, array, matrix_column_length) -> str:
        key_elements = [int(i) for i in list(self.key)]
        encrypted_array = np.array([])

        for i in range(self.key_length):
            encrypted_array = np.append(encrypted_array, array[:, int(key_elements[i]) - 1])

        encrypted_array.shape = (self.key_length, int(matrix_column_length))
        encrypted_array = str(encrypted_array.transpose())

        return encrypted_array

    def result_print(self, array_original, encrypted_array, string_encrypted):
        print(f'Изначальное сообщение -> {self.original_text}')
        print(f'Оригинальное сообщение в матрице:\n {array_original}')
        print(f'Cообщение после перестановок в матрице:\n {encrypted_array}')
        print(f'Зашифрованное сообщение -> {string_encrypted}')

    def start(self):
        Encoding.formatting_original_text(self)

        array_original, matrix_column_length = Encoding.create_original_matrix(self)

        encrypted_array = Encoding.matrix_encode(self, array_original, matrix_column_length)

        string_encrypted = get_clean_string(encrypted_array)

        Encoding.result_print(self, array_original, encrypted_array, string_encrypted)

        return string_encrypted


class Decoding:
    def __init__(self, encrypted_message, key, key_length):
        self.encrypted_message = encrypted_message
        self.key = key
        self.key_length = key_length
        self.matrix_column_length = len(self.encrypted_message) / self.key_length

    def create_matrix(self):
        original_text = str(list(self.encrypted_message.replace(" ", "_")))

        matrix = np.array(list(map(str, original_text.split(','))))
        matrix.shape = (int(self.matrix_column_length), self.key_length)

        return matrix

    def matrix_decode(self, array):
        key_elements = [int(i) - 1 for i in list(self.key)]

        decrypted_array = np.array([])

        for i in range(self.key_length):
            decrypted_array = np.append(decrypted_array, array[:, key_elements.index(min(key_elements))])
            key_elements.insert(key_elements.index(min(key_elements)), 9999)
            key_elements.pop(key_elements.index(min(key_elements)))

        decrypted_array.shape = (self.key_length, int(self.matrix_column_length))

        final_array = decrypted_array.transpose()

        return final_array, decrypted_array

    def get_string_from_matrix(self, decrypted_array) -> str:
        decrypted_array.shape = (1, len(self.encrypted_message))
        encrypted_string = get_clean_string(str(decrypted_array)).replace('_', ' ')

        return encrypted_string

    @staticmethod
    def result_print(decrypt_string, final_array):
        print(f'Расшифрованное сообщение в матрице:\n{final_array}')
        print(f'Расшифрованное сообщение -> {decrypt_string}')

    def start(self):
        array = Decoding.create_matrix(self)
        final_array, decrypted_array  = Decoding.matrix_decode(self, array)
        decrypt_string = Decoding.get_string_from_matrix(self, decrypted_array)
        Decoding.result_print(decrypt_string, final_array)


if __name__ == "__main__":
    original_text = 'Иванов Иван Иванович'.upper()
    key = '3142'
    key_length = len(key)

    encrypted_message = Encoding(original_text, key_length, key).start()
    Decoding(encrypted_message, key, key_length).start()
