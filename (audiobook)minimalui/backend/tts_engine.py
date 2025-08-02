from gtts import gTTS

voice_profiles = {
    "Emma (English)": "en",
    "Aarohi (Hindi)": "hi",
    "Ravi (Telugu)": "te"
}

def convert_text_to_speech(text, voice):
    lang_code = voice_profiles.get(voice, "en")
    tts = gTTS(text=text, lang=lang_code, slow=False)
    filename = f"{voice.replace(' ', '_')}_output.mp3"
    tts.save(filename)
    return filename