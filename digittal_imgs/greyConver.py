import cv2

def GreyCon(event,path):
    image = cv2.imread(path)
    resized_image = cv2.resize(image, (350,600))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()