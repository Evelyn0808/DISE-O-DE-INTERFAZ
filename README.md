# 🛡️ SEGURIDAD SOS — Sistema Unificado MD3 "Expressive" (5 Vistas)

> **Diseño de Interfaz Frontend & Móvil bajo los lineamientos de Material Design 3 (MD3) variante "Expressive".**

Este repositorio contiene la arquitectura completa, estilizada y funcional para la aplicación **SEGURIDAD SOS**, implementada en dos plataformas sincronizadas visual y funcionalmente:
1. **Versión Web:** HTML5 Semántico, CSS3 Puro con variables MD3 Expressive, JavaScript Vanilla interactivo con Web Audio API.
2. **Versión Móvil:** Python con **Kivy** y **KivyMD** (1.2.0 / 2.0 compatible), arquitectura de pantallas `MDScreenManager`, `MDBottomNavigation` y soporte táctil.

---

## 📱 Las 5 Vistas Principales

1. **Iniciar Sesión:** Acceso seguro con número de teléfono móvil y PIN numérico de 4 dígitos.
2. **Crear Cuenta:** Registro con nombre completo, teléfono móvil y PIN de seguridad.
3. **Inicio (Alerta SOS):** Saludo personalizado, botón central de pánico SOS con pulsado sostenido de 3 segundos y anillo de progreso SVG, y acceso directo a cámaras.
4. **Mis Cámaras:** Grilla de monitoreo en tiempo real con chips de filtrado (*Todas*, *En línea*, *Grabando*), marcas de tiempo sincronizadas y botón de retorno.
5. **Mi Perfil:** Panel de usuario con nombre, teléfono registrado, estado de protección satelital GPS activa y botón de cierre de sesión.

---

## 🎨 Principios de Diseño: Material Design 3 "Expressive"

* **Paleta Tonal Dinámica (Dark Mode OLED):**
  * `Primary Expressive SOS`: `#D32F2F` / `#E53935` (Rojo Carmesí de Alta Visibilidad).
  * `Surface & Background`: `#0F0F12` y `#18181E` (Obsidiana para ahorro de energía y legibilidad nocturna).
  * `Surface Container Variant`: `#262732` (Elevación táctil para tarjetas y campos).
  * `Success Monitor`: `#4CAF50` (Indicador en verde de cámaras y GPS activo).
* **Formas Ergonómicas y Píldoras:**
  * Botones y Tabs: Radio completo `9999px` (Pill Shape) para interacción rápida con el pulgar.
  * Tarjetas de cámaras y perfil: Radio `20px` a `28px` (Extra-Large MD3 Shape).
  * Campos de texto: Esquinas superiores redondeadas `12px 12px 0 0` con línea indicadora activa.
* **Microinteracciones y Audio Háptico:**
  * Anillo circular SVG con temporizador progresivo de 3 segundos al pulsar el botón SOS.
  * Cancelación instantánea si el usuario suelta antes de los 3 segundos.
  * Sirena disuasoria acústica generada en tiempo real mediante la **Web Audio API** (sin librerías ni archivos externos).
  * Barras de escaneo y relojes sincronizados en las cámaras de seguridad.

---

## 📁 Estructura del Proyecto

```text
DISEÑO DE INTERFAZ/
├── web/
│   ├── index.html            # Aplicación web con Shell de smartphone y 5 vistas
│   ├── styles.css            # Tokens MD3 Expressive, estilos CCTV y animaciones
│   └── app.js                # Lógica de navegación, pulsado de 3s y Web Audio API
├── mobile/
│   ├── main.py               # Aplicación móvil KivyMD con MDScreenManager y 5 vistas
│   ├── requirements.txt      # Dependencias verificadas (Kivy, KivyMD, Pillow)
│   └── run.bat               # Script lanzador para Windows
├── index.html                # Acceso directo raíz Web
├── styles.css                # Estilos raíz
├── app.js                    # Script raíz
├── main.py                   # Acceso directo raíz Móvil KivyMD
├── run_mobile.bat            # Lanzador rápido un solo clic para Windows
├── .gitignore                # Archivos ignorados para Git
└── README.md                 # Documentación técnica completa
```

---

## 🚀 Instrucciones de Ejecución

### 1. Versión Web (HTML5 / CSS3 / JavaScript)
1. Haz doble clic en `index.html` (o `web/index.html`) para abrirlo en cualquier navegador (Chrome, Edge, Firefox).
2. **Interacciones destacadas:**
   * Alterna entre **INICIAR SESIÓN** y **CREAR CUENTA**.
   * Escribe tu nombre, teléfono y PIN para ver cómo se actualiza tu perfil e inicio en tiempo real.
   * Mantén presionado el botón central **SOS** durante 3 segundos para activar la alarma.
   * Entra a **Ver cámaras** y prueba los chips de filtrado (*Todas*, *En línea*, *Grabando*).
   * Ve a **Ajustes** en la barra inferior para ver tus datos en **Mi perfil** y cerrar sesión.

### 2. Versión Móvil (Python / KivyMD)
#### Método Rápido (Doble Clic):
* Ejecuta el archivo `run_mobile.bat` ubicado en la raíz del proyecto.

#### Método por Consola:
```powershell
py main.py
```
