"""
=============================================================================
SEGURIDAD SOS - VERSIÓN MÓVIL KIVYMD (MATERIAL DESIGN 3 EXPRESSIVE)
PALETA DE COLORES SÓLIDOS SIN DEGRADADOS
=============================================================================
"""

import traceback
import db_manager
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
from kivy.animation import Animation
from kivy.uix.screenmanager import CardTransition, SlideTransition, FadeTransition
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

                # --- VISTA LOGIN ---
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: '12dp'
                    adaptive_height: True
                    opacity: 1 if app.auth_tab == 'login' else 0
                    disabled: app.auth_tab != 'login'
                    size_hint_y: None
                    height: self.minimum_height if app.auth_tab == 'login' else 0

                    MDLabel:
                        text: "Bienvenido de nuevo"
                        font_style: 'H6'
                        bold: True
                        adaptive_height: True
                        theme_text_color: 'Custom'
                        text_color: app.text_primary

                    MDLabel:
                        text: "Ingresa con tu correo y contraseña registrados"
                        font_style: 'Caption'
                        adaptive_height: True
                        theme_text_color: 'Custom'
                        text_color: app.text_secondary

                    MDTextField:
                        id: login_email
                        hint_text: "Correo Electrónico"
                        mode: "fill"
                        icon_left: "email-outline"
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
                        radius: [14, 14, 0, 0]

                    MDTextField:
                        id: login_password
                        hint_text: "Contraseña"
                        mode: "fill"
                        icon_left: "lock-outline"
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
                        radius: [14, 14, 0, 0]

                    MDFillRoundFlatButton:
                        text: "INICIAR SESIÓN"
                        font_size: "15sp"
                        bold: True
                        size_hint_x: 1
                        md_bg_color: app.btn_primary
                        text_color: app.text_primary
                        padding: "16dp"
                        radius: [100, 100, 100, 100]
                        on_release: app.process_auth_submit()

                # --- VISTA REGISTRO ---
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: '12dp'
                    adaptive_height: True
                    opacity: 1 if app.auth_tab == 'register' else 0
                    disabled: app.auth_tab != 'register'
                    size_hint_y: None
                    height: self.minimum_height if app.auth_tab == 'register' else 0

                    MDLabel:
                        text: "Crea tu cuenta SOS"
                        font_style: 'H6'
                        bold: True
                        adaptive_height: True
                        theme_text_color: 'Custom'
                        text_color: app.text_primary

                    MDLabel:
                        text: "Protege a tu familia y comunidad las 24 horas"
                        font_style: 'Caption'
                        adaptive_height: True
                        theme_text_color: 'Custom'
                        text_color: app.text_secondary

                    MDTextField:
                        id: reg_name
                        hint_text: "Nombre Completo"
                        mode: "fill"
                        icon_left: "account-outline"
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
                        radius: [14, 14, 0, 0]

                    MDTextField:
                        id: reg_phone
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
                        radius: [14, 14, 0, 0]

                    MDTextField:
                        id: reg_email
                        hint_text: "Correo Electrónico"
                        mode: "fill"
                        icon_left: "email-outline"
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
                        radius: [14, 14, 0, 0]

                    MDTextField:
                        id: reg_password
                        hint_text: "Contraseña de seguridad"
                        mode: "fill"
                        icon_left: "lock-outline"
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
                        radius: [14, 14, 0, 0]

                    MDFillRoundFlatButton:
                        text: "CREAR MI CUENTA SOS"
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
                                            circle: (self.center_x, self.center_y, dp(90 * app.sos_scale))
                                            width: dp(4)
                                        Color:
                                            rgba: app.accent_cyan
                                        Line:
                                            circle: (self.center_x, self.center_y, dp(90 * app.sos_scale), 0, app.sos_progress * 360)
                                            width: dp(5)

                                MDFillRoundFlatButton:
                                    text: "SOS\\nPEDIR AYUDA"
                                    halign: "center"
                                    font_size: "24sp"
                                    bold: True
                                    size_hint: None, None
                                    size: (dp(162 * app.sos_scale), dp(162 * app.sos_scale))
                                    pos_hint: {"center_x": .5, "center_y": .54}
                                    md_bg_color: app.sos_red
                                    text_color: app.text_primary
                                    radius: [dp(81 * app.sos_scale), dp(81 * app.sos_scale), dp(81 * app.sos_scale), dp(81 * app.sos_scale)]
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
                            on_release: app.navigate_to('cameras', 'left')

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
            left_action_items: [['arrow-left', lambda x: app.navigate_to('main', 'right')]]
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
    # Paleta de colores Material Design 3 Expressive
    bg_main = ColorProperty(get_color_from_hex('#0A0E24'))
    bg_input_nav = ColorProperty(get_color_from_hex('#141A38'))
    bg_card = ColorProperty(get_color_from_hex('#1E2750'))
    border_input = ColorProperty(get_color_from_hex('#384878'))
    text_primary = ColorProperty(get_color_from_hex('#FFFFFF'))
    text_secondary = ColorProperty(get_color_from_hex('#A0B0D8'))
    accent_cyan = ColorProperty(get_color_from_hex('#00F2FE'))
    btn_primary = ColorProperty(get_color_from_hex('#FF2D55'))
    zone_alert = ColorProperty(get_color_from_hex('#431D78'))
    sos_red = ColorProperty(get_color_from_hex('#FF2D55'))
    action_blue = ColorProperty(get_color_from_hex('#2563EB'))

    auth_tab = StringProperty('login')
    user_name = StringProperty('Usuario')
    user_phone_display = StringProperty('Sin registrar')
    camera_filter = StringProperty('all')
    current_user_id = NumericProperty(0)
    current_user_email = StringProperty('')
    current_user_role = StringProperty('')

    sos_progress = NumericProperty(0.0)
    sos_status_text = StringProperty('Mantén pulsado 3 segundos')
    sos_alert_active = BooleanProperty(False)
    sos_scale = NumericProperty(1.0)
    live_beacon_alpha = NumericProperty(1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._sos_event = None
        self._sos_elapsed = 0.0

    def build(self):
        self.title = "Seguridad SOS - MD3 Expressive (Vigía DB)"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        Window.bind(on_keyboard=self.on_back_key)

        # Prueba de conexión a PostgreSQL
        try:
            ok, msg = db_manager.test_db_connection()
            if ok:
                print("[Vigía PostgreSQL]: Conectado exitosamente a 'Diseño de Interfaz'.")
            else:
                print(f"[Vigía PostgreSQL Aviso]: {msg}")
        except Exception as e:
            print(f"[Vigía PostgreSQL Error]: {e}")

        root = Builder.load_string(KV)
        root.transition = CardTransition(direction='left', mode='push', duration=0.36)
        return root

    def on_start(self):
        # Micro-animación de Reposo: Respiración suave del botón SOS
        sos_breathing = (
            Animation(sos_scale=1.03, duration=1.6, t='in_out_sine') +
            Animation(sos_scale=1.0, duration=1.6, t='in_out_sine')
        )
        sos_breathing.repeat = True
        sos_breathing.start(self)

        # Micro-animación de Reposo: Faro de baliza en vivo para cámaras
        beacon_breathing = (
            Animation(live_beacon_alpha=0.35, duration=1.0, t='in_out_quad') +
            Animation(live_beacon_alpha=1.0, duration=1.0, t='in_out_quad')
        )
        beacon_breathing.repeat = True
        beacon_breathing.start(self)

    def navigate_to(self, screen_name, direction='left'):
        if not self.root:
            return
        if self.root.current == screen_name:
            return
        mode = 'push' if direction == 'left' else 'pop'
        self.root.transition = CardTransition(direction=direction, mode=mode, duration=0.36)
        self.root.current = screen_name

    def on_back_key(self, window, key, *args):
        if key != 27:
            return False
        if self.sos_alert_active:
            self.cancel_sos_alert()
            return True
        current = self.root.current
        if current == 'cameras':
            self.navigate_to('main', direction='right')
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

        try:
            if self.auth_tab == 'register':
                name = auth_screen.ids.reg_name.text.strip()
                phone = auth_screen.ids.reg_phone.text.strip()
                email = auth_screen.ids.reg_email.text.strip()
                password = auth_screen.ids.reg_password.text.strip()

                if not name:
                    self.show_snackbar("Por favor escribe tu nombre completo.")
                    return
                if not phone:
                    self.show_snackbar("Por favor escribe tu teléfono móvil.")
                    return
                if not email:
                    self.show_snackbar("Por favor escribe tu correo electrónico.")
                    return
                if not password:
                    self.show_snackbar("Por favor ingresa una contraseña.")
                    return

                success, message, user_data = db_manager.register_user(name, email, phone, password)
                if not success:
                    self.show_snackbar(message)
                    return

                self.current_user_id = user_data['id']
                self.user_name = user_data['name']
                self.user_phone_display = user_data.get('phone') or user_data.get('email')
                self.current_user_email = user_data.get('email', '')
                self.current_user_role = user_data.get('role', 'viewer')
                auth_screen.ids.reg_password.text = ""
            else:
                email = auth_screen.ids.login_email.text.strip()
                password = auth_screen.ids.login_password.text.strip()

                if not email:
                    self.show_snackbar("Por favor escribe tu correo electrónico.")
                    return
                if not password:
                    self.show_snackbar("Por favor ingresa tu contraseña.")
                    return

                success, message, user_data = db_manager.login_user(email, password)
                if not success:
                    self.show_snackbar(message)
                    return

                self.current_user_id = user_data['id']
                self.user_name = user_data['name']
                self.user_phone_display = user_data.get('phone') or user_data.get('email')
                self.current_user_email = user_data.get('email', '')
                self.current_user_role = user_data.get('role', 'viewer')
                auth_screen.ids.login_password.text = ""

            main_screen = self.root.get_screen('main')
            main_screen.ids.bottom_nav.switch_tab('nav_home')
            self.navigate_to('main', direction='left')
            self.show_snackbar(message)
        except Exception as e:
            traceback.print_exc()
            self.show_snackbar(f"Error de conexión: {e}")

    def start_sos_hold(self):
        self.cancel_sos_hold()
        self._sos_elapsed = 0.0
        self.sos_progress = 0.0
        self.sos_scale = 0.95  # Tactile button compression (Acción)
        self.sos_status_text = "¡ENVIANDO ALERTA EN 3s!"
        self._sos_event = Clock.schedule_interval(self._update_sos_hold, 0.05)

    def _update_sos_hold(self, dt):
        self._sos_elapsed += dt
        self.sos_progress = min(self._sos_elapsed / 3.0, 1.0)
        remaining = max(1, int(3 - self._sos_elapsed) + 1)
        self.sos_status_text = f"¡ENVIANDO ALERTA EN {remaining}s!"
        if self._sos_elapsed >= 3.0:
            self.cancel_sos_hold()
            self.activate_sos_overlay()

    def cancel_sos_hold(self):
        if self._sos_event is not None:
            self._sos_event.cancel()
            self._sos_event = None
        self._sos_elapsed = 0.0
        self.sos_progress = 0.0
        self.sos_scale = 1.0
        self.sos_status_text = "Mantén pulsado 3 segundos"

    def activate_sos_overlay(self):
        self.sos_alert_active = True
        try:
            if self.current_user_id:
                db_manager.record_sos_alert(self.current_user_id)
        except Exception:
            pass

    def cancel_sos_alert(self):
        self.sos_alert_active = False
        self.show_snackbar("Alerta SOS desactivada.")

    def logout(self):
        self.cancel_sos_hold()
        self.sos_alert_active = False
        self.current_user_id = 0
        self.current_user_email = ""
        self.current_user_role = ""
        self.user_name = "Usuario"
        self.user_phone_display = "Sin registrar"
        auth_screen = self.root.get_screen('auth')
        if 'login_password' in auth_screen.ids:
            auth_screen.ids.login_password.text = ""
        self.navigate_to('auth', direction='right')
        self.show_snackbar("Has cerrado sesión con éxito.")


if __name__ == '__main__':
    ExpressiveApp().run()