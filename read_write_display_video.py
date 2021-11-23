import cv2

# Create a video capture object, in this case we are reading the video from a file
# vid_capture = cv2.VideoCapture('videos/test.mp4')

# video capture object from sequence of frames
# vid_capture = cv2.VideoCapture('videos/test_frames/frame_%d.jpg')

# video capture from webcam
vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

frame_width = int(vid_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(vid_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)
fps = 30

output = cv2.VideoWriter('videos/video_output/saved_video.avi',
                         cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, frame_size)

if vid_capture.isOpened() == False:
    print('Error opening the video file')
# Read fps and frame count
else:
    # Get frame rate information
    # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
    fps = vid_capture.get(cv2.CAP_PROP_FPS)
    print('Frames per second : ', fps, 'FPS')

    # Get frame count
    frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print('Frame count: ', frame_count)

    count = 0
    while(vid_capture.isOpened()):
        # vid_capture.read() methods returns a tuple, first element is a bool, second is a frame
        ret, frame = vid_capture.read()

        # frame = cv2.resize(frame, (1280, 720))

        if ret == True:
            cv2.imshow('Frame', frame)
            cv2.resizeWindow('Frame', 1280, 720)

            # cv2.imwrite(f'videos/test_frames/frame_{count}.jpg', frame)
            output.write(frame)

            key = cv2.waitKey(50)

            if key == ord('q'):
                break
        else:
            break

        count += 1

vid_capture.release()
cv2.destroyAllWindows()
