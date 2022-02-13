from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import datetime
from uuid import uuid4

app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'

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

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Questions(db.Model):
    __tablename__ = 'NHES_19_PFI'
    id = db.Column(db.Integer, primary_key=True)
    ALLGRADEX = db.Column(db.Integer)
    # SEGRADES = db.Column(db.Integer)
    # CENREG = db.Column(db.Integer)
    # SCH_TYPE = db.Column(db.Integer)
    # EDCPUB = db.Column(db.Integer)
    # EDCCAT = db.Column(db.Integer)
    # EDCREL = db.Column(db.Integer)
    # EDCPRI = db.Column(db.Integer)
    # EDCINTK12 = db.Column(db.Integer)
    # EDCHSFL = db.Column(db.Integer)
    # DISTASSI = db.Column(db.Integer)
    # SCHRTSCHL = db.Column(db.Integer)
    # SCHLMAGNET = db.Column(db.Integer)
    # SPBSCH = db.Column(db.Integer)
    # SOTHRSCH = db.Column(db.Integer)
    # STUTR = db.Column(db.Integer)
    # SOTHSCH = db.Column(db.Integer)
    # SEENJOY = db.Column(db.Integer)
    # SEABSNT = db.Column(db.Integer)
    # FCSCHOOL = db.Column(db.Integer)
    # FCTEACHR = db.Column(db.Integer)
    # FCSTDS = db.Column(db.Integer)
    # FCSUPPRT = db.Column(db.Integer)
    # FHHOME = db.Column(db.Integer)
    # FHWKHRS = db.Column(db.Integer)
    # FOSTORY2X = db.Column(db.Integer)
    # FOCRAFTS = db.Column(db.Integer)
    # FOGAMES = db.Column(db.Integer)
    # FOBUILDX = db.Column(db.Integer)
    # FOSPORT = db.Column(db.Integer)
    # FORESPON = db.Column(db.Integer)
    # FOHISTX = db.Column(db.Integer)
    # FODINNERX = db.Column(db.Integer)
    # FOLIBRAYX = db.Column(db.Integer)
    # FOBOOKSTX = db.Column(db.Integer)
    # FOCONCRTX = db.Column(db.Integer)
    # FOMUSEUMX = db.Column(db.Integer)
    # FOZOOX = db.Column(db.Integer)
    # FOGROUPX = db.Column(db.Integer)
    # FOSPRTEVX = db.Column(db.Integer)
    # HHENGLISH = db.Column(db.Integer)
    # CSPEAKX = db.Column(db.Integer)
    # HHTOTALXX = db.Column(db.Integer)
    # HHPRTNRSX = db.Column(db.Integer)
    # P1REL = db.Column(db.Integer)
    # P1SEX = db.Column(db.Integer)
    # P1MRSTA = db.Column(db.Integer)
    # P1AGE = db.Column(db.Integer)
    # P2GUARD = db.Column(db.Integer)
    # P2AGE = db.Column(db.Integer)
    # P2REL = db.Column(db.Integer)
    # P2SEX = db.Column(db.Integer)
    # P2MRSTA = db.Column(db.Integer)
    # PAR1EMPL = db.Column(db.Integer)
    # PAR1FTFY = db.Column(db.Integer)
    # PAR2FTFY = db.Column(db.Integer)
    # NUMSIBSX = db.Column(db.Integer)
    # TTLHHINC = db.Column(db.Integer)
    # OWNRNTHB = db.Column(db.Integer)
    # HVINTSPHO = db.Column(db.Integer)
    # HVINTCOM = db.Column(db.Integer)
    # INTACC = db.Column(db.Integer)
    # CHLDNT = db.Column(db.Integer)
    # LRNCOMP = db.Column(db.Integer)
    # LRNTAB = db.Column(db.Integer)
    # LRNCELL = db.Column(db.Integer)

    def __init__(self,id,ALLGRADEX):
    
                # SEGRADES,CENREG,SCH_TYPE,EDCPUB,EDCCAT,EDCREL,EDCPRI,
                # EDCINTK12,EDCHSFL,DISTASSI,SCHRTSCHL,SCHLMAGNET,SPBSCH,SOTHRSCH, 
                # STUTR,SOTHSCH,SEENJOY,SEABSNT,FCSCHOOL,FCTEACHR,FCSTDS,FCSUPPRT, 
                # FHHOME,FHWKHRS,FOSTORY2X,FOCRAFTS,FOGAMES,FOBUILDX,FOSPORT,FORESPON,
                # FOHISTX,FODINNERX,FOLIBRAYX,FOBOOKSTX,FOCONCRTX,FOMUSEUMX,FOZOOX,FOGROUPX,
                # FOSPRTEVX,HHENGLISH,CSPEAKX,HHTOTALXX,HHPRTNRSX,P1REL,P1SEX,P1MRSTA,
                # P1AGE,P2GUARD,P2AGE,P2REL,P2SEX,P2MRSTA,PAR1EMPL,PAR1FTFY,PAR2FTFY,
                # NUMSIBSX,TTLHHINC,OWNRNTHB,HVINTSPHO,HVINTCOM,INTACC,CHLDNT,LRNCOMP,
                # LRNTAB,LRNCELL):
        
        self.id = id
        self.ALLGRADEX = ALLGRADEX
        # self.SEGRADES = SEGRADES
        # self.CENREG = CENREG
        # self.SCH_TYPE = SCH_TYPE
        # self.EDCPUB = EDCPUB
        # self.EDCCAT = EDCCAT
        # self.EDCREL = EDCREL
        # self.EDCPRI = EDCPRI
        # self.EDCINTK12 = EDCINTK12
        # self.EDCHSFL = EDCHSFL
        # self.DISTASSI = DISTASSI
        # self.SCHRTSCHL = SCHRTSCHL
        # self.SCHLMAGNET = SCHLMAGNET
        # self.SPBSCH = SPBSCH
        # self.SOTHRSCH = SOTHRSCH
        # self.STUTR = STUTR
        # self.SOTHSCH = SOTHSCH
        # self.SEENJOY = SEENJOY
        # self.SEABSNT = SEABSNT
        # self.FCSCHOOL = FCSCHOOL
        # self.FCTEACHR = FCTEACHR
        # self.FCSTDS = FCSTDS
        # self.FCSUPPRT = FCSUPPRT
        # self.FHHOME = FHHOME
        # self.FHWKHRS = FHWKHRS
        # self.FOSTORY2X = FOSTORY2X
        # self.FOCRAFTS = FOCRAFTS
        # self.FOGAMES = FOGAMES
        # self.FOBUILDX = FOBUILDX
        # self.FOSPORT = FOSPORT
        # self.FORESPON = FORESPON
        # self.FOHISTX = FOHISTX
        # self.FODINNERX = FODINNERX
        # self.FOLIBRAYX = FOLIBRAYX
        # self.FOBOOKSTX = FOBOOKSTX
        # self.FOCONCRTX = FOCONCRTX
        # self.FOMUSEUMX = FOMUSEUMX
        # self.FOZOOX = FOZOOX
        # self.FOGROUPX = FOGROUPX
        # self.FOSPRTEVX = FOSPRTEVX
        # self.HHENGLISH = HHENGLISH
        # self.CSPEAKX = CSPEAKX
        # self.HHTOTALXX = HHTOTALXX
        # self.HHPRTNRSX = HHPRTNRSX
        # self.P1REL = P1REL
        # self.P1SEX = P1SEX
        # self.P1MRSTA = P1MRSTA
        # self.P1AGE = P1AGE
        # self.P2GUARD = P2GUARD
        # self.P2AGE = P2AGE
        # self.P2REL = P2REL
        # self.P2SEX = P2SEX
        # self.P2MRSTA = P2MRSTA
        # self.PAR1EMPL = PAR1EMPL
        # self.PAR1FTFY = PAR1FTFY
        # self.PAR2FTFY = PAR2FTFY
        # self.NUMSIBSX = NUMSIBSX
        # self.TTLHHINC = TTLHHINC
        # self.OWNRNTHB = OWNRNTHB
        # self.HVINTSPHO = HVINTSPHO
        # self.HVINTCOM = HVINTCOM
        # self.INTACC = INTACC
        # self.CHLDNT = CHLDNT
        # self.LRNCOMP = LRNCOMP
        # self.LRNTAB = LRNTAB
        # self.LRNCELL = LRNCELL

class AddRecord(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    ALLGRADEX = IntegerField('What is this child’s current grade, grade equivalent, or year of school?', [ InputRequired(),
        NumberRange(min=1, max=12, message="Invalid range")
        ])
    # FODINNERX = IntegerField('In the past week, how many days has your family eaten the evening meal together?', [ InputRequired(),
    #     NumberRange(min=0, max=7, message="Invalid range")
    #     ])
    # FOREADTOX = IntegerField('How many times have you or someone in your family read to this child the past week?', [ InputRequired(),
    #     NumberRange(min=0, max=999, message="Invalid range")
    #     ])
    # FORDDAYX = IntegerField('About how many minutes on each of those times did you or someone in your family read to this child?', [ InputRequired(),
    #     NumberRange(min=0, max=999, message="Invalid range")
    #     ])
    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')

# +++++++++++++++++++++++
# get local date - does not account for time zone
# note: date was imported at top of script
def stringdate():
    today = datetime.today()
    date_list = str(today).split('-')
    # build string in format 01-01-2000
    date_string = date_list[1] + "-" + date_list[2] + "-" + date_list[0]
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
    form1 = AddRecord()
    if form1.validate_on_submit():
        ALLGRADEX = request.form['ALLGRADEX']
        # FOREADTOX = request.form['FOREADTOX']
        # FORDDAYX = request.form['FORDDAYX']
        # get today's date from function, above all the routes
        id = genID()
        updated = stringdate()
        # the data to be inserted into questionair model - the table
        record = Questions(id, ALLGRADEX)#, FODINNERX, FOREADTOX, FORDDAYX, updated)
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
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record.html', form1=form1)

# result of edit - this function updates the record
@app.route('/edit_result', methods=['POST'])
def edit_result():
    id = request.form['id_field']
    # call up the record from the database
    questions = Questions.query.filter(Questions.id == id).first()
    # update all values
    ALLGRADEX = request.form['ALLGRADEX']
    FODINNERX = request.form['FODINNERX']
    FOREADTOX = request.form['FOREADTOX']
    FORDDAYX = request.form['FORDDAYX']
    # get today's date from function, above all the routes
    questions.updated = stringdate()

    form1 = AddRecord()
    if form1.validate_on_submit():
        # update database record
        db.session.commit()
        # create a message to send to the template
        message = f"Your answers have been updated."
        return render_template('result.html', message=message)
    else:
        # show validaton errors
        questions.id = id
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('edit_or_delete.html', form1=form1, questions=questions, choice='edit')


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