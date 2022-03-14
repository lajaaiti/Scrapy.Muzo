import scrapy


class Muzo(scrapy.Spider):
    name = 'muzo'
    start_urls = ['https://fr.muzeo.com/recherche/oeuvre/affiche/periode-renaissance/type-cadre-tableau']

   

    def parse(self, response):
        for produits in response.css('div.oeuvre_container.reproduction_class'):
            try:
                yield {
                'titre' :  produits.css('a.title_oeuvre::text').get(),
                'prix' : produits.css('div.oeuvre_price_wrapper::text').get(),
                'url_image' : produits.css('img.oeuvre_img.lazy.reproduction_class').attrib['src'] ,
                }
            except:
                 yield {
                'titre' :  produits.css('a.title_oeuvre::text').get(),
                'prix' : 'prix indisponible',
                'url_image' : produits.css('img.oeuvre_img.lazy.reproduction_class').attrib['src'] ,
                }
                    
            
        
        
            
            