# Movie recommendation system
    Расскажу про этот проект кратко и постараюсь ясно:
    Это система рекомедации фильмов работает следующим образом:
    Ищем пять последних оценок пользователей, если их меньше 10, то используются все оценки.
    Из последних оценок извлекаем теги фильмов.
    Ищем все фильмы, которые содержат хотя бы один из тегов из последних оценок.
    Если у пользователя есть любимые фильмы, то из предыдущих результатов выбирается только те, которые содержат лишь один из тегов любимых фильмов.
    Из отфильтрованных фильмов представлены только те, которые были выпущены за последние 6 месяцев.
    Если осталось меньше 10, то возвращаем фильмы их все.
    Сортируем фильмы по количеству совпадающих тегов с чувствами чувств пользователей.
    Возвращает 10 лучших фильмов совпадающих тегов.

- Сначала склонируй репозиторий, используя комманду:
  -     git clone https://github.com/SyntaxStorm/Movie-recommendation-system

- Создай виртуальное окружение
  -     python3 -m venv <название окружение>

- Активируй вертуальное окружение
  -     source <название окружение>/bin/activate

  - Установи зависимости из файла req.txt
  -     pip3 install -r req.txt

- Переименуй env_example файл в файл .env и вставь свои значения


- Дальше надо сделать миграцию использую комманды:
  -     python3 manage.py migrate

- Запусти проект командой

-       python3 manage.py runserver

