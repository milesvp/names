import pickle
import locale
import pylab

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


girlname_dict_filename = 'girlname.dict'

def saveGirlDict(names):
    f = open(girlname_dict_filename, 'w')
    names_dict = pickle.dump(names,f)
    f.close()
    
def openGirlDict():
    f = open(girlname_dict_filename, 'r')
    names_dict = pickle.load(f)
    f.close()
    return names_dict

def makeGirlNames():
    first_year = 1880
    last_year = 2011

    names = {}

    for year in xrange(first_year,last_year+1):
        f = open('names.' + str(year),'r')
        name_list = pickle.load(f)
        f.close()
        
        year_names = {}
        for name_rank in name_list:
            year_names[name_rank[3]] = name_rank[4]
        names[year] = year_names

    return names

def makeGirlList():
    girlname_dict = openGirlDict()
    names = {}
    for year in girlname_dict.keys():
        for name,count in girlname_dict[year].iteritems():
            try:
                names[name][year] = locale.atoi(count)
            except:
                names[name] = {}
                names[name][year] = locale.atoi(count)
    return names

def getMinYear(name):
    return min([year for year, count in name.iteritems()])

def getMaxYear(name):
    return max([year for year, count in name.iteritems()])

def getYearRange(names):
    min_years = []
    max_years = []
    for name in names:
        min_years.append(getMinYear(name))
        max_years.append(getMaxYear(name))
    return min(min_years), max(max_years)

def getAnnualCounts(name, start_year = None, end_year = None):
    if not start_year:
        start_year = getMinYear(name)
    if not end_year:
        end_year = getMaxYear(name)
    counts = []
    for year in xrange(start_year, end_year+1):
        if name.has_key(year):
            counts.append(int(name[year]))
        else:
            counts.append(0)
    return counts

        
def plot(names):
    min_year, max_year = getYearRange(names)
    years = range(min_year, max_year+1)
    for name in names:
        pylab.plot(years, getAnnualCounts(name, min_year, max_year))
    pylab.show()

def main():
    names = []
    for name, years in makeGirlList().iteritems():
        if len(years) >4:
            names.append(name)
    names.sort()
    for name in names:
        print name

if __name__ == "__main__":
    main()




