"""
=============================================================================
SEGURIDAD SOS - VERSIÓN MÓVIL KIVYMD (MATERIAL DESIGN 3 EXPRESSIVE)
PALETA DE COLORES SÓLIDOS SIN DEGRADADOS
=============================================================================
"""

import traceback
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    StringProperty,
)
from kivy.utils import get_color_from_hex, platform
from kivymd.uix.label import MDLabel

try:
    from kivymd.uix.snackbar import MDSnackbar
    HAS_MD_SNACKBAR = True
except ImportError:
    from kivymd.uix.snackbar import Snackbar
    HAS_MD_SNACKBAR = False

if platform in ('win', 'linux', 'macosx'):
    Window.size = (414, 896)

KV = '''
#:import dp kivy.metrics.dp

MDScreenManager:
    id: sm
    AuthScreen:
        id: auth_screen
        name: 'auth'
    MainScreen:
        id: main_screen
        name: 'main'
    CamerasScreen:
        id: cameras_screen
        name: 'cameras'

# =========================================================================
# VISTA 1 & 2: AUTENTICACIÓN (LOGIN Y REGISTRO)
# =========================================================================
<AuthScreen@MDScreen>:
    md_bg_color: app.bg_main

    MDBoxLayout:
        orientation: 'vertical'
        padding: ['20dp', '28dp', '20dp', '16dp']
        spacing: '14dp'

        # Encabezado
        MDBoxLayout:
            adaptive_height: True
            orientation: 'vertical'
            spacing: '6dp'
            padding: [0, '14dp', 0, '8dp']

            MDBoxLayout:
                adaptive_height: True
                pos_hint: {'center_x': .5}
                spacing: '10dp'
                MDIcon:
                    icon: 'shield-check'
                    theme_text_color: 'Custom'
                    text_color: app.btn_primary
                    font_size: '34sp'
                MDLabel:
                    text: "SEGURIDAD SOS"
                    bold: True
                    font_style: 'H5'
                    theme_text_color: 'Custom'
                    text_color: app.text_primary
                    adaptive_size: True
                    pos_hint: {'center_y': .5}

            MDLabel:
                text: "Tu tranquilidad empieza aquí"
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: app.text_secondary
                font_style: 'Caption'

        # Tabs Segmentados
        MDBoxLayout:
            adaptive_height: True
            spacing: '10dp'
            padding: [0, '4dp', 0, '8dp']

            MDFillRoundFlatButton:
                text: "INICIAR SESIÓN"
                font_size: "13sp"
                bold: True
                size_hint_x: 0.5
                md_bg_color: app.btn_primary if app.auth_tab == 'login' else app.bg_card
                text_color: app.text_primary if app.auth_tab == 'login' else app.text_secondary
                on_release: app.set_auth_tab('login')

            MDFillRoundFlatButton:
                text: "CREAR CUENTA"
                font_size: "13sp"
                bold: True
                size_hint_x: 0.5
                md_bg_color: app.btn_primary if app.auth_tab == 'register' else app.bg_card
                text_color: app.text_primary if app.auth_tab == 'register' else app.text_secondary
                on_release: app.set_auth_tab('register')

        # Formulario
        ScrollView:
            do_scroll_x: False
            MDBoxLayout:
                orientation: 'vertical'
                spacing: '14dp'
                adaptive_height: True
                padding: [0, '8dp', 0, '20dp']

                MDLabel:
                    text: "Crea tu cuenta" if app.auth_tab == 'register' else "Bienvenido"
                    font_style: 'H6'
                    bold: True
                    adaptive_height: True
                    theme_text_color: 'Custom'
                    text_color: app.text_primary

                MDTextField:
                    id: reg_name
                    hint_text: "Nombre Completo"
                    mode: "fill"
                    icon_left: "account"
                    icon_left_color_normal: app.accent_cyan
                    icon_left_color_focus: app.accent_cyan
                    text_color_normal: app.text_primary
                    text_color_focus: app.text_primary
                    hint_text_color_normal: app.text_secondary
                    hint_text_color_focus: app.accent_cyan
                    line_color_normal: app.border_input
                    line_color_focus: app.accent_cyan
                    fill_color_normal: app.bg_input_nav
                    fill_color_focus: app.bg_input_nav
                    radius: [12, 12, 0, 0]
                    opacity: 1 if app.auth_tab == 'register' else 0
                    size_hint_y: None
                    height: dp(56) if app.auth_tab == 'register' else 0
                    disabled: app.auth_tab != 'register'

                MDTextField:
                    id: user_phone
                    hint_text: "Teléfono Móvil"
                    mode: "fill"
                    icon_left: "cellphone"
                    icon_left_color_normal: app.accent_cyan
                    icon_left_color_focus: app.accent_cyan
                    text_color_normal: app.text_primary
                    text_color_focus: app.text_primary
                    hint_text_color_normal: app.text_secondary
                    hint_text_color_focus: app.accent_cyan
                    line_color_normal: app.border_input
                    line_color_focus: app.accent_cyan
                    fill_color_normal: app.bg_input_nav
                    fill_color_focus: app.bg_input_nav
                    radius: [12, 12, 0, 0]

                MDTextField:
                    id: user_pin
                    hint_text: "PIN (4 dígitos)"
                    mode: "fill"
                    icon_left: "lock"
                    icon_left_color_normal: app.accent_cyan
                    icon_left_color_focus: app.accent_cyan
                    text_color_normal: app.text_primary
                    text_color_focus: app.text_primary
                    hint_text_color_normal: app.text_secondary
                    hint_text_color_focus: app.accent_cyan
                    line_color_normal: app.border_input
                    line_color_focus: app.accent_cyan
                    fill_color_normal: app.bg_input_nav
                    fill_color_focus: app.bg_input_nav
                    password: True
                    max_text_length: 4
                    input_filter: "int"
                    radius: [12, 12, 0, 0]

                MDFillRoundFlatButton:
                    text: "CREAR MI CUENTA SOS" if app.auth_tab == 'register' else "INICIAR SESIÓN"
                    font_size: "15sp"
                    bold: True
                    size_hint_x: 1
                    md_bg_color: app.btn_primary
                    text_color: app.text_primary
                    padding: "16dp"
                    radius: [100, 100, 100, 100]
                    on_release: app.process_auth_submit()

# =========================================================================
# VISTA 3: INICIO (SOS) Y VISTA 5: MI PERFIL + OVERLAY SOS
# =========================================================================
<MainScreen@MDScreen>:
    md_bg_color: app.bg_main

    MDFloatLayout:
        MDBottomNavigation:
            id: bottom_nav
            panel_color: app.bg_input_nav
            text_color_active: app.btn_primary
            text_color_normal: app.text_secondary

            # PESTAÑA 1: INICIO (SOS)
            MDBottomNavigationItem:
                name: 'nav_home'
                text: 'Inicio'
                icon: 'home'

                ScrollView:
                    do_scroll_x: False
                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: ['20dp', '16dp', '20dp', '20dp']
                        spacing: '12dp'
                        adaptive_height: True
                        md_bg_color: app.bg_main

                        MDBoxLayout:
                            adaptive_height: True
                            pos_hint: {'center_x': .5}
                            spacing: '8dp'
                            MDIcon:
                                icon: 'shield-check'
                                theme_text_color: 'Custom'
                                text_color: app.btn_primary
                                font_size: '24sp'
                            MDLabel:
                                text: "SEGURIDAD SOS"
                                bold: True
                                font_style: 'Subtitle1'
                                theme_text_color: 'Custom'
                                text_color: app.text_primary
                                adaptive_size: True
                                pos_hint: {'center_y': .5}

                        MDLabel:
                            text: "Hola, " + app.user_name
                            font_style: 'H5'
                            bold: True
                            theme_text_color: 'Custom'
                            text_color: app.text_primary
                            adaptive_height: True

                        MDLabel:
                            text: "Sistema de protección activo 24/7"
                            font_style: 'Caption'
                            theme_text_color: 'Custom'
                            text_color: app.text_secondary
                            adaptive_height: True

                        # Zona de Alerta Morada (#4C1D95) + Botón SOS (#E11D48)
                        MDCard:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: '265dp'
                            md_bg_color: app.zone_alert
                            radius: [24, 24, 24, 24]
                            padding: '16dp'
                            spacing: '8dp'

                            MDFloatLayout:
                                Widget:
                                    size_hint: None, None
                                    size: "196dp", "196dp"
                                    pos_hint: {"center_x": .5, "center_y": .54}
                                    canvas.before:
                                        Color:
                                            rgba: 1, 1, 1, 0.25
                                        Line:
                                            circle: (self.center_x, self.center_y, dp(90))
                                            width: dp(4)
                                        Color:
                                            rgba: app.accent_cyan
                                        Line:
                                            circle: (self.center_x, self.center_y, dp(90), 0, app.sos_progress * 360)
                                            width: dp(5)

                                MDFillRoundFlatButton:
                                    text: "SOS\\nPEDIR AYUDA"
                                    halign: "center"
                                    font_size: "24sp"
                                    bold: True
                                    size_hint: None, None
                                    size: "162dp", "162dp"
                                    pos_hint: {"center_x": .5, "center_y": .54}
                                    md_bg_color: app.sos_red
                                    text_color: app.text_primary
                                    radius: [81, 81, 81, 81]
                                    on_press: app.start_sos_hold()
                                    on_release: app.cancel_sos_hold()

                            MDLabel:
                                text: app.sos_status_text
                                halign: "center"
                                font_style: "Caption"
                                bold: True
                                adaptive_height: True
                                theme_text_color: "Custom"
                                text_color: app.text_primary

                        # Acciones Rápidas (Azul intenso #1665C1)
                        MDLabel:
                            text: "ACCESOS RÁPIDOS"
                            font_style: 'Caption'
                            bold: True
                            adaptive_height: True
                            theme_text_color: 'Custom'
                            text_color: app.accent_cyan

                        MDGridLayout:
                            cols: 2
                            spacing: '12dp'
                            size_hint_y: None
                            height: '86dp'

                            MDCard:
                                orientation: 'vertical'
                                padding: '14dp'
                                spacing: '6dp'
                                md_bg_color: app.action_blue
                                radius: [16, 16, 16, 16]
                                ripple_behavior: True
                                on_release: app.show_snackbar("Llamando al 911...")
                                MDIcon:
                                    icon: 'phone'
                                    theme_text_color: 'Custom'
                                    text_color: app.accent_cyan
                                MDLabel:
                                    text: "Llamar al 911"
                                    bold: True
                                    font_style: 'Caption'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_primary

                            MDCard:
                                orientation: 'vertical'
                                padding: '14dp'
                                spacing: '6dp'
                                md_bg_color: app.action_blue
                                radius: [16, 16, 16, 16]
                                ripple_behavior: True
                                on_release: app.show_snackbar("Ubicación GPS compartida")
                                MDIcon:
                                    icon: 'map-marker'
                                    theme_text_color: 'Custom'
                                    text_color: app.accent_cyan
                                MDLabel:
                                    text: "Compartir ubicación"
                                    bold: True
                                    font_style: 'Caption'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_primary

                        # Tarjeta: Ver Cámaras (#243575)
                        MDCard:
                            adaptive_height: True
                            padding: '16dp'
                            md_bg_color: app.bg_card
                            radius: [20, 20, 20, 20]
                            ripple_behavior: True
                            on_release: app.root.current = 'cameras'

                            MDIcon:
                                icon: 'video'
                                theme_text_color: 'Custom'
                                text_color: app.accent_cyan
                                font_size: '26sp'
                                pos_hint: {'center_y': .5}

                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: ['12dp', 0, 0, 0]
                                MDLabel:
                                    text: "Ver cámaras"
                                    bold: True
                                    font_style: 'Subtitle2'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_primary
                                    adaptive_height: True
                                MDLabel:
                                    text: "3 dispositivos conectados"
                                    font_style: 'Caption'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_secondary
                                    adaptive_height: True

                            MDIcon:
                                icon: 'chevron-right'
                                theme_text_color: 'Custom'
                                text_color: app.accent_cyan
                                pos_hint: {'center_y': .5}

            # PESTAÑA 2: SOS RÁPIDO
            MDBottomNavigationItem:
                name: 'nav_sos'
                text: 'SOS'
                icon: 'shield-alert'

                MDBoxLayout:
                    orientation: 'vertical'
                    padding: '24dp'
                    spacing: '18dp'
                    md_bg_color: app.bg_main

                    MDLabel:
                        text: "CENTRAL DE EMERGENCIA SOS"
                        bold: True
                        halign: 'center'
                        font_style: 'Subtitle1'
                        theme_text_color: 'Custom'
                        text_color: app.accent_cyan
                        adaptive_height: True

                    MDFillRoundFlatButton:
                        text: "DISPARAR ALERTA INMEDIATA"
                        size_hint: (1, None)
                        height: "140dp"
                        font_size: "18sp"
                        bold: True
                        md_bg_color: app.sos_red
                        text_color: app.text_primary
                        radius: [28, 28, 28, 28]
                        on_release: app.activate_sos_overlay()

                    MDLabel:
                        text: "Envía coordenadas GPS en tiempo real a la patrulla policial y a tus contactos de emergencia."
                        halign: 'center'
                        font_style: 'Caption'
                        theme_text_color: 'Custom'
                        text_color: app.text_secondary
                        adaptive_height: True

                    Widget:

            # PESTAÑA 3: MI PERFIL / AJUSTES
            MDBottomNavigationItem:
                name: 'nav_profile'
                text: 'Ajustes'
                icon: 'cog'

                MDBoxLayout:
                    orientation: 'vertical'
                    padding: ['20dp', '16dp', '20dp', '16dp']
                    spacing: '14dp'
                    md_bg_color: app.bg_main

                    MDLabel:
                        text: "Mi perfil"
                        font_style: 'H5'
                        bold: True
                        theme_text_color: 'Custom'
                        text_color: app.text_primary
                        adaptive_height: True

                    MDLabel:
                        text: "Gestión de cuenta y configuración de seguridad"
                        font_style: 'Caption'
                        theme_text_color: 'Custom'
                        text_color: app.text_secondary
                        adaptive_height: True

                    MDCard:
                        orientation: 'vertical'
                        adaptive_height: True
                        padding: '16dp'
                        spacing: '14dp'
                        md_bg_color: app.bg_card
                        radius: [20, 20, 20, 20]

                        MDBoxLayout:
                            adaptive_height: True
                            spacing: '14dp'
                            MDIcon:
                                icon: 'account-circle'
                                theme_text_color: 'Custom'
                                text_color: app.accent_cyan
                                font_size: '28sp'
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                MDLabel:
                                    text: app.user_name
                                    bold: True
                                    font_style: 'Subtitle2'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_primary
                                    adaptive_height: True
                                MDLabel:
                                    text: "Titular de la cuenta SOS"
                                    font_style: 'Caption'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_secondary
                                    adaptive_height: True

                        MDSeparator:
                            color: app.border_input

                        MDBoxLayout:
                            adaptive_height: True
                            spacing: '14dp'
                            MDIcon:
                                icon: 'cellphone'
                                theme_text_color: 'Custom'
                                text_color: app.accent_cyan
                                font_size: '26sp'
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                MDLabel:
                                    text: app.user_phone_display
                                    bold: True
                                    font_style: 'Subtitle2'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_primary
                                    adaptive_height: True
                                MDLabel:
                                    text: "Teléfono registrado para alertas"
                                    font_style: 'Caption'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_secondary
                                    adaptive_height: True

                        MDSeparator:
                            color: app.border_input

                        MDBoxLayout:
                            adaptive_height: True
                            spacing: '14dp'
                            MDIcon:
                                icon: 'shield-check'
                                theme_text_color: 'Custom'
                                text_color: app.accent_cyan
                                font_size: '26sp'
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                MDLabel:
                                    text: "Protección Satelital GPS"
                                    bold: True
                                    font_style: 'Subtitle2'
                                    theme_text_color: 'Custom'
                                    text_color: app.text_primary
                                    adaptive_height: True
                                MDLabel:
                                    text: "Activa (Precisión: 3 metros)"
                                    font_style: 'Caption'
                                    theme_text_color: 'Custom'
                                    text_color: app.accent_cyan
                                    adaptive_height: True

                    Widget:

                    MDFillRoundFlatButton:
                        text: "CERRAR SESIÓN"
                        font_size: "14sp"
                        bold: True
                        size_hint_x: 1
                        md_bg_color: app.bg_card
                        text_color: app.accent_cyan
                        padding: "14dp"
                        radius: [100, 100, 100, 100]
                        on_release: app.logout()

        # OVERLAY DE ALERTA SOS TRANSMITIDA
        MDBoxLayout:
            orientation: 'vertical'
            padding: '28dp'
            spacing: '20dp'
            md_bg_color: app.sos_red
            opacity: 1 if app.sos_alert_active else 0
            disabled: not app.sos_alert_active
            size_hint: (1, 1) if app.sos_alert_active else (0, 0)

            Widget:
            MDIcon:
                icon: 'bell-ring'
                halign: 'center'
                font_size: '72sp'
                theme_text_color: 'Custom'
                text_color: app.text_primary
            MDLabel:
                text: "¡ALERTA SOS TRANSMITIDA!"
                halign: 'center'
                font_style: 'H5'
                bold: True
                adaptive_height: True
                theme_text_color: 'Custom'
                text_color: app.text_primary
            MDLabel:
                text: "Coordenadas GPS enviadas a la patrulla policial y a tus contactos de emergencia."
                halign: 'center'
                font_style: 'Body2'
                adaptive_height: True
                theme_text_color: 'Custom'
                text_color: app.text_primary
            MDFillRoundFlatButton:
                text: "DESACTIVAR ALERTA SOS"
                font_size: "15sp"
                bold: True
                size_hint_x: 1
                md_bg_color: app.text_primary
                text_color: app.sos_red
                padding: "16dp"
                radius: [100, 100, 100, 100]
                on_release: app.cancel_sos_alert()
            Widget:

# =========================================================================
# VISTA 4: MIS CÁMARAS
# =========================================================================
<CamerasScreen@MDScreen>:
    md_bg_color: app.bg_main

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Mis cámaras"
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'main')]]
            md_bg_color: app.bg_main
            elevation: 0
            specific_text_color: app.text_primary

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: '20dp'
                spacing: '14dp'
                adaptive_height: True

                MDBoxLayout:
                    adaptive_height: True
                    spacing: '8dp'
                    MDFillRoundFlatButton:
                        text: "Todas (3)"
                        font_size: "12sp"
                        size_hint_x: 1/3
                        md_bg_color: app.btn_primary if app.camera_filter == 'all' else app.bg_card
                        text_color: app.text_primary if app.camera_filter == 'all' else app.text_secondary
                        on_release: app.set_camera_filter('all')
                    MDFillRoundFlatButton:
                        text: "En línea (2)"
                        font_size: "12sp"
                        size_hint_x: 1/3
                        md_bg_color: app.btn_primary if app.camera_filter == 'online' else app.bg_card
                        text_color: app.text_primary if app.camera_filter == 'online' else app.text_secondary
                        on_release: app.set_camera_filter('online')
                    MDFillRoundFlatButton:
                        text: "Grabando (1)"
                        font_size: "12sp"
                        size_hint_x: 1/3
                        md_bg_color: app.btn_primary if app.camera_filter == 'recording' else app.bg_card
                        text_color: app.text_primary if app.camera_filter == 'recording' else app.text_secondary
                        on_release: app.set_camera_filter('recording')

                # Cámara 1
                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: dp(205) if app.camera_filter in ('all', 'online') else 0
                    opacity: 1 if app.camera_filter in ('all', 'online') else 0
                    disabled: app.camera_filter not in ('all', 'online')
                    md_bg_color: app.bg_card
                    radius: [20, 20, 20, 20]
                    padding: '12dp' if app.camera_filter in ('all', 'online') else 0
                    spacing: '8dp'

                    MDBoxLayout:
                        orientation: 'vertical'
                        md_bg_color: app.bg_input_nav
                        radius: [14, 14, 14, 14]
                        padding: '10dp'
                        MDLabel:
                            text: "EN LÍNEA • CAM 01"
                            font_style: 'Caption'
                            bold: True
                            adaptive_height: True
                            theme_text_color: 'Custom'
                            text_color: app.accent_cyan
                        MDIcon:
                            icon: 'video'
                            halign: 'center'
                            font_size: '42sp'
                            theme_text_color: 'Custom'
                            text_color: app.border_input

                    MDBoxLayout:
                        adaptive_height: True
                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True
                            MDLabel:
                                text: "Entrada principal"
                                bold: True
                                font_style: 'Subtitle1'
                                adaptive_height: True
                                theme_text_color: 'Custom'
                                text_color: app.text_primary
                            MDLabel:
                                text: "Resolución 1080p • 30fps"
                                font_style: 'Caption'
                                adaptive_height: True
                                theme_text_color: 'Custom'
                                text_color: app.text_secondary
                        MDIconButton:
                            icon: 'fullscreen'
                            theme_icon_color: 'Custom'
                            icon_color: app.accent_cyan
                            on_release: app.show_snackbar("Maximizando Entrada Principal")

                # Cámara 2
                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: dp(205) if app.camera_filter in ('all', 'online') else 0
                    opacity: 1 if app.camera_filter in ('all', 'online') else 0
                    disabled: app.camera_filter not in ('all', 'online')
                    md_bg_color: app.bg_card
                    radius: [20, 20, 20, 20]
                    padding: '12dp' if app.camera_filter in ('all', 'online') else 0
                    spacing: '8dp'

                    MDBoxLayout:
                        orientation: 'vertical'
                        md_bg_color: app.bg_input_nav
                        radius: [14, 14, 14, 14]
                        padding: '10dp'
                        MDLabel:
                            text: "EN LÍNEA • CAM 02"
                            font_style: 'Caption'
                            bold: True
                            adaptive_height: True
                            theme_text_color: 'Custom'
                            text_color: app.accent_cyan
                        MDIcon:
                            icon: 'pine-tree'
                            halign: 'center'
                            font_size: '42sp'
                            theme_text_color: 'Custom'
                            text_color: app.border_input

                    MDBoxLayout:
                        adaptive_height: True
                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True
                            MDLabel:
                                text: "Patio trasero"
                                bold: True
                                font_style: 'Subtitle1'
                                adaptive_height: True
                                theme_text_color: 'Custom'
                                text_color: app.text_primary
                            MDLabel:
                                text: "Visión nocturna infrarroja activa"
                                font_style: 'Caption'
                                adaptive_height: True
                                theme_text_color: 'Custom'
                                text_color: app.text_secondary
                        MDIconButton:
                            icon: 'fullscreen'
                            theme_icon_color: 'Custom'
                            icon_color: app.accent_cyan
                            on_release: app.show_snackbar("Maximizando Patio Trasero")

                # Cámara 3
                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: dp(205) if app.camera_filter in ('all', 'recording') else 0
                    opacity: 1 if app.camera_filter in ('all', 'recording') else 0
                    disabled: app.camera_filter not in ('all', 'recording')
                    md_bg_color: app.bg_card
                    radius: [20, 20, 20, 20]
                    padding: '12dp' if app.camera_filter in ('all', 'recording') else 0
                    spacing: '8dp'

                    MDBoxLayout:
                        orientation: 'vertical'
                        md_bg_color: app.bg_input_nav
                        radius: [14, 14, 14, 14]
                        padding: '10dp'
                        MDLabel:
                            text: "REC • CAM 03 • GRABANDO"
                            font_style: 'Caption'
                            bold: True
                            adaptive_height: True
                            theme_text_color: 'Custom'
                            text_color: app.sos_red
                        MDIcon:
                            icon: 'garage'
                            halign: 'center'
                            font_size: '42sp'
                            theme_text_color: 'Custom'
                            text_color: app.border_input

                    MDBoxLayout:
                        adaptive_height: True
                        MDBoxLayout:
                            orientation: 'vertical'
                            adaptive_height: True
                            MDLabel:
                                text: "Garaje vehicular"
                                bold: True
                                font_style: 'Subtitle1'
                                adaptive_height: True
                                theme_text_color: 'Custom'
                                text_color: app.text_primary
                            MDLabel:
                                text: "Detección de movimiento activada"
                                font_style: 'Caption'
                                adaptive_height: True
                                theme_text_color: 'Custom'
                                text_color: app.text_secondary
                        MDIconButton:
                            icon: 'fullscreen'
                            theme_icon_color: 'Custom'
                            icon_color: app.accent_cyan
                            on_release: app.show_snackbar("Maximizando Garaje")

                MDFillRoundFlatButton:
                    text: "+ AÑADIR CÁMARA"
                    font_size: "14sp"
                    bold: True
                    size_hint_x: 1
                    md_bg_color: app.btn_primary
                    text_color: app.text_primary
                    padding: "14dp"
                    radius: [100, 100, 100, 100]
                    on_release: app.show_snackbar("Buscando cámaras en la red Wi-Fi...")
'''


class ExpressiveApp(MDApp):
    # Paleta exacta de colores sólidos (Figma)
    bg_main = ColorProperty(get_color_from_hex('#111A4D'))
    bg_input_nav = ColorProperty(get_color_from_hex('#1A275E'))
    bg_card = ColorProperty(get_color_from_hex('#243575'))
    border_input = ColorProperty(get_color_from_hex('#5266AD'))
    text_primary = ColorProperty(get_color_from_hex('#FFFFFF'))
    text_secondary = ColorProperty(get_color_from_hex('#CDD9FF'))
    accent_cyan = ColorProperty(get_color_from_hex('#79F2ED'))
    btn_primary = ColorProperty(get_color_from_hex('#D9165D'))
    zone_alert = ColorProperty(get_color_from_hex('#4C1D95'))
    sos_red = ColorProperty(get_color_from_hex('#E11D48'))
    action_blue = ColorProperty(get_color_from_hex('#1665C1'))

    auth_tab = StringProperty('register')
    user_name = StringProperty('Usuario')
    user_phone_display = StringProperty('Sin registrar')
    camera_filter = StringProperty('all')

    sos_progress = NumericProperty(0.0)
    sos_status_text = StringProperty('Mantén pulsado 3 segundos')
    sos_alert_active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._sos_event = None
        self._sos_elapsed = 0.0

    def build(self):
        self.title = "Seguridad SOS - MD3 Expressive"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        Window.bind(on_keyboard=self.on_back_key)
        return Builder.load_string(KV)

    def on_back_key(self, window, key, *args):
        if key != 27:
            return False
        if self.sos_alert_active:
            self.cancel_sos_alert()
            return True
        current = self.root.current
        if current == 'cameras':
            self.root.current = 'main'
            return True
        if current == 'main':
            nav = self.root.get_screen('main').ids.bottom_nav
            if nav.ids.tab_manager.current != 'nav_home':
                nav.switch_tab('nav_home')
            return True
        return False

    def show_snackbar(self, message, bg_color=None):
        Clock.schedule_once(lambda dt: self._open_snackbar(message, bg_color), 0.15)

    def _open_snackbar(self, message, bg_color=None):
        color = bg_color if bg_color is not None else self.zone_alert
        try:
            if HAS_MD_SNACKBAR:
                MDSnackbar(
                    MDLabel(
                        text=message,
                        theme_text_color="Custom",
                        text_color=self.text_primary,
                    ),
                    y=dp(24),
                    pos_hint={"center_x": 0.5},
                    size_hint_x=0.9,
                    md_bg_color=color,
                ).open()
            else:
                Snackbar(text=message, bg_color=color).open()
        except Exception as e:
            print(f"[Aviso]: {message} ({e})")

    def set_auth_tab(self, tab):
        self.auth_tab = tab

    def set_camera_filter(self, filter_name):
        self.camera_filter = filter_name

    def process_auth_submit(self):
        auth_screen = self.root.get_screen('auth')
        phone = auth_screen.ids.user_phone.text.strip()
        pin = auth_screen.ids.user_pin.text.strip()

        if not phone:
            self.show_snackbar("Por favor escribe tu número de teléfono móvil.")
            return
        if len(pin) != 4:
            self.show_snackbar("El PIN debe tener exactamente 4 dígitos.")
            return

        try:
            if self.auth_tab == 'register':
                name = auth_screen.ids.reg_name.text.strip()
                self.user_name = name if name else "Usuario"
                message = f"¡Bienvenido a Seguridad SOS, {self.user_name}!"
            else:
                message = "Sesión iniciada correctamente."

            self.user_phone_display = phone
            auth_screen.ids.user_pin.text = ""

            main_screen = self.root.get_screen('main')
            main_screen.ids.bottom_nav.switch_tab('nav_home')
            self.root.transition.direction = 'left'
            self.root.current = 'main'
        except Exception:
            traceback.print_exc()
            self.show_snackbar("No se pudo iniciar sesión.")
            return

        self.show_snackbar(message)

    def start_sos_hold(self):
        self.cancel_sos_hold()
        self._sos_elapsed = 0.0
        self.sos_progress = 0.0
        self.sos_status_text = "Mantén pulsado... 3s"
        self._sos_event = Clock.schedule_interval(self._update_sos_hold, 0.05)

    def _update_sos_hold(self, dt):
        self._sos_elapsed += dt
        self.sos_progress = min(self._sos_elapsed / 3.0, 1.0)
        remaining = max(1, int(3 - self._sos_elapsed) + 1)
        self.sos_status_text = f"Enviando alerta en {remaining}s..."
        if self._sos_elapsed >= 3.0:
            self.cancel_sos_hold()
            self.activate_sos_overlay()

    def cancel_sos_hold(self):
        if self._sos_event is not None:
            self._sos_event.cancel()
            self._sos_event = None
        self._sos_elapsed = 0.0
        self.sos_progress = 0.0
        self.sos_status_text = "Mantén pulsado 3 segundos"

    def activate_sos_overlay(self):
        self.sos_alert_active = True

    def cancel_sos_alert(self):
        self.sos_alert_active = False
        self.show_snackbar("Alerta SOS desactivada.")

    def logout(self):
        self.cancel_sos_hold()
        self.sos_alert_active = False
        auth_screen = self.root.get_screen('auth')
        auth_screen.ids.user_pin.text = ""
        self.root.transition.direction = 'right'
        self.root.current = 'auth'
        self.show_snackbar("Has cerrado sesión con éxito.")


if __name__ == '__main__':
    ExpressiveApp().run()