from config import *
from flask import jsonify, request

class Games():

    def getDatos(self):
        return {
            'id':self.id,
            'console':self.console,
            'game':self.game,
            'year':self.year,
            'gender':self.gender,
            'publisher':self.publisher,
            'north america':self.nort_america,
            'europe':self.europe,
            'japan':self.japan,
            'rest of world':self.rest_of_world,
            'global':self.global_game
        }
    
    def m_consult_games(self):
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM "tblGames"')
            rv = cursor.fetchall()
            cursor.close()
            payload = []
            content = {}
            for result in rv:
                content = {
                    'id':result[0],
                    'console':result[1],
                    'game':result[2],
                    'year':result[3],
                    'gender':result[4],
                    'publisher':result[5],
                    'north_america':result[6],
                    'europe':result[7],
                    'japan':result[8],
                    'rest_of_world':result[9],
                    'global':result[10]
                }
                payload.append(content)
                content = {}
            print(payload)
            return jsonify(payload)
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'information':error})
    
    def m_consult_game_by_id(self):
        try:
            id_game = request.json['id']

            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM "tblGames" WHERE "IdGame" = {id_game}')
            rv = cursor.fetchall()
            cursor.close()
            payload = []
            content = {}
            for result in rv:
                content = {
                    'id':result[0],
                    'console':result[1],
                    'game':result[2],
                    'year':result[3],
                    'gender':result[4],
                    'publisher':result[5],
                    'north_america':result[6],
                    'europe':result[7],
                    'japan':result[8],
                    'rest_of_world':result[9],
                    'global':result[10]
                }
                payload.append(content)
                content = {}
            print(payload)
            return jsonify(payload)

        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'infomation':error})

    def m_create_game(self):
        try:
            console = request.json['console']
            game = request.json['game']
            year = request.json['year']
            gender = request.json['gender']
            publisher = request.json['publisher']
            north_america = request.json['north_america']
            europe = request.json['europe']
            japan = request.json['japan']
            rest_of_world = request.json['rest_of_world']
            global_game = request.json['global']

            cursor = connection.cursor()
            cursor.execute('INSERT INTO "tblGames" ("Console", "Game", "Year", "Genre", "Publisher", "North America", "Europe", "Japan", "Rest of World", "Global" ) '+
                           f"VALUES ('{console}', '{game}', '{year}', '{gender}', '{publisher}', '{north_america}', '{europe}', '{japan}', '{rest_of_world}', '{global_game}')")
            cursor.connection.commit()
            cursor.close()

            return jsonify({'information':'created successfully'})
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'information':error})
        
    def m_update_game(self):
        try:
            id_game = request.json['id']
            console = request.json['console']
            game = request.json['game']
            year = request.json['year']
            gender = request.json['gender']
            publisher = request.json['publisher']
            north_america = request.json['north_america']
            europe = request.json['europe']
            japan = request.json['japan']
            rest_of_world = request.json['rest_of_world']
            global_game = request.json['global']

            cursor = connection.cursor()
            cursor.execute('UPDATE "tblGames" SET '+
                           f'"Console" = \'{console}\', '+
                           f'"Game" = \'{game}\', '+
                           f'"Year" = \'{year}\', '+
                           f'"Genre" = \'{gender}\', '+
                           f'"Publisher" = \'{publisher}\', '+
                           f'"North America" = \'{north_america}\', '+
                           f'"Europe" = \'{europe}\', '+
                           f'"Japan" = \'{japan}\', '+
                           f'"Rest of World" = \'{rest_of_world}\', '+
                           f'"Global" = \'{global_game}\' '+
                           f'WHERE "IdGame" = {id_game}')
            cursor.connection.commit()
            cursor.close()

            return jsonify({'information':'updated successfully'})
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'information':error})
        
    def m_delete_game(self):
        try:
            id_game = request.json['id']

            cursor = connection.cursor()
            cursor.execute(f'DELETE FROM "tblGames" WHERE "IdGame" = {id_game}')
            cursor.connection.commit()
            cursor.close()

            return jsonify({'information':'deleted successfully'})
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'information':error})