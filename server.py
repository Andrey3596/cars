from flask import Flask, render_template


app = Flask(__name__)


nav = [
    { "title": "Historicar Auto Portal", "URL": "/" },
    { "title": "Mercedes-Benz", "URL": "/car_page_merc" },
    { "title": "BMW", "URL": "/car_page_bmw" },
    { "title": "AUDI", "URL": "/car_page_audi" },
    { "title": "Glossary", "URL": "/car_page_glossary" },
    { "title": "About me", "URL": "/car_page_me" },
]


@app.context_processor
def global_context():
    return{
        "nav":nav
    }


@app.route("/")
def main_page():
    return render_template("main_page.html", name="Historicar Auto Portal",)


@app.route("/car_page_merc")
def car_page_merc():
    return render_template("car_page_merc.html",name="Mercedes-Benz")


@app.route("/car_page_bmw")
def car_page_bmw():
    return render_template("car_page_bmw.html",name="BMW")


@app.route("/car_page_audi")
def car_page_audi():
    return render_template("car_page_audi.html",name="AUDI")


@app.route("/car_page_glossary")
def car_page_glossary():
    return render_template("car_page_glossary.html",name="Glossary")


@app.route("/car_page_me")
def car_page_about():
    return render_template("car_page_about.html",name="About me")


if __name__ == "__main__": # проверка что вырбран наш файл
    app.run(debug=True)