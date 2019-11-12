# Алгоритм Эль-Гамаля

Перейдём сразу же к коду

```python
if __name__ == "__main__":
    message = "Иванов Иван Иванович".lower()    #сообщение
    p_number = 37                               #любое протое число
    g_number = 2                                #первообразный корень по модулю p, чтобы это не значило
    x_number = 5                                #любое число, которое меньше p

    El_Gamal(message=message, p_number=p_number, g_number=g_number, x_number=x_number).start()
```
Сначала, обратим внимание на инициализацию в классе

```python
class El_Gamal:
        ....
        self.k_number = random.randint(2, self.p_number - 2) #случайное число k, при условии, что 1 < K < P - 1
```

Теперь, перейдём к функции start

```python
   def start(self):
        alphabet_for_encryption, alphabet_for_decryption = El_Gamal.letter_numerating() #получение словарей для шифровки и дешифровки
        a_part_encryption = El_Gamal.first_part_encryption(self)  #пользуемся обычной формулой, a = gˆk mod(p)

        letter_position_in_message = El_Gamal.get_position_for_letter_in_message(self, alphabet_for_encryption) #узнаём позицию букв сообщения в алфавите

        b_part_encruption = El_Gamal.second_part_encryption(self, self.public_key, letter_position_in_message)  #тут тоже ничего сложно, пользуемся формулой b = (yˆk * T) mod p

        decrypt = El_Gamal.decryption(self, a_part_encryption, b_part_encruption)   #здесь тоже всё в одну формулу T = (b(aˆx)ˆ-1)mod(p)

        decrypted_message = El_Gamal.get_decrypted_message(decrypt, alphabet_for_decryption) #преобразование расшифрованного сообщение в строку

        El_Gamal.result_print(self, a_part_encryption, b_part_encruption, decrypted_message)       #вывод результата
```

На этом всё, как вы, наверное, заметили, эта лабораторная самая простая, т.к. закодить формулы ничего не стоит. Всем спасибо!<br>
**P.S.**<br>
(づ￣ ³￣)づ