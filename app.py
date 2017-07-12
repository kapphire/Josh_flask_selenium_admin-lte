from flask import Flask, render_template, request, jsonify
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from scrapping.bet365 import bet365_scrapping
from scrapping.bet10 import bet10_scrapping
from scrapping.titanbet import titan_scrapping
from scrapping.betfred import betfred_scrapping
from scrapping.coral import coral_scrapping
from scrapping.eight88 import eight88_scrapping
from scrapping.ladbrokes import ladbrokes_scrapping
from scrapping.netbet import netbet_scrapping
from scrapping.paddy import paddy_scrapping
from scrapping.real import real_scrapping
from scrapping.stan import stan_scrapping

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/josh'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email


class Bet365(db.Model):
    __tablename__ = "bet365s"
    id = db.Column(db.Integer, primary_key=True)
    sports = db.Column(db.Float)
    casino = db.Column(db.Float)
    poker = db.Column(db.Float)
    games_bingo = db.Column(db.Float)
    total = db.Column(db.Float)
    withdrawal = db.Column(db.Float)
    balance = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class Eight88(db.Model):
    __tablename__ = "eight88s"
    id = db.Column(db.Integer, primary_key=True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    lead = db.Column(db.Integer)
    money_player = db.Column(db.Integer)
    balance = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class Bet10(db.Model):
    __tablename__ = "bet10s"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class RealDeal(db.Model):
    __tablename__ = "realDeals"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class LadBroke(db.Model):
    __tablename__ = "ladBrokes"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class BetFred(db.Model):
    __tablename__ = "betFreds"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class Paddy(db.Model):
    __tablename__ = "paddyies"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class NetBet(db.Model):
    __tablename__ = "netBets"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class TitanBet(db.Model):
    __tablename__ = "titanBets"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class Stan(db.Model):
    __tablename__ = "stans"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.Float)

    def __init__(self, email):
        self.id = id


class Coral(db.Model):
    __tablename__ = "corals"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.Float)

    def __init__(self, email):
        self.id = id



@app.route('/')
def dashboard():
	return render_template('home.html')


@app.route('/bet365/')
def bet365():
	data = bet365_scrapping()
	return render_template('pages/bet365.html', data = data)


@app.route('/eight88/')
def eight88():
	data = eight88_scrapping()
	return render_template('pages/eight88.html', data = data)


@app.route('/bet10/')
def bet10():
	data = bet10_scrapping()
	return render_template('pages/bet10.html', data = data)


@app.route('/realDeal/')
def realDeal():
	data = real_scrapping()
	return render_template('pages/realDeal.html', data = data)


@app.route('/ladBroke/')
def ladBroke():
	data = ladbrokes_scrapping()
	return render_template('pages/ladBroke.html', data = data)


@app.route('/betFred/')
def betFred():
	data = betfred_scrapping()
	return render_template('pages/betFred.html', data = data)


@app.route('/paddy/')
def paddy():
	data = paddy_scrapping()
	return render_template('pages/paddy.html', data = data)


@app.route('/netBet/')
def netBet():
	data = netbet_scrapping()
	return render_template('pages/netBet.html', data = data)


@app.route('/titanBet/')
def titanBet():
	data = titan_scrapping()
	return render_template('pages/titanBet.html', data = data)


@app.route('/stan/')
def stan():
	data = stan_scrapping()
	return render_template('pages/stan.html', data = data)


@app.route('/coral/')
def coral():
	data = coral_scrapping()
	return render_template('pages/coral.html', data = data)


@app.route('/skyBet')
def skyBet():
    data = "Woops, credential is not valid. Please tell me account info."
    return render_template('pages/error.html', data = data)


@app.route('/william')
def william():
    data = "Woops, credential is not valid. Please tell me account info."
    return render_template('pages/error.html', data = data)


@app.route('/victor')
def victor():
    data = "Woops, credential is not valid. Please tell me account info."
    return render_template('pages/error.html', data = data)


if __name__ == '__main__':
	app.debug = True
	app.run()