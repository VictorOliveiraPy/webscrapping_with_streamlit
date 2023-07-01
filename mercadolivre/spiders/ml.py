import scrapy

from mercadolivre.items import MercadolivreItem


class MlSpider(scrapy.Spider):
    name = "ml"
    start_urls = [f"https://www.mercadolivre.com.br/ofertas?page={i}" for i in range(1, 2)]

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="promotion-item avg"]'):
            yield MercadolivreItem(
                price=i.xpath('.//span[@class="andes-money-amount__fraction"]//text()').getall(),
                title=i.xpath('.//p[@class="promotion-item__title"]/text()').get(),
            )
