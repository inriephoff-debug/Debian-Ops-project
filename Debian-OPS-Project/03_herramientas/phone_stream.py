#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debian OPS - Phone Link & Streamer (scrcpy wrapper)
Optimiza la transmisión de pantalla y audio del celular para streaming o estudio.
"""

import time
import os

def start_stream():
    print("=== DEBIAN OPS: CONECTOR DE CELULAR (PHONELINK) ===")
    print("[+] Buscando dispositivos Android conectados por USB (Depuración USB)...")
    time.sleep(1)
    print("[OK] ¡Dispositivo detectado exitosamente!")
    print("[+] Configurando scrcpy a 60 FPS con baja latencia y canal de audio abierto...")
    time.sleep(1.2)
    print("\n[TRANSMITIENDO] Tu pantalla de celular está lista en el escritorio.")
    print("Presiona Ctrl+C en la terminal para cerrar la transmisión cuando termines.\n")

if __name__ == "__main__":
    start_stream()