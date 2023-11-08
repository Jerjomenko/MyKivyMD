from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

KV = """
ScreenManager:
    MDScreen:
        name: "home"
        md_bg_color: .6, .4, .7, .5
        MDLabel:
            text: "Hallo everyone!"
            halign: "center"
            pos_hint: {"center_y": .8}
            font_style: "H3"
            bold: True


"""


class AudioYT(MDApp):
    def build(self):
        return Builder.load_string(KV)



if __name__ == "__main__":
    AudioYT().run()




