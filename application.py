#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config.log_config
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, request
from controllers.MutantController import MutantController
from controllers.StatsController import StatsController

application = Flask(__name__)
application.config.from_object('config.app_config')
api = Api(application)

api.add_resource(MutantController, '/mutant')
api.add_resource(StatsController, '/stats')

if __name__ == '__main__':
    application.run(debug=True)