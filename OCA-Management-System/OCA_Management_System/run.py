from app import create_app
from flask import request, redirect, url_for

app = create_app()
@app.route('/submit_event', methods=['POST'])
def submit_event():
    event_name = request.form.get('name')
    date = request.form.get('date')
    data = f"Event Submission:\nEvent Name: {event_name}\nDate: {date}\n\n"
    with open("submissions.txt", "a") as file:
        file.write(data)
    return redirect(url_for('index'))
@app.route('/room_booking', methods=['POST'])
def room_booking():
    room_id = request.form.get('room_id')
    data = f"Room Booking:\nRoom ID: {room_id}\n\n"
    with open("submissions.txt", "a") as file:
        file.write(data)
    return redirect(url_for('index'))
@app.route('/submit_budget', methods=['POST'])
def submit_budget():
    club_name = request.form.get('club_name')
    amount = request.form.get('amount')
    data = f"Budget Request:\nClub Name: {club_name}\nAmount: {amount}\n\n"
    with open("submissions.txt", "a") as file:
        file.write(data)
    return redirect(url_for('index'))
@app.route('/send_message', methods=['POST'])
def send_message():
    sender = request.form.get('sender')
    receiver = request.form.get('receiver')
    message = request.form.get('message')
    data = f"Message:\nSender: {sender}\nReceiver: {receiver}\nMessage: {message}\n\n"
    with open("submissions.txt", "a") as file:
        file.write(data)
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)