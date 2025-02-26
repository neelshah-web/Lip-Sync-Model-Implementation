# Lip Sync Model Implementation

This project implements an open-source lip sync model to generate lip-synced videos based on an input image and audio file.

## **Setup Instructions**

### **1️⃣ Create a Virtual Environment**
Open **Command Prompt (cmd)** and run:
```sh
python3 -m venv wav2lip-env
```

### **2️⃣ Activate the Virtual Environment**
For **Windows (Command Prompt):**
```sh
wav2lip-env\Scripts\activate
```

### **3️⃣ Install Dependencies**
Run the following commands inside the activated virtual environment:
```sh
pip install torch
pip install opencv-python-headless  # If you don't need GUI functions like imshow()
pip install librosa==0.8.1
pip install numpy==1.22.4 scipy==1.8.1
pip install tqdm
pip install gtts
```

---
## **Generating the Audio File**
Create a Python script named **`generate_audio.py`** and paste the following code:

```python
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
```

Run the script to generate the audio file:
```sh
python generate_audio.py
```

---
## **Running the Lip Sync Model**
Execute the following command to generate the lip-synced video:
```sh
python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face input_image.jpeg --audio audio.wav --outfile output.mp4
```

---
## **Playing the Generated Video**
Use the following command to play the output video:
```sh
ffplay output.mp4
```

---
## **Additional Notes**
- Ensure that `input_image.jpeg` and `audio.wav` exist in the project directory.
- The model checkpoint file `wav2lip_gan.pth` must be placed inside the `checkpoints/` directory.
- If `ffplay` is not installed, you can play the video using any media player (e.g., VLC, MPV).

---
## **Contributors**
- **Your Name**  
- **GitHub Repository:** [GitHub Link Here]

---
## **License**
This project is for educational purposes only. Refer to the original [Wav2Lip repository](https://github.com/Rudrabha/Wav2Lip) for licensing details.

---

### 🚀 Happy Coding! 🎬

