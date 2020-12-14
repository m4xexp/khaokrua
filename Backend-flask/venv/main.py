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

@app.route('/')
@cross_origin()
def home():
    return "Hello World"

@app.route('/api/addrecipe', methods=['POST'])
@cross_origin()
def add_recipe():
    print(request.form)
    title = request.form["title"]
    description = request.form["description"]
    photoRecipe = request.form["photo_recipe"]
    author = request.form["author"]
    serve = request.form["serve"]
    prep_time = request.form["prep_time"]
    cook_time = request.form["cook_time"]
    tag = request.form["tag"]
    yield2 = request.form["yield2"]
    ingredients = request.form["ingredients"]
    steps = request.form["steps"]
    log = r.addRecipe(title, description, photoRecipe, author, serve, prep_time, cook_time, yield2, tag, ingredients, steps)
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

@app.route('/api/recipe/edit', methods=['PUT'])
@cross_origin()
def update_recipe_by_id():
    recipe_id = request.form["recipe_id"]
    title = request.form["title"]
    description = request.form["description"]
    photoRecipe = request.form["photo_recipe"]
    serve = request.form["serve"]
    prep_time = request.form["prep_time"]
    cook_time = request.form["cook_time"]
    tag = request.form["tag"]
    yield2 = request.form["yield2"]
    ingredients = request.form["ingredients"]
    steps = request.form["steps"]
    log = r.updateReceipeByID(recipe_id, title, description, photoRecipe, serve, prep_time, cook_time, yield2, tag, ingredients, steps)
    return jsonify(log)


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