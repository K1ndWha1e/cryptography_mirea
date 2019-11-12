# Шифр перестановки

**Шифр перестановки** - метод симетричного шифрования, в котором для шифровки сообщения используются матрицы и перестановки.

#### Принцип работы шифра перестановки:
Нужно опретелиться с тем, что мы шифровуем - словосочетание, отлично, пускай это будет ФИО одного очень известного человека _Иванова Ивана Ивановича_. Подсчитаем количество символов, учитывая пробелы и получим.... ლ(ಠ_ಠ ლ).... у меня пальцы на руках закончились, подключаем к расчёту пальцы на ногах ლ(¯ロ¯"ლ) .... двадцать символов всего. Это хорошо, ведь, двадцать можно получить путём перемножения четырёх и пяти. 

Теперь же, составим матрицу 4 x 5, куда впишем наше сообщение по столбцам и пронумеруем каждый столбец:


1 | 2 | 3 | 4
--- | --- | --- | ---
И | В| Н| Н
В       |       -|       -|       О
А       |       И|       И|       В
Н       |       В|       В|       И
О       |       А|       А|       Ч


Отлично, у нас есть матрица, теперь, необходимо составить ключ. Ключ составляется следующим образом:

	1234 - выписали пронумированные столнцы, теперь их нужно пермешать
	3142 - вот наш зашифрованный ключ, у вас он мог получиться другим, но это не важно
	
У нас есть ключ шифрования, составим новую матрицу


3 | 1 | 4 | 2
--- | --- | --- | ---
Н | И| Н| В
_       |       В|       О|       _
И       |       А|       В|       И
В       |       Н|       И|       В
А       |       О|       Ч|       А


Осталовь последнее действие, выписать зашифрованное сообщение по **строкам**:

	НИНВ-ВО-ИАВИВНИВАОЧА ＼(≧▽≦)／


#### Путь к расшифровке
Поскольку это симетричный шифр, то ключ у нас остаётся тот же. Зашифрованное сообщение записываем в матрицу по **строкам**.

3 | 1 | 4 | 2
--- | --- | --- | ---
Н | И| Н| В
_       |       В|       О|       _
И       |       А|       В|       И
В       |       Н|       И|       В
А       |       О|       Ч|       А

Теперь просто берём и расставляем столбцы по порядку (по возрастанию).

1 | 2 | 3 | 4
--- | --- | --- | ---
И | В| Н| Н
В       |       -|       -|       О
А       |       И|       И|       В
Н       |       В|       В|       И
О       |       А|       А|       Ч

О, чудо, вы получили исходное сообщение, выпишем же его... и получаем:

	ИВАНОВ_ИВАН_ИВАНОВИЧ
	
### Разбираем работу кода
Вы ведь сюда пришли за этим не так ли? Тогда не будем тянуть быка за рога.


Как и в "бумажном" методе, нужно определиться, что мы шифруем и какой будет ключ. Не будем изворачиваться и возьмём _Иванова Ивана Ивановича_ и наш старый ключ и занесём их в соответствующие переменные:

```python
if __name__ == "__main__":
    original_text = 'Иванов Иван Иванович'.upper()  #.upper() переводит наше сообшение в верхний регистр
    key = '3142'
    lenght_key = len(key)

    print(f'Изначальное сообщение -> {original_text}')

    encrypted_message = Encoding(original_text, lenght_key, key).start()
    decrypted_message = Decoding(encrypted_message, key, lenght_key).start()
```

Перейдём к классу Encoding фукции start:

```python
    def start(self):
        Encoding.formatting_original_text(self) #если из сообщения нельзя состравить матрицу, то эта функцую "добьёт" пробелами до необходимой длины.

```
Обращаем внимание на следующую фукцию:

```python
def formatting_original_text(self):
        remain = self.lenght_original_text % self.lenght_key #делится ли длина сообщения на длину ключа без остатка [20 / 4 = 5 (остаток 0)]
        empty_line = " "

        if remain == 0:
            self.original_text = self.original_text
        else:
            self.original_text += empty_line * (self.lenght_key - remain)
```
Так, теперь, из нашего сообщения можно составить матрицу, вернёмся к классу **start**

```python
   def start(self):
        Encoding.formatting_original_text(self)

        array_original, matrix_column_lenght = Encoding.create_original_matrix(self) # здесь мы создаём саму матрицу
```

Перескакиваем к созданию матрицы:


```python
    def create_original_matrix(self):
        matrix_column_length = len(self.original_text) / self.key_length #подсчёт количкства строчек

        scrub_original_text = str(list(self.original_text.replace(" ", "_")))
        array_in_single_line = np.array(list(map(str, scrub_original_text.split(',')))) #заменяем пробелы на нижнее подчёркивание, чтоб визуализировать пробелы

        array_in_single_line.shape = (self.key_length, int(matrix_column_length)) #преобразование матрицы (4 на 5)
        array_original = array_in_single_line.transpose() #транспонируем, для того чтоб сообщение было записано по столбцам


        return array_original, matrix_column_length # возвращаем элементы, которые понадобятся в будущем

```

И снова же верёмся к истокам:

```python
    def start(self):
        Encoding.tuning_original_text(self)

        array_original, matrix_column_lenght = Encoding.create_original_matrix(self)

        encrypted_array = Encoding.matrix_encode(self, array_original, matrix_column_lenght) #шифруем матрицу
```

Итак, наконец - то шифрование (если, честно, то сам не знаю, что там происходит):

```python
    def matrix_encode(self, array, matrix_column_lenght) -> str:
        key_elements = [int(i) for i in list(self.key)] #создаём список из элементов ключей

        encrypted_array = np.array([])                  #создаём пустой numpy массив, куда будем складывать столцы в новой последовательности
        for i in range(self.key_length):                #i (integer) по по длине ключа
            encrypted_array = np.append(encrypted_array, array[:, int(key_elements[i]) - 1])

        encrypted_array.shape = (self.key_length, int(matrix_column_length))
        encrypted_array = str(encrypted_array.transpose())

        return encrypted_array  #возвращаем зашифрованное сообщение
```

Если вывести полученную матрицу, то будет страшно, а чтобы мы жили спокойно, нужно очистить её от 'мусора':

```python
def clean_matrix(encrypted_array): 
    trash = {" ": "", "[": "", "]": "", "'": "", '"': "", "\n": ""} # {что заменяем: на что заменяем}

    trash = dict((re.escape(k), v) for k, v in trash.items()) #находим жертву
    pattern = re.compile("|".join(trash.keys())) #разжигаем костёр и читаем молитвы
    clean_encrypted_line = pattern.sub(lambda m: trash[re.escape(m.group(0))], encrypted_array) #Боги услышали нас, они... они... ах, что же это?

    return clean_encrypted_line #(ﾉ>ω<)ﾉ :｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆ туман рассеивается 
```

Шифрование удалось, теперь, посмотрим, что получилось:

```python
    def start(self):
        Encoding.tuning_original_text(self)

        array_original, matrix_column_lenght = Encoding.create_original_matrix(self)

        encrypted_array = Encoding.matrix_encode(self, array_original, matrix_column_lenght)

        string_encrypted = clean_matrix(encrypted_array)

        print(f'Оригинальное сообщение в матрице:\n{array_original}')
        print(f'Cообщение после перестановок в матрице:\n{encrypted_array}')
        print(f'Зашифрованное сообщение -> {string_encrypted}')
```

Фух, было сложно, но мы ~~взд..~~ зашифровали.

Теперь, нужно расшифровать (ノ°益°)ノ вернёмся к самому - самому началу...

```python
if __name__ == "__main__":
	 original_text = 'Иванов Иван Иванович'.upper()
    key = '3142'
    lenght_key = len(key)

    print(f'Изначальное сообщение -> {original_text}')

    encrypted_message = Encoding(original_text, lenght_key, key, crypto_text).start()
    decrypted_message = Decoding(encrypted_message, key, lenght_key).start() #обращаемся к классу Encoding
```

Понятно ж, что будет дальше, верно?

```python
def start(self):
        array = Decoding.create_matrix(self) #делаем матрицу, тем же методом, что и в шифровании, не буду на этом останавливаться
        final_array, decrypted_array  = Decoding.matrix_decode(self, array) #расшифровка, ничего сложно, но нужно взгрянуть
```

─=≡Σ((( つ＞＜)つ

```python
    def matrix_decode(self, array):
    	key_elements = [int(i) - 1 for i in list(self.key)]

        decrypted_array = np.array([]) #опять


        for i in range(self.lenght_key):
            decrypted_array = np.append(decrypted_array, array[:, key_elements.index(min(key_elements))]) #ноходится столбец с наименьшим значением
            key_elements.insert(key_elements.index(min(key_elements)), 9999) #добавляем большое число
            key_elements.pop(key_elements.index(min(key_elements))) #удаляем столбец с наименьшим значением

        decrypted_array.shape = (self.lenght_key, int(self.matrix_column_lenght)) 

        final_array = decrypted_array.transpose()

        return final_array, decrypted_array #всему своё время
```

```python
    def start(self):
        array = Decoding.create_matrix(self)
        final_array, decrypted_array  = Decoding.matrix_decode(self, array)
        decrypted_string = Decoding.get_string_from_matrix(self, decrypted_array) #получаем строку
        print(f'Расшифрованное сообщение в матрице:\n{final_array}') #выводим расшифрованную матрицу
        print(f'Расшифрованное сообщение -> {decrypted_string}') #выводим расшифрованное сообщение
```

На этой чудесной ноте, мы завершаем, всем удачи, встретимся в третьей лабораторной.

**P.S.**<br>
(づ ◕‿◕ )づ


### F.A.Q.

- Что такое симетрическое шифрование?
	
	> Шифрование, в котором для шифровки и расшифроки используется один ключ.
	
- Что делать если количество символов не хватает чтобы построить матрицу?
	
	>Всё очень просто, добиваем нехватку пробелами.
	
