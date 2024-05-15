# Веб-приложение djangoLesta
## Описание проекта:
Данный проект был выполнен в качестве тестового задания к вакансии стажера веб-разработчика на Python в компанию Lesta Games.<br/> 
В текущем сервисе можно загрузить текстовый файл и после его обработки получить таблицу, содержащую следующие колонки: 
* Слово
* Tf, сколько раз это слово встречается в тексте
* Idf, обратная частота документа <br/>
Вывод ограничен пятьюдесятью словами и упорядочен по уменьшению idf.<br/>
Также подключена пагинация для итоговой таблицы.<br/>

## СТЕК технологий:
* Python == 3.12.0
* Django == 5.0.4

## Как установить проект локально:
Клонировать репозиторий и перейти в него в командной строке:

```sh
git clone git@github.com:FeodorPyth/djangoLesta.git
```

```sh
cd djangoLesta
```

Создать и активировать виртуальное окружение:

Windows
```python
python -m venv venv
source venv/Scripts/activate
```

Linux/macOS
```python
python3 -m venv venv
source venv/bin/activate
```

Обновить пакетный менеджер PIP:

Windows
```python
python -m pip install --upgrade pip
```

Linux/macOS
```python
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```python
pip install -r requirements.txt
```

Выполнить миграции:

Windows
```python
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```python
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустить проект:

Windows
```python
python manage.py runserver
```

Linux/macOS
```python
python3 manage.py runserver
```

## Автор:
[FeodorPyth](https://github.com/FeodorPyth)
