from application import app, db
from application.models import Todos

@app.route('/add')
def add():
    new_todo = Todos(name="New Todo")
    db.session.add(new_todo)
    db.session.commit()
    return "Added new todo to database"

@app.route('/read')
def read():
    all_todo = Todos.query.all()
    todo_string = ""
    for todo in all_todo:
        todo_string += "<br>"+ todo.name
    return todo_string

@app.route('/update/<name>/<num>')
def update(name, num):
    wot = num
    last_todo = Todos.query.get(wot)
    last_todo.name = name
    db.session.commit()
    return last_todo.name

@app.route('/update_all/<update>')
def all_status(update):
    all_todo = Todos.query.all()
    todo_status = ''
    status = ''
    for todo in all_todo:
        
        if update == 'incomplete':
            status = 'Incomplete'
            todo_status += '<br>' + todo.name + ' ' + status
        elif update == 'done':
            status = 'Done'
            todo_status += '<br>' + todo.name + ' ' + status
    return todo_status

@app.route('/delete/<name>')
def delete(name):
    todo = Todos.query.filter_by(name=name).first()
    if todo is not None:
        db.session.delete(todo)
        db.session.commit()
        return 'Todo removed'
    else:
        return 'Todo not found!'








    