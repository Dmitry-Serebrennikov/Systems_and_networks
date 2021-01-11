import cognitive_face as CF
from PIL import Image

def get_cropped_face(face):
    original_image = Image.open('man.jpg')
    cropped_face = original_image.crop((face['left'], face['top'], face['left'] + face['width'], face['top'] + face['height']))
    cropped_face.save('cropped_face.png')

if __name__ == '__main__':
    KEY = '196f6913f1ad4394821ce3d8915ec2dd'
    CF.Key.set(KEY)

    BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'
    CF.BaseUrl.set(BASE_URL)

    filename = 'man.jpg'
    result = CF.face.detect(filename)
    get_cropped_face(result[0]['faceRectangle'])
    

