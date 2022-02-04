from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.modelos.modelRecipes import Recipes
from datetime import datetime


@app.route( '/dashboard', methods=["GET"] )
def desployDashboard():
    if "id" not in session:
        return redirect('/')

    recipeList = Recipes.getRecipeList()
    variables = [session["id"], session["first_name"]]
    return render_template( "dashboard.html", recipeList=recipeList, variables=variables)


@app.route( '/recipes/new', methods=["GET"] )
def createRecipe():
    return render_template( "new.html" )


@app.route( '/new', methods=["POST"] )
def createRecipe_P():
    if not Recipes.verifyRecipes( request.form ):
        return redirect( '/recipes/new' )

    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "date_on" : request.form["date_on"],
        "under" : request.form["under"],
        "key_likes" : 0,
        "likes" : 0,
        "created_at" : datetime.today(),
        "updated_at" : datetime.today(),
        "user_id" : session["id"]
    }
    Recipes.addRecipe( data )
    return redirect( "/dashboard")


@app.route( '/recipes/<idRecipe>', methods=["GET"] )
def showRecipe( idRecipe ):
    data = {
        "id" : idRecipe
    }
    recipe = Recipes.getRecipe( data )
    variables = [ session["id"], session["first_name"] ]
    return render_template( "show.html", recipe=recipe, variables=variables )


@app.route( '/recipes/edit/<idRecipe>', methods=["GET"] )
def editRecipe( idRecipe ):
    data = {
        "id" : idRecipe
    }
    recipe = Recipes.getRecipe( data )
    return render_template( "edit.html", recipe=recipe )


@app.route( '/recipes/edit/<idRecipe>', methods=["POST"] )
def editRecipe_P( idRecipe ):
    if not Recipes.verifyRecipes( request.form ):
        return redirect(url_for( 'editRecipe', idRecipe=idRecipe  ))

    data = {
        "id" : idRecipe,
        "name" : request.form["name"],
        "description" : request.form["description"],
        "date_on" : request.form["date_on"],
        "under" : request.form["under"],
        "instruction" : request.form["instruction"],
        "updated_at" : datetime.today()
    }
    Recipes.editRecipe( data )
    return redirect( "/dashboard")


@app.route( '/recipes/<idRecipe>/destroy', methods=["POST"] )
def destroyRecipe( idRecipe ):
    data = {
        "id": idRecipe
    }
    Recipes.deleteRecipe( data )
    return redirect( '/dashboard' )


@app.route( '/recipes/<idRecipe>/like', methods=["POST"] )
def likeShow( idRecipe ):
    data = {
        "id": idRecipe
    }
    recipe = Recipes.getRecipe(data)
    if recipe["key_likes"] == 0:
        recipe["likes"] += 1
        data["key_likes"] = 1
    else:
        recipe["likes"] -= 1
        data["key_likes"] = 0

    data["likes"] = recipe["likes"]
    Recipes.likeRecipe( data )
    return redirect( '/dashboard' )