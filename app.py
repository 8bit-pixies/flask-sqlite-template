from flask import Flask, render_template, request
from sqlalchemy import create_engine

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)

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

