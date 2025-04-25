🎮 PSP Pose Controller – Control PSP Emulator Using Body Movements!
🚀 PSP Pose Controller is an innovative Python-based project that enables users to control a PSP emulator using body movements detected via a webcam! It leverages MediaPipe Pose, OpenCV, and PyAutoGUI to map different postures to PSP button presses.

🔥 Features 
✅ Hand-Free PSP Control – Move your body to simulate D-Pad, buttons, and analog stick inputs.
✅ MediaPipe Pose Detection – Uses AI-powered pose estimation to track shoulders, wrists, and body posture.
✅ Custom Key Mapping – Simulates PSP controls (D-Pad, Cross, Circle, Square, Triangle, etc.).
✅ Real-Time Detection – Works with a standard webcam at 30 FPS.
✅ Lightweight & Easy to Use – Requires only Python and a webcam!

🎮 How It Works
The program captures live video from your webcam.
It uses Google MediaPipe Pose to track shoulders & wrists.
Specific body positions & hand movements trigger PSP button presses via PyAutoGUI.

🕹️ Control Mappings
Movement	PSP Button
Move shoulders left	D-Pad Left
Move shoulders right	D-Pad Right
Raise shoulders	D-Pad Up
Lower shoulders	D-Pad Down
Hands close together	Cross (✖️)
Raise right hand	Circle (⭕)
Raise left hand	Triangle (🔺)
Lower left hand	Square (⬜)
Lean left	Analog Left
Lean right	Analog Right
Lean forward	Analog Up
Lean backward	Analog Down
Extend left arm forward	L Button (L1)
Extend right arm forward	R Button (R1)
🛠️ Installation & Setup
1️⃣ Install Dependencies
pip install mediapipe opencv-python pyautogui
2️⃣ Run the Program
python psp_pose_controller.py
3️⃣ Control Your PSP Emulator! 🎮
📝 Requirements
Python 3.7+
Webcam (for real-time tracking)
PPSSPP Emulator (for PSP gaming)
🚀 Future Improvements
🏆 Gesture Customization – Add user-configurable mappings.
🎥 Improved Pose Detection – Enhance accuracy with AI tuning.
📱 Mobile Support – Extend to Android/iOS apps.


## License

This project is for **educational and research reference only**.

🛑 **Unauthorized use, reproduction, or distribution of this code is strictly prohibited.**
Please contact the author for permission.

