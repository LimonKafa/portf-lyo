# Import
from flask import Flask, render_template,request, redirect



from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma
# Kullanıcı tablosu oluşturun
class Kullanici(db.Model):
    # Sütunlar oluşturuluyor
    #id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Giriş
    mail = db.Column(db.String(100), nullable=False)
    # Geri bildirim
    feedback = db.Column(db.String(30), nullable=False)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    return render_template('index.html', 
                           button_python=button_python,
                           button_discord=button_discord
                           )
@app.route('/feedback', methods=['POST'])
def feedback_form():
    if request.method == 'POST':
        mail= request.form['email']
        feedback = request.form['text']
        
        # Kullanıcı verilerinin veri tabanına kaydedilmesini sağlayın
        kullanici = Kullanici(mail=mail, feedback=feedback)
        db.session.add(kullanici) # eklemek
        db.session.commit() # kaydetmek
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
