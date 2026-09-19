from flask import Flask, request

app = Flask(__name__)
contacts = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        contacts.append(request.form.get("client_msg"))
        return "<h1 style='text-align:center; margin-top:100px;'>Shukria! Me jald rabta karunga! <br><a href='/'>Wapas jao</a></h1>"

    return """
    <html>
    <head><title>Afaq Anwar- Web Developer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body{font-family:Arial; margin:0; background:#f4f4f4;}
        .header{background:#111; color:white; padding:40px; text-align:center;}
        .header h1{margin:0; color:#00ff88;}
        .skills{display:flex; justify-content:center; flex-wrap:wrap; gap:15px; padding:30px;}
        .card{background:white; width:250px; padding:20px; border-radius:12px; box-shadow:0 2px 10px #ccc; text-align:center;}
        .card h3{color:green;}
        .contact{background:white; width:350px; margin:20px auto; padding:20px; border-radius:12px; text-align:center;}
        input, textarea{width:90%; padding:10px; margin:8px; border-radius:6px; border:1px solid #ccc;}
        button{background:#00c853; color:white; padding:12px 25px; border:none; border-radius:6px; font-size:16px; cursor:pointer;}
    </style>
    </head>
    <body>
        <div style="display:flex; align-items:center; justify-content:center; gap:40px; padding:50px 20px; background:white; flex-wrap:wrap;">
     <img src="/static/afaq.jpg"
    <div>
    <p style="color:#2a5bd7; font-weight:bold;">Welcome to My Website!</p>
    <h1 style="font-size:38px; margin:10px 0;">Let's Build Something Amazing Together</h1>
    <p>I'm Afaq Anwar— Web Developer</p>
    <a href="#contact" style="background:#2a5bd7; color:white; padding:10px 25px; border-radius:25px; text-decoration:none; display:inline-block; margin-top:10px;">Hire Me</a>
  </div>
</div>
        <h2 style="text-align:center; margin-top:20px;">My Skills / My Work</h2>
        <div class="skills">
            <div class="card">
                <h3>🌐 Website developer</h3>
                <p> Full stack developer - Front + Back</p>
                
            </div>
            <div class="card">
                <h3>🐍 Python work</h3>
                <p>Python Script, Automation, Bot</p>
                
            </div>
            <div class="card">
                <h3>🎨 Logo / Designing</h3>
                <p>Any type of designing work</p>
                
            </div>
        </div>

        <div class="contact">
            <h2>Let's Start Your Project</h2>
<p style="color:#666;">contact me for any project</p>
            <form method="POST">
                <input type="text" name="client_msg" placeholder="write your message here" required>
                <textarea placeholder="your whatsapp number" name="whatsapp_number"></textarea>
                <button type="submit">Submit</button>
            </form>
        </div>
        <a href="https://wa.me/923160969006" target="_blank" style="position:fixed; bottom:20px; right:20px; background:#25d366; width:65px; height:65px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 10px black; z-index:999;">
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" style="width:40px; height:40px;">
</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
