from crypt import methods
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html',submited=False)
    if request.method == 'POST':
        return render_template('contact.html',submited=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0")