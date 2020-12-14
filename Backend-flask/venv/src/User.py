from src.DBHelper import DBHelper
from src.helper_functions import *


class User:
    def __init__(self):
        self.db = DBHelper()

    def create(self, userID, fname, lname, profilePic, email, password, profile_name):
        self.db.execute ("INSERT INTO tbl_user \
                          VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(userID, fname, lname, profilePic, email, password, profile_name))
        
        return {'Error': False, 'Message': ""}
    
    def register(self, fname, lname, profilePic, email, password, profile_name):
        data, columns = self.db.fetch ("   SELECT * \
                                            FROM tbl_user u \
                                            WHERE u.email = '{}' ".format(email)
                                        )
        print(data)
        if len(data) == 1:
            user = row_as_dict(data, columns)
            result = [ i for i in user]
            if result[0]['email'] == email:
                return ({'Error': True, 'Message': "Email is already exist" }) 
            # else:
            #     data, columns = self.db.fetch ("SELECT MAX(u.user_id)  FROM tbl_user u")
            #     newID = increaseID(data[0][0],"kk")
            #     log = self.create(newID, fname, lname, profilePic, email, password, profile_name)
            #     return log
        else:
            data, columns = self.db.fetch ("SELECT MAX(u.user_id)  FROM tbl_user u")
            newID = increaseID(data[0][0],"kk")
            log = self.create(newID, fname, lname, profilePic, email, password, profile_name)
            return log
                
 
    def dump(self):
        # Will dump all recipe data by returning 1 dictionary as output.
        
        data, columns = self.db.fetch ('SELECT * FROM tbl_user '
                              ' ')
        return row_as_dict(data, columns)


    def getUserById(self, user_id):
        # Will dump all recipe data by returning 1 dictionary as output.
        
        data, columns = self.db.fetch ("select * from tbl_user where user_id = '{}'".format(user_id) )
        return row_as_dict(data, columns)

    # def getFavoriteRecipe(self):

    #     data, columns = self.db.fetch ('select "" from "TBL_User"')
    #     return row_as_dict(data, columns)

    def login(self, username, password):
         data, columns = self.db.fetch ("   SELECT * \
                                            FROM tbl_user u \
                                            WHERE u.email = '{}' ".format(username)
                                        )
         if len(data) == 1:
            user = row_as_dict(data, columns)
            result = [ i for i in user]
            if result[0]['password'] == password:
                data , columns = self.db.fetch ("   SELECT u.user_id as userID \
                                                    FROM tbl_user u \
                                                    WHERE u.email = '{}' ".format(username)
                                        )
                return ({'Error': False, 'Message': data[0][0] })
            else:
                return ({'Error': True, 'Message': "Password is wrong" })
         else:
             return ({'Error': True, 'Message': "User not found" })


