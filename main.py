import asyncio
import edge_tts
from modules.playAudio import play_audio
from modules.recognizeAudio import recognize_audio
import json
import requests

done = False
while not done:
    user = recognize_audio("alfred")
    if user == "stop":
        done = True

    requestData = requests.post("https://api.carterlabs.ai/chat", headers={
        "Content-Type": "application/json"
    }, data=json.dumps({
        "text": user,
        "key": "8cfa7e30-4640-47b4-80ad-a038b428be2a",
        "user_id": "Rishan Pancham", # THIS CAN BE ANYTHING YOU WANT!
        "speak": False # DEFAULT FALSE | FOR VOICE OUTPUT
    }))

    data = requestData.json()
    output = data["output"]
    response = output["text"]

    TEXT = response
    VOICE = "en-GB-RyanNeural"
    OUTPUT_FILE = "StreamFile.mp3"

    async def generate() -> None:
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(OUTPUT_FILE)

    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(generate())
    except RuntimeError as e:
        print(e)

    play_audio(OUTPUT_FILE)

