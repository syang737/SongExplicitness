from flask import Flask, request, render_template
from songexplicitness import swear_dict
from visualize import plot_swears
import StringIO
import base64

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def my_form_post():
    img = StringIO.StringIO()

    songname = request.form['songname']
    swears = swear_dict(songname)
    fig = plot_swears(swears)
    fig.show()
    fig.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue())

    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run()
