import cv2
import mediapipe as mp


def main():
    capture = cv2.VideoCapture(0)

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_draw = mp.solutions.drawing_utils
    success, img = capture.read()
    h, w, c = img.shape

    fourcc = cv2.VideoWriter_fourcc(*'MPV4')
    writer = cv2.VideoWriter('output.mp4', fourcc, 20.0, (w, h))

    while success:
        success, img = capture.read()
        results = pose.process(img)
        cv2.putText(img, "Do some jumping jacks", (0, 20), 0, 1, (255, 255, 255), 3)
        # cv2.putText(img, "Do some squats", (0, 20), 0, 1, (255, 255, 255), 3)

        if results.pose_landmarks:
            mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            landmarks = results.pose_landmarks.landmark

            # Jumping jacks
            if landmarks[14].y < landmarks[0].y:
                cv2.putText(img, "Good! Now lower your arms.", (0, 100), 0, 1, (255, 255, 255), 3)
            else:
                cv2.putText(img, "Raise your arms above your head!", (0, 100), 0, 1, (255, 255, 255), 3)

            # Squats
            # if landmarks[24].y < landmarks[26].y:
            #     cv2.putText(img, "Bend your knees and lower your body", (0, 100), 0, 1, (255, 255, 255), 3)
            # else:
            #     cv2.putText(img, "Great! Stand up and do it again!", (0, 100), 0, 1, (255, 255, 255), 3)


        writer.write(img)

        cv2.imshow('Image', img)
        cv2.waitKey(1)

    capture.release()
    writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
