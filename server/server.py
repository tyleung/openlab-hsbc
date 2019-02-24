#! /usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import json
from flask import Flask, request, make_response, jsonify
from analysis_service import Analyst
from render_service import Graph_Formatter
from realtime_monitor_service import Realtime_Monitor

app = Flask(__name__)
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(name)s][%(levelname)s][%(message)s]')
logger = logging.getLogger(__name__)


@app.route("/")
def hello():
  return "Hello World!"


@app.route("/search_locations_by_product_type", methods=['GET'])
def get_transactions():
  product_type = request.args.get('product_type')
  logger.info(f"search location by product type: {product_type}")
  result = {"Status": "OK"}
  return json.dumps(result)


@app.route("/get_area_info", methods=['GET'])
def get_area_info():
  x = request.args.get('x')
  y = request.args.get('y')
  logger.info(f"get transactions around ({x}, {y})")
  result = {"Status": "OK"}
  return json.dumps(result)


@app.route("/get_chart", methods=['GET'])
def get_chart():
  # ana = Analyst(user_db='../data/customer_info.json', trans_db="../data/transactions.json")
  # result = ana.analysis()
  # graph = Graph_Formatter().get_graph(title_text="Age Distribution of the Area",
  #                                     xdata=['[0, 10)', '[21, 30)', '[15, 21)', '[10, 15)', '[30, 35)', '[35, 100)'],
  #                                     ydata=[2578, 2249, 1603, 1293, 1222, 1055],
  #                                     series_type = 'bar')
  graph = Graph_Formatter(type='pi').get_graph()
  response = make_response(jsonify(graph), 200)
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response


@app.route("/realtime_chart", methods=['GET'])
def realtime_chart():
  xdata, ydata = Realtime_Monitor.get_current_data()
  graph = Graph_Formatter().get_graph(title_text="Transactions In the Area",
                                      xdata=xdata,
                                      ydata=ydata,
                                      series_type = 'line')
  response = make_response(jsonify(graph), 200)
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response