from flask import Flask, request
from flask import render_template, redirect, url_for, request, g

from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET', 'POST'])
def get_score():
    if request.method == 'POST':
        department_name = request.form['department_name']
        position_title  = request.form['position_title']
        
        # TODO: add some server side validation         
        """
        completion = validate(department_name, position_title)
        if not completion:
            # do stuff
        else:
            # do some stuff
        """
        
        # TODO: sql magic
        # this will look something similar to below
        conn = e.connect()
        query = conn.execute("select * from salaries where Department='%s' and position='%s'" %(department_name.upper(), position_title.upper()))
        
        salary = query.cursor.fetchone()[3]
        print(salary)
        return render_template('score.html', salary=salary)    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

"""
class Departments_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct DEPARTMENT from salaries")
        return {'departments': [i[0] for i in query.cursor.fetchall()]}

class Departmental_Salary(Resource):
    def get(self, department_name):
        conn = e.connect()
        query = conn.execute("select * from salaries where Department='%s'"%department_name.upper())
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
    #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient
       
api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
api.add_resource(Departments_Meta, '/departments')
"""
