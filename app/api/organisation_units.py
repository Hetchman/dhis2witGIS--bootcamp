"""
Platform dhis2.org
Filename "organisation_units.py"
"""


"""
Class "OrganisationUnits"
Serves the endpoint /api/organisationUnits.json
"""
class OrganisationUnits():

   def __init__(self, value=2):
      self.url = "https://play.dhis2.org/release1/api/organisationUnits.json"
      self.payload = {
         "paging": "false",
         "level": value,
         "fields": ["code", "name", "id"]
      }
      self.endpoint = {
         "url": self.url,
         "payload": self.payload
      }

   # @property
   # def payload():
   #    """ Get payload """
   #    return self._payload
   # @payload.setter
   # def payload(self, value):
   #    """ Set payload """
   #    self._payload = value
   # @payload.deleter
   # def payload():
   #    """ Delete payload """
   #    del self._payload
