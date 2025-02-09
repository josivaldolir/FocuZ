import flet as ft
from utils import *
from random import randint

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "FocuZ"
    page.window.always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def start(e):
        error_display.top = page.height/2 - error_display.height / 2
        error_display.left = page.width/2 - error_display.width / 2
        error_display.update()

    def mute_unmute(e):
        if video.volume:
            video.volume = 0
            button_mute.icon = ft.Icons.VOLUME_OFF
            button_mute.update()
            video.update()
        else:
            video.volume = 100
            button_mute.icon = ft.Icons.VOLUME_UP
            button_mute.update()
            video.update()

    def pause_resume(e):
        if video.is_playing():
            video.pause()
            button_pause.icon=ft.Icons.PLAY_ARROW
            button_pause.update()
        else:
            video.play()
            button_pause.icon=ft.Icons.PAUSE
            button_pause.update()
    
    def fullscreen(e):
        if button_fullscreen.icon == ft.Icons.FULLSCREEN:
            page.window.title_bar_hidden = True
            button_fullscreen.icon = ft.Icons.FULLSCREEN_EXIT
            page.update()
        else:
            page.window.title_bar_hidden = False
            button_fullscreen.icon = ft.Icons.FULLSCREEN
            page.update()
    
    def aspect_ratio(e):
        if video.aspect_ratio == 16 / 9:
            video.aspect_ratio = 9 / 16
            video.update()
        else:
            video.aspect_ratio = 16 / 9
            video.update()
        
    def forward(e):
        if (video.get_current_position() + 10000) < video.get_duration():
            video.seek(video.get_current_position() + 10000)
        else:
            video.next()
            
    def backwards(e):
        if (video.get_current_position() - 10000) > 0:
            video.seek(video.get_current_position() - 10000)
        else:
            video.previous()
        
    # Começa a animação para esconder os botões
    def buttons_fade(e):
        if e.data == "blur":
            button_manager.set_opacity(0)
            button_manager.update()
        elif e.data == "focus":
            button_manager.set_opacity(1)
            button_manager.update()
    
    def error_handling(e):
        if e.data == "tcp" or "Failed to" in e.data:
            error_display.content = ft.Text("Hmm 😟, problema de rede detectado.\nVerifique sua conexão e tente novamente.\n",
                                            size=15,
                                            text_align="center", font_family="arial")
        else:
            error_display.content = ft.Text(e.data, size=15, text_align="center")
        error_display.update()
            
    def adjust_error_display(e):
        error_display.height = page.height/2
        error_display.width = page.width/2
        error_display.top = page.height/2 - error_display.height / 2
        error_display.left = page.width/2 - error_display.width / 2
        error_display.update()
            
    page.window.on_event = buttons_fade
    video = ft.Video(
        expand=True,
        playlist=sample_media[randint(0, len(sample_media) - 1):],
        playlist_mode=ft.PlaylistMode.LOOP,
        shuffle_playlist=True,
        show_controls=False,
        aspect_ratio=16 / 9,
        volume=0,
        autoplay=True,
        filter_quality=ft.FilterQuality.LOW,
        fit=ft.ImageFit.FILL,
        on_track_changed=lambda e: video.seek(60000),
        wakelock=True,
        on_loaded=start
        )
    
    video.on_error = error_handling
    
    button_mute = ft.FloatingActionButton(
        icon=ft.Icons.VOLUME_OFF,
        on_click=mute_unmute
        )
    button_pause = ft.FloatingActionButton(
        icon=ft.Icons.PAUSE,
        on_click=pause_resume
        )
    button_skip = ft.FloatingActionButton(
        icon=ft.Icons.SKIP_NEXT,
        on_click=lambda e:video.next()
        )
    button_fullscreen = ft.FloatingActionButton(
        icon=ft.Icons.FULLSCREEN,
        on_click=fullscreen
        )
    button_ratio = ft.FloatingActionButton(
        icon=ft.Icons.LOOP,
        on_click=aspect_ratio
        )
    button_forward = ft.FloatingActionButton(
        icon=ft.Icons.FORWARD_10,
        on_click=forward
        )
    
    button_backwards = ft.FloatingActionButton(
        icon=ft.Icons.REPLAY_10,
        on_click=backwards
        )
    
    # Passa todos os atributos e métodos da classe button_manager para os botões
    button_manager = ButtonManager(button_fullscreen, button_mute, button_pause, button_skip, button_ratio, button_forward, button_backwards)
    
    # Ordem dos botões na tela
    button_row = ft.Row(
        [
            button_mute,
            button_ratio,
            button_backwards,
            button_pause,
            button_forward,
            button_skip,
            button_fullscreen
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=-7
        )
    
    page.on_resized = adjust_error_display
    
    error_display = ft.Container(
        width=page.width/2,
        height=page.height/2,
        alignment=ft.alignment.center)
    
    # Adiciona todo o conteúdo à tela
    page.add(
        ft.Stack(
            [
                video,
                button_row,
                error_display
            ]
        )
    )

if __name__ == "__main__":
    ft.app(main)