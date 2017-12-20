import logging
from config.database import db_session
from flask_restful import Resource, abort, request
from models.Mutant import Mutant
from sqlalchemy import func


class StatsController(Resource):
    """Class for the Stats Controller."""

    def get(self):
        """Returns the stats info."""
        try:
            # Get the sumarized values from DB
            data = db_session.query(Mutant.isMutant, func.count(
                Mutant.id)).group_by(Mutant.isMutant).all()
            # Prepare and fill the response
            response = {'count_mutant_dna': 0,
                        'count_human_dna': 0,
                        'ratio': None}
            for index, row in enumerate(data):
                if row[0]:
                    response['count_mutant_dna'] = row[1]
                else:
                    response['count_human_dna'] = row[1]
            # Calculate ratio
            if response['count_mutant_dna'] > 0 and response['count_human_dna'] > 0:
                response['ratio'] = float(
                    float(response['count_mutant_dna'] * 100 / response['count_human_dna']) / 100)
            else:
                response['ratio'] = float(0.0)
            return response, 200
        except RuntimeError as ex:
            logging.error("Ah ocurrido un error en la ejecucion.")
            logging.error(ex)
            abort(500, message="Unespected error")
