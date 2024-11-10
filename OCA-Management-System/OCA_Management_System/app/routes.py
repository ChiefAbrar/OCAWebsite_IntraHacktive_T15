from flask import Blueprint, request, redirect, url_for, render_template
from .models import db, Event, Room, Budget, Communication

main_routes = Blueprint("main_routes", __name__)
@main_routes.route('/')
def index():
    return render_template("index.html")
@main_routes.route('/submit_event', methods=['POST'])
def submit_event():
    name = request.form['name']
    date = request.form['date']
    new_event = Event(name=name, date=date)
    db.session.add(new_event)
    db.session.commit()
    return redirect(url_for('main_routes.index'))
@main_routes.route('/room_booking', methods=['POST'])
def room_booking():
    room_id = request.form['room_id']
    room = Room.query.get(room_id)
    if room:
        room.is_booked = True
        db.session.commit()
    return redirect(url_for('main_routes.index'))
@main_routes.route('/submit_budget', methods=['POST'])
def submit_budget():
    club_name = request.form['club_name']
    amount = request.form['amount']
    new_budget = Budget(club_name=club_name, amount_requested=amount)
    db.session.add(new_budget)
    db.session.commit()
    return redirect(url_for('main_routes.index'))
@main_routes.route('/send_message', methods=['POST'])
def send_message():
    sender = request.form['sender']
    receiver = request.form['receiver']
    message = request.form['message']
    comm = Communication(sender=sender, receiver=receiver, message=message)
    db.session.add(comm)
    db.session.commit()
    return redirect(url_for('main_routes.index'))