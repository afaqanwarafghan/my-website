from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Afaq Anwar</title>
        <style>
            body{margin:0; font-family:'Segoe UI', Arial; background:#fff; color:#111;}
            .top{padding:60px 8%; background:#fff; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:20px;}
            .top-text{flex:1; min-width:300px;}
            .small-blue{color:#0d6efd; font-weight:600; font-size:15px; margin-bottom:10px;}
            .main-heading{font-size:50px; font-weight:800; line-height:1.2; margin:10px 0; color:#1a1a1a;}
            .sub-text{color:#444; font-size:18px; margin-top:15px;}
            .hire-btn{display:inline-block; margin-top:25px; background:#0d6efd; color:white; padding:12px 28px; border-radius:25px; text-decoration:none; font-weight:600;}
            .profile-pic{width:200px; height:200px; border-radius:50%; border:4px solid #0d6efd; object-fit:cover; box-shadow:0 4px 15px rgba(0,0,0,0.1);}
            .skills-section{background:#f7f7f5; padding:40px 8%; text-align:center;}
            .skills-title{font-size:26px; font-weight:700; margin-bottom:30px;}
            .cards{display:flex; justify-content:center; gap:20px; flex-wrap:wrap;}
            .card{background:white; width:300px; padding:25px; border-radius:14px; box-shadow:0 4px 12px rgba(0,0,0,0.06); text-align:left;}
            .card h3{margin:0; font-size:18px;}
            .card p{color:#555; font-size:14px; margin-top:10px; line-height:1.5;}
            .contact-section{padding:50px 8%; background:#fff; text-align:center;}
            .contact-title{font-size:30px; font-weight:800; margin-bottom:30px;}
            .form-box{display:flex; justify-content:center; gap:20px; flex-wrap:wrap;}
            .input-field{width:350px; padding:18px; border-radius:12px; border:1px solid #ccc; font-size:16px; outline:none;}
            .send-btn{margin-top:25px; background:#0d6efd; color:white; padding:14px 40px; border:none; border-radius:25px; font-size:16px; font-weight:600; cursor:pointer;}
            .whatsapp-float{position:fixed; width:62px; height:62px; bottom:22px; right:22px; background:#25d366; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 10px rgba(0,0,0,0.3); z-index:999;}
            .whatsapp-float img{width:36px; height:36px;}
        </style>
    </head>
    <body>
        <div class="top">
            <div class="top-text">
                <div class="small-blue">Welcome to My Website!</div>
                <div class="main-heading">Let's Build Something<br>Amazing Together</div>
                <div class="sub-text">I'm Afaq Anwar - Web Developer</div>
                <a href="#order" class="hire-btn">Hire Me</a>
            </div>
            <img src="https://github.com/afaqanwarafghan.png" class="profile-pic">
        </div>

        <div class="skills-section">
            <div class="skills-title">My Skills / My Work</div>
            <div class="cards">
                <div class="card"><h3>🌐 Website developer</h3><p>Full stack developer - Front + Back<br>HTML, CSS, Flask, Python</p></div>
                <div class="card"><h3>🔄 Python work</h3><p>Python Script, Automation, Bot<br>All type of Python work</p></div>
                <div class="card"><h3>🎨 Logo / Designing</h3><p>Any type of designing work<br>Logo, Poster, Thumbnail</p></div>
            </div>
        </div>

        <div class="contact-section" id="order">
            <div class="contact-title">Mujh se Rabta Karo / Order Do</div>
            <div class="form-box">
                <input id="msg" class="input-field" type="text" placeholder="write your massage here">
                <input id="num" class="input-field" type="text" placeholder="write your whatsapp number here">
            </div>
            <button class="send-btn" onclick="sendWhatsApp()"submit"</button>
        </div>

        <a href="https://wa.me/923160969006" class="whatsapp-float" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg">
        </a>

        <script>
        function sendWhatsApp(){
            var m = document.getElementById('msg').value;
            var n = document.getElementById('num').value;
            var text = "Order: " + m + " | My Number: " + n;
            window.open("https://wa.me/923160969006?text=" + encodeURIComponent(text), "_blank");
        }
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
