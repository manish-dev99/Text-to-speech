# print("How to push code in github.")
import subprocess

while True:
    text = input("You: ")

    if text.lower() == "exit":
        break

    if not text.strip():
        continue

    subprocess.run([
        "python",
        "-m",
        "piper",
        "-m",
        "en_US-lessac-medium",
        "--output_file",
        "speech.wav"
    ], input=text.encode())

    # Play the generated WAV file
    subprocess.run([
        "powershell",
        "-c",
        "(New-Object Media.SoundPlayer 'speech.wav').PlaySync()"
    ])