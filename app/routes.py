from app import app
from flask import render_template, redirect
from app.forms import CreateIssue
from app.jira import SubmitForm


@app.route("/", methods=["GET", "POST"])
def issue():
    form = CreateIssue()
    if form.validate_on_submit():
        with open("formData.txt", "w") as file:
            file.writelines(str(form.data))  # Export form data
        return redirect("/success"), SubmitForm()
    return render_template("create-issue.html", title="Create Issue", form=form)


@app.route("/success")
def success():
    return render_template("issue-submitted.html", title="Success")
