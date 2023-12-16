from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import mainthread
from kivy.utils import platform

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from camera4kivy import Preview
from PIL import Image

from pyzbar.pyzbar import decode


Builder.load_string("""

<Cam>:
    name:"cam"
    
    BoxLayout:
        padding: dp(20)
        spacing: dp(20)
		orientation: 'vertical'
		ScanAnalyze:
			id:preview
			aspect_ratio: '16:9'
			extracted_data:root.got_result

		MDLabel:
			size_hint_y: None
			height:'130dp'
			id:ti
        Button:
            text: "signup"
            on_press:root.switch_to_signup()
""")

class Cam(Screen):
    def on_kv_post(self, obj):
        # Ändere die Kamera-ID auf "zwei"
        self.ids.preview.connect_camera(camera_id="1", enable_analyze_pixels=True, default_zoom=0.0)

    @mainthread
    def got_result(self, result):
        self.ids.ti.text = str(result)
        print(self.ids.ti.text)

    def switch_to_signup(self):
        self.manager.current = "signup"


class ScanAnalyze(Preview):
    extracted_data = ObjectProperty(None)

    def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):
        pimage = Image.frombytes(mode='RGBA', size=image_size, data=pixels)
        list_of_all_barcodes = decode(pimage)

        if list_of_all_barcodes:
            if self.extracted_data:
                self.extracted_data(list_of_all_barcodes[0][0])
            else:
                print("Not found")
