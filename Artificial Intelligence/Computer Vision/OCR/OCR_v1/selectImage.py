import cv2
import numpy as np
import time


class image():
    def __init__(self, path):
        self.path = path
        self._img = cv2.imread(self.path)
        self._img_master = cv2.cvtColor(self._img, cv2.COLOR_BGR2RGB)
        self._img = self._img_master.copy()
        self._draw = False
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._allowed = 0

        cv2.namedWindow(winname='image')
        cv2.setMouseCallback('image', self._select)

        while True:
            cv2.imshow('image', self._img)
            if ((cv2.waitKey(1) & 0xFF) == ord('q')) or self._allowed:
                break

        cv2.destroyAllWindows()

    def _select(self, event, x, y, flag, param):
        if (event == cv2.EVENT_LBUTTONDOWN):
            self._x1 = x
            self._y1 = y
            self._draw = True

        elif (event == cv2.EVENT_MOUSEMOVE) and (self._draw):
            # used deep copy  otherwise master copy will be modified
            self._img = self._img_master.copy()
            cv2.rectangle(self._img,
                          pt1=(self._x1, self._y1),
                          pt2=(x, y),
                          color=(0, 1, 0),
                          thickness=1)

        elif (event == cv2.EVENT_LBUTTONUP):
            self._draw = False
            self._x2 = x
            self._y2 = y
            cv2.rectangle(self._img,
                          pt1=(self._x1, self._y1),
                          pt2=(self._x2, self._y2),
                          color=(0, 1, 0),
                          thickness=1)
            self._crop()
            self._allowed = 1

    def _crop(self):
        if self._y1 > self._y2 and self._x1 > self._x2:
            self.selectedImg = self._img[self._y2:self._y1, self._x2:self._x1]
        elif self._y1 > self._y2 and self._x1 < self._x2:
            self.selectedImg = self._img[self._y2:self._y1, self._x1:self._x2]
        elif self._y1 < self._y2 and self._x1 > self._x2:
            self.selectedImg = self._img[self._y1:self._y2, self._x2:self._x1]
        elif self._y1 < self._y2 and self._x1 < self._x2:
            self.selectedImg = self._img[self._y1:self._y2, self._x1:self._x2]


# obj = image('file.png')