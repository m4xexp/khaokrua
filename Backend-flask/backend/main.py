from flask import Flask, jsonify, request, Response
from src import Recipe, User, Search
from src import helper_functions

from flask_cors import CORS, cross_origin


r = Recipe.Recipe()
user = User.User()
hf = helper_functions
s = Search.Search()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# CORS(app)

data = [
        {
            "recipeid": 1,
            "title": "Django",
            "description": "",
            "time" : "1",
            "Author" : "XXX",
            "src" : "https://d12man5gwydfvl.cloudfront.net/wp-content/uploads/2019/06/shutterstock_430308484.jpg"
        },
        {
            "recipeid": 2,
            "title": "Django",
            "description": "",
            "time" : "2",
            "Author" : "XXX",
            "src" : "https://d12man5gwydfvl.cloudfront.net/wp-content/uploads/2019/06/shutterstock_430308484.jpg"
        },
        {
            "recipeid": 3,
            "title": "Django",
            "description": "",
            "time" : "3",
            "Author" : "YYY",
            "src" : "https://d12man5gwydfvl.cloudfront.net/wp-content/uploads/2019/06/shutterstock_430308484.jpg"
        },
        {
            "recipeid": 4,
            "title": "Django",
            "description": "",
            "time" : "4",
            "Author" : "YYY",
            "src" : "https://d12man5gwydfvl.cloudfront.net/wp-content/uploads/2019/06/shutterstock_430308484.jpg"
        }
    ]


@app.route('/')
@cross_origin()
def home():
    return "Hello World"

@app.route('/api/addrecipe', methods=['POST'])
@cross_origin()
def add_recipe():
    title = request.form["title"]
    description = request.form["description"]
    photoRecipe = request.form["photo_recipe"]
    serve = request.form["serve"]
    author = request.form["author"]
    prep_time = request.form["prep_time"]
    cook_time = request.form["cook_time"]
    tag = request.form["tag"]
    yield2 = request.form["yield2"]
    ingredients = request.form["ingredients"]
    steps = request.form["steps"]
    log = r.addRecipe(title, description, photoRecipe, serve, author, prep_time, cook_time, tag, yield2, ingredients, steps)
    return jsonify(log)

@app.route('/api/recipe', methods=['GET'])
@cross_origin()
def get_recipe_home():
    result = r.dump()
    # data = hf.contoJson(result)
    print(result)
    return jsonify(result)  # Return web frameworks information\

@app.route('/api/recipe/<id>', methods=['GET'])
@cross_origin()
def get_recipe_by_id(id):
    result = r.getReceipeByID(id)
    print(result)
    return jsonify(result)  # Return web frameworks information         

@app.route('/api/recipe/edit/<recipe_id>', methods=['PUT'])
@cross_origin()
def update_recipe_by_id(recipe_id):
    # recipe_id = request.form["recipe_id"]
    newTitle = request.form["title"]
    newDescription = request.form["description"]
    newPhotoRecipe = request.form["photo_recipe"]
    newServe = request.form["serve"]
    result = r.updateReceipeByID(recipe_id, newTitle, newDescription, newPhotoRecipe, newServe)
    print(result)
    return jsonify(result)  # Return web frameworks information 


@app.route('/api/recipe/<recipe_id>', methods=['DELETE'])
@cross_origin()
def del_recipe_by_id(recipe_id):
    result = r.delReceipeByID(recipe_id)
    print(result)
    return jsonify(result)  # Return web frameworks information 


@app.route('/api/recipe/detail', methods=['GET'])
@cross_origin()
def get_api():
    result = r.getRecipeDetail()
    print(result)
    return jsonify(result)  # Return web frameworks information


@app.route('/api/user', methods=['GET'])
@cross_origin()
def get_user_info():
    result = user.dump()
    print(result)
    return jsonify(result)  # Return web frameworks information


@app.route('/api/user/<user_id>', methods=['GET'])
@cross_origin()
def get_user_by_id(user_id):
    result = user.getUserById(user_id)
    print(result)
    return jsonify(result)  # Return web frameworks information


@app.route('/api/favorite', methods=['GET'])
@cross_origin()
def get_favorite_recipe():
    result = r.getFavoriteRecipe()
    print(result)
    return jsonify(result)  # Return web frameworks information

@app.route('/api/favorite/<user_id>', methods=['GET'])
@cross_origin()
def get_favorite_recipe_by_author(user_id):
    result = r.getFavoriteRecipeByAuthor(user_id)
    print(result)
    return jsonify(result)  # Return web frameworks information

@app.route('/api/addfavorite/<recipe_id>/<user_id>', methods=['POST'])
@cross_origin()
def add_favorite_recipe(recipe_id,user_id):
    log = r.addFavoriteRecipe( recipe_id, user_id)
    return jsonify(log)


@app.route('/api/favorite/<fav_id>/<recipe_id>', methods=['DELETE'])
@cross_origin()
def del_favorite_recipe(fav_id,recipe_id):
    result = r.delFavoriteRecipe(fav_id,recipe_id)
    print(result)
    return jsonify(result)  # Return web frameworks information 


@app.route('/api/myrecipe/<user_id>', methods=['GET'])
@cross_origin()
def get_my_recipe(user_id):
    result = r.getMyRecipe(user_id)
    print(result)
    return jsonify(result)  # Return web frameworks information


@app.route('/api/search/<keyword>', methods=['GET'])
@cross_origin()
def search(keyword):
    result = s.search(keyword)
    print(result)
    return jsonify(result)  # Return web frameworks information


@app.route('/api/search/keyword', methods=['GET'])
@cross_origin()
def fetch():
    result = s.fetch()
    print(result)
    return jsonify(result)  # Return web frameworks information

# @app.route('/api/tag', methods=['GET'])
# def getTag():
#     result = r.
#     return jsonify(log)

@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():
    username = request.form["username"]
    password = request.form["password"]
    log = user.login(username,password)
    return jsonify(log)

@app.route('/api/register', methods=['POST'])
@cross_origin()
def regiser():
    fname = request.form["fname"]
    lname = request.form["lname"]
    profilePic = request.form["profilePic"]
    email = request.form["email"]
    password = request.form["password"]
    profile_name = request.form["profile_name"]
    log = user.register(fname, lname, profilePic, email, password, profile_name)
    return jsonify(log)
    

if __name__ == "__main__":
    app.run(debug=True)