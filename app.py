from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Afaq Anwar Afghan</title>
        <style>
            body{margin:0; font-family:'Segoe UI', Arial; background:#fff; color:#111;}
            .top{padding:60px 10%; background:#fff; display:flex; align-items:center; gap:40px; flex-wrap:wrap;}
            .top-text{flex:1; min-width:280px;}
            .small-blue{color:#0d6efd; font-weight:600; font-size:15px; margin-bottom:10px;}
            .main-heading{font-size:50px; font-weight:800; line-height:1.2; margin:10px 0; color:#1a1a1a;}
            .sub-text{color:#444; font-size:18px; margin-top:15px;}
            .hire-btn{display:inline-block; margin-top:25px; background:#0d6efd; color:white; padding:12px 28px; border-radius:25px; text-decoration:none; font-weight:600;}
            .profile-pic{width:180px; height:180px; border-radius:50%; border:4px solid #0d6efd; object-fit:cover;}
            .skills-section{background:#f7f7f5; padding:40px 8%; text-align:center;}
            .skills-title{font-size:26px; font-weight:700; margin-bottom:30px;}
            .cards{display:flex; justify-content:center; gap:20px; flex-wrap:wrap;}
            .card{background:white; width:300px; padding:25px; border-radius:14px; box-shadow:0 4px 12px rgba(0,0,0,0.06); text-align:left;}
            .card h3{margin:0; font-size:18px; color:#1a5d1a;}
            .card p{color:#555; font-size:14px; margin-top:10px;}
            .whatsapp-float{position:fixed; width:62px; height:62px; bottom:22px; right:22px; background:#25d366; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 10px rgba(0,0,0,0.3); z-index:999;}
            .whatsapp-float img{width:36px; height:36px;}
        </style>
    </head>
    <body>
        <div class="top">
            <div class="top-text">
                <div class="small-blue">Welcome to My Website!</div>
                <div class="main-heading">Let's Build Something Amazing Together</div>
                <div class="sub-text">I'm Afaq Anwar - Web Developer</div>
                <a href="https://wa.me/923160969006" class="hire-btn">Hire Me</a>
            </div>
            <img src="https://github.com/afaqanwarafghan.png" class="profile-pic" alt="Afaq Photo">
        </div>

        <div class="skills-section">
            <div class="skills-title">My Skills / My Work</div>
            <div class="cards">
                <div class="card"><h3>🌐 Website developer</h3><p>Full stack developer - Front + Back<br>HTML, CSS, Flask, Python</p></div>
                <div class="card"><h3>🔄 Python work</h3><p>Python Script, Automation, Bot</p></div>
                <div class="card"><h3>🎨 Logo / Designing</h3><p>Any type of designing work</p></div>
            </div>
        </div>

        <a href="https://wa.me/923160969006" class="whatsapp-float" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg">
        </a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
