# Программы для выполнения лаборатоных работ по криптографии

![Last Commit](https://img.shields.io/github/last-commit/K1ndWha1e/cryptography_mirea)
![Commit status](https://img.shields.io/github/commit-status/K1ndWha1e/cryptography_mirea/master/4ef2d4cfbf6430d4b4aaaf7661fc9ecf73d2bb3a)
![Watchers](https://img.shields.io/github/watchers/K1ndWha1e/cryptography_mirea?style=social)

В этом репозитории представлены программы для решения лабораторных работ по криптографии в РТУ МИРЭА

## Установка

```
#клонирование репозитория
$ git clone https://github.com/K1ndWha1e/cryptography_mirea.git

#открываем папку репозитория
$ cd cryptography_mirea

#скачать python3 и python3-pip, если ещё не установлены

#теперь, скачиваем необходимые пакеты
$ python3 -m pip install -r requirements.txt
```

## Использование
Лабораторная 1. Шифр перестановки

```python
if __name__ == "__main__":
    original_text = 'Иванов Иван Иванович'.upper().   #здесь можно вписать ваше сообщение
    key = '3142' #1 < любой ключ < много-много
    key_length = len(key)

    encrypted_message = Encoding(original_text, key_length, key).start()
    Decoding(encrypted_message, key, key_length).start()
```

Лабораторная 3. RSA алгоритм

```python
if __name__ == '__main__':
    message = "Иванов Иван Иванович"   #меняем сообщение на своё
    p = 7                              #любое простое число
    q = 17                             #любое простое число
    e = 29                             #любое простое число, которое обратно по модулю числу эйлера

    RSA(message=message, p=p, q=q, e=e).start()
```

Лабораторная 3. Алгоритм на основе задачи об укладке ранца.

```python
if __name__ == "__main__":
    message = 'Иванов Иван Иванович'.lower()         #меняем сообщение на своё
    secret_key = [2, 3, 6, 13, 27, 52, 105, 210]     #секретный ключ, где каждый последующий элемент больше суммы придыдущих
    number_m = 420                                   #число, которое больше всех элементов ключа
    number_n = 31                                    #число, которое пропорционально по модулю числу 'm'

    Backpack(message=message, secret_key=secret_key, m=number_m, n=number_n).start()
```

Лабораторная 3. Алгоритм Эль-Гамаля

```python
if __name__ == "__main__":
    message = "Иванов Иван Иванович".lower()         #меняем сообщение на своё
    p_number = 37                                    #любое простое число
    g_number = 2                                     #число, которое первообразным корнем по модулю p и меньше p (что бы это не значило)
    x_number = 5                                     #

    El_Gamal(message=message, p_number=p_number, g_number=g_number, x_number=x_number).start()
```
