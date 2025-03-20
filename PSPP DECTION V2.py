import mediapipe as mp
import cv2
import pyautogui
import threading

# Disable PyAutoGUI fail-safe (Use with caution)
pyautogui.FAILSAFE = False  

class PSPPoseController:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.85, min_tracking_confidence=0.85)
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_pose(self, image):
        """Detects pose landmarks in the given image."""
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)
        return results

    def get_posture(self, image, results):
        """Determines posture based on pose landmarks."""
        if not results.pose_landmarks:
            return "None"
        
        height, width, _ = image.shape
        landmarks = results.pose_landmarks.landmark

        # Extract key points
        left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_wrist = landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST]
        right_wrist = landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST]
        nose = landmarks[self.mp_pose.PoseLandmark.NOSE]  # Head tracking

        # Calculate positions
        center_x = width // 2
        left_x = int(left_shoulder.x * width)
        right_x = int(right_shoulder.x * width)
        left_wrist_y = int(left_wrist.y * height)
        right_wrist_y = int(right_wrist.y * height)
        mid_shoulder_y = (left_shoulder.y + right_shoulder.y) / 2 * height
        head_x = int(nose.x * width)
        head_y = int(nose.y * height)

        # Head movement detection (New addition)
        if head_x < center_x - 100:
            return "D-Pad Left"
        elif head_x > center_x + 100:
            return "D-Pad Right"
        elif head_y < height * 0.3:
            return "D-Pad Up"
        elif head_y > height * 0.7:
            return "D-Pad Down"

        # Hand-based controls
        if left_wrist_y < height * 0.3:
            return "Square"
        elif left_wrist_y > height * 0.7:
            return "Cross"
        elif right_wrist_y < height * 0.3:
            return "Triangle"
        elif right_wrist_y > height * 0.7:
            return "Circle"

        # Block detection (both hands together)
        if abs(left_wrist.x - right_wrist.x) < 0.1 and abs(left_wrist_y - right_wrist_y) < 40:
            return "Block"

        return "None"

    def control_psp(self, posture):
        """Maps postures to PSP key presses."""
        key_map = {
            "D-Pad Up": "up",
            "D-Pad Down": "down",
            "D-Pad Left": "left",
            "D-Pad Right": "right",
            "Square": "d",
            "Cross": "z",
            "Circle": "a",
            "Triangle": "s",
            "Block": "w",
            "Start": "enter",
            "Select": "shift"
        }

        if posture in key_map:
            try:
                pyautogui.keyDown(key_map[posture])
                pyautogui.keyUp(key_map[posture])
            except pyautogui.FailSafeException:
                print("FailSafe triggered! Move the mouse away from the screen corners.")

    def run(self):
        """Captures video and processes pose detection in real-time."""
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Lower resolution for speed
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        cap.set(cv2.CAP_PROP_FPS, 60)  # Higher FPS for fast response

        def process_video():
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                results = self.detect_pose(frame)
                posture = self.get_posture(frame, results)
                self.control_psp(posture)

                cv2.putText(frame, posture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("PSP Controller", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        video_thread = threading.Thread(target=process_video, daemon=True)
        video_thread.start()
        video_thread.join()

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    controller = PSPPoseController()
    controller.run()
