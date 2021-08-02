import os
from slack_bolt import App
import requests

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.command("/tex")
def tex(ack, say, command):
    content = command['text']
    # replace url
    r = requests.post('http://0.0.0.0:5000/', json={"tex": content})
    code = r.status_code
    print("Code: " + str(code))
    if code != 204:
        ack()
        say("Syntax Error: " + content)
        return None
    ack()
    # replace image_url
    say(
        blocks = [
            {
                "type": "image",
                "image_url": "https://afb6aa371817.ngrok.io/output/output.png",
                "alt_text": "TeX"
            }
        ],
        text=f"{command['text']}"
    )

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
