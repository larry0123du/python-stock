import requests
import pprint
import urllib, time, os, re, csv
import bs4 as bs
import pandas_datareader.data as web
import datetime
from datetime import datetime as dt


def fetch_data(ticker, interval, period):
    url = url = "https://www.google.com/finance/getprices?q={0}&i={1}&p={2}&f=d,o,h,l,c,v".format(ticker, interval, period)
    resp = urllib.urlopen(url).readlines()
    attr = resp[4][8:-1].split(',')

    data = [attr]

    for i in xrange(7, len(resp)):
        if resp[i].count(',') is not 5: continue
        offset,close,high,low,open,volume = resp[i].split(',')
        if offset[0]=='a':
            day = float(offset[1:])
            offset = 0
        else:
            offset = float(offset)
        buffer = [float(x) for x in [open,high,low,close,volume]]
        t = dt.fromtimestamp(day+(60*offset))
        buffer.insert(0, t)
        data.append(buffer)

    pprint.pprint(data)
	# with open('google_stock.dat', 'wb') as f:
	# 	f.write(resp)
	# attr = re.findall('th\ class=.*?>.*', resp)
	# print attr
	# resp = requests.get(url+ticker)
	# soup = bs.BeautifulSoup(resp.text)
	# table = soup.find("table", {"class":"gf-table historical_price"})
	# attr = [str(a.text[:-1]) for a in table.findAll("th")]
	# # print attr
	# for row in table.findAll("tr")[1:]:

	# start = datetime.datetime(2000, 1, 1)
	# end = dt.today()

	# q = web.DataReader(ticker, 'google', start, end)

	# pprint.pprint(q)
	# print type(q)
	
fetch_data('GOOG', 60, '1M')

