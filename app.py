from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Afaq Anwar - Portfolio</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="margin:0; padding:0; font-family: Arial, sans-serif; background:#ffffff; text-align:center;">
        
        <div style="padding-top:60px; padding-bottom:40px;">
            <img src="https://github.com/afaqanwarafghan.png" 
                 style="width:220px; height:220px; border-radius:50%; border:4px solid black; object-fit:cover;">

            <h1 style="font-size:36px; margin-top:25px; margin-bottom:10px; color:#111;">Welcome to My Website</h1>
            
            <h2 style="font-size:24px; color:#333; margin-top:10px;">I am Afaq Anwar</h2>
            
            <p style="font-size:16px; color:#555; margin-top:15px;">Web Developer</p>
            
            <a href="#" style="display:inline-block; margin-top:25px; background:#0d6efd; color:white; padding:12px 30px; text-decoration:none; border-radius:25px; font-weight:bold; font-size:16px;">Hire Me</a>
            
            <div style="margin-top:40px;">
                <h3 style="font-size:20px; color:#222;">My Skills</h3>
                <p style="font-size:16px; color:#555;">HTML | CSS | Python | Flask</p>
            </div>
        </div>

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
