from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField, Recaptcha
from wtforms import SubmitField, SelectField, HiddenField, IntegerField
from wtforms.validators import InputRequired, NumberRange

from datetime import datetime
from uuid import uuid4

app = Flask(__name__)

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

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Questions(db.Model):
    __tablename__ = 'Surveys'
    id = db.Column(db.Integer, primary_key=True)
    updated = db.Column(db.Date)
    ALLGRADEX = db.Column(db.Integer)
    SEGRADES = db.Column(db.Integer)
    CENREG = db.Column(db.Integer)
    DISTASSI = db.Column(db.Integer)
    SCHRTSCHL = db.Column(db.Integer)
    SCHLMAGNET = db.Column(db.Integer)
    SEENJOY = db.Column(db.Integer)
    SEABSNT = db.Column(db.Integer)
    FCSCHOOL = db.Column(db.Integer)
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
    HHENGLISH = db.Column(db.Integer)
    CSPEAKX = db.Column(db.Integer)
    HHTOTALXX = db.Column(db.Integer)
    HHPRTNRSX = db.Column(db.Integer)
    P1REL = db.Column(db.Integer)
    P2AGE = db.Column(db.Integer)
    P2REL = db.Column(db.Integer)
    P2SEX = db.Column(db.Integer)
    P2MRSTA = db.Column(db.Integer)
    PAR1EMPL = db.Column(db.Integer)
    PAR1FTFY = db.Column(db.Integer)
    NUMSIBSX = db.Column(db.Integer)
    TTLHHINC = db.Column(db.Integer)
    OWNRNTHB = db.Column(db.Integer)
    CHLDNT = db.Column(db.Integer)
    LRNCELL = db.Column(db.Integer)

    def __init__(self,id,updated, ALLGRADEX, SEGRADES, FOBOOKSTX, FOCONCRTX, FOGAMES, FOLIBRAYX, FOMUSEUMX,
                FOSTORY2X, FORESPON, CSPEAKX, FOHISTX, HHENGLISH, HHPRTNRSX, HHTOTALXX,
                NUMSIBSX, OWNRNTHB, P1REL, P2AGE, P2MRSTA, P2REL, P2SEX, PAR1EMPL, PAR1FTFY,
                TTLHHINC, CENREG, FHHOME, FHWKHRS, SEABSNT, FCSCHOOL, FCSTDS, FCTEACHR,
                SEENJOY, DISTASSI, SCHLMAGNET, SCHRTSCHL, CHLDNT, INTACC, LRNCELL
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
        self.FCSCHOOL = FCSCHOOL
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
        self.HHENGLISH = HHENGLISH
        self.CSPEAKX = CSPEAKX
        self.HHTOTALXX = HHTOTALXX
        self.HHPRTNRSX = HHPRTNRSX
        self.P1REL = P1REL
        self.P2AGE = P2AGE
        self.P2REL = P2REL
        self.P2SEX = P2SEX
        self.P2MRSTA = P2MRSTA
        self.PAR1EMPL = PAR1EMPL
        self.PAR1FTFY = PAR1FTFY
        self.NUMSIBSX = NUMSIBSX
        self.TTLHHINC = TTLHHINC
        self.OWNRNTHB = OWNRNTHB
        self.INTACC = INTACC
        self.CHLDNT = CHLDNT
        self.LRNCELL = LRNCELL

class Region(FlaskForm):
    # id used only by update/edit
    CENREG = SelectField('In which region do you live?', coerce=int,
        choices=[(1, 'Northeast (CN, ME, MA, NH, NJ, NY, PA, RI, VT)'), 
        (2,'South (AL, AR, DE, DC, FL, GA, KY, LA, MD, MS, NC, OK, SC, TN, TX, VA, WV)'), 
        (3,'Midwest (IL, IN, IA, KN, MI, MN, MO, NB, ND, OH, SD, WI)'), 
        (4,'West (AK, AZ, CA, CO, HI, ID, MT, NN, NM, OR, UT, WH, WY)')
        ])

class Grades(FlaskForm):
    ALLGRADEX = IntegerField('What is this child’s current grade, grade equivalent, or year of school?', [ InputRequired(),
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
    FCSCHOOL = SelectField('How satisfied are you with the school your child attends?', coerce=int,
        choices=[(1,'Very satisfied'), (2,'Somewhat satisfied'), (3,'Somewhat dissatisfied'), (4,'Very dissatisfied')
        ])
    FCTEACHR = SelectField('How satisfied are you with the school\'s teachers?', coerce=int,
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

class FamilyDem(FlaskForm):
    PAR1EMPL = SelectField('What is your current work status?', coerce=int,
        choices=[(1,'Work 35+ hours per week'), (2,'Work less than 35 hours per week'), (3,'Looking for work'), (4,'Not in the labor force')
        ])
    PAR1FTFY = SelectField('Do you work full-time?', coerce=int,
        choices=[(1,'Full time and full year'), (2,'Less than full time or less than full year'), (3,'Not employed during the past year')
        ])
    P1REL = SelectField('What is your relationship to the child?', coerce=int,
        choices=[(1,'Biological parent'), (2,'Adoptive parent'), (3,'Stepparent'), (4,'Foster parent'), (5,'Grandparent'), (6,'Other guardian')
        ])
    P2REL = SelectField('What is your partner\'s relationship to the child?', coerce=int,
        choices=[(1,'Biological parent'), (2,'Adoptive parent'), (3,'Stepparent'), (4,'Foster parent'), (5,'Grandparent'), (6,'Other guardian')
        ])
    P2SEX = SelectField('What is the sex of the child\'s second parent?', coerce=int,
        choices=[(1,'Male'), (2,'Female')
        ])
    P2AGE = SelectField('How old is the child\'s second parent or guardian?', coerce=int,
        choices=[(1,'0 - 20'), (2,'20 - 40'), (3,'40 - 60'), (4,'60 - 80'), (5,'80 - 100')
        ])
    P2MRSTA = SelectField('What is the child\'s second partner or guardian\'s current marital status?', coerce=int,
        choices=[(1,'Now married'), (2,'Widowed'), (3,'Divorced'), (4,'Separated'), (5,'Never married')
        ])
    HHTOTALXX = IntegerField('Including children, how many people live in live in this household?', [ InputRequired(),
        NumberRange(min=1, max=10, message="Invalid range, enter a number between 1 and 10")
        ])
    NUMSIBSX = IntegerField('How many siblings does your child have?', [ InputRequired(),
        NumberRange(min=0, max=10, message="Invalid range, enter a number between 1 and 10")
        ])
    HHENGLISH = SelectField('Do you speak English at home?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    CSPEAKX = SelectField('What is the Language spoken by the child at home?', coerce=int,
        choices=[(1,'English'), (2,'Spanish'), (3,'English and Spanish equally'), (4,'A language other than English and Spanish'), (5,'English and another language equally')
        ])
    HHPRTNRSX = SelectField('Does your girlfriend/boyfriend/partner live in the household with this child?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    OWNRNTHB = SelectField('Do you own or rent your household?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    TTLHHINC = SelectField('Which category best fits the total income of all persons in you household over the past 12 months', coerce=int,
        choices=[(1,'$0 - $40,000'), (2,'$40,001 - $100,000'), (3,'$100,001 - $200,000'), (4,'200,001 - $250,000+')
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
    LRNCELL = SelectField('Does your child use the internet for learning activities on a call phone?', coerce=int,
        choices=[(1,'Yes'), (2,'No')
        ])
    CHLDNT = SelectField('How often does this child use the Internet at home often does this child use the Internet at home for learning activities?', coerce=int,
        choices=[(1,'Every day'), (2,'A few times a week'), (3, 'A few times a month'), (4, 'A few times a year'), (5, 'Never')
        ])

class HiddenFields(FlaskForm):
    id_field = HiddenField()
    updated = HiddenField()

class ReCaptcha(FlaskForm):
    recaptcha = RecaptchaField(validators=[Recaptcha()])

class SubmitForm(FlaskForm):
    submit = SubmitField('Submit Answers')

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
    form6 = FamilyDem()
    form7 = Enrichment()
    form8 = Technology()
    form9 = HiddenFields()
    form10 = ReCaptcha()
    form11 = SubmitForm()

    if (form1.validate_on_submit() and form2.validate_on_submit() and form2.validate_on_submit()
        and form4.validate_on_submit() and form5.validate_on_submit() and form6.validate_on_submit()
        and form7.validate_on_submit() and form8.validate_on_submit() and form9.validate_on_submit()
        and form10.validate_on_submit() and form11.validate_on_submit()):

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
        CSPEAKX = request.form['CSPEAKX']
        FOHISTX = request.form['FOHISTX']
        HHENGLISH = request.form['HHENGLISH']
        HHPRTNRSX = request.form['HHPRTNRSX']
        HHTOTALXX = request.form['HHTOTALXX']
        NUMSIBSX = request.form['NUMSIBSX']
        OWNRNTHB = request.form['OWNRNTHB']
        P1REL = request.form['P1REL']
        P2AGE = request.form['P2AGE']
        P2MRSTA = request.form['P2MRSTA']
        P2REL = request.form['P2REL']
        P2SEX = request.form['P2SEX']
        PAR1EMPL = request.form['PAR1EMPL']
        PAR1FTFY = request.form['PAR1FTFY']
        TTLHHINC = request.form['TTLHHINC']
        FHHOME = request.form['FHHOME']
        FHWKHRS = request.form['FHWKHRS']
        SEABSNT = request.form['SEABSNT']
        FCSCHOOL = request.form['FCSCHOOL']
        FCSTDS = request.form['FCSTDS']
        FCTEACHR = request.form['FCTEACHR']
        SEENJOY = request.form['SEENJOY']
        DISTASSI = request.form['DISTASSI']
        SCHLMAGNET = request.form['SCHLMAGNET']
        SCHRTSCHL = request.form['SCHRTSCHL']
        CHLDNT = request.form['CHLDNT']
        INTACC = request.form['INTACC']
        LRNCELL = request.form['LRNCELL']


        # get today's date from function, above all the routes
        id = genID()
        updated = stringdate()
        # the data to be inserted into page
        record = Questions(id,updated, CENREG, ALLGRADEX, SEGRADES, FOBOOKSTX, FOCONCRTX, FOGAMES, FOLIBRAYX, FOMUSEUMX,
                FOSTORY2X, FORESPON, CSPEAKX, FOHISTX, HHENGLISH, HHPRTNRSX, HHTOTALXX,
                NUMSIBSX, OWNRNTHB, P1REL, P2AGE, P2MRSTA, P2REL, P2SEX, PAR1EMPL, PAR1FTFY,
                TTLHHINC, FHHOME, FHWKHRS, SEABSNT, FCSCHOOL, FCSTDS, FCTEACHR,
                SEENJOY, DISTASSI, SCHLMAGNET, SCHRTSCHL, CHLDNT, INTACC, LRNCELL)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = f"Your answers have been submitted."
        return render_template('add_record.html', message=message, id=id)
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
        return render_template('add_record.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9, form10=form10, form11=form11)


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