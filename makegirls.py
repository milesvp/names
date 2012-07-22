import pickle

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
                names[name].append((year,count))
            except:
                names[name] = [(year,count)]
    return names

def getMinYear(name):
    return min([year for year, count in name])

def getMaxYear(name):
    return max([year for year, count in name])

def getYearRange(names, girlname_dict):
    min_years = []
    max_years = []
    for name in names:
        min_years.append(getMinYear(girlname_dict[name]))
        max_years.append(getMaxYear(girlname_dict[name]))
    return min(min_years), max(max_years)

