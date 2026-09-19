from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Afaq Website</title></head>
    <body style="text-align:center; font-family:Arial; padding-top:40px; background:white;">
        <img src="https://github.com/afaqanwarafghan.png" 
             style="width:200px; height:200px; border-radius:50%; border:5px solid black;">
        <h1>Welcome to My Website</h1>
        <h2>I am Afaq Anwar Afghan</h2>
        <p>Web Developer | My Website is LIVE!</p>
        <br>
        <a href="#" style="background:blue; color:white; padding:12px 25px; text-decoration:none; border-radius:25px; font-weight:bold;">Hire Me</a>
        <br><br>
        <h3>My Skills</h3>
        <p>HTML | CSS | Python | Flask</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
