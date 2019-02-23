#! /usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import json
from flask import Flask, request, Response

app = Flask(__name__)
logging.basicConfig(level = logging.INFO,
                    format = '[%(asctime)s][%(name)s][%(levelname)s][%(message)s]')
logger = logging.getLogger(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/search_locations_by_product_type", methods=['GET'])
def get_transactions():
    product_type = request.args.get('product_type')
    logger.info(f"search location by product type: {product_type}")
    result = {"Status":"OK"}
    return json.dumps(result)

@app.route("/get_area_info", methods=['GET'])
def get_area_info():
    x = request.args.get('x')
    y = request.args.get('y')
    logger.info(f"get ansactions around ({x}, {y})")
    result = {"Status":"OK"}
    return json.dumps(result)