import requests

filename = input("Please select your file: ")

text_file = open(filename, mode="r", encoding='utf-8')
text = text_file.read()
text_file.close()

key = "1db01788ad86488d90d573a7fe502c11"
auth_url = "https://eastasia.api.cognitive.microsoft.com/sts/v1.0/issueToken"
lang_url = "https://eastasia.tts.speech.microsoft.com/cognitiveservices/voices/list"
text_to_speech_url = "https://eastasia.tts.speech.microsoft.com/cognitiveservices/v1"

auth_headers = {"Ocp-Apim-Subscription-Key": key, "Content-Length": "0",
                "Content-type": "application/x-www-form-urlencoded"}
auth_response = requests.post(auth_url, headers=auth_headers)
token = auth_response.text
print(token)

lang_headers = {"Authorization": "Bearer " + token}
lang_response = requests.get(lang_url, headers=lang_headers)
json_langs = lang_response.json()

for id, dictor in enumerate(json_langs):
    print(id, ")", dictor['ShortName'], ",", dictor['Gender'], ",", dictor['Locale'])

selectedDictor = json_langs[int(input("Select dictor: "))]

text_to_speech_headers = {
    "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",
    "Content-Type": "application/ssml+xml",
    "Content-Length": "225",
    "Authorization": "Bearer " + token
}
text_to_speech_data = """
            <speak version='1.0' xml:lang='{Locale}'>
                <voice 
                    xml:lang='{Locale}' 
                    xml:gender='{Gender}' 
                    name='{Name}'>
                        {Text}
                </voice>
            </speak>
            """.format(Locale=selectedDictor['Locale'], Gender=selectedDictor['Gender'], Name=selectedDictor['ShortName'], Text=text)
text_to_speech_response = requests.post(text_to_speech_url, data=text_to_speech_data.encode(
    'utf-8'), headers=text_to_speech_headers, stream=True)

audio_file = open(filename[:-4] + "_converted_by_" + selectedDictor['ShortName'] + ".mp3", "wb")
for chunk in text_to_speech_response.iter_content(chunk_size=128):
    audio_file.write(chunk)
audio_file.close()