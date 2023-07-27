```python
from flask import Flask, render_template, request, jsonify
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .scrapy_spider import RedditSpider

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_scrape', methods=['POST'])
def start_scrape():
    url = request.json['url']
    process = CrawlerProcess(get_project_settings())
    process.crawl(RedditSpider, start_urls=[url])
    process.start()
    return jsonify(message="scrape_complete")

if __name__ == "__main__":
    app.run(debug=True)
```