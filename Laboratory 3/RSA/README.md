# RSA (Rivest, Shamir, Adleman)

**RSA** - асиметрический алгоритм шифрования, основывающийся на вычислительной сложности задачи факторизации больших целых чисел.

Сразу же обратимся к программе:

```python
if __name__ == "__main__":
    message = "Иванов Иван Иванович" #исходное сообщение
    p = 7                            #простое числа 'p'
    q = 17							 #простое число 'q'
    e = 29                           #взаимно простое число с числом эйлера, при 0 < e < n

    RSA(message=message, p=p, q=q, e=e).start()
```

Отправляемся к классу RSA функции start

```python
    def start(self):
        n = self.p * self.q                     #произведение 'p' и 'q'

        euler_num = (self.p - 1) * (self.q - 1) #число эйлера произведение 'p - 1' и 'q - 1'
        public_key = [self.e, n]                #открытый ключ

        alphabet_for_encrypt, alphabet_for_decrypt = RSA.letter_numerating()  #получаем алфавит для шифрования и дешифрования

        encrypt_message = RSA.encrypt(self, public_key, alphabet_for_encrypt) #сам процесс шифрования
```

Смотрим, как происходит шифрование

```python
    def encrypt(self, public_key, alphabet_for_encrypt) -> Tuple[List[str], Dict[int, chr]]:
        crypto_string = [alphabet_for_encrypt[ch] ** public_key[0] % public_key[1] for ch in self.message]     #получение зашифрованного сообщения

        return crypto_string
```

Секретный ключ вычисляется по следующей формуле:
**(d * e) mod (число эйлера) =  1**

```python
    def start(self):
        ...
        secret_key = RSA.get_secret_key(self, euler_num) #получение секрет ключа для расшифровки
        decrypt_message = RSA.decrypt(secret_key, alphabet_for_decrypt, encrypt_message, public_key[1]) #расшифровка сообщения        
```

Расшифрока происходит в одну формулу:

```python
    @staticmethod
    def decrypt(secret_key, alphabet, encrypte_message, n) -> str:
        position_decrypt = [i ** secret_key % n for i in encrypte_message] #расшифровка позиции символов сообщения

        message_decrypt = ''.join(alphabet[i] for i in position_decrypt) #составление самого сообщения

        return message_decrypt
```


Теперь, нужно посмотреть, что у нас получилось, для этого обратимся к **result_print**

```python
    def result_print(self, encrypt_message, decrypt_message):
        print(f'Изначальное сообщение -> {self.message}')
        print(f'Зашифрованное сообщение -> {encrypt_message}')
        print(f'Расшифрованное сообщение -> {decrypt_message}')
        print(['Расшифрованное сообщение совпадает с исходным текстом' if decrypt_message == self.message else
               'Расшифрованное сообщение НЕ совпадает с исходным текстом'])

```


