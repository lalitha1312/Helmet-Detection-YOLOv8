import cv2    
import os

video_path = 'bike3.mp4'
output_dir = r"C:\Users\lalitha\Downloads\yolov8helmetdetection-main\images"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_count = 0
max_frames = 60 # Limit to 50 frames

while frame_count < max_frames:
    ret, frame = cap.read()
    if not ret:
        print(f"Video ended early. Total frames extracted: {frame_count}")
        break

    frame = cv2.resize(frame, (1080, 500))
    image_path = os.path.join(output_dir, f"helmet_{frame_count}.jpg")
    cv2.imwrite(image_path, frame)

    cv2.imshow("Helmet Frame Capture", frame)
    print(f"Extracting frame {frame_count}")

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to stop manually
        print("Stopped manually.")
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()
