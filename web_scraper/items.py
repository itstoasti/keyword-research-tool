```python
import scrapy

class WebScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
```