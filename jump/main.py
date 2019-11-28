# coding: utf-8

import pyxel

WINDOW_W = 160
WINDOW_H = 160
CAT_W = 16
CAT_H = 16

class App:
    def __init__(self):
        self.IMG_ID0 = 0
        self.IMG_ID1 = 1
        self.IMG_ID0_X = 60
        self.IMG_ID1_Y = 65

        pyxel.init(WINDOW_W, WINDOW_H, caption='Hello inamuu')
        pyxel.image(self.IMG_ID0).load(0, 0, "pyxel_examples/assets/pyxel_logo_38x16.png")
        pyxel.image(self.IMG_ID1).load(0, 0, "pyxel_examples/assets/cat_16x16.png")

        pyxel.mouse(False)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.IMG_ID0_X, self.IMG_ID1_Y, self.IMG_ID0, 0, 0, 38, 16)
        self.cat()

    def cat(self):
        x = pyxel.mouse_x
        y = pyxel.mouse_y

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            pyxel.blt(x, y, self.IMG_ID1, 0, 0, -CAT_W, CAT_H, 5)
        else:
            pyxel.blt(x, y, self.IMG_ID1, 0, 0, CAT_W, CAT_H, 5)

App()
