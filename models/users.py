from config import *
from flask import jsonify, request

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
                content = {
                    'id':result[0],
                    'name':result[1],
                    'lastname':result[2],
                    'email':result[3],
                    'username':result[4],
                    'password':result[5]
                }
                payload.append(content)
                content = {}
            print(payload)
            return jsonify(payload)
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'information':error})