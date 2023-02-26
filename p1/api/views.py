from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from bs4 import BeautifulSoup as bs 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
class Web(APIView):
    def post(self, request, format=None):
        url = request.data.get('url')
        if url:
            r = requests.get(url)
            soup = bs(r.content, 'html.parser') 
            try:
                price=soup.find('div', attrs = {"class":"_30jeq3 _16Jk6d"}).text
                product = soup.find('span', attrs={'class':'B_NuCI'}).text
            except:
                price = None
                product = None
                return Response({"result": "Invalid url"})
            URL = "https://www.coingecko.com/en/coins/polygon"
            req = requests.get(URL)
            bsoup = bs(req.content, 'html.parser') 
            polygon_price=bsoup.find('span', attrs = {"class":"no-wrap"}).text
            dict1 = {
                "polygon Current Price ": polygon_price
            }
            dict2 = {
                "product":product,
                "price": price,

            }
            dict3 = {
                "Polygon ": dict1,
                "item price": dict2
            }
            return Response(dict3)
        else:
            dict = {
                "result": False, 
                "info": "please provide url"
            }
            return Response(dict)