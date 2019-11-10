# Алгоритм на основе задачи об укладке ранца

Приступим сразу же к делу:

```python
if __name__ == "__main__":
    message = 'Иванов Иван Иванович'.lower()      #исходное сообщение
    secret_key = [2, 3, 6, 13, 27, 52, 105, 210]  #секртетный ключ, где каждое последующие число больше суммы придыдущих
    number_m = 420
    number_n = 31

    Backpack(message=message, secret_key=secret_key, m=number_m, n=number_n).start()
```
.........

```python
    def start(self):
        alphabet_for_encryption, alphabet_for_decryption = Backpack.alphabet_code_bin()      #получение словарей с алфавитом для шифрование и расшифрования

        public_key = Backpack.get_public_key(self) #получения публичного ключа

        cipher_text = Backpack.encryption(self, alphabet_for_encryption, public_key)  #процесс шифрования
```

Дайте рассмотрим процесс шифрования:

```python
    def encryption(self, alphabet_bin: dict, public_key: list) -> list:
        cipher_text = list()

        for i in range(len(self.message)):
            string_num = str(alphabet_bin[self.message[i]])
            summ = 0

            for ch in range(len(string_num)):
                summ += int(string_num[ch]) * public_key[ch]

            cipher_text.append(summ)

        return cipher_text
```
Осталось ещё немножко

```python
    def start(self):
        ...
        inverse_number_n = Backpack.get_inverse_number_n(self) #получение обратного числа по модулю, тот же метод, что и алгритме 
        weight_summ = [Backpack.summary_weight(self, inverse_number_n, cipher_text[i]) for i in range(len(cipher_text))]

        decrypted_message = Backpack.decryption(self, alphabet_for_encryption, alphabet_for_decryption, secret_key, weight_summ) #расшифровка сообщение
```

Последний шаг:

```python
    def decryption(self, alphabet_letter_bin, alphabet_bin_letter, secret_key, weight_summ) -> str:
        finals_weight = list()
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя " #алфавит + пробел

        for count in range(len(weight_summ)):
            for i in range(len(alphabet)):
                string_num = str(alphabet_letter_bin[alphabet[i]])
                summ = 0

                for ch in range(len(string_num)):
                    summ += int(string_num[ch]) * int(secret_key[ch])  #получение исходной суммы весов

                if summ == weight_summ[count]:
                    finals_weight.append(alphabet_letter_bin.get(alphabet[i]))   #получение исходных данных весов

        original_text = ''.join(alphabet_bin_letter[finals_weight[i]] for i in range(len(self.message)))

        return original_text
```

И, наконец, вывод результата :

```python
    def result_print(self, public_key, weight_summ, cipher_text, decrypted_message):
        print(f'Исходное сообщение -> {self.message}')
        print(f"Открытый ключ -> {public_key}")
        print(f'Сумма весов -> {weight_summ}')
        print(f'Шифр текст -> {cipher_text}')
        print(f'Расшифрованное сообщение -> {decrypted_message}')
        print(['Расшифрованное сообщение совпадает с исходным текстом' if decrypted_message == self.message else
               'Расшифрованное сообщение НЕ совпадает с исходным текстом'])
```