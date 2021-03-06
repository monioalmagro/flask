from flask import Flask
from flask import render_template, request

app = Flask(__name__)

#####################CALLBACKS
@app.before_request
def before_request():
    print("antes de la petición")

@app.after_request
def after_request(response):
    print("Despúes de la petición")
    return response
###########################

@app.route('/')
def index():
    name = 'Emi'
    course = 'Python web'
    is_premiun = False
    courses = ['Python', 'Ruby','Java']


    return render_template('index.html', username=name,
                                        coursename= course,
                                        is_premiun=is_premiun,
                                        courses=courses)

@app.route('/usuario/<last_name>/<username>/<int:age>')# para trabajar con parametro con forma dinamica
def usuario(username,last_name,age):
    return 'Hola '+ last_name +'  '+ username + ' '+ str(age)

@app.route('/datos')
def datos():
    nombre = request.args.get('nombre','') #args es un diccionario por eso usamos .get()
    curso = request.args.get('curso','')
    print(request.args)
    return 'Listado de datos : ' + nombre +'  '+ curso

@app.route('/about')
def about():
    print("Estamos en el about")
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug =  True, port=9000)

