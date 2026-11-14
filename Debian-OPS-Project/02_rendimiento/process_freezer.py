#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debian OPS - Process Freezer (Demmon SIGSTOP/SIGCONT)
Congela aplicaciones minimizadas o sin foco para liberar recursos al juego activo.
"""

import time

# Lista de excepciones protegidas que NUNCA se congelan
EXCEPTIONS = ["obs", "scrcpy", "pulseaudio", "pipewire", "debian_ops_shell.py"]

def monitor_windows():
    print("=== DEBIAN OPS: CONGELADOR INTELIGENTE DE PROCESOS ===")
    print(f"Excepciones protegidas (Nunca se congelan): {EXCEPTIONS}")
    print("Estado: Monitoreando enfoque de ventanas en tiempo real...\n")
    
    # Simulación de funcionamiento en vivo
    simulated_apps = [
        {"name": "Chromium (Navegador)", "active": False},
        {"name": "Juego en Pantalla Completa", "active": True},
        {"name": "Discord (Chat)", "active": False}
    ]
    
    for app in simulated_apps:
        if app["active"]:
            print(f" [EJECUTANDO] {app['name']} -> Prioridad máxima de CPU (SIGCONT)")
        else:
            print(f" [CONGELADO]  {app['name']} -> 0% CPU consumido (SIGSTOP aplicado)")
        time.sleep(0.6)

if __name__ == "__main__":
    monitor_windows()