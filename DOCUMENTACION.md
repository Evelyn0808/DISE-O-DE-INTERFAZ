# 🛡️ DOCUMENTACIÓN INTEGRAL — SISTEMA VIGÍA / SEGURIDAD SOS
> **Arquitectura Unificada Móvil (KivyMD) & Web (HTML5/CSS3/JS) conectada a PostgreSQL 18 bajo Material Design 3 "Expressive".**

---

## 1. 📐 Arquitectura General del Sistema

El ecosistema **VIGÍA SOS** está compuesto por tres capas principales sincronizadas en tiempo real:

```text
[ Capa de Presentación ]
  ├── 📱 App Móvil KivyMD (main.py / mobile/main.py)
  ├── 💻 Panel Web Escritorio (web/index.html)
  └── 📱 Web Móvil Shell (index.html)
          │
          ▼
[ Capa de Backend & Lógica ]
  ├── ⚙️ db_manager.py (Conexión directa PostgreSQL & SHA-256)
  └── 🚀 api_server.py (API REST Puerto 5000 para clientes Web)
          │
          ▼
[ Capa de Persistencia ]
  └── 🐘 PostgreSQL 18 (BD: 'Diseño de Interfaz' en localhost:5432)
```

---

## 2. 🗄️ Parámetros de Conexión a PostgreSQL

* **Host:** `localhost`
* **Puerto:** `5432`
* **Base de Datos:** `Diseño de Interfaz`
* **Usuario:** `postgres`
* **Contraseña:** `1234`

### Módulos y Tablas (12 Tablas)
1. **Infraestructura:** `zones`, `cameras`, `sirens`
2. **Incidentes & Evidencia:** `incident_categories`, `incidents`, `evidence`
3. **Alertas & Protocolos:** `protocols`, `emergency_contacts`, `notifications`
4. **Usuarios & Términos:** `users`, `terms_and_conditions`, `terms_acceptances`

---

## 3. 🔐 Apartado de Autenticación con Campos Separados

Tanto en la versión móvil como en la versión web:

### Iniciar Sesión (Login)
* **Campo 1:** `Correo Electrónico` (con icono de email)
* **Campo 2:** `Contraseña` (con icono de cerrojo, campo oculto)
* **Botón:** `INICIAR SESIÓN`

### Crear Cuenta (Registro)
* **Campo 1:** `Nombre Completo`
* **Campo 2:** `Teléfono Móvil`
* **Campo 3:** `Correo Electrónico`
* **Campo 4:** `Contraseña de seguridad`
* **Botón:** `CREAR MI CUENTA SOS`

### 👤 Usuario Administrador para Pruebas
Se depuraron los usuarios de prueba temporales; el único usuario registrado actualmente en la base de datos es:
* **Correo:** `admin@vigia.local`
* **Contraseña:** `1234`
* **Rol:** `admin`
* **Teléfono:** `0990000000`

---

## 4. 🎨 Paleta de Diseño: Material Design 3 "Expressive"

* `Fondo Principal (bg_main)`: `#0A0E24` (Midnight Obsidian profundo)
* `Superficie / Contenedores (bg_input_nav)`: `#141A38` (Azul medianoche enriquecido)
* `Tarjetas Elevadas (bg_card)`: `#1E2750` (Tonal Elevation M3)
* `Bordes de Campos (border_input)`: `#384878` (Delineado fino)
* `Acento Neón Cyan (accent_cyan)`: `#00F2FE` (Cyan eléctrico brillante)
* `Botón Principal / SOS (btn_primary / sos_red)`: `#FF2D55` (Carmín Expressive vibrante)
* `Zona de Alerta (zone_alert)`: `#431D78` (Púrpura real)
* `Acciones Rápidas (action_blue)`: `#2563EB` (Azul zafiro)
* `Texto Principal (text_primary)`: `#FFFFFF`
* `Texto Secundario (text_secondary)`: `#A0B0D8`

---

## 5. 🎬 Animaciones de Transición entre Pantallas

Tanto en la versión móvil como en la versión web se añadieron transiciones fluidas con físicas desaceleradas (`cubic-bezier(0.16, 1, 0.3, 1)`):
* **Navegación Hacia Adelante (Push):** Desplazamiento lateral elástico de derecha a izquierda con suave desenfoque y escala (`translateX(45px) scale(0.96) -> translateX(0) scale(1)`).
* **Navegación Hacia Atrás (Pop):** Desplazamiento inverso fluido al regresar o al cerrar sesión (`logout()`).
* **Cascada de Elementos (Staggered Children):** Las tarjetas, botones y listas ingresan con un retraso escalonado de 40 a 60ms para una sensación dinámica y orgánica.
* **Kivy Mobile:** Implementación de `CardTransition(direction, mode='push'|'pop', duration=0.38)` en `MDScreenManager`.

---

## 6. ⚡ Los 3 Estados de Interfaz: Reposo • Interacción • Acción

Se implementó el ciclo de experiencia de usuario completo en todos los componentes:

### 1. Estado de Reposo (Rest / Idle)
* **Objetivo:** Mostrar una interfaz viva, serena y equilibrada mientras espera al usuario.
* **Botón SOS:** Micro-animación de respiración suave ambiental (`sosReposoBreathing` de 3.2s) con halo carmesí tenue y oscilación de escala (1.0 a 1.03).
* **Cámaras en Vivo:** Baliza circular cian (`live-dot`) parpadeante tipo faro de vigilancia (`@keyframes liveDotBeacon`).
* **Campos y Tarjetas:** Bordes precisos `#384878` y elevación de superficie sin saturación.

### 2. Estado de Interacción (Hover / Focus / Touch-Down)
* **Objetivo:** Responder inmediatamente cuando el usuario explora o enfoca un elemento.
* **Botones Principales y Acciones:** Elevación vertical (`translateY(-2px) scale(1.015)`), aumento de brillo del fondo y resplandor de neón (`box-shadow: 0 8px 25px rgba(255, 45, 85, 0.55)`).
* **Campos de Texto:** `:focus-within` activa halo cian de 3px (`box-shadow: 0 0 0 3px rgba(0, 242, 254, 0.25)`), cambio de color de icono y borde a Cyan Eléctrico.
* **Tarjetas:** Elevación con borde iluminado en cyan sutil (`border-color: rgba(0, 242, 254, 0.5)`).

### 3. Estado de Acción (Active / Pressed / Trigger / Feedback)
* **Objetivo:** Confirmar de forma física e inequívoca que la acción se ha ejecutado.
* **Compresión Física:** En `:active`, los botones y tarjetas sufren una compresión táctil elástica (`transform: scale(0.95)`).
* **Material Wave Ripple:** Ondas expansivas translúcidas que nacen exactamente en las coordenadas donde el usuario hace clic o toque.
* **Botón SOS Mantenido:** Activación de clase `.holding` con pulsación rápida de latidos (`@keyframes sosAccionHeartbeat` cada 0.35s), progreso radial SVG dinámico y cuenta regresiva enérgica: `¡ENVIANDO ALERTA EN 2s!`.
* **Disparo de Alerta:** Apertura del modal de emergencia con ondas concéntricas de radar de rescate (`@keyframes radarWaveExpand`).
* **Error de Validación:** Micro-animación de sacudida elástica horizontal (`@keyframes shakeErrorAction`) en el campo inválido.
* **Notificaciones Toast:** Entrada con rebote elástico (`@keyframes toastActionBounce`).

---

## 7. 🚀 Scripts de Lanzamiento Rápido

* **`mobile/run.bat`** o **`run_mobile.bat`**: Ejecuta la aplicación móvil en Python KivyMD.
* **`run_api.bat`**: Inicia el servidor de API en `http://localhost:5000` para la versión web.
* **`index.html`** y **`web/index.html`**: Se pueden abrir en cualquier navegador para usar la versión web.
* **`database/vigia_schema.sql`**: Script DDL para recrear la base de datos si fuera necesario.
* **`database/vigia_seeds.sql`**: Script de datos iniciales con cámaras, zonas y usuario admin.
