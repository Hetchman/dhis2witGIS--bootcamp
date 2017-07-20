"""
Platform dhis2.org
Filename "analytics.py"
"""


"""
Class "Analytics"
Serves the endpoint /api/27/analytics.json
"""
class Analytics():
   
   # api endpoint for events analytics
   endpoint_url = "https://play.dhis2.org/release1/api/27/analytics.json"

   payload = {
      "dimension": "pe:LAST_12_MONTHS",
      "filter": "dx:dwEq7wi6nXV",
      "displayProperty": "NAME",
      "skipMeta": "true"
   }

   endpoint = {
      "url": endpoint_url,
      "payload": payload
   }

   def __init__(self):
      pass


   # function returns a string suitable for url parameters
   # for the analytics endpoint
   # param | ?dimenstion=ou:
   def insert_dimension_id(orgunits):
      # a list to hold dimension ids
      dimension = []
      for org in orgunits["organisationUnits"]:
         dimension.append(org["id"])
      dimensions = ";".join(dimension)
      return "ou:" + dimensions
