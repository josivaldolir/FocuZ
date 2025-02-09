import flet as ft

sample_media = [
        # Subway surfers
        ft.VideoMedia("https://archive.org/download/vcompress_419/vcompress_419.mp4"),
        ft.VideoMedia("https://archive.org/download/vcompress_422/vcompress_422.mp4"),
        ft.VideoMedia("https://archive.org/download/subway-surfers-north-pole-christmas-gameplay-v-2-i-phone-i-pad-i-os-android-game/SUBWAY%20SURFERS%20NORTH%20POLE%20-%20Christmas%20Gameplay%20%28V2%29%20%28iPhone%2C%20iPad%2C%20iOS%2C%20Android%20Game%29.mp4"),
        ft.VideoMedia("https://archive.org/download/vcompress_74/vcompress_74.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1708371779/RPReplay_Final1708371779.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1706562329/RPReplay_Final1706562329.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1682375679/RPReplay_Final1682375679.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1685970481/RPReplay_Final1685970481.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1693227251/RPReplay_Final1693227251.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1690153368/RPReplay_Final1690153368.mp4"),
        
        # Diversos
        ft.VideoMedia("https://archive.org/download/RocketLeague3v3ExibitionMatchPS4Gameplay/Rocket%20League%203v3%20Exibition%20Match%20%28PS4%20Gameplay%29.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1687087224/RPReplay_Final1687087224.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1704983659/RPReplay_Final1704983659.mp4"),
        ft.VideoMedia("https://archive.org/compress/SRS_pvz-gameplay-endless/formats=H.264&file=/SRS_pvz-gameplay-endless.zip"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1695226359/RPReplay_Final1695226359.mp4"),
        ft.VideoMedia("https://archive.org/download/rpreplay-final-1684249681/RPReplay_Final1684249681.mp4"),
        ft.VideoMedia("https://archive.org/download/GTA5_eng_mega/buldoser_1.mp4"),
        ft.VideoMedia("https://archive.org/download/GTA5_eng_mega/speed_car.mp4"),
        ft.VideoMedia("https://archive.org/download/GTA5_eng_mega/car_rage_1.mp4"),
        ft.VideoMedia("https://archive.org/download/hungry-shark-evolution/1%20-%20hungry%20shark%20Clip%201.mp4"),
        ft.VideoMedia("https://dn720300.ca.archive.org/0/items/hungry-shark-evolution/2%20-%20hungry%20shark%201%20Clip%2011.mp4")
    ]

class ButtonManager:
    def __init__(self, *buttons):
        self.buttons = buttons
        for button in self.buttons:
            button.width = 40
            button.height = button.width
            button.bgcolor = ft.Colors.BLACK45
            button.shape = ft.ContinuousRectangleBorder(radius=10)
            button.scale = 0.8
            button.animate_opacity = ft.Animation(duration=500, curve=ft.AnimationCurve.EASE_IN)
            button.opacity = 1

    def set_opacity(self, opacity):
        for button in self.buttons:
            button.opacity = opacity
    
    def update(self):
        for button in self.buttons:
            button.update()
            