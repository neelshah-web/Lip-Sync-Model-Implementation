from gtts import gTTS

script = """Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit 
card dues. Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which 
needs to be paid by 31st December 2024. Missing this payment could lead to two significant consequences:
First, a late fee will be added to your outstanding balance. Second, your credit score will be negatively 
impacted, which may affect your future borrowing ability. Make your payment by clicking the link here...
Pay through UPI or bank transfer. Thank you!"""

tts = gTTS(text=script, lang='en', tld='co.in')  # Indian accent
tts.save("audio.wav")
print("Audio file generated: audio.wav")
