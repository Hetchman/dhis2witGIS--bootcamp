"""
Platform dhis2.org
Filename "indicators.py"
"""


"""
Class "Indicators"
Serves the endpoint /api/indicators.json
"""
class Indicators():
   
   def __init__(self, value=None):
      """ Set api endpoints for our data """
      # confirm value sent and set url
      if value == "type":
         self.url = "https://play.dhis2.org/release1/api/indicatorTypes"
      elif value == "group":
         self.url = "https://play.dhis2.org/release1/api/indicatorGroups"
      else:
         self.url = "https://play.dhis2.org/release1/api/indicators"
      
      self.payload = {
         "paging": "false",
         "fields": ["id", "name", "code"]
      }
      self.endpoint = {
         "url": self.url,
         "payload": self.payload
      }


