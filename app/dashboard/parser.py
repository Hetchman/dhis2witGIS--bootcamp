# 

def parse_params(data):
   # pass
   _class_name = data["class"]

   from ..api import organisation_units
   
   _class = getattr(organisation_units, _class_name)

   _class.payload.update(data["payload"])
   return _class.payload
   # return _class.payload.update(data["payload"])
