import urllib, urllib2
from BeautifulSoup import BeautifulSoup as BS
import pickle

def getHTML(year = 1880):
    url = "http://www.ssa.gov/cgi-bin/popularnames.cgi"
    values = {'top': 1000, 'number': 'n', 'year': str(year)}
    data = urllib.urlencode(values)
    req = urllib2.Request(url,data)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

def getNames(year = 1880):
    html = getHTML(year)
    soup = BS(''.join(html))
    soup.prettify()
    tables = soup.findAll('table')

    rows = tables[2].findAll('tr')
    rowdata = []
    for tr in rows:
        cols = tr.findAll('td')
        row = []
        for td in cols:
            row.append(''.join(td.find(text=True)))
        rowdata.append(row)
    return rowdata[1:1001]

def pickleNames(year_start = 2011, year_end = 1880):
    for year in xrange(year_start, year_end-1, -1):
        print year
        data = getNames(year)
        f = open ('names.'+str(year), 'w')
        pickle.dump(data,f)
        f.close()


