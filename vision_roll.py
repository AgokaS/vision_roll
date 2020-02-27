"""Основной файли проекта по компьютерному зрению
Avtors: Denis Pankratov, Egor Sidorov """
import cv2 
import numpy as np
import neurolab as nl
import tkinter as tk

def __CameraVisionColibrated__():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow( "settings") # создаем окно настроек
    
    
    # создаем 6 бегунков для настройки начального и конечного цвета фильтра
    cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
    
    while True:
        flag, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
        # считываем значения бегунков
        h1 = cv2.getTrackbarPos('h1', 'settings')
        s1 = cv2.getTrackbarPos('s1', 'settings')
        v1 = cv2.getTrackbarPos('v1', 'settings')
        h2 = cv2.getTrackbarPos('h2', 'settings')
        s2 = cv2.getTrackbarPos('s2', 'settings')
        v2 = cv2.getTrackbarPos('v2', 'settings')
    
        # формируем начальный и конечный цвет фильтра
        h_min = np.array((h1, s1, v1), np.uint8)
        h_max = np.array((h2, s2, v2), np.uint8)
    
        # накладываем фильтр на кадр в модели HSV
        thresh = cv2.inRange(hsv, h_min, h_max)        
        cv2.imshow('settings', thresh) 
        
        #отрисовка контуров
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(gray, h_min, h_max )
        contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 0)
        cv2.drawContours(img, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 2)
    
        cv2.imshow('Counrours', img)
     
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    


if __name__ == '__main__':
    def nothing(*arg):
        pass


Vision = tk.Tk()
Vision.title("Компьютерное зрение")
Vision.minsize(1200, 800)
f_right = tk.Frame(Vision,
                   width = 200,
                   height = 100,
                   bg = 'red')

OptionsCamera = tk.Button(f_right ,
                          text ="Настройка" ,
                          command =__CameraVisionColibrated__)

f_right.pack(side = tk.RIGHT)
OptionsCamera.pack(side = tk.TOP)

Vision.mainloop() 


