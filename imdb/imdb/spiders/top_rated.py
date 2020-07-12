import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TopRatedSpider(CrawlSpider):
    name = 'top_rated'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
            'duration': response.xpath("normalize-space(//div[@class='subtext']/time/text())").get(),
            'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'rating': response.xpath("//div[@class='ratingValue']/strong/span/text()").get(),
            'url': response.url
        }
