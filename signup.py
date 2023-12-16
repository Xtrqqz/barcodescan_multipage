from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""

<Signup>:
    name:"signup"

    Label:
        text: "Signup"
    Button:
        on_press:root.back_to_cam()

""")


class Signup(Screen):
    def back_to_cam(self):
        self.manager.current="cam"