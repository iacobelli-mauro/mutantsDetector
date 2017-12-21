#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import re
from config.database import db_session
from flask_restful import abort, Resource, request
from flask import current_app
from models.Mutant import Mutant
from services.MutantDetectorService import MutantDetector


class MutantController(Resource):
    """Class for the Mutant Controller."""
    def post(self):
        """Validate the base proteins and returns the result."""
        input_data = request.get_json()['mutantDna']
        # Load the matrix length for validations
        matrix_i = current_app.config['MATRIX_I_LENGTH']
        matrix_x = current_app.config['MATRIX_X_LENGTH']
        # Check the matrix i legth
        if not input_data or len(input_data) < matrix_i:
            abort(400, message="Deben de existir, " +
                  str(matrix_i) + " lineas de proteina")
        for index, row in enumerate(input_data):
            # Check the matrix X legth
            if len(row) < matrix_x:
                abort(400, message="El largo de de la cadena de proteinas debe de ser de "
                      + str(matrix_x))
            # Check if the proteins list contains invalid characters
            regexp = re.compile('^[ATCG]+$')
            if not regexp.match(row):
                abort(
                    400, message="La cadena de ADN solo puede contener los caracteres ATGC")
        try:
            # Load the mutant detector
            mutant_detector = MutantDetector(input_data)
            is_mutant = mutant_detector.is_mutant_dna()
            # Save the data
            mutant = Mutant(input_data)
            mutant.isMutant = is_mutant
            db_session.add(mutant)
            db_session.commit()
            # Return the response
            if is_mutant:
                return {'status': 'Is a Mutant'}, 200
            else:
                abort(403, message="Not a Mutant")
        except RuntimeError as ex:
            db_session.rollback()
            logging.error("Ah ocurrido un error en la ejecucion.")
            logging.error(ex)
            abort(500, message="Unespected error")
