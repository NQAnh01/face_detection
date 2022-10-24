import cv2
from numpy import empty
from regex import P


def detected(name = ''):
    face_detector = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
            
    image_path = './media/images/' + name
    img = cv2.imread(image_path)
    if img is None:
        print('khong mo dc file\n')
        return "failed"
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(img_gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.imwrite("./media/detected/" + name, img)

    cv2.destroyAllWindows()
