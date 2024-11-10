import pandas as pd
from app.models import db, Event
def generate_report():
    events = Event.query.all()
    data = [(e.id, e.name, e.date, e.status) for e in events]
    df = pd.DataFrame(data, columns=['Event ID', 'Name', 'Date', 'Status'])
    summary = df.describe()
    print("Summary:\n", summary)
    df.to_csv("event_report.csv", index=False)