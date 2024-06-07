import cv2
import numpy as np

def gen_dolmatin(N, output_filename="dolmatin.png"):
    height, width = 500, 500
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    circles = []
    min_radius, max_radius = 10, 30

    for _ in range(N):
        while True:
            # Генерация случайного радиуса и координат круга
            radius = np.random.randint(min_radius, max_radius)
            center_x = np.random.randint(radius, width - radius)
            center_y = np.random.randint(radius, height - radius)
            new_circle = (center_x, center_y, radius)
            
            # Проверка пересечений с уже существующими кругами
            intersects = False
            for circle in circles:
                dist = np.sqrt((new_circle[0] - circle[0])**2 + (new_circle[1] - circle[1])**2)
                if dist < new_circle[2] + circle[2]:
                    intersects = True
                    break
            if not intersects:
                circles.append(new_circle)
                break
    
    # Рисование кругов на изображении
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 0, 0), -1)

    cv2.imwrite(output_filename, image)


def count_stops(image_filename):
    image = cv2.imread(image_filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, 
                               minDist=20, param1=50, param2=30, 
                               minRadius=10, maxRadius=30)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        return len(circles)
    else:
        return 0

if __name__ == '__main__':
    gen_dolmatin(20, "dolmatin.png")
    print(f"Количество кругов на изображении: {count_stops('dolmatin.png')}")