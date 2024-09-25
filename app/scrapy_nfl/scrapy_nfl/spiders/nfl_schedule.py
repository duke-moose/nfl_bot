import scrapy

"""
Scrapes NFL Schedule Website

run in terminal: scrapy crawl nfl_schedule -o [year]_nfl_schedule.json



xpath example: response.xpath('/html/body/table/tbody/tr/td/text()') 
css response.css("html.body.table.tbody.tr.td::text")
.get: returns the entire selector
.get(): returns only data from the selector
.getall(): get all children tags that fit the query within.
"""

class nfl_schedule(scrapy.Spider):
    name = "nfl_schedule"
    start_urls = [
        'http://www.espn.com/nfl/schedulegrid',
    ]

    def parse(self, response):
        for row in ["tr.oddrow", "tr.evenrow"]:
            for quote in response.css(row):
                yield {
                    'team': quote.css("a::text").get(),
                    'opponents': quote.css("td::text").getall(),
                    }