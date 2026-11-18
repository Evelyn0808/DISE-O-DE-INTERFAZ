/* ==========================================================================
   SEGURIDAD SOS - MD3 EXPRESSIVE JAVASCRIPT CONTROLLER (5 VISTAS)
   ========================================================================== */

// Estado global de la aplicación sin datos predeterminados
const SOSApp = {
    user: {
        name: '',
        phone: '',
        pin: ''
    },
    currentScreen: 'auth-screen',
    sosPressTimer: null,
    sosPressStartTime: 0,
    sosHoldDuration: 3000, // 3 segundos
    sosAnimationFrame: null,
    audioCtx: null,
    sirenOsc: null
};

document.addEventListener('DOMContentLoaded', () => {
    initClock();
    initCameraClocks();
    initSosLongPress();
});

/**
 * Control de Pestañas en Autenticación (Login / Registro)
 */
function switchAuthTab(type) {
    const tabLogin = document.getElementById('tab-login');
    const tabRegister = document.getElementById('tab-register');
    const formLogin = document.getElementById('form-login');
    const formRegister = document.getElementById('form-register');

    if (!tabLogin || !tabRegister || !formLogin || !formRegister) return;

    tabLogin.classList.remove('active');
    tabRegister.classList.remove('active');
    formLogin.classList.remove('active');
    formRegister.classList.remove('active');

    if (type === 'login') {
        tabLogin.classList.add('active');
        formLogin.classList.add('active');
    } else {
        tabRegister.classList.add('active');
        formRegister.classList.add('active');
    }
}

/**
 * Navegación Principal entre Pantallas
 */
function navigateTo(screenId) {
    SOSApp.currentScreen = screenId;
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    
    const target = document.getElementById(screenId);
    if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    const globalNav = document.getElementById('global-nav');
    if (screenId === 'home-screen' || screenId === 'profile-screen') {
        globalNav.style.display = 'flex';
        const navItems = document.querySelectorAll('.nav-item');
        navItems.forEach(nav => nav.classList.remove('active'));

        if (screenId === 'home-screen') {
            if (navItems[1]) navItems[1].classList.add('active');
        } else if (screenId === 'profile-screen') {
            if (navItems[2]) navItems[2].classList.add('active');
        }
    } else {
        globalNav.style.display = 'none';
    }
}

/**
 * Navegación desde la Barra Inferior (Bottom Nav)
 */
function navigateNav(screenId, element) {
    document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
    element.classList.add('active');
    navigateTo(screenId);
}

/**
 * Envío de Formularios de Login / Registro
 */
function handleAuthSubmit(event, type) {
    event.preventDefault();

    if (type === 'register') {
        const nameInput = document.getElementById('reg-name');
        const phoneInput = document.getElementById('reg-phone');
        const pinInput = document.getElementById('reg-pin');

        const enteredName = nameInput ? nameInput.value.trim() : '';
        const enteredPhone = phoneInput ? phoneInput.value.trim() : '';
        const enteredPin = pinInput ? pinInput.value.trim() : '';

        if (!enteredPhone) {
            showToast('Por favor ingresa tu número telefónico.');
            return;
        }
        if (enteredPin.length !== 4) {
            showToast('El PIN debe tener exactamente 4 dígitos.');
            return;
        }

        SOSApp.user.name = enteredName || 'Usuario';
        SOSApp.user.phone = enteredPhone;
        SOSApp.user.pin = enteredPin;

        showToast(`¡Cuenta creada con éxito! Bienvenido, ${SOSApp.user.name}`);
    } else {
        const phoneInput = document.getElementById('login-phone');
        const pinInput = document.getElementById('login-pin');

        const enteredPhone = phoneInput ? phoneInput.value.trim() : '';
        const enteredPin = pinInput ? pinInput.value.trim() : '';

        if (!enteredPhone) {
            showToast('Por favor ingresa tu número de teléfono móvil.');
            return;
        }
        if (enteredPin.length !== 4) {
            showToast('El PIN debe tener 4 dígitos numéricos.');
            return;
        }

        if (!SOSApp.user.name) {
            SOSApp.user.name = 'Usuario';
        }
        SOSApp.user.phone = enteredPhone;
        SOSApp.user.pin = enteredPin;

        showToast('Sesión iniciada correctamente.');
    }

    // Actualizar datos en pantalla de Inicio y Perfil
    updateUserProfileDisplays();

    // Navegar a Home
    setTimeout(() => {
        navigateTo('home-screen');
    }, 400);
}

function updateUserProfileDisplays() {
    const greeting = document.getElementById('home-greeting');
    const profileName = document.getElementById('profile-name-display');
    const profilePhone = document.getElementById('profile-phone-display');

    const displayName = SOSApp.user.name || 'Usuario';
    const displayPhone = SOSApp.user.phone || 'Sin registrar';

    if (greeting) greeting.textContent = `Hola, ${displayName.split(' ')[0]}`;
    if (profileName) profileName.textContent = displayName;
    if (profilePhone) profilePhone.textContent = displayPhone;
}

/**
 * LÓGICA DE PULSADO LARGO (3 SEGUNDOS) PARA EL BOTÓN SOS
 * Incluye barra de progreso circular SVG animada y cancelación al soltar.
 */
function initSosLongPress() {
    const btn = document.getElementById('btnSos');
    const circle = document.getElementById('progress-circle');
    const statusLabel = document.getElementById('sos-status-label');
    if (!btn || !circle) return;

    const totalCircumference = 603; // 2 * Math.PI * 96

    const startPress = (e) => {
        e.preventDefault();
        btn.classList.add('pressing');
        SOSApp.sosPressStartTime = performance.now();
        if (statusLabel) statusLabel.textContent = 'Manteniendo... ¡3 segundos!';

        // Loop de animación fluida del círculo de progreso
        const updateProgress = (now) => {
            const elapsed = now - SOSApp.sosPressStartTime;
            const progress = Math.min(elapsed / SOSApp.sosHoldDuration, 1);
            
            // Reducir offset del trazo SVG (0 = completo)
            circle.style.strokeDashoffset = totalCircumference * (1 - progress);

            if (progress < 1) {
                SOSApp.sosAnimationFrame = requestAnimationFrame(updateProgress);
            } else {
                // Se completaron los 3 segundos
                triggerEmergencyAlert();
                resetPressState();
            }
        };

        cancelAnimationFrame(SOSApp.sosAnimationFrame);
        SOSApp.sosAnimationFrame = requestAnimationFrame(updateProgress);
    };

    const cancelPress = () => {
        resetPressState();
    };

    const resetPressState = () => {
        btn.classList.remove('pressing');
        cancelAnimationFrame(SOSApp.sosAnimationFrame);
        circle.style.strokeDashoffset = totalCircumference;
        if (statusLabel) statusLabel.textContent = 'Mantén pulsado 3 segundos';
    };

    // Eventos de ratón
    btn.addEventListener('mousedown', startPress);
    btn.addEventListener('mouseup', cancelPress);
    btn.addEventListener('mouseleave', cancelPress);

    // Eventos táctiles para móviles
    btn.addEventListener('touchstart', startPress, { passive: false });
    btn.addEventListener('touchend', cancelPress);
    btn.addEventListener('touchcancel', cancelPress);
}

/**
 * Disparo de la Alerta SOS Inmediata
 */
function triggerEmergencyAlert() {
    const overlay = document.getElementById('alert-overlay');
    if (overlay) overlay.classList.add('active');

    // Vibración háptica en dispositivos móviles soportados
    if (navigator.vibrate) {
        navigator.vibrate([300, 150, 300, 150, 500]);
    }

    startAudioSiren();
    showToast('🚨 ¡ALERTA SOS ENVIADA A CENTRAL Y POLICÍA!');
}

function cancelSOSAlert() {
    const overlay = document.getElementById('alert-overlay');
    if (overlay) overlay.classList.remove('active');
    stopAudioSiren();
    showToast('Alerta SOS desactivada.');
}

/**
 * Sintetizador Acústico de Sirena de Emergencia (Web Audio API)
 */
function startAudioSiren() {
    try {
        if (!SOSApp.audioCtx) {
            SOSApp.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (SOSApp.audioCtx.state === 'suspended') {
            SOSApp.audioCtx.resume();
        }

        if (SOSApp.sirenOsc) return;

        const ctx = SOSApp.audioCtx;
        const osc = ctx.createOscillator();
        const lfo = ctx.createOscillator();
        const gain = ctx.createGain();
        const lfoGain = ctx.createGain();

        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(800, ctx.currentTime);

        lfo.type = 'sine';
        lfo.frequency.setValueAtTime(2.5, ctx.currentTime);
        lfoGain.gain.setValueAtTime(280, ctx.currentTime);

        lfo.connect(osc.frequency);
        osc.connect(gain);
        gain.connect(ctx.destination);
        gain.gain.setValueAtTime(0.18, ctx.currentTime);

        osc.start();
        lfo.start();

        SOSApp.sirenOsc = { osc, lfo };
    } catch (e) {
        console.warn('Audio API no disponible:', e);
    }
}

function stopAudioSiren() {
    if (SOSApp.sirenOsc) {
        try {
            SOSApp.sirenOsc.osc.stop();
            SOSApp.sirenOsc.osc.disconnect();
            SOSApp.sirenOsc.lfo.stop();
            SOSApp.sirenOsc.lfo.disconnect();
        } catch (e) {}
        SOSApp.sirenOsc = null;
    }
}

/**
 * Filtro de Cámaras por Estado
 */
function filterCameras(filter, chipElement) {
    document.querySelectorAll('.md3-chip').forEach(c => c.classList.remove('active'));
    chipElement.classList.add('active');

    const cameras = document.querySelectorAll('.camera-item');
    cameras.forEach(cam => {
        if (filter === 'all') {
            cam.style.display = 'flex';
        } else if (filter === 'online') {
            cam.style.display = cam.classList.contains('online') ? 'flex' : 'none';
        } else if (filter === 'recording') {
            cam.style.display = cam.classList.contains('recording') ? 'flex' : 'none';
        }
    });
}

/**
 * Reloj de barra de estado
 */
function initClock() {
    const clockEl = document.getElementById('current-clock');
    if (!clockEl) return;
    const tick = () => {
        const now = new Date();
        const h = String(now.getHours()).padStart(2, '0');
        const m = String(now.getMinutes()).padStart(2, '0');
        clockEl.textContent = `${h}:${m}`;
    };
    tick();
    setInterval(tick, 10000);
}

/**
 * Relojes en tiempo real para las cámaras de seguridad
 */
function initCameraClocks() {
    const updateCamClocks = () => {
        const now = new Date();
        const pad = n => String(n).padStart(2, '0');
        const timeStr = `${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
        document.querySelectorAll('.cam-clock').forEach((el, index) => {
            el.textContent = `CAM 0${index + 1} • ${timeStr} REC`;
        });
    };
    updateCamClocks();
    setInterval(updateCamClocks, 1000);
}

/**
 * Toast Feedback Notificador
 */
let toastTimeout = null;
function showToast(msg) {
    const toast = document.getElementById('md3-toast');
    const text = document.getElementById('toast-text');
    if (!toast || !text) return;

    text.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
        toast.classList.remove('show');
    }, 3200);
}
