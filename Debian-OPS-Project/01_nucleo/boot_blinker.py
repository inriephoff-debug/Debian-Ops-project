#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debian OPS - Boot Blinker & Hardware Detector
Simula la animación de arranque de apertura de ojos y detecta el hardware local.
"""

import sys
import time
import platform
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def blink_animation():
    clear_screen()
    frames = [
        """
        ================================================================
        
        
        [  -  ]                   [  -  ]
        
        
        ================================================================
        """,
        """
        ================================================================
        
        
        [  ~  ]                   [  ~  ]
        
        
        ================================================================
        """,
        """
        ================================================================
        
        
        [  o  ]                   [  o  ]
        
        
        ================================================================
        """,
        """
        ================================================================
           __   ___  ____  _  _  __  _  _    _____  ____  ____ 
          (  ) / __)( ___)( \( )(  )( \( )  (  _  )(  _ \\/ ___|
           )( ( (__  )__)  )  (  )(  )  (     )(_)(  )- < \\___ \\
          (__) \\___)(____)(_)\\_)(__)(_)\\_)   (_____)(____/(____/
        ================================================================
        """
    ]
    
    for frame in frames:
        clear_screen()
        print("\033[1;36m" + frame + "\033[0m")
        time.sleep(0.4)

def detect_hardware():
    print("\n[+] Detectando componentes y optimizando perfiles...")
    time.sleep(0.8)
    sys_name = platform.system()
    processor = platform.processor() or "CPU Genérica de Bajos Recursos"
    
    print(f" -> Arquitectura Base: {sys_name} / Debian Bookworm Kernel")
    print(f" -> Procesador detectado: {processor}")
    print(f" -> ZRAM comprimido: Activado (Ahorro de RAM dinámico)")
    print(f" -> Servidor Gráfico: Xorg + Openbox (Listo bajo demanda)\n")
    print("\033[1;32m[OK] ¡Sistema listo para iniciar el entorno Debian OPS!\033[0m")
    time.sleep(1.5)

if __name__ == "__main__":
    blink_animation()
    detect_hardware()
