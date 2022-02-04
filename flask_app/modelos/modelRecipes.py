import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class Recipes:
    def __init__( self, id, name, description, instruction, date_on, under, key_likes, likes, created_at, update_at, user_id ):
        self.id = id
        self.name = name
        self.description = description
        self.instruction = instruction
        self.date_on = date_on
        self.under = under
        self.key_likes = key_likes
        self.likes = likes
        self.created_at = created_at
        self.update_at = update_at
        self.user_id = user_id

    @classmethod
    def addRecipe( cls, data ):
        query1 = "ALTER TABLE recipes AUTO_INCREMENT = 1;"
        connectToMySQL( "recetas_db" ).query_db( query1 )
        query2 = "INSERT INTO recipes(name, description, instruction, date_on, under, key_likes, likes, created_at, updated_at, user_id) VALUES(%(name)s, %(description)s, %(instruction)s, %(date_on)s, %(under)s, %(likes)s, %(key_likes)s, %(created_at)s, %(updated_at)s, %(user_id)s);"
        result = connectToMySQL( "recetas_db" ).query_db( query2, data )
        return result
    
    @classmethod
    def getRecipe( cls, data ):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL( "recetas_db" ).query_db( query, data )
        if len( result ) > 0:
            return result[0]
        else:
            return None
    
    @classmethod
    def getRecipeList( cls ):
        query = "SELECT * FROM recipes;"
        result = connectToMySQL( "recetas_db" ).query_db( query )
        return result

    @classmethod
    def editRecipe( cls, data ):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date_on = %(date_on)s, under = %(under)s, updated_at = %(updated_at)s WHERE recipes.id = %(id)s;"
        connectToMySQL( "recetas_db" ).query_db( query, data )
    
    @classmethod
    def deleteRecipe( cls, data ):
        query = "DELETE FROM recipes WHERE recipes.id = %(id)s;"
        connectToMySQL( "recetas_db" ).query_db( query, data )
    
    @classmethod
    def likeRecipe( cls, data ):
        query = "UPDATE recipes SET key_likes = %(key_likes)s, likes = %(likes)s WHERE recipes.id = %(id)s;"
        connectToMySQL( "recetas_db" ).query_db( query, data )

    @classmethod
    def verifyRecipes( cls, data ):
        is_valid = True

        if len( data["name"] ) < 3:
            flash( "El título debe contener al menos 3 letras", "show" )
            is_valid = False
        
        if len( data["description"] ) < 3:
            flash( "La descripcion debe contener al menos 3 letras", "show" )
            is_valid = False
        
        if len( data["instruction"] ) < 3:
            flash( "Las instrucciones debe contener al menos 3 letras", "show" )
            is_valid = False

        return is_valid