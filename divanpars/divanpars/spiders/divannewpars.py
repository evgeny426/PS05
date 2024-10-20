import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        light_sources = response.css('div._Ud0k')
        for light_source in light_sources:
            yield {
                'name': light_source.css('div.lsooF span::text').get(),
                'price': light_source.css('div.pY3d2 span::text').get(),
                'url': light_source.css('a').attrib['href']
            }
