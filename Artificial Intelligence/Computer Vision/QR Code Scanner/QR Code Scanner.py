# Developed at anotherwebguy.com
# Importing required modules
import cv2
from pyzbar.pyzbar import decode
from warnings import filterwarnings
filterwarnings('ignore')

# Capture the video from default camera
capture = cv2.VideoCapture(0)

print("Escape Key (Esc) to exit...")
print("Follow us at https://www.youtube.com/c/AnotherWebGuy ")
print('--------------------------------------------------------------------------------------------\n')

recieved_data = None
while True:
    # reading frame from the camera
    _, frame = capture.read()
    # Decoding the QR Code 
    decoded_data = decode(frame)
    try:
        data = decoded_data[0][0]
        if data != recieved_data:
            recieved_data = data
            print("\n", data, "\n")
    except:
        pass
    
    # Showing video.
    cv2.imshow("QR CODE Scanner", frame)

    # To exit press Esc Key.
    key = cv2.waitKey(1)
    if key == 27:
        break