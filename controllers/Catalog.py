from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
import re

# Quarter enumerations
FALL = 'F'
WINTER = 'W'
SPRING = 'S'
SUMMER = 'U'

class Catalog:
    def __init__(self):
        self.courses = {}
        self.min_year = None
        self.max_year = None

    # Add courses for a specific program
    def add(self, program):
        current_year = get_current_catalog_year(program)
        year = current_year
        # Scrape url page for course information
        while True:
            try:
                url = get_course_descriptions_url(current_year, program, year)
                html = urlopen(url)
            except:
                break

            soup = BeautifulSoup(html, 'html.parser')
            if year in [2015, 2016]:
                self.__scrape_2015_and_2016(program, soup)
            year -= 1

        if self.min_year is None or self.min_year > year:
            self.min_year = year
        if self.max_year is None or self.min_year < year:
            self.max_year = year

    # Get course nbrs available
    def get_courses(self):
        return self.courses.keys()

    # Get course title
    def get_title(self, nbr):
        return self.courses[nbr][0]

    # Get course units
    def get_units(self, nbr):
        return self.courses[nbr][1]

    # Get course prereqs (a list of course nbrs)
    def get_prereqs(self, nbr):
        return self.courses[nbr][2]

    # Is course offered at certain year, quarter
    def is_offered(self, nbr, year, quarter):
        return (year, quarter) in self.courses[nbr][3]

    # Are the prereqs meet for course
    def is_satisfied(self, transcript, nbr):
        for prereq in self.get_prereqs(nbr):
            if not transcript.has(prereq):
                return False
        return True

    # Get earliest year recorded
    def min_year(self):
        return self.min_year

    # Get most recent year recorded
    def max_year(self):
        return self.max_year

    def __add_course(self, nbr, title, units, prereqs, offerings):
        # print nbr, title, units, prereqs, offerings
        self.courses[nbr] = (title, units, prereqs, offerings)

    def __scrape_2015_and_2016(self, program, soup):
        div = soup.find('div', {'class': 'content contentBox'})
        for p in div.find_all('p'):
            strongs = p.find_all('strong')
            ems = p.find_all('em')
            if len(strongs) > 2:
                nbr = program.upper() + ' ' + strongs[0].text.replace('.', '')
                title = strongs[1].text.replace('.', '')
                offerings = [quarter for quarter in strongs[-1].text.split(',') if quarter in [FALL, WINTER, SPRING, SUMMER]]

                # Parse units
                units = 5
                m = re.search('(\d+) [cC]redits', str(p))
                if m:
                    units = int(m.group(1))

                # Parse prereqs
                """
                m = re.search('Prerequisite\(s\): ([^\.]+)', str(p))
                if m:
                    print m.group(1)
                    m = re.search('(\d+)', m.group(1))
                    if m:
                        print m.groups()
                """

                self.__add_course(nbr, title, units, [], offerings)


def get_current_catalog_year(program):
    html = urlopen('http://registrar.ucsc.edu/catalog/programs-courses/program-statements/' + program + '.html')
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', {'class': 'content contentBox'})
    p = div.find_all('p')[1]
    m = re.match(r'(\d+)\-\d+', p.text)
    return int(m.group(1))

def get_course_descriptions_url(current_year, program, year):
    if current_year == year:
        return 'http://registrar.ucsc.edu/catalog/programs-courses/course-descriptions/' + program + '.html'
    else:
        year -= 2000
        academic_year = str(year) + '-' + str(year + 1)
        return 'http://registrar.ucsc.edu/catalog/archive/' + academic_year + '/programs-courses/course-descriptions/' + program + '.html'

catalog = Catalog()
catalog.add('cmps')

