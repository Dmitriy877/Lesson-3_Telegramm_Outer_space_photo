# Публикация фотографий компаний NASA, EPIC, SPACEX в телеграмм канале с помощью бота.

TODO:

telegramm_post_bot_random.py Данный скрипт принимает в качестве аргумента название картинки в директории images и публикует ее в телеграмм канале, если название файла не указано то публикует случайную картинку из директории images.

telegramm_post_bot_time.py Данный скрипт принимает в качестве аргумента время через которе публиковать картинку из директории images (время указывать в часах), если время не указано публикует картинку раз в 4 часа, после публикаии всех картинок директории перемешивает картинки и начинает публикацию заново.

fetch_epic_images.py Данный скрипт принимает в качестве аргумента количество фотографий которые необходимо загрузить с сайта компании epic, если аргумент не указан скачивает 6 и кладет в директорию images, если директория не создана создает ее.

fetch_nasa_images.py Данный скрипт принимает в качестве аргумента количество фотографий которые необходимо загрузить с сайта компании nasa, если аргумент не указан скачивает 6 и кладет в директорию images, если директория не создана создает ее.

fetch_spacex_images.py Данный скрипт принимает в качестве аргумента id запуска и скачивает фотографии с него. Если аргумент не указан скачивает фотографии с последнего запуска. Если при запуске фотографии не делались выводит сообщение об этом.

save_picture.py Вспомогательный скрипт необходимый для работы других скриптов. Получает ссылку и скачивает фотографию.

file_resolution_script Вспомогательный скрипт необходимый для работы других скриптов. Определяет расширение файла по ссылке.

telegramm_post_image.py Вспомогательный скрипт необходимый для работы  скриптов. Отправляет в канал картинку с указанным именем.

Для работы скриптов необходимо их запускать с ссылкой в качестве аргумента, например: 

```python telegramm_post_bot_random.py image1.jpg ```

Скрипты содержат следующие переменные:

`token` - переменная которая хранит токен NASA_EPIC_API_KEY, ELEGRAMM_API_KEY импортированный из .env файла (Необходимы для работы скриптов);
`chat_id` - переменная которая хранит chat id канала импортированный из .env файла, значение TELEGRAMM_CHAT_ID (Необходимы для работы скриптов)
`directory_epic, directory_nasa, directory_spacex` хранят название папку в которую сохраняют фотографии (по умолчанию image).
`filename_epic, filename_nasa, filename_spacex` хранят название файла которе будет присваивать скрипт при скачивании фотографий.

### Как установить

Python3 должен быть установлен.
Затем используйте "pip" (или "pip3", есть конфлик с python2) для устанвки зависимостей:

```pip install -r requerements.txt```

Перед запуском необходимо создать .env файл где разместить токен NASA_EPIC_API_KEY, ELEGRAMM_API_KEY в созданных переменных `NASA_EPIC_API_KEY, TELEGRAMM_API_KEY`.

Рекомендуется использовать [vitrualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Как запустить

Для запуска скриптов убедитесь что вложили в папку с скриптом файл .env с переменными `NASA_EPIC_API_KEY, TELEGRAMM_API_KEY, TELEGRAMM_CHAT_ID` и передали в данную переменную соответсвующие токены, а также указали chat id бота в скриптах telegramm_post_bot_random.py, telegramm_post_bot_time.py.

Например:

для скрипта telegramm_post_bot_random.py

* Откройте консоль
* Перейдите в консоли в папку с скриптом
* введите в консоль команду запуска скрипта с названием картинки из директории image в качестве аргумента, например 
 ```python telegramm_post_bot_random.py image1.jpg ```
* Произойдет публикация в канал указанной картинки от имени бота

для скрипта telegramm_post_bot_time.py

* Откройте консоль
* Перейдите в консоли в папку с скриптом
* введите в консоль команду запуска скрипта с количеством часов в качестве аргумента, например
 ```python telegramm_post_bot_time.py 10 ```
* Произойдет публикация в канал указанной картинки от имени бота
* Следующая картинка будет опубликована через 10 часов (если аргумент не указан, то через 4)
* Когда бот опубликует все картинки он их перемешает и начнет публиковать заново

для скрипта fetch_epic_images.py

* Откройте консоль
* Перейдите в консоли в папку с скриптом
* введите в консоль команду запуска скрипта с количеством картинок в качестве аргумента, например
 ```python fetch_epic_images.py 2 ```
* Произойдет создание директории images и скачивание туда 2 картинок с именем epic_image (если аргумент не указан, то будет скачано 6)

для скрипта fetch_nasa_images.py

* Откройте консоль
* Перейдите в консоли в папку с скриптом
* введите в консоль команду запуска скрипта с количеством картинок в качестве аргумента, например 
 ```python etch_nasa_images.py 2```
* Произойдет создание директории images и скачивание туда 2 картинок с именем nasa_image (если аргумент не указан, то будет скачано 6)

для скрипта fetch_spacex_images.py

* Откройте консоль
* Перейдите в консоли в папку с скриптом
* введите в консоль команду запуска скрипта с id запуска в качестве аргумента, например 
 ```python fetch_spacex_images.py 5a9fc479ab70786ba5a1eaaa ```
* Произойдет создание директории images и скачивание туда картинок с именем spacex_image с указанного запуска (если аргумент не указан, то будут скачаны катинки с последнего запуска, но если фотографии во время запуска не делались будет выведено сообщение об этом)


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)