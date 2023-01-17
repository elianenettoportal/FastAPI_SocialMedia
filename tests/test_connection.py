from App.database import get_db
from ..App import utils

def test_db_connection():
    assert utils.database_exists() == True
