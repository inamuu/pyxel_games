# coding: utf-8

import pyxel

WINDOW_W = 120
WINDOW_H = 160
CAT_W = 16
CAT_H = 16

class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, caption='Hello inamuu')
        pyxel.image(0).load(0, 0, "pyxel_examples/assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "pyxel_examples/assets/cat_16x16.png")

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(60, 65, 0, 0, 0, 38, 16)
        pyxel.blt(75, 45, 1, 0, 0, CAT_W, CAT_H, 5)

App()
