Пошаговое руководство установки и
настройки паука для вебинара по scrapy.

Все что было нужно, установить корректный Xpath.

Шаг 1: Установка Scrapy
-----------------------
Установите Scrapy через pip, если он еще не установлен:
```bash
pip install scrapy
```

Шаг 2: Создание нового Scrapy проекта
-------------------------------------
Создайте новый Scrapy проект в вашей рабочей директории:
```bash
scrapy startproject wikimedia_downloader
```

Шаг 3: Создание Scrapy паука
-----------------------------
Перейдите в папку проекта и создайте паука:
```bash
cd wikimedia_downloader
scrapy genspider wikimedia commons.wikimedia.org
```

Шаг 4: Написание кода паука
---------------------------
Откройте файл `wikimedia.py` в папке `spiders` и замените его кодом:
```python
import scrapy

class WikimediaSpider(scrapy.Spider):
    name = 'wikimedia'
    start_urls = ['https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons']

    def parse(self, response):
        for image in response.xpath('//*[@id="mw-category-media"]/ul/li/div/span/a/img'):
            image_url = image.xpath('@src').extract_first()
            yield scrapy.Request(response.urljoin(image_url), self.save_image)

    def save_image(self, response):
        filename = response.url.split('/')[-1]
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body)
```

Шаг 5: Настройка настроек проекта
--------------------------------
Откройте файл `settings.py` в папке проекта и измените настройки:
```python
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = 'images'
```

Шаг 6: Запуск паука
-------------------
Запустите паука командой:
```bash
scrapy crawl wikimedia
```

Важное примечание
-----------------

