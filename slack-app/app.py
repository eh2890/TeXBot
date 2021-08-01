import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.command("/echo")
def repeat_text(ack, say, command):
    print("echo")
    content = command['text']
    replaced = content.replace("\\", "\\\\")
    ack()
    say(f"{replaced}")
    say(f"{command['text']}")

@app.command("/tex")
def tex(ack, say, command):
    ack()
    say(
        blocks = [
            {
                "type": "image",
                "image_url": "https://i1.wp.com/thetempest.co/wp-content/uploads/2017/08/The-wise-words-of-Michael-Scott-Imgur-2.jpg?w=1024&ssl=1",
                "alt_text": "inspiration"
            }
        ],
        text=f"{command['text']}"
    )



# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
