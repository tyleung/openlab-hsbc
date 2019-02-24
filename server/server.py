#! /usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import json
from flask import Flask, request, make_response, jsonify
from analysis_service import Analyst
from search_service import Search
from render_service import Graph_Formatter
from realtime_monitor_service import Realtime_Monitor

app = Flask(__name__)

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(name)s][%(levelname)s][%(message)s]')
logger = logging.getLogger(__name__)

user_db = './data/customer_info.json'
trans_db = './data/transactions.json'

analysis_service = Analyst(user_db=user_db, trans_db=trans_db)
search_service = Search(src_paths=trans_db)

@app.route("/")
def hello():
  return "Hello World!"


@app.route("/search_locations_by_product_type", methods=['GET'])
def search_locations_by_product_type():
  product_type = request.args.get('product_type')
  logger.info(f"search location by product type: {product_type}")
  locations = search_service.get_locations_by_product_type(product_type=product_type)
  return jsonify({"locations": locations})


@app.route("/get_area_info", methods=['GET'])
def get_area_info():
  x = request.args.get('x')
  y = request.args.get('y')
  logger.info(f"get transactions around ({x}, {y})")
  customers = search_service.get_customers_by_location(x=x, y=y)
  logger.info(f"get custmers around location ({x}, {y}), customers count: {len(customers)}")

  result = dict()
  if len(customers) > 0:
    analysis_result = analysis_service.analysis_users(customers)
    age_info = analysis_result['age']
    credit_info = analysis_result['credit']
    edu_info = analysis_result['edu']
    gender_info = analysis_result['gender']

    if age_info:
      age_graph = Graph_Formatter().get_graph(title_text="Age Distribution of the Area",
                                          xdata=age_info[0],
                                          ydata=age_info[1],
                                          series_type = 'bar')
      result['age_graph'] = age_graph

    if credit_info:
      credit_graph = Graph_Formatter().get_graph(title_text="Credit Distribution of the Area",
                                          xdata=credit_info[0],
                                          ydata=credit_info[1],
                                          series_type = 'bar')
      result['credit_graph'] = credit_graph

    if edu_info:
      edu_graph = Graph_Formatter().get_graph(title_text="Education Level Distribution of the Area",
                                          xdata=edu_info[0],
                                          ydata=edu_info[1],
                                          series_type = 'bar')
      result['edu_info'] = edu_graph

    if gender_info:
      gender_graph = Graph_Formatter().get_graph(title_text="Gender Distribution of the Area",
                                          xdata=gender_info[0],
                                          ydata=gender_info[1],
                                          series_type = 'bar')
      result['gender_graph'] = gender_graph

  response = make_response(jsonify(result), 200)
  response.headers['Access-Control-Allow-Origin'] = '*'

  return response


@app.route("/get_chart", methods=['GET'])
def get_chart():
  # ana = Analyst(user_db='../data/customer_info.json', trans_db="../data/transactions.json")
  # result = ana.analysis()
  # graph = Graph_Formatter().get_graph(title_text="Age Distribution of the Area",
  #                                     xdata=['[0, 10)', '[21, 30)', '[15, 21)', '[10, 15)', '[30, 35)', '[35, 100)'],
  #                                     ydata=[2578, 2249, 1603, 1293, 1222, 1055],
  #                                     series_type = 'bar')
  graph = Graph_Formatter().get_graph()
  response = make_response(jsonify(graph), 200)
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response


@app.route("/realtime_chart", methods=['GET'])
def realtime_chart():
  radius = request.args.get('radius')
  product_type = request.args.get('product_type')
  if radius:
    logger.info(f"get real time transactions in radius: {radius}")
  if product_type:
    logger.info(f"get real time transactions for product_type: {product_type}")
  xdata, ydata = Realtime_Monitor.get_current_data(product_type=product_type, radius=float(radius))
  graph = Graph_Formatter().get_graph(title_text="Transactions In the Area",
                                      xdata=xdata,
                                      ydata=ydata,
                                      series_type = 'line')
  response = make_response(jsonify(graph), 200)
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response


if __name__=='__main__':
  app.run(debug=True)