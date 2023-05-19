from config import *
from flask import jsonify, request
import datetime, secrets

class User():

    def getDatos(self):
        return {
            'id':self.id,
            'name':self.name,
            'lastname':self.lastname,
            'email':self.email,
            'username':self.username,
            'password':self.password
        }
    
    def m_consult_user(self):
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM "tblUsers"')
            rv = cursor.fetchall()
            cursor.close()
            payload = []
            content = {}
            for result in rv:
                content = {
                    'id':result[0],
                    'name':result[1],
                    'lastname':result[2],
                    'email':result[3],
                    'username':result[4],
                    'password':result[5]
                }
                # `payload.append(content)` is adding a dictionary `content` to a list `payload`. The
                # `content` dictionary contains information about a user, such as their id, name,
                # lastname, email, username, and password. This is part of a method `m_consult_user`
                # that retrieves all users from a database and returns their information in JSON
                # format.
                payload.append(content)
                content = {}
            print(payload)
            return jsonify(payload)
        except (Exception, psycopg2.DatabaseError) as error :
            return jsonify({'information':error})
        
    def m_consult_user_by_id(self):
        try:
            id = request.json['id']

            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM "tblUsers" WHERE "IdUser" = {id}')
            rv = cursor.fetchall()
            cursor.close()
            payload = []
            content = {}
            for result in rv:
                id_game = result[0]
                content = {
                    'id':id_game,
                    'name':result[1],
                    'lastname':result[2],
                    'email':result[3],
                    'username':result[4],
                    'password':result[5],
                    'token':self.create_token(id_game)
                }
                payload.append(content)
                content = {}
            print(payload)
            return jsonify(payload)
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'information':error})
        

    def create_token(self, id):
        try:
            if (self.consult_token(id)):
                self.delete_token(id)
            token = self.generate_token()
            
            cursor = connection.cursor()
            cursor.execute('INSERT INTO "tblToken" ("IdUser", "Token", "ExpiredTime") '+
                           f"VALUES ({id}, '{token}', '{self.consult_time()}')")
            cursor.connection.commit()
            cursor.close()
            
            return token
        except (Exception, psycopg2.DatabaseError) as error:
            return error
        
    def consult_token(self, id):
        try:
            cursor = connection.cursor()
            cursor.execute(f'SELECT EXISTS (SELECT * FROM "tblToken" WHERE "IdUser" = {id})')
            rv = cursor.fetchall()
            cursor.close()
            payload = rv[0][0]
            print(payload)
            return payload
        except (Exception, psycopg2.DatabaseError) as error:
            return error
        
    def delete_token(self, id):
        try:
            cursor = connection.cursor()
            cursor.execute(f'DELETE FROM "tblToken" WHERE "IdUser" = {id}')
            cursor.connection.commit()
            cursor.close()
            print('ok')
            return 'ok'
        except (Exception, psycopg2.DatabaseError) as error:
            return error
            
    def m_update_token(self):
        try:
            id_user = request.json['id']

            cursor = connection.cursor()
            cursor.execute(f'UPDATE "tblToken" SET "ExpiredTime" = \'{self.consult_time()}\' WHERE "IdUser" = {id_user};')
            cursor.connection.commit()
            cursor.close()
            print('ok')
            return jsonify({'information':'update token time'})
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'information':error})
        
    def consult_time(self):
        ahora = datetime.datetime.now()
        hora = ahora.hour
        minuto = ahora.minute + 10
        segundo = ahora.second
        if minuto >= 60:
            hora += 1
            minuto -= 60
            if hora > 24:
                hora = 1
        return f"{hora}:{self.minute_config(minuto)}:{segundo}"
    
    def minute_config(self, minute):
        if len(str(minute)) < 2:
            return f'0{minute}'
        else:
            return minute
    
    def generate_token(self):
        token = secrets.token_hex(32)
        return token