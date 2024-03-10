from flask import Flask, request, render_template, url_for
import os

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def photo():
    if request.method == 'POST':
        file = request.files['file']
        print("okey")
        if file:
            print("yeah")
            file.save('static/img/marse.png')
            print("good")
            image_url = url_for('static', filename='img/marse.png')
            return render_template('index.html', image_url=image_url,
                                   css_url=url_for('static', filename='css/style.css'))

    return render_template('index.html', image_url=None,
                           css_url=url_for('static', filename='css/style.css'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')