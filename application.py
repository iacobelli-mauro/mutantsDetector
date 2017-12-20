#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config.log_config
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, request
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object('config.app_config')
api = Api(application)
db = SQLAlchemy(application)

from controllers.MutantController import MutantController
from controllers.StatsController import StatsController
from controllers.CreateDatabase import CreateDatabase

api.add_resource(MutantController, '/mutant')
api.add_resource(StatsController, '/stats')
api.add_resource(CreateDatabase, '/create')

if __name__ == '__main__':
    application.run(debug=True)