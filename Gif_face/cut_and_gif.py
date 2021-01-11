import cognitive_face as CF
from PIL import Image
import cv2
import matplotlib.pyplot as plt

def get_cropped_face(image, face):
    image = Image.fromarray(image)
    cropped_image = image.crop((face['left'], face['top'], face['left'] + face['width'], face['top'] + face['height']))
    return cropped_image

if __name__ == '__main__':
    KEY = '196f6913f1ad4394821ce3d8915ec2dd'
    CF.Key.set(KEY)

    BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'
    CF.BaseUrl.set(BASE_URL)

    cap = cv2.VideoCapture('savvateev.mp4')
    images = []
    
    frame_number = 0
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    while frame_number < frame_count:
        ret, frame = cap.read()
        frame_number += 1
        if ret is None:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.imsave('img.jpg', frame)
        result = CF.face.detect(open('img.jpg', 'rb'))
        print(result)
        images.append(get_cropped_face(frame, result[0]['faceRectangle']))
    images[0].save('result.gif', save_all=True, append_images=images[1:], loop=0)


