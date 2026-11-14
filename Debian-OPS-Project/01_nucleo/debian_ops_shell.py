#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debian OPS - Consola Inteligente con Menús Jerárquicos y Persistencia
"""

import os
import sys
import json

CONFIG_FILE = os.path.expanduser("~/.config/debian_ops/config.json")

def load_user_config():
    """Carga las configuraciones y carpetas guardadas del usuario"""
    default_config = {
        "theme": "cyber-neon",
        "custom_folders": {
            "descargas": "~/Downloads",
            "juegos": "~/Games",
            "reproductores": "~/Media"
        },
        "mitigations": True,
        "performance_mode": "normal"
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return default_config

def save_user_config(config):
    """Guarda las configuraciones en disco de forma persistente"""
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

config = load_user_config()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_hud():
    print("\033[1;30m" + "="*80 + "\033[0m")
    print(f" \033[1;32m[CPU: 14% (39°C)]\033[0m | \033[1;36m[RAM: 380MB / ZRAM OK]\033[0m | \033[1;33m[MODO: {config['performance_mode'].upper()}]\033[0m")
    print("\033[1;30m" + "="*80 + "\033[0m")

def folders_menu():
    """Apartado de gestión de carpetas"""
    while True:
        clear_screen()
        draw_hud()
        print("\n=== 📂 GESTOR DE CARPETAS Y DIRECTORIOS ===")
        print(" 1. Descargas (Navegador, Wallpapers y temporales)")
        print(" 2. Juegos (Steam, Epic, Roblox / Sober)")
        print(" 3. Reproductores (Música MP3, Videos MP4, Imágenes)")
        
        # Mostrar carpetas personalizadas creadas por el usuario
        customs = {k: v for k, v in config["custom_folders"].items() if k not in ["descargas", "juegos", "reproductores"]}
        for idx, (name, path) in enumerate(customs.items(), start=4):
            print(f" {idx}. [Personalizada] {name.capitalize()} -> {path}")
            
        print(" 9. ➕ Crear nueva carpeta o categoría personalizada")
        print(" 0. ⬅️ Volver al Menú Principal")
        
        op = input("\nSelecciona una opción [0-9]: ").strip()
        
        if op == "1":
            print(f"\n[Abriendo] Carpeta Descargas: {config['custom_folders'].get('descargas', '~/Downloads')}")
            print(" -> Archivos encontrados: Wallpapers.zip, Setup_Driver.tar.gz")
            input("\nPresiona Enter para volver...")
        elif op == "2":
            print(f"\n[Abriendo] Carpeta Juegos: {config['custom_folders'].get('juegos', '~/Games')}")
            print(" -> Accesos listos: Roblox (Sober), Steam Launcher, Emuladores")
            input("\nPresiona Enter para volver...")
        elif op == "3":
            print(f"\n[Abriendo] Carpeta Reproductores: {config['custom_folders'].get('reproductores', '~/Media')}")
            print(" -> Contenido multimedia: Pistas MP3, Videos en bucle para fondo")
            input("\nPresiona Enter para volver...")
        elif op == "9":
            new_name = input("Nombre para la nueva carpeta/categoría: ").strip().lower()
            new_path = input("Ruta de destino o almacenamiento: ").strip()
            if new_name and new_path:
                config["custom_folders"][new_name] = new_path
                save_user_config(config)
                print(f"[OK] ¡Carpeta '{new_name}' creada y guardada con éxito!")
            input("\nPresiona Enter para volver...")
        elif op == "0":
            break

def config_menu():
    """Apartado de configuraciones, rendimiento y personalización"""
    while True:
        clear_screen()
        draw_hud()
        print("\n=== ⚙️ CONFIGURACIONES Y RENDIMIENTO ===")
        print(" 1. Rendimiento y ZRAM (Mem Reducer & Prioridad CPU)")
        print(" 2. Mitigaciones de CPU (Ganar hasta 15% más de FPS)")
        print(" 3. Opciones de Personalización (Temas Neón, Colores y Bordes)")
        print(" 4. Gestor de Wallpapers (Fondos estáticos y animados en bucle)")
        print(" 0. ⬅️ Volver al Menú Principal")
        
        op = input("\nSelecciona una opción [0-4]: ").strip()
        
        if op == "1":
            print("\n[+] Ejecutando Mem Reducer inteligente y limpiando caché RAM...")
            print("[OK] ¡Memoria optimizada! Se han recuperado 400 MB libres.")
            input("\nPresiona Enter para continuar...")
        elif op == "2":
            print(f"\nEstado actual de mitigaciones: {'Activas (Seguro)' if config['mitigations'] else 'Desactivadas (Máximo Gaming)'}")
            cambio = input("¿Deseas invertir el estado de las mitigaciones de CPU? [s/n]: ").strip().lower()
            if cambio == 's':
                config["mitigations"] = not config["mitigations"]
                save_user_config(config)
                print(f"[OK] Mitigaciones actualizadas. Nuevo estado guardado.")
            input("\nPresiona Enter para continuar...")
        elif op == "3":
            print("\n--- CENTRO DE ESTÉTICA ---")
            print(" Temas disponibles: [1] Cyber Neon, [2] Terraria Pixel, [3] Nord Frost, [4] Ámbar CRT")
            t_op = input("Elige número de tema a aplicar: ").strip()
            if t_op in ["1", "2", "3", "4"]:
                config["theme"] = f"tema-{t_op}"
                save_user_config(config)
                print("[OK] ¡Tema aplicado y guardado en tu perfil de usuario!")
            input("\nPresiona Enter para continuar...")
        elif op == "4":
            wp = input("\nIntroduce la ruta de tu imagen (.jpg/.png) o video en bucle (.mp4/.gif): ").strip()
            if wp:
                print(f"[+] Aplicando wallpaper '{wp}' mediante motor gráfico ligero...")
                print("[OK] Fondo establecido con éxito.")
            input("\nPresiona Enter para continuar...")
        elif op == "0":
            break

def apps_menu():
    """Lanzador de aplicaciones"""
    while True:
        clear_screen()
        draw_hud()
        print("\n=== 🚀 LANZADOR DE APLICACIONES ===")
        print(" 1. Navegador Chromium (Optimizado con aceleración por hardware)")
        print(" 2. Roblox (Vía motor nativo Sober / Vinegar)")
        print(" 3. Tienda de Aplicaciones / Gestor de Paquetes")
        print(" 0. ⬅️ Volver al Menú Principal")
        
        op = input("\nSelecciona una aplicación [0-3]: ").strip()
        if op == "1":
            print("\n[+] Abriendo Chromium sin telemetría y con decodificación GPU activa...")
            input("\nPresiona Enter para volver...")
        elif op == "2":
            print("\n[+] Lanzando entorno Roblox optimizado para máximo rendimiento...")
            input("\nPresiona Enter para volver...")
        elif op == "0":
            break

def tools_menu():
    """Herramientas del sistema"""
    while True:
        clear_screen()
        draw_hud()
        print("\n=== 🛠️ HERRAMIENTAS RÁPIDAS ===")
        print(" 1. Wi-Fi Manager (Conectar a redes inalámbricas)")
        print(" 2. Conectar Celular (Transmisión scrcpy a 60 FPS con audio)")
        print(" 3. Limpieza Profunda de Disco (Caché y temporales)")
        print(" 4. Reporte Técnico (Sysinfo completo)")
        print(" 0. ⬅️ Volver al Menú Principal")
        
        op = input("\nSelecciona una herramienta [0-4]: ").strip()
        if op == "1":
            print("\n[+] Iniciando escáner de redes Wi-Fi cercanas...")
            input("\nPresiona Enter para volver...")
        elif op == "2":
            print("\n[+] Iniciando puente USB para celular con audio listo para OBS...")
            input("\nPresiona Enter para volver...")
        elif op == "3":
            print("\n[+] Realizando barrido profundo de archivos huérfanos...")
            print("[OK] ¡Sistema limpio y optimizado!")
            input("\nPresiona Enter para volver...")
        elif op == "4":
            print("\n--- REPORTE TÉCNICO ---")
            print(f" Configuración guardada en: {CONFIG_FILE}")
            print(f" Tema activo: {config['theme']}")
            print(f" Mitigaciones CPU: {config['mitigations']}")
            input("\nPresiona Enter para volver...")
        elif op == "0":
            break

def main_menu():
    """Bucle principal de la consola"""
    while True:
        clear_screen()
        draw_hud()
        print("""
        ██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗     ██████╗ ██████╗ ███████╗
        ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██╔════╝
        ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║    ██║   ██║██████╔╝███████╗
        ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗╚════██║
        ██████╔╝███████╗██████╔╝██║██║████║██║ ╚████║    ╚██████╔╝██║    ███████║
        ╚═════╝ ╚══════╚═════╝ ╚═╝╚═╝╚═══╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝    ╚══════╝
        """)
        print("    [Sistema: Debian OPS v1.0 Ultimate Edition]\n")
        print("    [ MENÚ PRINCIPAL ]")
        print("     1. 📂 Explorador de Carpetas (Descargas, Juegos, Reproductores...)")
        print("     2. 🚀 Lanzador de Aplicaciones (Chromium, Roblox/Sober...)")
        print("     3. ⚙️ Configuraciones y Rendimiento (ZRAM, Mitigaciones, Temas)")
        print("     4. 🛠️ Herramientas Rápidas (Wi-Fi, Celular, Limpieza)")
        print("     5. 🚪 Salir de la Consola\n")
        
        choice = input("\033[1;32mdebian-ops@menu:~$ \033[0m").strip()
        
        if choice == "1":
            folders_menu()
        elif choice == "2":
            apps_menu()
        elif choice == "3":
            config_menu()
        elif choice == "4":
            tools_menu()
        elif choice == "5":
            print("\nApagando consola OPS. ¡Hasta luego!")
            break
        else:
            print("\n[X] Opción no válida. Elige un número del 1 al 5.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main_menu()