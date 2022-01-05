import scrapy

def verify_label(response):
            if '#Verificamos' in response:
                return 1
            else:
                return 0

class LupaSpider(scrapy.Spider):
    name = 'LupaSpider'
    start_urls = ['https://piaui.folha.uol.com.br/lupa/'] 
    
    def parse(self, response):
        responses = response.xpath('*//div[@class ="bloco"]')
        next_page = response.xpath("*//div[@class='column size-3-4 column-main']/a/@href").get()
        
        for noticia in  responses:
            #response_body = scrapy.Request(response.xpath("*//h3[@class='bloco-chamada']/a").get())
            yield {
            'title': noticia.xpath("*//h2[@class='bloco-title']/a/@title").get(),
            'vinheta': noticia.xpath("*//span[@class='vinheta']/text()").get(),
            'data': noticia.xpath("*//div[@class='bloco-meta']/text()").get(),
            'lide': noticia.xpath("*//h3[@class='bloco-chamada']/a/text()").get(),
            'label': verify_label(noticia.xpath("*//h2[@class='bloco-title']/a/@title").get()),
            }
        
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)