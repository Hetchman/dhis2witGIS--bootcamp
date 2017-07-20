from flask import jsonify, request, render_template

from . import dashboard, parser
from .geo import analytics_data, preg_comp

from ..api import get_json
from ..api.indicators import Indicators
from ..api.organisation_units import OrganisationUnits as OU

@dashboard.route("/", methods=["GET"])
def index():
   return render_template("dashboard/index.html")

@dashboard.route("/maps", methods=["GET"])
def maps():
   return render_template("dashboard/maps.html")   


@dashboard.route("/dataElements", methods=["POST"])
def dataElements():
   # get data from POST
   req = request.get_json()

   return jsonify(result)

@dashboard.route("/indicators", methods=["POST"])
def indicators():
   # DEFAULT functionality
   # result = get_json(ind.endpoint)
   
   
   # get data from POST
   req = request.get_json()

   ind = Indicators(req["kind"])
   result = get_json(ind.endpoint)

   return jsonify(result)

@dashboard.route("/organisationUnits", methods=["POST"])
def organisationUnits():
   # get data from POST
   req = request.get_json()

   ou = OU(req["payload"]["level"])
   result = get_json(ou.endpoint)

   return jsonify(result)

@dashboard.route("/analytics", methods=["POST"])
def analytics():
   # get data from POST
   req = request.get_json()

   return jsonify(result)

@dashboard.route("/geojson")
def geojson():
   response = {}
   argument = request.args.get("type")

   if argument == "analytics":
      response = analytics_data()
   elif argument == "preg":
      response = preg_comp()

   return jsonify(response)
