from crypt import methods
from urllib import request
from flask import Flask, render_template, request
import pandas as pd
import plotly
import json
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from compare_funcs import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chartsajax.html', graph1JSON=heightChart(), graph2JSON=areaChart(), graph3JSON=barChart())


@app.route('/compare')
def compare():
    return render_template('compare.html', graphJSON=compare_function())


def compare_function():
    pass


@app.route('/callback-1', methods=['POST', 'GET'])
def cb1():
    print("callback-1: {}".format(request.args))
    return heightChart(crop=request.args.get('crop'), tray_position=request.args.get('tray_position'),
                       treatment=request.args.get('treatment'))


@app.route('/callback-2', methods=['POST', 'GET'])
def cb2():
    print("callback-2: {}".format(request.args))
    return areaChart(crop=request.args.get('crop'), tray_position=request.args.get('tray_position'),
                     treatment=request.args.get('treatment'))


@app.route('/callback-3', methods=['POST', 'GET'])
def cb3():
    print("callback-3: {}".format(request.args))
    return barChart(variety=request.args.get('variety'))


@app.route('/callback-cc-1', methods=['POST', 'GET'])
def compare_cc_1():
    print("callback-cc-1: {}".format(request.args))
    return compare_crops_height(crop_1=request.args.get('crop_1'),
                                crop_2=request.args.get('crop_2'),
                                tray_position=request.args.get('tray_position_cc'),
                                treatment=request.args.get('treatment_cc'))


@app.route('/callback-cc-2', methods=['POST', 'GET'])
def compare_cc_2():
    print("callback-cc-2: {}".format(request.args))
    return compare_crops_area(crop_1=request.args.get('crop_1'),
                              crop_2=request.args.get('crop_2'),
                              tray_position=request.args.get('tray_position_cc'),
                              treatment=request.args.get('treatment_cc'))


@app.route('/callback-cc-3', methods=['POST', 'GET'])
def compare_cc_3():
    print("callback-cc-3: {}".format(request.args))
    return compare_crops_greennes(crop_1=request.args.get('crop_1'),
                                  crop_2=request.args.get('crop_2'),
                                  tray_position=request.args.get('tray_position_cc'),
                                  treatment=request.args.get('treatment_cc'))


@app.route('/callback-ctp-1', methods=['POST', 'GET'])
def compare_ctp_1():
    print("callback-ctp-1: {}".format(request.args))
    return compare_tray_positions_height(tray_position_1=request.args.get('tray_position_1'),
                                         tray_position_2=request.args.get('tray_position_2'),
                                         treatment_ctp=request.args.get('treatment_ctp'),
                                         crop_ctp=request.args.get('crop_ctp'))


@app.route('/callback-ctp-2', methods=['POST', 'GET'])
def compare_ctp_2():
    print("callback-ctp-2: {}".format(request.args))
    return compare_tray_positions_area(tray_position_1=request.args.get('tray_position_1'),
                                       tray_position_2=request.args.get('tray_position_2'),
                                       treatment_ctp=request.args.get('treatment_ctp'),
                                       crop_ctp=request.args.get('crop_ctp'))


@app.route('/callback-ctp-3', methods=['POST', 'GET'])
def compare_ctp_3():
    print("callback-ctp-3: {}".format(request.args))
    return compare_tray_positions_greennes(tray_position_1=request.args.get('tray_position_1'),
                                           tray_position_2=request.args.get('tray_position_2'),
                                           treatment_ctp=request.args.get('treatment_ctp'),
                                           crop_ctp=request.args.get('crop_ctp'))


@app.route('/callback-ct-1', methods=['POST', 'GET'])
def compare_ct_1():
    print("callback-ct-1: {}".format(request.args))
    return compare_treatments_height(treatment_1=request.args.get('treatment_1'),
                                     treatment_2=request.args.get('treatment_2'),
                                     tray_position_ct=request.args.get('tray_position_ct'),
                                     crop_ct=request.args.get('crop_ct'))


@app.route('/callback-ct-2', methods=['POST', 'GET'])
def compare_ct_2():
    print("callback-ct-2: {}".format(request.args))
    return compare_treatments_area(treatment_1=request.args.get('treatment_1'),
                                   treatment_2=request.args.get('treatment_2'),
                                   tray_position_ct=request.args.get('tray_position_ct'),
                                   crop_ct=request.args.get('crop_ct'))


@app.route('/callback-ct-3', methods=['POST', 'GET'])
def compare_ct_3():
    print("callback-ct-3: {}".format(request.args))
    return compare_treatments_greennes(treatment_1=request.args.get('treatment_1'),
                                       treatment_2=request.args.get('treatment_2'),
                                       tray_position_ct=request.args.get('tray_position_ct'),
                                       crop_ct=request.args.get('crop_ct'))





if __name__ == '__main__':
    app.run(debug=True)
