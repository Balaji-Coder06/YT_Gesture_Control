🖐️ YouTube Gesture Control using Python & MediaPipe
Control YouTube playback with your hand gestures using your webcam 🎥  
This project uses Python, OpenCV, MediaPipe, and PyAutoGUI.

📂 Files
- `yt_gesture_control.py`: Main Python script
- `requirements.txt`: List of required Python packages

⚙️ Requirements
- Python 3.9 or 3.10 (recommended)
- Webcam

📦 Installation
 1. Clone the repository:
bash
git clone https://github.com/your-username/yt-gesture-control.git
cd yt-gesture-control
 2. Create a virtual environment (optional but recommended):
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
 3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the Script
Make sure your webcam is connected.
Then simply run:
bash
Copy
Edit
python yt_gesture_control.py
Open a YouTube video in your browser before running this!

✋ Hand Gesture Controls
Gesture	Action
Open Palm	Play Video
Fist	Pause Video
Swipe Right	Forward 10 sec
Swipe Left	Rewind 10 sec

🧠 Built With
MediaPipe
OpenCV
PyAutoGUI

🤝 Contributing
Feel free to fork, improve, and send pull requests!
