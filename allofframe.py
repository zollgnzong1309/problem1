import cv2

cap = cv2.VideoCapture("something.mp4")
if not cap.isOpened():
    print("Cannot open video file. Check the file path!")
    exit()

frame_num = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No frame read or end of video.")
        break

    cv2.putText(frame, f"Frame: {frame_num}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Video", frame)

    key = cv2.waitKey(30)
    if key == ord('e'):
        break

    frame_num += 1

cap.release()
cv2.destroyAllWindows()
