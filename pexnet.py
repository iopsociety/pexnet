from bottle import route, run, template, request
import sqlite3

queries = {
    'tasks': 'SELECT id, task, desirability_rating, empowerment_rating FROM tasks %s order by id',
    'goods': 'SELECT id, good, description, price FROM goods %s order by id', 
    'my_goods': 'SELECT id, good_id, quantity FROM my_goods %s order by id',
    'my_tasks': 'SELECT id, task_id, hours FROM my_tasks %s order by id' }

headers_to_use = {
    'goods': ['id', 'good', 'description', 'price'],
    'tasks': ['id', 'task', 'desirability_rating', 'empowerment_rating'],
    'my_goods': ['id', 'good_id', 'quantity'], 
    'my_tasks': ['id', 'task_id', 'hours'] }

def get_data(f, q):
    t = []
    conn = sqlite3.connect('pexnet.db')
    c = conn.cursor()
    search_query = '' 
    if q != '' and q is not None:
        search_query = ' WHERE %s like "%%%s%%" ' % (f[:-1], q)
    for r in c.execute(queries[f] % search_query):
        if f == 'tasks':
            t.append({'id': r[0], 'task': r[1], 'desirability_rating': r[2], 'empowerment_rating': r[3]})
        elif f == 'goods':
            t.append({'id': r[0], 'good': r[1], 'description': r[2], 'price': r[3]})
        elif f == 'my_goods':
            t.append({'id': r[0], 'good_id': r[1], 'quantity': r[2]})
        elif f == 'my_tasks':
            t.append({'id': r[0], 'task_id': r[1], 'hours': r[2]})
    c.close() 
    conn.close()
    return t

def get_my_data(i):
    t = i.replace('_', ' ')
    return template('templates/get_all_data', rows=get_data(i, ''), headers=headers_to_use[i], title=t)

def add_my_data(d):
    conn = sqlite3.connect('pexnet.db')
    c = conn.cursor()
    k = {} 
    if request.forms.get('submit','').strip():
        for i in request.forms.decode():
            if i != 'submit':
                if d == 'goods': 
                    c.execute('''INSERT INTO my_goods (good_id, quantity) VALUES (?, ?)''', (int(i), float(request.forms.get(i, '').strip())))
                elif d == 'tasks': 
                    c.execute('''INSERT INTO my_tasks (task_id, hours) VALUES (?, ?)''', (int(i), float(request.forms.get(i, '').strip())))
    conn.commit()
    c.close()
    conn.close()
    return template('templates/get_all_data', rows=get_data(d, ''), headers=headers_to_use[d], title=d)

def add_content(v):
    conn = sqlite3.connect('pexnet.db')
    c = conn.cursor()
    if v.has_key('good'):
        c.execute("INSERT INTO goods (good, description) VALUES (?,?)", (v['good'],v['description']))
    if v.has_key('task'):
        c.execute("INSERT INTO tasks (task) VALUES (?)", (v['task'],))
    conn.commit()
    c.close()
    conn.close()

def add_datum(i):
    v = {}
    if request.forms.get('submit','').strip():
        if i == 'goods':
            good = request.forms.get('good', '').strip()
            description = request.forms.get('description', '').strip()
            v = {'good': good, 'description': description}
        elif i == 'tasks':
            task = request.forms.get('task', '').strip()
            v = {'task': task}
        add_content(v)
        return template('templates/get_all_data', rows=get_data(i, ''), headers=headers_to_use[i], title=i)
    else:
        return template('templates/add_' + i) 

@route('/add_goods', method='POST')
@route('/add_goods')
def add_good():
    return add_datum('goods')

@route('/add_tasks', method='POST')
@route('/add_tasks')
def add_task():
    return add_datum('tasks')

@route('/add_my_tasks', method='POST')
@route('/add_my_tasks')
def add_my_tasks():
    return add_my_data('tasks')

@route('/add_my_goods', method='POST')
@route('/add_my_goods')
def add_my_goods():
    return add_my_data('goods')

@route('/my_tasks')
def my_tasks():
    return get_my_data('my_tasks')

@route('/my_goods')
def my_goods():
    return get_my_data('my_goods')

@route('/') 
@route('/<fn>')
@route('/<fn>/', method='GET')
def main(fn='tasks'):
    q = request.GET.get('q')
    return template('templates/get_all_data', rows=get_data(fn, q), headers=headers_to_use[fn], title=fn) 

run(host='localhost', port=8085, debug=True)
