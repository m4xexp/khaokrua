from src.DBHelper import DBHelper
from src.helper_functions import *


class Search:
    def __init__(self):
        self.db = DBHelper()

 
    #get all recipe
    def search(self,keyword):
        data, columns = self.db.fetch ("SELECT *  "
                              "  FROM tbl_recipe "
                              "  WHERE title like '%{}%' ".format(keyword))
        return row_as_dict(data, columns)


        # like '%{}%'

    #get all recipe
    def fetch(self):
        data, columns = self.db.fetch ("SELECT title  "
                              "  FROM tbl_recipe " )
        return row_as_dict(data, columns)

        # like '%{}%'

    