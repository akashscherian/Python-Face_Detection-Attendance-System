import cv2

inp = input('Enter person name: ')

# Assuming you have already initialized 'cam' as a VideoCapture instance
cam = cv2.VideoCapture(0)  # Replace with the appropriate camera port number

# If image will be detected without any error, show result
while True:
    ret, image = cam.read()

    if ret:
        cv2.imshow(inp, image)

        # Wait for a key press
        key = cv2.waitKey(1)

        # If the 'Enter' key is pressed, save the image and break from the loop
        if key == 13:  # 13 is the ASCII code for 'Enter' key
            cv2.imwrite(inp + ".png", image)
            print("Image taken")
            break

    else:
        print("No image detected. Please try again.")

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
