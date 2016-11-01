import CsvHelper
from Crawler import Crawler


for url in CsvHelper.read_file('webshops.csv'):
    print("Processing: %s" % url)

    splitter = url.split('.')[0]
    sitename = splitter[len(splitter) - 2]

    result = Crawler(sitename, 'webshop_certain.csv').run()
    print(result.get_found())

    print("Done")
