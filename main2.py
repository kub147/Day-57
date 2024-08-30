from flask import Flask, render_template
import requests
import random
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', rand=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    gender_api = requests.get(f'https://api.genderize.io/?name={name}')
    age_api = requests.get(f'https://api.agify.io/?name={name}')

    precent = gender_api.json().get('probability')
    gender = gender_api.json().get('gender')
    age = age_api.json().get('age')

    return render_template('gender.html', precent=precent, gender=gender, name=name, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts = requests.get(blog_url)
    posts = posts.json()
    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
