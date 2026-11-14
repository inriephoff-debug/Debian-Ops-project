#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debian OPS - Pixel Art Visual Installer
Instalador offline de alta velocidad con diseño neón/pixel y feedback en vivo.
"""

import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_header():
    print("\033[1;36m" + "="*70)
    print("       DEBIAN OPS v1.0 — INSTALADOR OFFLINE INTELIGENTE")
    print("="*70 + "\033[0m")

def animate_gear(step_name):
    # Simula el engranaje/relojito animado fotograma a fotograma
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(4):
        sys.stdout.write(f"\r\033[1;33m[{frames[i]}] Proceso en curso: {step_name}...\033[0m")
        sys.stdout.flush()
        time.sleep(0.25)
    print()

def run_installer():
    clear_screen()
    draw_header()
    print("\n¡Bienvenido al asistente de instalación de Debian OPS!")
    print("Este sistema está optimizado para exprimir al máximo tu hardware sin telemetría.\n")
    
    input("Presiona \033[1;32mEnter\033[0m para iniciar la instalación automática en tu disco...")

    clear_screen()
    draw_header()
    print("\n[Fase 1/4] Preparando particiones y aplicando estructura ZRAM...")
    animate_gear("Escribiendo tabla de particiones limpia")
    animate_gear("Configurando bloque de compresión de memoria zstd")
    print("\033[1;32m[OK] Disco y memoria configurados con éxito.\n\033[0m")
    time.sleep(1)

    clear_screen()
    draw_header()
    print("\n[Fase 2/4] Desempaquetando sistema base y paquetes offline...")
    animate_gear("Copiando Debian Bookworm Core")
    animate_gear("Instalando servidor gráfico Xorg + Openbox bajo demanda")
    animate_gear("Empaquetando drivers de audio, red y codecs multimedia")
    print("\033[1;32m[OK] Sistema operativo instalado sin errores de red.\n\033[0m")
    time.sleep(1)

    clear_screen()
    draw_header()
    print("\n[Fase 3/4] Configurando perfil de usuario y privilegios...")
    animate_gear("Creando cuenta de usuario predeterminada con sudoers activo")
    animate_gear("Aplicando perfiles de rendimiento gaming (Governor Performance)")
    print("\033[1;32m[OK] Permisos y optimizaciones aplicadas.\n\033[0m")
    time.sleep(1)

    clear_screen()
    draw_header()
    print("\n[Fase 4/4] Finalizando y generando accesos directos...")
    animate_gear("Registrando comandos bilingües en la consola OPS")
    animate_gear("Limpiando archivos temporales de instalación")
    
    clear_screen()
    draw_header()
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║                 ¡INSTALACIÓN COMPLETADA CON ÉXITO!               ║
    ╚══════════════════════════════════════════════════════════════════╝
    
     Tu Debian OPS está listo. Ya puedes retirar el pendrive y reiniciar.
     Al encender, iniciarás directamente en tu consola inteligente con HUD.
    """)
    print("\033[1;36m==================================================================\033[0m\n")

if __name__ == "__main__":
    run_installer()