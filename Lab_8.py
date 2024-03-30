#Бархоткина Анастасия, 408226
import cv2

def image_resizing():
    img = cv2.imread('images/variant-6.png')
    resized_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    cv2.imshow('Resized image', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def point_detecting():
    cap = cv2.VideoCapture("sample.mp4")
    while (cv2.waitKey(1) != 27):
        ret, image = cap.read()
        if not ret:
            break
        mask = cv2.inRange(image, (80, 80, 80), (255, 255, 255))
        ret, thresh = cv2.threshold(mask, 110, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def side_counting():
    OLDposition = 2
    Left = 0
    Right = 0
    cap = cv2.VideoCapture("sample.mp4")
    while (cv2.waitKey(1) != 27):
        ret, image = cap.read()
        if not ret:
            break
        mask=cv2.inRange(image, (80, 80, 80), (255, 255, 255))
        ret, thresh = cv2.threshold(mask, 110, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        centreX = image.shape[1]//2
        if x > (centreX):
            NEWposition = 2
        if x + w < (centreX):
            NEWposition = 1
        if NEWposition != OLDposition:
            if OLDposition == 2:
                Left += 1
            if OLDposition == 1:
                Right += 1
            OLDposition = NEWposition
        cv2.putText(image,  str(Left), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(image,  str(Right), (500,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fly_detecting():
    OLDposition = 2
    Left = 0
    Right = 0
    cap = cv2.VideoCapture("sample.mp4")
    while (cv2.waitKey(1) != 27):
        ret, image = cap.read()
        if not ret:
            break
        mask=cv2.inRange(image, (80, 80, 80), (255, 255, 255))
        ret, thresh = cv2.threshold(mask, 110, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        a = x + (w // 2)
        b = y + (h // 2)
        #print(a, b)
        fly = cv2.imread("fly64.png")
        fly = cv2.resize(fly,(64,64))
        for i in range(64):
            for j in range(64):
                dx = (a - 32 + j)
                if dx < 0:
                    dx = 0
                if dx > image.shape[1] - 1:
                    dx = image.shape[1] - 1
                dy = (b - 32 + i)
                if dy < 0:
                    dy = 0
                if dy > image.shape[0] - 1:
                    dy = image.shape[0] - 1
                image[dy][dx] = fly[j][i]
        centreX = image.shape[1]//2
        if x>(centreX):
            NEWposition = 2
        if x+w<(centreX):
            NEWposition = 1
        if NEWposition != OLDposition:
            if OLDposition == 2:
                Left += 1
            if OLDposition == 1:
                Right += 1
            OLDposition=NEWposition
        cv2.putText(image,  str(Left), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0) , 2)
        cv2.putText(image,  str(Right), (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0) , 2)
        cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image_resizing()
    point_detecting()
    side_counting()
    fly_detecting()
    
    