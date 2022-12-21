from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm



app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'

app.config[
    "SECRET_KEY"
] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"

db=SQLAlchemy(app)
app.app_context().push()


#db.init_app(app)



tv = [
    {
        "name": "TV_LG",
        "photo": "Tv LG.jpg",
    },
    {
        "name": "TV_samsung",
        "photo": "Tv samsung.jpg",
    },
    {
        "name": "TV_sharp",
        "photo": "Tv sharp.jpg",
    },
]

washingmachine = [
    {
        "name": "washing_machine_LG",
        "photo": "wish Lg.jpg",
    },
    {
        "name": "washing_machine_samsung",
        "photo": "wish samsung.webp",
    },
    {
        "name": "washing_machine_sharp",
        "photo": "wish sharp.png",
    },
]

fridge = [
    {
        "name": "fridge_LG",
        "photo": "FRE Lg.jpg",
    },
    {
        "name": "fridge_samsung",
        "photo": "FRE samsung.jpg",
    },
    {
        "name": "fridge_sharp",
        "photo": "FRE sharp.jpg",
    },
]

aircons = [
    {
        "name": "air-conditioner-LG",
        "photo": "Air Lg.jpg",
    },
    {
        "name": "air-conditioner-samsung",
        "photo": "Air samsung.jpg",
    },
    {
        "name": "air-conditioner-sharp",
        "photo": "Air sharp.jpg",
    },
]

fans = [
    {
        "name": "extractor_LG",
        "photo": "fan Lg.jpg",
    },
    {
        "name": "extractor_samsung",
        "photo": "fan samsung.jpg",
    },
    {
        "name": "extractor_sharp",
        "photo": "fan sharp.jpg",
    },
]

@app.route("/")
def home():
    return render_template('intro.html',custom_css="intro",title="تسوق اسهل")

@app.route("/categories")
def categories():
    return render_template('categories.html',custom_css="categories",title="تسوق اسهل") 

@app.route("/air-conditioner-devices")
def air_conditioner_devices():
    return render_template('air-conditioner-devices.html',custom_css="air-conditioner-devices",title="تسوق اسهل",aircons = aircons)

@app.route("/air-conditioner-LG")
def air_conditioner_LG():
    return render_template('air-conditioner-LG.html',custom_css="air-conditioner-LG",title="تسوق اسهل")

@app.route("/air-conditioner-samsung")
def air_conditioner_samsung():
    return render_template('air-conditioner-samsung.html',custom_css="air-conditioner-samsung",title="تسوق اسهل")

@app.route("/air-conditioner-sharp")
def air_conditioner_sharp():
    return render_template('air-conditioner-sharp.html',custom_css="air-conditioner-sharp",title="تسوق اسهل")    

@app.route("/extractor-devices")
def extractor_devices():
    return render_template('extractor-devices.html',custom_css="extractor-devices",title="تسوق اسهل",fans = fans)

@app.route("/extractor_LG")
def extractor_LG():
    return render_template('extractor_LG.html',custom_css="extractor_LG",title="تسوق اسهل")

@app.route("/extractor_samsung")
def extractor_samsung():
    return render_template('extractor_samsung.html',custom_css="extractor_samsung",title="تسوق اسهل")

@app.route("/extractor_sharp")
def extractor_sharp():
    return render_template('extractor_sharp.html',custom_css="extractor_sharp",title="تسوق اسهل")

@app.route("/fridge-devices")
def fridge_devices():
    return render_template('fridge-devices.html',custom_css="fridge-devices",title="تسوق اسهل",fridge = fridge)

@app.route("/fridge_LG")
def fridge_LG():
    return render_template('fridge_LG.html',custom_css="fridge_LG",title="تسوق اسهل")

@app.route("/fridge_samsung")
def fridge_samsung():
    return render_template('fridge_samsung.html',custom_css="fridge_samsung",title="تسوق اسهل")

@app.route("/fridge_sharp")
def fridge_sharp():
    return render_template('fridge_sharp.html',custom_css="fridge_sharp",title="تسوق اسهل")

@app.route("/tv-devices")
def tv_devices():
    return render_template('tv-devices.html',custom_css="tv-devices",title="تسوق اسهل",tv = tv)

@app.route("/TV_LG")
def TV_LG():
    return render_template('TV_LG.html',custom_css="TV_LG",title="تسوق اسهل")

@app.route("/TV_samsung")
def TV_samsung():
    return render_template('TV_samsung.html',custom_css="TV_samsung",title="تسوق اسهل")

@app.route("/TV_sharp")
def TV_sharp():
    return render_template('TV_sharp.html',custom_css="TV_sharp",title="تسوق اسهل")

@app.route("/washing-machine-devices")
def washing_machine_devices():
    return render_template('washing-machine-devices.html',custom_css="washing-machine-devices",title="تسوق اسهل",washingmachine = washingmachine)

@app.route("/washing_machine_LG")
def washing_machine_LG():
    return render_template('washing_machine_LG.html',custom_css="washing_machine_LG",title="تسوق اسهل")

@app.route("/washing_machine_samsung")
def washing_machine_samsung():
    return render_template('washing_machine_samsung.html',custom_css="washing_machine_samsung",title="تسوق اسهل")

@app.route("/washing_machine_sharp")
def washing_machine_sharp():
    return render_template('washing_machine_sharp.html',custom_css="washing_machine_sharp",title="تسوق اسهل")                   

@app.route("/payment", methods=["GET", "POST"])
def payment ():
    return render_template('payment.html',custom_css="payment",title="تسوق اسهل")

@app.route("/thanks")
def thanks():
    return render_template('thanks.html',custom_css="thanks", title="تسوق اسهل")

       

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created successfully for {form.username.data}", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.email.data == "modern@email.com"
            and form.password.data == "PASS!!word123"
        ):
            flash("You have been logged in!", "success")
            return redirect(url_for("categories"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template("login.html", title="Login", form=form)

class Device(db.Model):
    D_id = db.Column(db.Integer, primary_key=True)
    D_name = db.Column(db.String(25), nullable=False) 
    D_photo = db.Column(db.String(20), nullable=False, default='default.jpg') 
    D_model = db.Column(db.String(25), nullable=False)
    D_details = db.Column(db.String(150), nullable=False)
    D_price = db.Column(db.Float(25), nullable=False)
    brand_id= db.Column(db.Integer, db.ForeignKey('brand.brand_id'), nullable=False)
    sec_id= db.Column(db.Integer, db.ForeignKey('section.sec_id'), nullable=False)
    customer_email= db.Column(db.Integer, db.ForeignKey('customer.customer_email'), nullable=False)   
    
def __repr__(self):
    return f"Device('{self.D_name}','{self.D_photo}','{self.D_price})"

class Section(db.Model):
    sec_id = db.Column(db.Integer, primary_key=True) 
    sec_name = db.Column(db.String(25), nullable=False) 
    sec_photo = db.Column(db.String(20), nullable=False, default='default.jpg')
    d_sec= db.relationship('device',backref='device_section', lazy=True)

def __repr__(self):
    return f"Section('{self.sec_name}','{self.sec_photo}')"

class Brand(db.Model):
    brand_id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(25), nullable=False)
    logo = db.Column(db.String(20), nullable=False, default='default.jpg')
    device = db.relationship('device',backref='device_brand', lazy=True)

def __repr__(self):
    return f"Brand('{self.brand_name}','{self.brand_logo}')"

class Customer(db.Model):
    customer_email = db.Column(db.String(125), primary_key=True,nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username= db.Column(db.String(25),unique=True, nullable=False)
    customer_phone= db.Column(db.VARCHAR(20),nullable=False) 
    customer_pass = db.Column(db.String(60), nullable=False)
    sec_photo = db.Column(db.String(20), nullable=False, default='default.jpg')
    custom_device= db.relationship('device',backref='customer.devices', lazy=True)
   
def __repr__(self):
    return f"Customer('{self.customer_name}','{self.customer_phone}','{self.custom_device})"


if __name__ == "__main__":
    app.run(debug=True)