from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://i.gifer.com/8l9j.gif",
    "https://i.gifer.com/MS2f.gif",
    "https://i.gifer.com/Daxl.gif",
    "https://i.gifer.com/HJAQ.gif",
    "https://i.gifer.com/GArb.gif",
    "https://i.gifer.com/C4F.gif",
    "https://i.gifer.com/7t5l.gif",
    "https://i.gifer.com/asX.giff",
    "https://i.gifer.com/VBJO.gif",
    "https://i.gifer.com/RWz.gif",
    "https://i.gifer.com/TPk.gif",
    "https://i.gifer.com/yPf.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")