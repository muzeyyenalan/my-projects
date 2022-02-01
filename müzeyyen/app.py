from flask import Flask


app=Flask(__name__)

@app.route('/')
def index():
    return'<h1> Ana Sayfa </h1>'

@app.route('/user/<name>')
def user(name):
    return'<h1> Merhaba, {}</h1>' .format(name)
    
    
    
if __name__=='__main__':
    app.run(debug=True)