from random import randrange
from flask import Flask, jsonify, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField, Recaptcha
from flask_login import current_user, login_user
from sqlalchemy import null
from wtforms import SubmitField, SelectField, HiddenField, IntegerField, TextField, StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired, NumberRange, DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
from uuid import uuid4
import pandas as pd

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'MLXH243Gh3JD281skdN17FDhdwYF56wPj8'

# Flask-Bootstrap requires this line
Bootstrap(app)

#################################################
# Database Setup
#################################################
# (https://help.heroku.com/ZKNTJQSK/
# why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://guxdnmjbofwoac:d33409f0568bac78d191dbd2511c27a1f888d857258d97a9deaf8211db08339f@ec2-3-227-15-75.compute-1.amazonaws.com:5432/da7ntdovasosdk'

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# setup recaptcha
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeJQngeAAAAAPb66gTSi69KL6JvhCJmfpyj6tIE'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeJQngeAAAAAIheQ_SdVALaVAfxQ9K_OVUoQJh7'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}

class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type

class Students(db.Model):
    __tablename__ = 'NHES_19_PFI'
    id = db.Column(db.Text, primary_key=True)
    SEGRADES = db.Column(db.Integer)
    CENREG = db.Column(db.Integer)
    DISTASSI = db.Column(db.Integer)
    SCHRTSCHL = db.Column(db.Integer)
    SCHLMAGNET = db.Column(db.Integer)
    SEENJOY = db.Column(db.Integer)
    SEABSNT = db.Column(db.Integer)
    FCTEACHR = db.Column(db.Integer)
    FCSTDS = db.Column(db.Integer)
    FHHOME = db.Column(db.Integer)
    FHWKHRS = db.Column(db.Integer)
    FOSTORY2X = db.Column(db.Integer)
    FOGAMES = db.Column(db.Integer)
    FORESPON = db.Column(db.Integer)
    FOHISTX = db.Column(db.Integer)
    FOLIBRAYX = db.Column(db.Integer)
    FOBOOKSTX = db.Column(db.Integer)
    FOCONCRTX = db.Column(db.Integer)
    FOMUSEUMX = db.Column(db.Integer)
    CHLDNT = db.Column(db.Integer)
    INTACC = db.Column(db.Integer)

    def __init__(self, id, SEGRADES, CENREG, FOBOOKSTX, FOCONCRTX, FOGAMES, FOLIBRAYX, FOMUSEUMX,
            FOSTORY2X, FORESPON, FOHISTX, FHHOME, FHWKHRS, SEABSNT, FCSTDS, FCTEACHR,
            SEENJOY, DISTASSI, SCHLMAGNET, SCHRTSCHL, CHLDNT, INTACC
            ):      
        self.id = id
        self.SEGRADES = SEGRADES
        self.CENREG = CENREG
        self.DISTASSI = DISTASSI
        self.SCHRTSCHL = SCHRTSCHL
        self.SCHLMAGNET = SCHLMAGNET
        self.SEENJOY = SEENJOY
        self.SEABSNT = SEABSNT
        self.FCTEACHR = FCTEACHR
        self.FCSTDS = FCSTDS
        self.FHHOME = FHHOME
        self.FHWKHRS = FHWKHRS
        self.FOSTORY2X = FOSTORY2X
        self.FOGAMES = FOGAMES
        self.FORESPON = FORESPON
        self.FOHISTX = FOHISTX
        self.FOLIBRAYX = FOLIBRAYX
        self.FOBOOKSTX = FOBOOKSTX
        self.FOCONCRTX = FOCONCRTX
        self.FOMUSEUMX = FOMUSEUMX
        self.INTACC = INTACC
        self.CHLDNT = CHLDNT

class Questions(db.Model):
    __tablename__ = 'Surveys'
    id = db.Column(db.Text, primary_key=True)
    updated = db.Column(db.Date)
    ALLGRADEX = db.Column(db.Integer)
    SEGRADES = db.Column(db.Integer)
    CENREG = db.Column(db.Integer)
    DISTASSI = db.Column(db.Integer)
    SCHRTSCHL = db.Column(db.Integer)
    SCHLMAGNET = db.Column(db.Integer)
    SEENJOY = db.Column(db.Integer)
    SEABSNT = db.Column(db.Integer)
    FCTEACHR = db.Column(db.Integer)
    FCSTDS = db.Column(db.Integer)
    FHHOME = db.Column(db.Integer)
    FHWKHRS = db.Column(db.Integer)
    FOSTORY2X = db.Column(db.Integer)
    FOGAMES = db.Column(db.Integer)
    FORESPON = db.Column(db.Integer)
    FOHISTX = db.Column(db.Integer)
    FOLIBRAYX = db.Column(db.Integer)
    FOBOOKSTX = db.Column(db.Integer)
    FOCONCRTX = db.Column(db.Integer)
    FOMUSEUMX = db.Column(db.Integer)
    CHLDNT = db.Column(db.Integer)
    INTACC = db.Column(db.Integer)

    def __init__(self, id, updated, ALLGRADEX, SEGRADES, CENREG, FOBOOKSTX, FOCONCRTX, FOGAMES, FOLIBRAYX, FOMUSEUMX,
            FOSTORY2X, FORESPON, FOHISTX, FHHOME, FHWKHRS, SEABSNT, FCSTDS, FCTEACHR,
            SEENJOY, DISTASSI, SCHLMAGNET, SCHRTSCHL, CHLDNT, INTACC
            ):      
        self.id = id
        self.updated = updated
        self.ALLGRADEX = ALLGRADEX
        self.SEGRADES = SEGRADES
        self.CENREG = CENREG
        self.DISTASSI = DISTASSI
        self.SCHRTSCHL = SCHRTSCHL
        self.SCHLMAGNET = SCHLMAGNET
        self.SEENJOY = SEENJOY
        self.SEABSNT = SEABSNT
        self.FCTEACHR = FCTEACHR
        self.FCSTDS = FCSTDS
        self.FHHOME = FHHOME
        self.FHWKHRS = FHWKHRS
        self.FOSTORY2X = FOSTORY2X
        self.FOGAMES = FOGAMES
        self.FORESPON = FORESPON
        self.FOHISTX = FOHISTX
        self.FOLIBRAYX = FOLIBRAYX
        self.FOBOOKSTX = FOBOOKSTX
        self.FOCONCRTX = FOCONCRTX
        self.FOMUSEUMX = FOMUSEUMX
        self.INTACC = INTACC
        self.CHLDNT = CHLDNT

class Features(db.Model):
    __tablename__ = 'Features'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Text)
    feature = db.Column(db.Text)
    group = db.Column(db.Text)

    def __init__(self, id, value, feature, group
            ):
        self.id = id
        self.value = value
        self.feature = feature
        self.group = group

class Resources(db.Model):
    __tablename__ = 'Resources'
    id = db.Column(db.Integer, primary_key=True)
    RESOURCE = db.Column(db.Text)
    GROUP = db.Column(db.Text)
    DESC = db.Column(db.Text)

    def __init__(self, RESOURCE, GROUP, DESC
            ):
        self.RESOURCE = RESOURCE
        self.GROUP = GROUP
        self.DESC = DESC

class Region(FlaskForm):
    # id used only by update/edit
    CENREG = SelectField('In which region do you live?', coerce=int,
        choices=[(1, 'Northeast (CN, ME, MA, NH, NJ, NY, PA, RI, VT)'), (2,'South (AL, AR, DE, DC, FL, GA, KY, LA, MD, MS, NC, OK, SC, TN, TX, VA, WV)'), (3,'Midwest (IL, IN, IA, KN, MI, MN, MO, NB, ND, OH, SD, WI)'), (4,'West (AK, AZ, CA, CO, HI, ID, MT, NN, NM, OR, UT, WH, WY)')
        ])

class Grades(FlaskForm):
    ALLGRADEX = IntegerField('What is this child???s current grade, grade equivalent, or year of school?', [ InputRequired(),
        NumberRange(min=1, max=12, message="Invalid range, enter a number between 1 and 12")
        ])
    SEGRADES = SelectField('Overall, across all subjects, what average grade does the child get?', coerce=int,
        choices=[(1,'Mostly A\'s'), (2,'Mostly B\'s'), (3,'Mostly C\'s'), (4,'D\'s or lower')
        ])

class SchoolType(FlaskForm):
    DISTASSI = SelectField('Is the school your child attends a district assigned school?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    SCHLMAGNET = SelectField('Does your child attend a magnet school or program?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    SCHRTSCHL = SelectField('Does your child attend a charter school?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])

class SchoolSent(FlaskForm):
    FCTEACHR = SelectField('How satisfied are your child\'s teachers?', coerce=int,
        choices=[(1,'Very satisfied'), (2,'Somewhat satisfied'), (3,'Somewhat dissatisfied'), (4,'Very dissatisfied')
        ])
    FCSTDS = SelectField('How satisfied are you with the school\'s academic standards?', coerce=int,
        choices=[(1,'Very satisfied'), (2,'Somewhat satisfied'), (3,'Somewhat dissatisfied'), (4,'Very dissatisfied')
        ])
    SEENJOY = SelectField('How much do you agree or disagree with the following: "This child enjoys school."', coerce=int,
        choices=[(1,'Strongly agree'), (2,'Agree'), (3,'Disagree'), (4,'Strongly disagree')
        ])

class SchoolBeh(FlaskForm):
    SEABSNT = SelectField('Since the beginning of this school year, how many days has child been absent from school?', coerce=int,
        choices=[(1,'0 - 5'), (2,'6 - 10'), (3,'11 - 20'), (4,'More than 20 days')
        ])
    FHWKHRS = SelectField('In an average week, how many hours does this child spend on homework outside of school?', coerce=int,
        choices=[(1,'0 - 20'), (2,'20 - 40'), (3,'40 - 60'), (4,'80+')
        ])
    FHHOME = SelectField('How often does this child do homework at home, an after-school program, or somewhere else outside of school?', coerce=int,
        choices=[(1,'Less than once a week'), (2,'1 to 2 days a week'), (3,'3 to 4 days a week'), (4,'5 or more days a week'), (5,'Never')
        ])

class Enrichment(FlaskForm):
    FORESPON = SelectField('In the past month, have you or someone in your family discussed with him or her how to manage time?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    FOHISTX = SelectField('In the past month, have you or someone in your family talked with him or her about the family\'s history or ethnic heritage?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    FOSTORY2X = SelectField('In the past month, have you or someone in your family told him or her a story? (Do not include read to him or her)', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    FOCONCRTX = SelectField('In the past month, have you or someone in your family gone to a play, convert, or other live show?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    FOGAMES = SelectField('In the past month, have you or someone in your family played board games or did puzzles with him or her?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    FOBOOKSTX = SelectField('In the past month, have you or someone in your family visited a bookstore?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    FOLIBRAYX = SelectField('In the past month, have you or someone in your family visited a library with the child?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    FOMUSEUMX = SelectField('In the past month, have you or someone in your family visited a museum, or historical site?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])

class Technology(FlaskForm):
    INTACC = SelectField('Does your household have internet access?', coerce=int,
        choices=[(1,'Yes'), (2,'At home and on a cell phone'), (3, 'Yes, at home only'), (4, 'Yes, on cell phone only'), (5, 'No')
        ])
    CHLDNT = SelectField('How often does this child use the Internet at home often does this child use the internet at home for learning activities?', coerce=int,
        choices=[(1,'Every day'), (2,'A few times a week'), (3, 'A few times a month'), (4, 'A few times a year'), (5, 'Never')
        ])

class HiddenFields(FlaskForm):
    id_field = HiddenField()
    updated = HiddenField()

class ReCaptcha(FlaskForm):
    recaptcha = RecaptchaField(validators=[Recaptcha()])

class SubmitForm(FlaskForm):
    submit = SubmitField('Submit Answers')

class AddResource(FlaskForm):
    RESOURCE = TextField('Enter URL', [ InputRequired()])
    GROUP = TextField('Enter Group', [ InputRequired()])
    DESC = TextField('Enter a Brief Description', [ InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

# +++++++++++++++++++++++
# get local date - does not account for time zone
# note: date was imported at top of script
def stringdate():
    today = datetime.today()
    date_list = str(today).split('-')
    date_list = date_list + date_list[2].split(' ')
    # build string in format 01-01-2000
    date_string = date_list[1] + "/" + date_list[3] + "/" + date_list[0]
    return date_string

def genID():
    uniqueID = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
    return uniqueID

# +++++++++++++++++++++++
# routes

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
def index():
    # get a list of unique values in the style column
    return render_template('index.html')

# add a new sock to the database
@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    form1 = Region()
    form2 = Grades()
    form3 = SchoolType()
    form4 = SchoolSent()
    form5 = SchoolBeh()
    form6 = Enrichment()
    form7 = Technology()
    form8 = HiddenFields()
    form9 = ReCaptcha()
    form10 = SubmitForm()

    if (form1.validate_on_submit() and form2.validate_on_submit() and form2.validate_on_submit()
        and form4.validate_on_submit() and form5.validate_on_submit() and form6.validate_on_submit()
        and form7.validate_on_submit() and form8.validate_on_submit() and form9.validate_on_submit()
        and form10.validate_on_submit()):

        ALLGRADEX = request.form['ALLGRADEX']
        SEGRADES = request.form['SEGRADES']
        CENREG = request.form['CENREG']
        FOCONCRTX = request.form['FOCONCRTX']
        FOBOOKSTX = request.form['FOBOOKSTX']
        FOGAMES = request.form['FOGAMES']
        FOLIBRAYX = request.form['FOLIBRAYX']
        FOMUSEUMX = request.form['FOMUSEUMX']
        FOSTORY2X = request.form['FOSTORY2X']
        FORESPON = request.form['FORESPON']
        FOHISTX = request.form['FOHISTX']
        FHHOME = request.form['FHHOME']
        FHWKHRS = request.form['FHWKHRS']
        SEABSNT = request.form['SEABSNT']
        FCSTDS = request.form['FCSTDS']
        FCTEACHR = request.form['FCTEACHR']
        SEENJOY = request.form['SEENJOY']
        DISTASSI = request.form['DISTASSI']
        SCHLMAGNET = request.form['SCHLMAGNET']
        SCHRTSCHL = request.form['SCHRTSCHL']
        CHLDNT = request.form['CHLDNT']
        INTACC = request.form['INTACC']

        # get today's date from function, above all the routes
        id = genID()
        updated = stringdate()
        # the data to be inserted into page
        record = Questions(id,updated, CENREG, ALLGRADEX, SEGRADES, FOBOOKSTX, FOCONCRTX, FOGAMES, FOLIBRAYX, FOMUSEUMX, FOSTORY2X, FORESPON, 
                            FOHISTX, FHHOME, FHWKHRS, SEABSNT, FCSTDS, FCTEACHR, SEENJOY, DISTASSI, SCHLMAGNET, SCHRTSCHL, CHLDNT, INTACC)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        return redirect(url_for('data', id=id))
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {} - {}".format(
                    getattr(form1, field).label.text,
                    error, getattr(form1, field).data
                ), 'error')
        for field, errors in form2.errors.items():
            for error in errors:
                flash("Error in {}: {} - {}".format(
                    getattr(form2, field).label.text,
                    error, getattr(form2, field).data
                ), 'error')
        for field, errors in form3.errors.items():
            for error in errors:
                flash("Error in {}: {} - {}".format(
                    getattr(form3, field).label.text,
                    error, getattr(form3, field).data
                ), 'error')
        return render_template('add_record.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9, form10=form10)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        logged_in = form.username.data
        return redirect(url_for('index', logged_in=logged_in))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

@app.route('/add_resource', methods=['GET', 'POST'])
@login_required
def add_resource():
    form1 = AddResource()
    form2 = SubmitForm()

    if (form1.validate_on_submit()):
        RESOURCE = request.form['RESOURCE']
        GROUP = request.form['GROUP']
        DESC = request.form['DESC']

        record = Resources(RESOURCE, GROUP, DESC)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()

        # create a message to send to the template
        message = f"The URL has been submitted."
        return render_template('add_resource.html', message=message, form2=form2)

    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {} - {}".format(
                    getattr(form1, field).label.text,
                    error, getattr(form1, field).data
                ), 'error')
        return render_template('add_resource.html', form1=form1, form2=form2)

@app.route('/data')
def data():

    #try:
    id = request.args.get('id', None)
    
    # function to sum values within group
    def sumVal(df, group):
        summed_df = df[df['group']==group]
        return summed_df['value'].sum()
    
    # function to normalize values
    def normVal(df, group, column):
        normalized_df = df[df['group']==group]
        normalized_df[column] = normalized_df[column]/normalized_df[column].sum()
        return normalized_df

    # function to filter data frame by features in important features table
    def filterQ (data, normalized):
        df = pd.DataFrame()
        row = data.to_frame()
        row.index = row.index.set_names('feature')
        row = row.reset_index()
        row.columns = ['feature', 'answer']
        for index_x, x in row.iterrows():
            for index_y, y in normalized.iterrows():
                if (x['feature'] == y['feature']):
                    #print("Found matches")
                    if (int(x['answer']) == int(y['answer'])):
                        #print(index_x, 'X:', x['feature'], x['answer'], index_y, 'Y:', y['feature'], y['answer'])
                        df = df.append(y)
        
        return df

    
    # query DB and tables to get data
    questions_data = Questions.query.filter_by(id=id).all()
    questions = [d.__dict__ for d in questions_data]
    features_data = Features.query.all()
    features = [d.__dict__ for d in features_data]
    resources_data = Resources.query.all()
    resources = [d.__dict__ for d in resources_data]
    national_data = Students.query.all()
    national = [d.__dict__ for d in national_data]

    
    # drop uneeded columns
    resources_df = pd.DataFrame(resources)
    resources_df = resources_df.drop(['_sa_instance_state'], axis=1)

    # drop uneeded columns and transpose the DF for comparison to the ideal features
    questions_df = pd.DataFrame(questions)
    questions_df = questions_df.drop(['_sa_instance_state', 'updated', 'id'], axis=1)
    # save columns for filtering 
    col = questions_df.columns.tolist()
    col.remove('ALLGRADEX')

    questions_df = questions_df.transpose()
    questions_df.index = questions_df.index.set_names('feature')
    questions_df = questions_df.reset_index()
    questions_df.columns = ['feature', 'answer']

    # drop uneeded columns
    national_df = pd.DataFrame(national)
    national_df = national_df.drop(['_sa_instance_state'], axis=1)
    national_clean_df = national_df[col].sample(n=100, random_state=randrange(100))

    # drop uneeded columns and split the answers from the feature name
    features_df = pd.DataFrame(features)
    features_df = features_df.drop(['_sa_instance_state'], axis=1)
    features_df[['feature1', 'answer']] = features_df['feature'].str.split("_", expand=True)
    features_df = features_df.drop(['feature'], axis = 1)
    features_df = features_df.rename(columns={'feature1': 'feature'})

    
    # normalize values within group to 1
    technology_df = normVal(features_df, 'Technology', 'value')
    enrichment_df = normVal(features_df, 'Enrichment Activity', 'value')
    behavior_df = normVal(features_df, 'School Behavior', 'value')
    school_df = normVal(features_df, 'School Type', 'value')
    schoolsent_df = normVal(features_df, 'School Sentiment', 'value')

    frames = [technology_df, enrichment_df, behavior_df, school_df, schoolsent_df]
    normalized_df = pd.concat(frames)

    
    # match questions to ideal answer and add to DF
    newdf = pd.DataFrame()
    for index_x, x in questions_df.iterrows():
        for index_y, y in normalized_df.iterrows():
            if (x['feature'] == y['feature']):
                #print("Found matches")
                if (int(x['answer']) == int(y['answer'])):
                    #print(index_x, 'X:', x['feature'], x['answer'], index_y, 'Y:', y['feature'], y['answer'])
                    newdf = newdf.append(y)

    newdf = newdf.drop(['id'], axis=1)

    # iterate over each row and gather the group values then average them
    national_values_df = pd.DataFrame()
    for index, x in national_clean_df.iterrows():
        national_clean_df = filterQ(x, normalized_df)

        tech_val_national = sumVal(national_clean_df, 'Technology')
        enrichment_val_national = sumVal(national_clean_df, 'Enrichment Activity')
        behavior_val_national = sumVal(national_clean_df, 'School Behavior')
        school_val_national = sumVal(national_clean_df, 'School Type')
        schoolsent_val_national = sumVal(national_clean_df, 'School Sentiment')

        national_values = [tech_val_national, enrichment_val_national, behavior_val_national, school_val_national, schoolsent_val_national]
        temp_df = pd.DataFrame(national_values).transpose()

        national_values_df = national_values_df.append(temp_df)

    national_values_df.columns = ['tech', 'enrich', 'behav', 'school', 'sent']   
    
    national_values_avg_df = national_values_df[['tech', 'enrich', 'behav', 'school', 'sent']].mean()
    national_chartdata = national_values_avg_df.tolist()
        
    # sum the values of the answers from the survey
    tech_val = sumVal(newdf, 'Technology')
    enrichment_val = sumVal(newdf, 'Enrichment Activity')
    behavior_val = sumVal(newdf, 'School Behavior')
    school_val = sumVal(newdf, 'School Type')
    schoolsent_val = sumVal(newdf, 'School Sentiment')
    
    # store values to be sent to the dashboard
    chartdata = [tech_val, enrichment_val, behavior_val, school_val, schoolsent_val]

    if (tech_val < 1):
        tech_resources_df = resources_df[resources_df['GROUP'] == 'Technology']
        tech_resources_df = tech_resources_df.drop(columns={'id', 'GROUP'})
        tech_resources = tech_resources_df.values.tolist()
    else:
        tech_resources = null

    if (enrichment_val < 1):
        enrichment_resources_df = resources_df[resources_df['GROUP'] == 'Enrichment Activity']
        enrichment_resources_df = enrichment_resources_df.drop(columns={'id', 'GROUP'})
        enrichment_resources = enrichment_resources_df.values.tolist()
    else:
        enrichment_resources = null

    if (behavior_val < 1):
        behavior_resources_df = resources_df[resources_df['GROUP'] == 'School Behavior']
        behavior_resources_df = behavior_resources_df.drop(columns={'id', 'GROUP'})
        behavior_resources = behavior_resources_df.values.tolist()
    else:
        behavior_resources = null

    if (school_val < 1):
        school_resources_df = resources_df[resources_df['GROUP'] == 'School Type']
        school_resources_df = school_resources_df.drop(columns={'id', 'GROUP'})
        school_resources = school_resources_df.values.tolist()
    else:
        school_resources = null

    if (schoolsent_val < 1):
        schoolsent_resources_df = resources_df[resources_df['GROUP'] == 'School Sentiment']
        schoolsent_resources_df = schoolsent_resources_df.drop(columns={'id', 'GROUP'})
        schoolsent_resources = schoolsent_resources_df.values.tolist()
    else:
        schoolsent_resources = null

    print(newdf)

    return render_template('dashboard.html', national_chartdata=national_chartdata, chartdata=chartdata, tech_resources=tech_resources, 
                            enrichment_resources=enrichment_resources, behavior_resources=behavior_resources,
                            school_resources=school_resources, schoolsent_resources=schoolsent_resources,
                            tech_val=tech_val, enrichment_val=enrichment_val, behavior_val=behavior_val,
                            school_val=school_val, schoolsent_val=schoolsent_val
                            )
    #except Exception as e:
        # # e holds description of the error
        # error_text = "<p>The error:<br>" + str(e) + "</p>"
        # hed = '<h1>Something is broken.</h1>'
        # return hed + error_text

# +++++++++++++++++++++++
# error routes
# https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/#registering-an-error-handler

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', pagetitle="404 Error - Page Not Found", pageheading="Page not found (Error 404)", error=e), 404

@app.errorhandler(405)
def form_not_posted(e):
    return render_template('error.html', pagetitle="405 Error - Form Not Submitted", pageheading="The form was not submitted (Error 405)", error=e), 405

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', pagetitle="500 Error - Internal Server Error", pageheading="Internal server error (500)", error=e), 500

# +++++++++++++++++++++++

if __name__ == '__main__':
    app.run(debug=True)