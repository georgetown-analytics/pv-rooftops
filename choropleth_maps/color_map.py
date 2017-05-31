import csv
from bs4 import BeautifulSoup

# Read in installation counts
count = {}
reader = csv.reader(open('open_pv_2015.csv'), delimiter=",")
for row in reader:
    try:
        full_fips = row[7] #row 7 or row[8] + row[9]
        rate = int(row[3])
        count[full_fips] = rate
    except:
        pass
		
		
# Load the SVG map (basemap)
svg = open('counties.svg', 'r').read()

# Load into Beautiful Soup
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])

# Find counties
paths = soup.findAll('path')

# Map colors
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

# County style
path_style ='font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'

# Color the counties based on counts
for p in paths:
     
    if p['id'] not in ["State_Lines", "separator"]:
        try:
            rate = count[p['id']]
        except:
            continue
             
         
        if rate > 3000:
            color_class = 5
        elif rate > 2000:
            color_class = 4
        elif rate > 1000:
            color_class = 3
        elif rate > 500:
            color_class = 2
        elif rate > 100:
            color_class = 1
        else:
            color_class = 0
 
 
        color = colors[color_class]
        p['style'] = path_style + color
 
print (soup.prettify())