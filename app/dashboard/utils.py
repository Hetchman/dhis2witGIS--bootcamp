import requests

base_url = 'https://play.dhis2.org/release1/api/'

organization_unit_url = 'organisationUnits.json'
dataElements_url = 'dataElements.json'
organ_unit_spatial = 'organisationUnits.geojson'
analy = '/25/analytics.json'


def get_org_units(query=None):
	params = {
		'paging': 'false',
		'query': query,
		'fields': 'name,code,level'
	}
	
	r = requests.get(base_url + organization_unit_url, params=params, auth=('admin', 'district')).json()
	return r


def get_data_el(query=None):
	params = {
		'paging': 'false',
		'query': query,
		'fields': 'name,code'
	}
	r = requests.get(base_url + dataElements_url, params=params, auth=('admin', 'district')).json()
	return r


def poly_units_geojson(level=2):
	params = {
		'level': level
	}
	r = requests.get(base_url + organ_unit_spatial, params=params, auth=('admin', 'district'))
	return r


def immun_analytics():
	params = {
		'dimension': 'dx:YtbsuPPo010;l6byfWFUGaP;s46m5MS0hxu',
		'dimension': 'pe:LAST_12_MONTHS',
		'filter': 'ou:ImspTQPwCqd&displayProperty=NAME',
		'skipMeta': 'false'
	}
	
	r = requests.get(
		'https://play.dhis2.org/release1/api/25/analytics.json?dimension=dx:YtbsuPPo010;l6byfWFUGaP;s46m5MS0hxu&dimension=pe:LAST_12_MONTHS&filter=ou:ImspTQPwCqd&displayProperty=NAME&skipMeta=false',
		auth=('admin', 'district'))
	return r.json()

def get_preg():
	r = requests.get(
		'https://play.dhis2.org/release1/api/25/analytics.json?dimension=ou:O6uvpzGd5pu;PMa2VCrupOd;jUb8gELQApl;kJq2mPyFEHo;lc3eMKXaEfw&dimension=pe:LAST_12_MONTHS&filter=dx:h8vtacmZL5j&displayProperty=NAME&skipMeta=true',
		auth=('admin', 'district'))
	return r.json()

def get_analytics():
	r = requests.get(
		'https://play.dhis2.org/release1/api/25/analytics.json?dimension=ou:O6uvpzGd5pu;PMa2VCrupOd;jUb8gELQApl;kJq2mPyFEHo;lc3eMKXaEfw&dimension=pe:LAST_12_MONTHS&filter=dx:dwEq7wi6nXV&displayProperty=NAME&skipMeta=true',
		auth=('admin', 'district'))
	
	return r.json()