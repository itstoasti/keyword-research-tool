```python
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .items import WebScraperItem

class RedditSpider(scrapy.Spider):
    name = "reddit_spider"
    start_urls = ['https://www.reddit.com']

    def parse(self, response):
        for post in response.css('div.thing'):
            item = WebScraperItem()
            item['title'] = post.css('p.title a::text').get()
            item['url'] = post.css('p.title a::attr(href)').get()
            item['upvotes'] = post.css('div.score.unvoted::attr(title)').get()
            yield item

        next_page = response.css('span.next-button a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(RedditSpider)
    process.start() # the script will block here until the crawling is finished
```