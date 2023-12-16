from kivy.utils import platform
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from cam import Cam
from signup import Signup

class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cam=Cam()
        signup=Signup()
        self.add_widget(cam)
        self.add_widget(signup)



class BarcodeApp(MDApp):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA, Permission.RECORD_AUDIO])
        return Interface()


if __name__ == '__main__':
    BarcodeApp().run()