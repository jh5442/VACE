import cv2

# Path to input video
video_path = '/home/ubuntu/jin-Vol/results/demos_for_product/vace/mt_lab_test_videos/test_04_14B_inpaiting_mask_salient/src_mask-inpainting.mp4'
# Path to save the first frame
output_image_path = '/home/ubuntu/jin-Vol/results/demos_for_product/vace/mt_lab_test_videos/test_04_14B_inpaiting_mask_salient/mask.png'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Read the first frame
    ret, frame = cap.read()
    if ret:
        # Save the frame as an image
        cv2.imwrite(output_image_path, frame)
        print(f"First frame saved to {output_image_path}")
    else:
        print("Error: Could not read the first frame.")

# Release the video capture object
cap.release()
