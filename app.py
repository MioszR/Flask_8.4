from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def aboutme():
    title = "O mnie"
    content = ["Imię:", "Nazwisko:", "Miłosz", "Roman"]
    return render_template("main.html", title=title, content=content)

@app.route('/mypage/kontakt', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        title = "Kontakt"
        items = ["Email:", "Telefon:"]
        return render_template("contact.html", title=title, items=items)
    elif request.method =='POST':
        print(request.form)
        return redirect("/mypage/kontakt")