from src.DBHelper import DBHelper
from src.helper_functions import *


class Recipe:
    def __init__(self):
        self.db = DBHelper()


    # create before add recipe
    def create (self, recipeID, title, description, photoRecipe, author, serve, prep_time, cook_time, yield2, tag, ingredients, steps):
        self.db.execute ("INSERT INTO tbl_recipe \
                          VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(recipeID, title, description, photoRecipe, author, serve, prep_time, cook_time, yield2, tag, ingredients, steps))
        
        return {'Is Error': False, 'Error Message': ""}

    #add recipe 
    def addRecipe(self, title, description, photoRecipe, author, serve, prep_time, cook_time, yield2, tag, ingredients, steps):
        data, columns = self.db.fetch ("SELECT MAX(rp.recipe_id) FROM tbl_recipe rp")
        newID = increaseID(data[0][0],"rp")
        log = self.create(newID, title, description, photoRecipe, author, serve, prep_time, cook_time, yield2, tag, ingredients, steps)
        return log
 
    #get all recipe
    def dump(self):
        data, columns = self.db.fetch ('SELECT r.recipe_id, r.title, r.serve, r.photo_recipe, r.prep_time, r.cook_time'
                              '  FROM tbl_recipe r'
                              ' ')
        return row_as_dict(data, columns)

    def tagAuto(self):
        data, columns = self.db.fetch ('SELECT tagName'
                              '  FROM tbl_tag'
                              ' ')
        return row_as_dict(data, columns)

    #get recipe by id (views)
    def getReceipeByID(self,id):
        # Will dump all recipe data by returning 1 dictionary as output.
        
        data, columns = self.db.fetch ("SELECT r.recipe_id, r.title, r.description, r.serve, r.photo_recipe, r.author, usr.profile_name, usr.profile_pic ,r.prep_time"
                              " , r.cook_time, r.yield, r.ingredients, r.steps "
                              " FROM tbl_recipe r JOIN tbl_user usr ON r.author = usr.user_id WHERE r.recipe_id = '{}' ".format(id))
        return row_as_dict(data, columns)

    #update recipe 
    def updateReceipeByID(self, recipe_id, title, description, photoRecipe, serve, prep_time, cook_time, yield2, tag, ingredients, steps):

        data, columns = self.db.fetch ("SELECT * FROM tbl_recipe WHERE recipe_id = '{}' ".format(recipe_id))

        if len(data) > 0:
            self.db.execute("UPDATE tbl_recipe SET                \
                                    title = '{}',                 \
                                    description = '{}',           \
                                    photo_recipe = '{}',          \
                                    serve = '{}',                 \
                                    prep_time = '{}',             \
                                    cook_time = '{}',             \
                                    yield = '{}',                 \
                                    tag = '{}',                   \
                                    ingredients = '{}',           \
                                    steps = '{}'                  \
                            WHERE recipe_id = '{}'".format(title, description, photoRecipe, serve, prep_time, cook_time, yield2, tag, ingredients, steps,recipe_id))     
            return {'Is Error': False, 'Error Message': ""}
        else:
            return {'Is Error': True, 'Error Message': "Recipe ID '{}' not found. Cannot Update.".format(recipe_id)}

    #delete recipe
    def delReceipeByID(self,recipe_id):
        data, columns = self.db.fetch ("SELECT * FROM tbl_recipe WHERE recipe_id = '{}' ".format(recipe_id))
        if len(data) > 0:
            self.db.execute ("DELETE FROM tbl_recipe WHERE recipe_id = '{}' ".format(recipe_id))
        else:
            return {'Is Error': True, 'Error Message': "Recipe ID '{}' not found. Cannot Delete".format(recipe_id)}
        return {'Is Error': False, 'Error Message': ""}


    #add favorite recipe
    def createFav(self,fav_id, user_id, recipe_id):
        self.db.execute ("INSERT INTO tbl_favorite \
                          VALUES ('{}','{}','{}')".format(fav_id, user_id, recipe_id))
        
        return {'Is Error': False, 'Error Message': ""}

    
    def addFavoriteRecipe(self, recipe_id, user_id):
        data, columns = self.db.fetch ("SELECT MAX(fav.fav_id)  FROM tbl_favorite fav")
        newID = increaseID(data[0][0],"fav")
        log = self.createFav(newID, recipe_id, user_id)
        return log


    def getFavoriteRecipe(self):
        # Will dump all recipe data by returning 1 dictionary as output.
        
        data, columns = self.db.fetch ("select fav.fav_id, r.recipe_id, r.title, r.photo_recipe ,r.serve from tbl_recipe r join tbl_favorite fav on r.recipe_id = fav.recipe_id ")
        return row_as_dict(data, columns)


    def getFavoriteRecipeByAuthor(self,user_id):
        # Will dump all recipe data by returning 1 dictionary as output.
        
        data, columns = self.db.fetch ("select fav.fav_id, r.recipe_id, r.title, r.photo_recipe ,r.serve "
                                        " from tbl_recipe r join tbl_favorite fav on r.recipe_id  = fav.recipe_id "
                                        " join tbl_user usr on fav.user_id = usr.user_id where fav.user_id = '{}'".format(user_id))
        return row_as_dict(data, columns)

    #delete favorite
    def delFavoriteRecipe(self,fav_id,recipe_id):
        data, columns = self.db.fetch ("SELECT * FROM tbl_favorite WHERE fav_id = '{}' and recipe_id = '{}'".format(fav_id,recipe_id))
        if len(data) > 0:

            self.db.execute ("DELETE FROM tbl_favorite WHERE fav_id = '{}' and recipe_id = '{}' ".format(fav_id,recipe_id))

        else:
            return {'Is Error': True, 'Error Message': "Favorite ID '{}' not found. Cannot Delete".format(fav_id,recipe_id)}

        return {'Is Error': False, 'Error Message': ""}


    def getMyRecipe(self,user_id):

        data, columns = self.db.fetch ("SELECT r.recipe_id, r.title, r.description, r.serve, r.photo_recipe, r.author  "                     
	                                    "FROM tbl_recipe r WHERE r.author = '{}' ".format(user_id))
                                        
        return row_as_dict(data, columns)

    def getTag(self):

        data, columns = self.db.fetch ("SELECT r.recipe_id, r.title, r.description, r.serve, r.photo_recipe, r.author  "                     
	                                    "FROM tbl_recipe r WHERE r.author = '{}' ".format(user_id))
                                        
        return row_as_dict(data, columns)

