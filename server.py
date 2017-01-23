from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "khkljhkjhkjl54535kjhk45435hkh5k34kjh534k34k5h34kjl534jkh543"


# YOUR ROUTES GO HERE

@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route("/apply")
def display_application():
    """Allow people to apply for jobs at UberMelon."""

    roles = ["Software Engineer",
             "QA Engineer",
             "Product Manager",
             "Developer Evangelist"
             ]

    return render_template("application-form.html", roles=roles)


@app.route("/thanks", methods=['POST'])
def acknowledge_application():
    """Return page verifying the info applicants submitted."""

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    role = request.form.get("role")
    salary = float(request.form.get("salary"))
    dollar_salary = "${:,.2f}".format(salary)

    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           role=role,
                           salary=dollar_salary
                           )


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
