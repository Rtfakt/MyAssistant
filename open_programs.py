import numpy as np
import cv2 as cv
import pyautogui as pag


class OpenPrograms:
    # шаблоны кнопок
    OTRT = cv.imread('images/ORTR_images/OCTRTButton.png', 0)
    take_photo = cv.imread('images/ORTR_images/TakePhotoOCRTRT.png', 0)
    document_photo = cv.imread('images/ORTR_images/ToDoDocument.png', 0)
    OKTRT = cv.imread('images/ORTR_images/OKTRT.png', 0)
    find_textTRT = cv.imread('images/ORTR_images/findText.png', 0)
    closeTRT = cv.imread('images/ORTR_images/CloseTRT.png', 0)
    addTRT = cv.imread('images/ORTR_images/addTRT.png', 0)
    prymenit = cv.imread('images/ORTR_images/Primenit.png', 0)
    WindowsCamIcon = cv.imread('images/ORTR_images/WindowsCamIcon.png', 0)
    blackClose = cv.imread('images/ORTR_images/blackCloseButton.png', 0)



    def findButtonInMyComputer(template, debug_mode=False):
        while True:
            screenshot = pag.screenshot()  # получение кадров с камеры
            screenshot = np.array(screenshot)
            screenshot = screenshot[:, :, ::-1].copy()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
            result = cv.matchTemplate(screenshot, template, cv.TM_CCOEFF_NORMED)  # сравниваем шаблоны
            cv.minMaxLoc(screenshot)

            button_h = template.shape[0]
            button_w = template.shape[1]

            # print('левая верхняя точка %s' % str(max_loc))
            # print('пороговое значение %s' % str(max_val))

            threshold = 0.90
            locations = np.where(result >= threshold)
            locations = list(zip(*locations[::-1]))
            # print(locations)

            rectangles = []
            for loc in locations:
                rect = [int(loc[0]), int(loc[1]), button_w, button_h]
                rectangles.append(rect)
                # print(rect)

            # print(rectangles)

            points = []
            if len(rectangles):

                marker_type = cv.MARKER_CROSS

                # Loop over all the rectangles
                for (x, y, w, h) in rectangles:
                    # Determine the center position
                    center_x = x + int(w / 2)
                    center_y = y + int(h / 2)
                    # Save the points
                    points.append((center_x, center_y))
                    cv.drawMarker(screenshot, (center_x, center_y), marker_type)
                    # print('точка х %s' % str(center_x))
                    # print('точка y %s' % str(center_y))
                    pag.moveTo(center_x, center_y)
                break
            else:
                pass
            if debug_mode is True:
                cv.imshow('Read screen', screenshot)

            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break

        return points
