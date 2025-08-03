# 🔎 Escáner de Puertos en Python

Este es un escáner de puertos TCP desarrollado como parte de mi aprendizaje en Python y ciberseguridad, con ayuda de la academia de [s4vitar](https://youtube.com/@s4vitar).

---

## 📦 Funcionalidades

- Escaneo de puertos TCP en una dirección IP
- Soporte para puertos individuales, múltiples separados por coma y rangos
- Uso del módulo `socket` para establecer conexiones
- Reporte claro de puertos abiertos

---

## 📢 Novedades

- Implementado escaneo por rangos (`1-1000`)
- Soporte para múltiples puertos (`22,80,443`)
- Limpieza y mejoras de rendimiento general

---

## ⚙️ Requisitos

- Python 3.x  
- Sistema operativo: Linux, Windows o macOS

---

## 🧪 Cómo usarlo

Este script permite escanear puertos en una dirección IP específica, ya sea un único puerto, varios separados por coma o un rango completo.

### 📌 Sintaxis general

```bash
python3 net_scan.py -H <dirección IP> -p <puertos>
```

## 📋 Ejemplos

Escanear del puerto 1 al 1000:

```bash
python3 net_scan.py -H 192.168.1.1 -p 1-1000
```

Escanear puertos específicos:

```bash
python3 net_scan.py -H 192.168.1.1 -p 22,80,443
```

Escanear un solo puerto

```bash
python3 net_scan.py -H 192.168.1.1 -p 80
```

---

## Instalación
1. Clona el repositorio
   
```bash
git clone https://github.com/b4dr3flxz/net_scan.git
cd netscan
```
2. Crea y activa un entorno virtual (Recomendado)
   
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Instala las dependencias

```bash
pip install -r requirements.txt
```
4. Ejecuta la herramienta
   
```bash
python3 net_scan.py -H 192.168.1.1 -p 1-443
```

---

## 🛠️ Próximas mejoras

- Multithreading para acelerar el escaneo
- Soporte para escaneos de tipo UDP
- Escaneo de red basado en subredes (subnet scanning)
- Versión con interfaz gráfica (GUI) con Tkinter compatible con Windows

---

## 📚 Créditos

Desarrollado por [b4dr3flxz](https://github.com/b4dr3flxz)
Inspirado en ejercicios y contenidos de la academia de [s4vitar](https://youtube.com/@s4vitar) y la plataforma [Hack4u](https://hack4u.io)
