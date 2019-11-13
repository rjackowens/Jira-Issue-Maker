from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CreateIssue(FlaskForm):
    issueType = SelectField("Select Application:", choices=[("Azure DevOps", "Azure DevOps"), ("TeamCity", "TeamCity"), ("Octopus", "Octopus"), ("Artifactory", "Artifactory"), ("Jira", "Jira"), ("TFS", "TFS"), ("GIT", "GIT"), ("AWS", "AWS"), ("Other", "Other")])
    issueTitle = StringField("Issue Title", validators=[DataRequired()])
    issueAs = StringField("As a", validators=[DataRequired()])
    issueWant = StringField("I want", validators=[DataRequired()])
    issueThat = StringField("So that", validators=[DataRequired()])
    issueStakeholder = StringField("Stakeholder Username", validators=[DataRequired()])

    issueAssign = BooleanField("Assign to Me")
    issueSubmit = SubmitField("Submit")
