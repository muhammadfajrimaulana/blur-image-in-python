import cv2

def main():
    image = cv2.imread("fajri.jpg")
    blurredImage = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imwrite("fajri.jpg", blurredImage)
    
if __name__ == "__main__":
    main()
    
