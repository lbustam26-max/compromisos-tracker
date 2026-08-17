# 📋 Seguimiento de Compromisos

Dashboard web para hacer seguimiento a compromisos, siempre disponible en un link fijo.

---

## ¿Cómo funciona?

```
Tú actualizas el Excel → corres actualizar.py → haces git push → Vercel publica automáticamente
```

Tu jefe siempre accede al mismo link y ve los datos más recientes.

---

## CONFIGURACIÓN INICIAL (solo una vez)

### Paso 1 — Instalar herramientas

1. Instala **Git**: https://git-scm.com/downloads  
2. Instala **Python**: https://www.python.org/downloads  
3. En la consola (CMD o Terminal) instala las librerías:
   ```
   pip install pandas openpyxl
   ```

### Paso 2 — Crear cuenta en GitHub

1. Ve a https://github.com y crea una cuenta gratuita
2. Crea un repositorio nuevo llamado `compromisos-tracker`  
   - Márcalo como **público**
   - NO agregues README (lo tienes ya)

### Paso 3 — Subir los archivos a GitHub

Abre la consola en la carpeta de este proyecto y ejecuta:

```bash
git init
git add .
git commit -m "Primer commit"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/compromisos-tracker.git
git push -u origin main
```

> Reemplaza `TU_USUARIO` con tu usuario de GitHub.

### Paso 4 — Publicar en Vercel

1. Ve a https://vercel.com y crea cuenta **con tu cuenta de GitHub**
2. Haz clic en **"Add New Project"**
3. Selecciona el repositorio `compromisos-tracker`
4. Deja todo por defecto y haz clic en **Deploy**
5. Vercel te dará un link como: `https://compromisos-tracker.vercel.app`

✅ **¡Ese link es el que le das a tu jefe!** Nunca cambia.

---

## ACTUALIZAR LOS DATOS (cada vez que haya cambios)

1. Actualiza tu archivo `Compromisos.xlsx` como siempre
2. Copia el Excel a la carpeta del proyecto (reemplaza el anterior)
3. En la consola, ejecuta:
   ```
   python actualizar.py
   ```
4. Luego sube los cambios a GitHub:
   ```
   git add .
   git commit -m "Actualización seguimiento"
   git push
   ```
5. Vercel detecta el push y actualiza la página en ~30 segundos ⚡

---

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `index.html` | El dashboard (no tocar) |
| `compromisos.json` | Datos generados por el script |
| `actualizar.py` | Script para convertir el Excel a JSON |
| `Compromisos.xlsx` | Tu archivo Excel con los datos |
