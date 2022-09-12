# PostOp Pose Tracking

> This project is a part of the submission for the [Future of Healthcare Hackathon](https://futureofhealthcare.devpost.com/) by Datavant

This project tracks your position and movement during exercise to provide corrective feedback. 

## Examples

The system can tell if you are doing certain exercises correctly by comparing the position of each joint on the pose model.

### Squats 

A correct squat is calculated when the vertical position of your hips is below that of your knees.

![Squats](./squat.gif)

### Jumping Jacks

A jumping jack is determined to be correct when the elbow's vertical position is above your head

![Jumping Jacks](./jacks.gif)

### Other Exercises

Feedback for other exercises can be implemented on a case-by-case basis by comparing the positions of each joint.

## Technical Implementation

The system was implemented using Python with the `opencv-python` and `mediapipe` libraries.

MediaPipe takes an image of a person and generates the coordinates of 33 body parts, or landmarks, which can be used to run calculations on relative positions and drawn on the image.

[![MediaPipe Landmark Model](./landmarks.png)](https://google.github.io/mediapipe/solutions/pose.html#pose-landmark-model-blazepose-ghum-3d)

## Applications

We see several applications for the use of this technology:

1. Guidance while performing routines for physical therapy. Can be used to ensure users are exercising correctly and do not injure themselves.
2. A virtual personal trainer that can give feedback on your exercise, to help with the obesity epidemic.

## Future development

With a pool of enough data, we could create trained AI models to give specific feedback on different types of workouts without having to hard-code comparisons between joint positions.

## Special Thanks

To the organizers and judges of the [Future of Healthcare Hackathon](https://futureofhealthcare.devpost.com/) by Datavant. 

To the authors of [OpenCV Python](https://docs.opencv.org/4.x/) and [MediaPipe Pose](https://google.github.io/mediapipe/solutions/pose)
