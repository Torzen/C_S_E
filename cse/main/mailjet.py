from mailjet_rest import Client
import authDetail  # To retrieving authentication detail
def sendMail(reciever,heading = 'Got mail from someone', subject = "default body",messageBody = 'default message bdy'):
    api_key = authDetail.getKey()
    api_secret = authDetail.getSecreat()
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "csebrtmail09@gmail.com",
            "Name": heading
        },
        "To": [
            {
            "Email": reciever,
            # "Name": "name"
            }
        ],
        "Subject": subject,
        "TextPart": messageBody,
        # "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
        "CustomID": "AppGettingStartedTest"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    # print(result.status_code)
    if str(result.status_code) == '200':
        return 'sucessfull'
    else:
        return "Something went wrong try later"

    # print(result.json())
