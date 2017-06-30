from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import csv
import os
import pickle
from bs4 import BeautifulSoup
import numpy as np
import requests
import urllib3
import pandas as pd
import math
import seaborn as sns 



def index(request):

    return get_choropleth(request)


def get_choropleth(request):
	# Read in installation counts
	print(os.getcwd())
	installation = pd.read_csv('pv/data/features_table.csv', sep=",")

	filename='pv/data/Randomforest.pickle'
	features=installation.ix[:, 3:15]

	loaded_model = pickle.load(open(filename, 'rb'))
	count = {}
	yr = request.GET['year']
	ppw = request.GET['price']
	qrtr = 4
	
	#installation_price_per_watt = calc_installation_price_per_watt(int(yr),4)
	installation_price_per_watt = float(ppw)
	#  Modify table to fulfill model input requirements (Order of features, # of columns, etc)

	#  STEP 1: Calculate exp(grid_to_panel) * (sfh + th) for each instance and append to features table
	features['exp(grid_to_panel) * (sfh + th)']=features.apply(lambda x: calc_X11(x,installation_price_per_watt), axis=1)
	
	#  STEP 2: Remove non-applicable features
	
	features.drop('avg_rtl_price', axis=1, inplace=True)
	#  STEP 3: Re-order features to match order expected by the model
	cols = list(features.columns.values)
	cols.pop(cols.index('latitude'))
	features = features[cols+['latitude']]

	#  Get installation count predictions 
	predicted_counts = loaded_model.predict(features)
	
	#  Re-arrange features table for svg creation
	features['count']=predicted_counts
	features['fips']=installation['fips']
	features['county_name']=installation['county_name']
	features['state_abbrv']=installation['state_abbrv']

	features['fips'] = features['fips'].apply(lambda x: '{0:0>5}'.format(x))
	
	#  Write out results to csv
	predicted_data = 'pv/data/'+str(installation_price_per_watt)+'.csv'
	features.to_csv(predicted_data)
	
	if(int(yr) <= 2015):
		reader = csv.reader(open('pv/data/open_pv_' + yr + '.csv'), delimiter=",")
		for row in reader:
			try:
				full_fips = row[7] #row 7 or row[8] + row[9]
				rate = int(row[3])
				count[full_fips] = rate
			except:
				pass
          
	else:
		reader = csv.reader(open(predicted_data), delimiter=",")
		for row in reader:
			try:
				full_fips = row[14] 
				rate = round(float(row[13]))
				count[full_fips] = rate 
			except:
				pass
	


	# Load the SVG map (basemap)
	svg = open('pv/templates/counties.svg', 'r').read()

	# Load into Beautiful Soup
	soup = BeautifulSoup(svg, "html.parser")

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
			except Exception as e:
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

	svg = soup.prettify(formatter="html")

	sutf8 = svg.encode('UTF-8')
	with open('pv/templates/django.svg', 'w') as f:
		f.write(svg)

	return (render(request, 'django.svg'))

	
	
	
def get_visualizations(request):
	yr = request.GET['year']
	ppw = request.GET['price']
	if(int(yr) <= 2015):
		table_name = 'pv/data/open_pv_' + yr + '.csv'
	else:
		table_name = 'pv/data/'+str(installation_price_per_watt)+'.csv'
	df = pd.read_csv(table_name)
	sns_plot = sns.pairplot(df['year'])
	output_img = 'pv/data/'+str(installation_price_per_watt)+'.csv'
	sns_plot.savefig(output_img)
	
	return (render(request, output_img))

def get_heatmap(request):
	yr = request.GET['year']
	ppw = request.GET['price']
	if(int(yr) <= 2015):
		table_name = 'pv/data/open_pv_' + yr + '.csv'
	else:
		table_name = 'pv/data/'+str(installation_price_per_watt)+'.csv'
	df = pd.read_csv(table_name)
	df.sort_values('count',ascending=False,inplace=True)
	print(df.head())
	for row in df.iterrows():
		#print(df['county'].loc[row[0]])
		http = urllib3.PoolManager()
		r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyC2RUFjvVCRtEUAYk-ndsIExuO2BoHgtOY'.format(df['county'].loc[row[0]]))
		print(r.json()['results'][0]['geometry']['location'])
		
	return None
	




# Estimates national average installation_price_per_watt
def calc_installation_price_per_watt(year, quarter):
	installation_price_per_watt= -6.561 * math.log(year + (0.25 * quarter) - 1990) + 25.602
	return installation_price_per_watt
	
# Calculates exp(grid_to_panel) * (sfh + th)
def calc_X11(row, installation_price_per_watt):
    X11 = (math.exp(row['avg_rtl_price']/installation_price_per_watt)) * (row['sfh_qty'] + row['th_qty'])
    return X11
