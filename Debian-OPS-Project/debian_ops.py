#!/usr/bin/env python3
import os
import sys

# Importación de módulos locales
from core.auth import login_screen
from visual.customizer import run_customizer
from rendimiento.optimizer import run_performance_menu
from herramientas.utilities import clean_system, phone_link

# Códigos de color base
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
WHITE = "\033[97m"
YELLOW = "\033[93m"

# Estado global del sistema
system_state = {
    "theme_color": "\033[92m",  # Verde por defecto
    "theme_name": "Verde Neón",
    "folder_style": "Con icono (📁)",
    "folder_icon": "📁",
    "border_style": "Doble línea"
}

current_path = os.getcwd()

def show_hud(section="CONSOLA PRINCIPAL"):
    color = system_state["theme_color"]
    print(f"{color}    ╔════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{color}    ║{RESET} {BOLD}DEBIAN OPS{RESET} │ Sección: {section} │ RAM: 180MB │ CPU: 2% (45°C)          {color}║{RESET}")
    print(f"{color}    ╚════════════════════════════════════════════════════════════════════════╝{RESET}\n")

def cmd_open(args):
    global current_path
    target = args[0] if args else current_path
    if target != current_path and not os.path.isabs(target):
        target = os.path.join(current_path, target)
        
    try:
        if os.path.isdir(target):
            current_path = os.path.abspath(target)
            show_hud("EXPLORADOR DE ARCHIVOS")
            print(f"    Directorio actual: {YELLOW}{current_path}{RESET}\n")
            
            items = os.listdir(current_path)
            if not items:
                print("       (Carpeta vacía)")
            for item in sorted(items):
                full = os.path.join(current_path, item)
                if os.path.isdir(full):
                    prefix = f"{system_state['folder_icon']} " if system_state['folder_icon'] else ""
                    print(f"       {prefix}{WHITE}{item}/{RESET}")
                else:
                    print(f"       📄 {WHITE}{item}{RESET}")
            print("")
        else:
            print(f"    {RED}❌ Directorio no válido.{RESET}")
    except PermissionError:
        print(f"    {RED}❌ Permiso denegado.{RESET}")

def cmd_help():
    print(f"""
    ========================================================================
                              GUÍA DE COMANDOS
    ========================================================================
      • abrir <carpeta>   -> Explora directorios con el estilo seleccionado.
      • rendimiento       -> Configura ZRAM, congelador, CPU, GPU y VRAM.
      • personalizar      -> Modifica temas de color, carpetas y bordes.
      • limpiar           -> Libera espacio y archivos temporales.
      • conectar          -> Vincula el celular por USB para streaming.
      • ayuda             -> Muestra esta guía.
      • salir             -> Cierra la sesión del sistema.
    ========================================================================
    """)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    login_screen()
    
    show_hud("CONSOLA PRINCIPAL")
    print(f"    {system_state['theme_color']}Sistema iniciado correctamente. Escriba 'ayuda' para comenzar.{RESET}\n")
    cmd_open([])
    
    while True:
        try:
            folder_name = os.path.basename(current_path) or "/"
            prompt_color = system_state["theme_color"]
            user_input = input(f"    {prompt_color}debian-ops:~/{folder_name} $ {RESET}").strip()
            
            if not user_input:
                continue
            
            parts = user_input.split()
            cmd = parts[0].lower()
            args = parts[1:]
            
            if cmd in ["abrir", "open", "cd", "ls"]:
                cmd_open(args)
            elif cmd in ["personalizar", "customize"]:
                show_hud("PERSONALIZACIÓN")
                run_customizer(system_state)
                show_hud("CONSOLA PRINCIPAL")
            elif cmd in ["rendimiento", "performance"]:
                show_hud("RENDIMIENTO")
                run_performance_menu()
                show_hud("CONSOLA PRINCIPAL")
            elif cmd in ["limpiar", "clean"]:
                show_hud("MANTENIMIENTO")
                clean_system()
                show_hud("CONSOLA PRINCIPAL")
            elif cmd in ["conectar", "phone"]:
                show_hud("CONEXIÓN MÓVIL")
                phone_link()
                show_hud("CONSOLA PRINCIPAL")
            elif cmd in ["ayuda", "help"]:
                cmd_help()
            elif cmd in ["salir", "exit"]:
                print(f"\n    Cerrando sesión de Debian OPS. ¡Hasta luego!\n")
                sys.exit(0)
            else:
                print(f"    {RED}❌ Comando no reconocido. Escriba 'ayuda'.{RESET}")
                
        except KeyboardInterrupt:
            print("\n    Use 'salir' para cerrar la sesión de forma segura.")
        except Exception as e:
            print(f"    {RED}⚠️ Error: {e}{RESET}")

if __name__ == "__main__":
    main()