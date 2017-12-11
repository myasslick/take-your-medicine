import datetime
import sqlite3

import bottle
from twilio import twiml

db_conn = sqlite3.connect("app.db")

def record_yes():
    """Record user's confirmation to database, including
    the date and the time the confirmation was received."""

    # This context manager will automatically rollback/commit
    with db_conn:
        cursor = db_conn.cursor()

        # Use UTC timestamp because SQLite timestamp type
        # accepts UTC, and the best practice is to convert
        # the stored timestamp to local time when "presenting".
        data = (datetime.datetime.utcnow(),)

        # The confirmed table has two columns:
        # pk (int, auto), datetime
        cursor.execute(
            "INSERT INTO confirmed VALUES (?)", data)

# uWSGI will search for "application"
app = application = bottle.Bottle()

@app.route("/sms", method="POST")
def sms_views():
    number = request.form['From']
    message_body = request.form['Body']

    if message_body.lower() in ("y", "yes"):
        record_yes()
        response = twiml.Response()
        response.message("Acked!")
        return str(response)

if __name__ == '__main__':
    run(host='localhost', port=8000)
else:
    application = default_app()
