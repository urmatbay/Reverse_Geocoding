import csv

lat_lng = [
"49.153485,-123.133912",
"49.265854,-123.168001",
"49.227239,-122.502279",
"49.091293,-122.613087",
"49.151895,-123.147852",
"49.27136,-123.049739",
"49.133771,-123.177046",
"49.079342,-122.65824",
"49.169092,-121.937449"
]


# def open_with_csv(filename):
# 	data = []
# 	with open(filename, encoding='utf-8') as tsvin:
# 		reader = csv.reader(tsvin)
# 		for line in  reader:
# 			data.append(line)
# 	return data

if __name__ == '__main__':
	lat_lng = open_with_csv('lat_lng.csv')
	print(lat_lng)
