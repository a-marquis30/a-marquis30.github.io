# This code is based on the tutorial "Web Scraping Weather Data with Python"
# by John Watson Rooney
from flask import Flask, request
from requests_html import HTMLSession

app = Flask(__name__)
@app.route('/weather_scraper', methods=['GET','POST'])
def weather_scraper ():
    location = request.args.get('location')
    s = HTMLSession()

    query = location
    url = f'https://www.google.com/search?q=weather+{query}'

    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})

    temperature = r.html.find('span#wob_tm', first=True).text
    unit = (r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text)
    weather = (r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text)

    return(f'The temperature in {query} is {temperature}{unit} and the weather is {weather}.')

if __name__ == '__main__':
    app.run(debug=True)

