import cv2

# Load the video
video_path = "/Users/jinhuang/Desktop/work/my_data/demo_for_design_and_product/data/mt_lab_test_videos/test_04.mp4"
cap = cv2.VideoCapture(video_path)

# Read the first frame
ret, frame = cap.read()
cap.release()

if not ret:
    raise ValueError("Failed to read the first frame from the video.")

# Mouse callback function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked coordinates: ({x}, {y})")

# Show frame and bind callback
cv2.imshow("First Frame", frame)
cv2.setMouseCallback("First Frame", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
