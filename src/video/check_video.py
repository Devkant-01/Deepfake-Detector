import cv2

video_path = "data/raw/video/fake/real_001.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Could not open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

duration = frames / fps if fps > 0 else 0
if video_path=="data/raw/video/fake/real_001.mp4":
    print("Video is fake:")

if video_path=="data/raw/video/real/real_001.mp4":
    print("Video is real:")

print("FPS:", fps)
print("Frames:", frames)
print("Resolution:", width, "x", height)
print("Duration:", duration, "seconds")

cap.release()