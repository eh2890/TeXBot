import os
from slack_bolt import App
import requests
from datetime import datetime

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.command("/tex")
def tex(ack, say, command):
    content = command['text']
    # replace url
    dt = str(datetime.now())
    dt = dt.replace(" ", "")
    r = requests.post('http://18.188.220.199:8000/', json={"tex": content, "dt": dt})
    code = r.status_code
    print("Code: " + str(code))
    if code != 204:
        ack()
        say("Syntax Error: " + content)
        return None
    url = "http://18.188.220.199:8000/output/output" + dt + ".png"
    print(url)
    ack()
    # replace image_url
    say(
        blocks = [
            {
                "type": "image",
                "image_url": "http://18.188.220.199:8000/output/output" + dt + ".png",
                "alt_text": "TeX"
            }
        ],
        text=f"{command['text']}"
    )
    say("Content: " + content)

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
