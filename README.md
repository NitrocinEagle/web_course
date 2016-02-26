Версия Python: 2.7

1. Клонируем репозиторий `git clone https://github.com/pc-mist/web_course.git`
2. Переходим в директорию web_course `cd web_course`
2. Создаём в нем виртуальной окружение с именем venv `virtualenv-2.7 venv`
3. Активируем виртуальное окружение `. venv/bin/activate`
4. Устанавливаем зависимости `pip install -r req.txt`
5. Запускаем миграцию базы данных `python manage.py migrate`
