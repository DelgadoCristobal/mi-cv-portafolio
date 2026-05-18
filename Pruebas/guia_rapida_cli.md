# 🚀 Guía Rápida de Gemini CLI

Bienvenido a tu manual de referencia esencial para dominar este entorno de desarrollo asistido por IA.

---

## 1. 🚀 ¿Qué es este entorno seguro? (Sandbox)

Estamos trabajando específicamente dentro de la carpeta `gemini-lab`. Esto no es por accidente, sino por **seguridad**:

*   **Aislamiento:** Al limitar el acceso del agente a esta carpeta, evitamos que realice cambios accidentales o no deseados en archivos críticos de tu sistema, configuraciones personales o documentos privados.
*   **Prevención de Riesgos:** Dar acceso a la carpeta raíz de usuario (`C:\Users\tu_usuario`) permitiría a la IA leer o modificar archivos sensibles (como claves SSH, historial del navegador o archivos de sistema). 
*   **Control Total:** Aquí tienes un "parque de juegos" (sandbox) donde puedes experimentar, programar y crear con la tranquilidad de que tu sistema operativo está protegido.

---

## 2. ⌨️ Atajos de Teclado (Shortcuts)

Utiliza estos comandos clave para interactuar de forma fluida con el CLI:

| Atajo | Función | Descripción |
| :--- | :--- | :--- |
| **`!`** | **Modo Shell** | Ejecuta comandos directamente en la terminal (PowerShell/CMD). |
| **`@`** | **Selección de Archivos** | Abre un selector para añadir archivos o carpetas al contexto de la charla. |
| **`Double Esc`** | **Limpiar y Rebobinar** | Limpia la pantalla y "olvida" el historial de la sesión actual para ahorrar tokens. |
| **`Ctrl + Y`** | **Modo YOLO** | **¡Peligro!** Salta las confirmaciones de seguridad. El agente ejecutará todo sin preguntar. |
| **`Ctrl + V`** | **Pegar Imágenes** | Adjunta capturas de pantalla o imágenes directamente desde el portapapeles. |
| **`Ctrl + G`** | **Editor Externo** | Abre tu editor de texto predeterminado para redactar prompts largos o complejos. |

---

## 3. 🔄 Cómo volver a entrar

Si cierras la terminal o necesitas retomar el trabajo más tarde, usa estos comandos en tu CMD o PowerShell de Windows:

1.  **Navega a la carpeta del proyecto:**
    ```powershell
    cd Desktop\gemini-lab
    ```
2.  **Inicia el agente:**
    ```powershell
    gemini
    ```

> [!TIP]
> **Memoria Contextual:** Al iniciar, el agente escaneará los archivos dentro de `gemini-lab`. Simplemente dile: *"Analiza los archivos actuales y dime en qué nos quedamos"* para que recupere el contexto de tu proyecto.

---

## 4. 💳 Cuentas y Límites

El rendimiento y la estabilidad dependen de tu tipo de acceso:

*   **Google Login (Free Tier):** 
    *   Ideal para pruebas rápidas.
    *   Tiene límites de velocidad (Rate Limits) más estrictos.
    *   Puedes experimentar bloqueos temporales si haces muchas peticiones seguidas.
*   **Gemini API Key (Paid Tier 1+):**
    *   Recomendado para desarrollo serio.
    *   Límites de velocidad mucho más altos.
    *   Pago por uso, lo que evita interrupciones en el flujo de trabajo.

---

*Documento generado por Gemini CLI para `gemini-lab`* 🛠️
