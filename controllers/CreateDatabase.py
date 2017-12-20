from config import database
from flask_restful import abort, Resource, request
from models.Mutant import Mutant

class CreateDatabase(Resource):
    def get(self):
        try:
            database.init_db()
            return "Process OK", 200
        except RuntimeError as ex:
            return "Algo fue mal:"+ex, 200