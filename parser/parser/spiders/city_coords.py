import scrapy

cities = ['Kentucky', 'California', 'Florida', 'North Carolina',
          'Washington', 'Texas', 'Wisconsin', 'Utah', 'Nebraska',
          'Pennsylvania', 'Illinois', 'Minnesota', 'Michigan', 'Delaware',
          'Indiana', 'New York', 'Arizona', 'Virginia', 'Tennessee',
          'Alabama', 'South Carolina', 'Oregon', 'Colorado', 'Iowa', 'Ohio',
          'Missouri', 'Oklahoma', 'New Mexico', 'Louisiana', 'Connecticut',
          'New Jersey', 'Massachusetts', 'Georgia', 'Nevada', 'Rhode Island',
          'Mississippi', 'Arkansas', 'Montana', 'New Hampshire', 'Maryland',
          'District of Columbia', 'Kansas', 'Vermont', 'Maine',
          'South Dakota', 'Idaho', 'North Dakota', 'Wyoming',
          'West Virginia']
urls = []
for city in cities:
    if city == 'Washington':
        city = 'Washington_(state)'
    if city == 'Georgia':
        city = 'Georgia_(U.S._state)'
    if city == 'New York':
        city = 'New_York_City'

    urls.append(f'https://en.wikipedia.org/wiki/{city}')

class CityCoordsSpider(scrapy.Spider):
    name = "city_coords"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = urls

    def parse(self, response):
        name = response.css('span.mw-page-title-main::text').get()
        if name == 'New York City':
            name = 'New York'
        if name == 'Georgia (U.S. state)':
            name = 'Georgia'
        if name == 'Washington (state)':
            name = 'Washington'
        if name == 'Washington, D.C.':
            name = 'District of Columbia'
        cords = response.css('span.geo-dec::text').get().split()
        latitude = round(float(cords[0][:-2]))
        longitude = round(float(cords[1][:-2]))
        yield {
            'state': name,
            'latitude': latitude,
            'longitude': longitude
        }
