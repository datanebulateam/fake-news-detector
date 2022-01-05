import scrapy

def verify_label(response):
            if '#FAKE' in response:
                return 1
            else:
                return 0

class G1Spider(scrapy.Spider):
    name = 'G1Spider'
    start_urls = ['https://g1.globo.com'] 
    
    def parse(self, response):
        responses = response.xpath('*//div[@class ="feed-post-body"]')
        next_page = response.xpath("*//div[@class='load-more gui-color-primary-bg']/a/@href").get()
        
        for noticia in  responses:
            #response_body = scrapy.Request(response.xpath("*//h3[@class='bloco-chamada']/a").get())

            yield {
            'title': noticia.xpath("*//a[@class='feed-post-link gui-color-primary gui-color-hover']/text()").get(),
            'vinheta': noticia.xpath("*//span[@class='feed-post-metadata-section']/text()").get(),
            'data': noticia.xpath("*//span[@class='feed-post-datetime']/text()").get(),
            'lide': noticia.xpath("*//div[@class='feed-post-body-resumo']/text()").get(),
            'label': verify_label(noticia.xpath("*//a[@class='feed-post-link gui-color-primary gui-color-hover']/text()").get()),
            }
        
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)