import scrapy

class WikimediaSpider(scrapy.Spider):
    name = 'wikimedia'
    start_urls = ['https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons']

    def parse(self, response):
        # Используем XPath для извлечения URL изображений
        for image in response.xpath('//*[@id="mw-category-media"]/ul/li/div/span/a/img'):
            image_url = image.xpath('@src').extract_first()
            yield scrapy.Request(response.urljoin(image_url), self.save_image)

    def save_image(self, response):
        # Получаем имя файла изображения
        filename = response.url.split('/')[-1]
        # Сохраняем изображение в папку images
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body)
