import os

MIN_OCURRENCE_NEEDED = 4
MIN_MUTANT_DNA_COUNT = 1
MATRIX_I_LENGTH = 6
MATRIX_X_LENGTH = 6
if 'ENVIRONMENT' in os.environ and os.environ['ENVIRONMENT'] == 'dev-aws':
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password01@aa1jkblomrj2mej.cshra1jzeyo7.sa-east-1.rds.amazonaws.com/ebdb?charset=utf8'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/mutantDB?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 50
