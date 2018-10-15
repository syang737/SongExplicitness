from flask import Flask, request, render_template
import songexplicitness
import visualize
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
    print(songname)
    swears = songexplicitness.swear_dict(songname)
    no_swears = ''
    if len(swears) > 0:
        fig = visualize.plot_swears(swears)
        fig.show()
        fig.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue())
    else:
        no_swears = '\'%s\' has no swear words.' % songname
        plot_url = ''

    if no_swears == '':
        title = songname
    else:
        title = ''

    return render_template('index.html', plot_url=plot_url, no_swears=no_swears, title=title)

if __name__ == '__main__':
    app.run()
