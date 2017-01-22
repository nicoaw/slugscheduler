from urllib2 import urlopen
from bs4 import BeautifulSoup
import json
import re


url = 'http://registrar.ucsc.edu/catalog/programs-courses/course-descriptions/cmps.html'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', {'class': 'content contentBox'})
for p in div.find_all('p'):
    strongs = p.find_all('strong')
    ems = p.find_all('em')
    print p
    if len(strongs) > 2:
        nbr = 'CMPS' + ' ' + strongs[0].text.replace('.', '')
        title = strongs[1].text.replace('.', '')
        offerings = [quarter for quarter in strongs[-1].text.split(',') if quarter in ['F', 'W', 'S', 'U']]

        # Parse units
        units = 5
        m = re.search('(\d+) [cC]redits', str(p))
        if m:
            units = int(m.group(1))

        print nbr, title, units, offerings
        db.course.insert(
                nbr=nbr,
                title=title,
                units=units,
                offerings=json.dumps(offerings)
                )
