import json
import requests
import urllib3
import time
from os import getenv
from ast import literal_eval


def SubmitForm():

    # Import Form Data
    with open("formData.txt", mode="r") as form:
        formRaw = form.read()
        formData = literal_eval(formRaw)

    issueType = formData.get("issueType")
    issueTitle = formData.get("issueTitle")
    issueAs = formData.get("issueAs")
    issueWant = formData.get("issueWant")
    issueThat = formData.get("issueThat")
    issueStakeholder = formData.get("issueStakeholder")
    issueAssign = formData.get("issueAssign")

    # Formatting Issue Title and Description
    if issueThat[0] is not "I":
        issueThat = issueThat[0].lower() + issueThat[1:]

    issueTitle = f"{issueType} - {issueTitle}"
    issueDescription = f"As a {issueAs} I want {issueWant[0].lower() + issueWant[1:]} so that {issueThat}."

    # Updating Payload Template with Form Data
    with open("rawPayload.txt", mode="r") as payload:
        payloadRaw = payload.read()
        payloadData = literal_eval(payloadRaw)

    username = getenv("username")

    payloadData["fields"].update({"summary": issueTitle, "description": issueDescription})
    payloadData["fields"]["reporter"].update({"name": username})

    if issueAssign is True:  # Assign issue to submitter if requested
        payloadData["fields"]["assignee"].update({"name": username})

    payloadData["fields"]["customfield_10207"].update({"name": issueStakeholder, "key": issueStakeholder})

    jsonPayload = json.dumps(payloadData)  # Convert Dictionary to JSON

    # POST Payload to JIRA
    jiraEndpoint = "http://jirap.stifel.com:8080/rest/api/latest/issue"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "aaa05642-d9b4-4c80-b563-c9bc83fd3784,94c8161e-a351-4518-b02d-e1ef047be905",
        'Host': "jirap.stifel.com:8080",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "386",
        'Cookie': "JSESSIONID=EA9F024816E7C82FCBD77B2A187290D7; atlassian.xsrf.token=B1TB-VPMQ-5FFS-6XQD_1b57db0c3b28a7305e4bda53ad1361e8320fa0c0_lin",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    request = requests.post(jiraEndpoint, headers=headers, data=jsonPayload)

    if request.status_code != 201:
        print("Something went wrong.")
        raise ConnectionError(f"Unable to submit form to Jira. Request returned {request.status_code}")

    time.sleep(1)  # Prevent connection stream from immediately closing
