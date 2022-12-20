from flask import Flask, request, jsonify, current_app, session
import pymysql
from flask_cors import *


app = Flask(__name__)
CORS(app, resources=r'*')
app.config['DBHOST'] = 'foodrm.cgnnqocprf5c.us-east-1.rds.amazonaws.com'
app.config['DBUSER'] = 'admin'
app.config['DBPWD'] = '1q2w3e4r'
app.config['DBNAME'] = 'apidb'
app.config['DBPORT'] = 3306
app.config['SECRET_KEY'] = 'test123ASLDFJKLJK1JKL23JKLd123b'

response_template = {'code':200, 'msg':'',  'data':''}


@app.route('/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        db = pymysql.connect(
                host = current_app.config.get('DBHOST'),
                port = current_app.config.get('DBPORT') ,
                user = current_app.config.get('DBUSER'),
                password = current_app.config.get('DBPWD'),
                database = current_app.config.get('DBNAME')
                )
        cursor = db.cursor()
        data = request.get_json()
        email = data['email']
        password = data['password']
        sql = "select * from user where email ='"+ email + "' and password='"+ password +"'"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results)==1:
                session['username'] = email
                db.close()
                return jsonify({'code':200, 'msg':'user login successfully',  'data':{'email':email} })
            else:
                return jsonify({'code':404, 'msg':'ID and password not matched, or ID not exists!',  'data':''})
        except Exception as e:
            print('exception - {}'.format(str(e)))
            db.rollback()
            return jsonify({'code':502, 'msg':'Exception occuried, please retry!',  'data':''})
      

@app.route('/auth/signup', methods=['POST'])
def register():
    if request.method == 'POST':
        db = pymysql.connect(
                host = current_app.config.get('DBHOST'),
                port = current_app.config.get('DBPORT'),
                user = current_app.config.get('DBUSER'),
                password = current_app.config.get('DBPWD'),
                database = current_app.config.get('DBNAME')
                )

        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        
        
        querysql = "select * from user where email ='"+ email +"' and password='"+ password +"'"
        try :    
            cursor = db.cursor()
            cursor.execute(querysql)
            results = cursor.fetchall()
            if len(results)==1:
                db.close()
                return jsonify({'code':500, 'msg':'user exists already, please check',  'data': '' })
            else:
                sql = "INSERT INTO user (username,email, password ) VALUES ('" + username +"', '" + email + "', '" + password + "')"  
                print(sql)
                cursor.execute(sql)
                db.commit()
                db.close()
                
                return jsonify({'code':200, 'msg':'user is created successfully',  'data': {'username':username} })
        except Exception as e:
            print('exception - {}'.format(str(e)))
            db.rollback()
            db.close()
            return jsonify({'code':502, 'msg':'Exception occuried, please retry!',  'data':''})
      
@app.route('/auth/logout')
def logout():
    session.pop('username', None)
    return jsonify({'code':200, 'msg':'user logout successfully',  'data':'' })

@app.route('/auth/hello', methods = ['GET'])
def gethello() :
    if request.method == 'GET' :
        return jsonify({'data ' : 'hello '})
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
