# from flask import jsonify


# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from django.core.serializers import serialize
# from django.views.generic import TemplateView
# from .models import WorldBorder
from .utils import get_org_units, get_data_el, poly_units_geojson, immun_analytics, get_preg , get_analytics
# from django.core.cache import cache


#Modify this views to see
org_names = {
	"O6uvpzGd5pu": "Bo",
	"fdc6uOvgoji": "Bombali",
	"lc3eMKXaEfw": "Bonthe",
	"jUb8gELQApl": "Kailahun",
	"PMa2VCrupOd": "Kambia",
	"kJq2mPyFEHo": "Kenema",
	"qhqAxPSTUXp": "Koinadugu",
	"Vth0fbpFcsO": "Kono",
	"jmIPBj66vD6": "Moyamba",
	"TEQlaapDQoK": "Port Loko",
	"bL4ooGhyHRQ": "Pujehun",
	"eIQbndfxQMb": "Tonkolili",
	"at6UHUQatSo": "Western Area"
}

def get_org_name(id_key):
	for k, v in org_names.items():
		if k == id_key:
			return v

def analytics_data():
	analitic_data = get_analytics()
	columns = {
		"records" : []
	}

	orgs = []

	for i in range(len(analitic_data["rows"])):
		dat = {}
		org = analitic_data['rows'][i][0]
		orgs.append(org)
		pe = analitic_data['rows'][i][1]
		val = analitic_data['rows'][i][2]
		dat['Organisation Unit'] = org
		dat['pe'] = pe
		dat['val'] = float(val)
		columns['records'].append(dat)

	unique_orgs = set(orgs)
	
	def get_geojson_pk():
		x = poly_units_geojson().json()

	collection = {}
	
	for org in unique_orgs:
		collection[org] = [{"period" : [], "value" : [], "name" : '', "average" : ''}]

	geojson = poly_units_geojson().json()
	
	for x in unique_orgs:
		for n in columns["records"]:
			org = n["Organisation Unit"]
			if x==org:
				org_name = get_org_name(x)
				collection[x][0]["period"].append(n['pe'])
				collection[x][0]["value"].append(n['val'])
				collection[x][0]["name"] = org_name
				tot = sum(collection[x][0]["value"])
				av = tot / len(collection[x][0]["period"])
				collection[x][0]["average"] = av

				for i in range(len(geojson["features"])):
					feat = geojson["features"][i]
					id = feat["id"]
					if x == id:
						total = sum(collection[x][0]["value"])
						av = total / len(collection[x][0]["period"])
						feat["properties"]['average'] = av

	collection["geojson"] = geojson
	return collection

def preg_comp():
	preg_data = get_preg()
	columns = {
		"records": []
	}
	
	orgs = []
	
	for i in range(len(preg_data["rows"])):
		dat = {}
		org = preg_data['rows'][i][0]
		orgs.append(org)
		pe = preg_data['rows'][i][1]
		val = preg_data['rows'][i][2]
		dat['Organisation Unit'] = org
		dat['pe'] = pe
		dat['val'] = float(val)
		columns['records'].append(dat)
	
	unique_orgs = set(orgs)
	
	def get_geojson_pk():
		x = poly_units_geojson().json()
	
	collection = {}
	
	for org in unique_orgs:
		collection[org] = [{"period": [], "value": [], "name": '', "average": ''}]
	
	geojson = poly_units_geojson().json()
	
	for x in unique_orgs:
		for n in columns["records"]:
			org = n["Organisation Unit"]
			if x == org:
				org_name = get_org_name(x)
				collection[x][0]["period"].append(n['pe'])
				collection[x][0]["value"].append(n['val'])
				collection[x][0]["name"] = org_name
				tot = sum(collection[x][0]["value"])
				av = tot / len(collection[x][0]["period"])
				collection[x][0]["average"] = av
				
				for i in range(len(geojson["features"])):
					feat = geojson["features"][i]
					id = feat["id"]
					if x == id:
						total = sum(collection[x][0]["value"])
						av = total / len(collection[x][0]["period"])
						feat["properties"]['average'] = av
	collection["geojson"] = geojson
	return collection

# def org_view(request):
# 	if 'q' in request.GET:
# 		q = request.GET['q']
# 		org_units = get_org_units(query=q)
# 	else:
# 		org_units = get_org_units()
	
# 	data = []
# 	for org in org_units['organisationUnits']:
# 		data.append(org)
	
# 	context = {
# 		'org_units': data
# 	}
# 	return render(request, 'world/home.html', context)


# def data_elements_view(request):
# 	if 'q' in request.GET:
# 		q = request.GET['q']
# 		data_elements = get_data_el(query=q)
# 	else:
# 		data_elements = get_data_el()
# 	data = []
# 	for el in data_elements['world/dataElements']:
# 		data.append(el)
	
# 	context = {
# 		'data_els': data
# 	}
# 	return render(request, 'world/data_el.html', context)
# 	return HttpResponse()


# def organ_units_polygon(request):
# 	geo_data = poly_units_geojson()
# 	return HttpResponse(geo_data)
	


# def map_view(request):
# 	return render(request, 'world/main.html')


# def analytics_immun(request):
# 	analytiks = immun_analytics()
# 	return HttpResponse(analytiks)
