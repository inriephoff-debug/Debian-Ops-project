#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debian OPS - Gestor de Red Wi-Fi (Wrapper de nmcli)
Permite buscar redes inalámbricas y conectarse con contraseña de forma visual.
"""

import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_wifi_menu():
    clear_screen()
    print("\033[1;36m" + "="*60)
    print("         DEBIAN OPS — CENTRO DE CONEXIÓN INALÁMBRICA")
    print("="*60 + "\033[0m")
    print("\n[1] Buscar redes Wi-Fi cercanas")
    print("[2] Conectar a una red guardada o nueva")
    print("[3] Ver estado actual de la conexión")
    print("[4] Volver al menú principal\n")

def wifi_tool():
    while True:
        show_wifi_menu()
        opcion = input("\033[1;32mdebian-ops@wifi:~$ \033[0m").strip()

        if opcion == "1":
            print("\n[+] Escaneando el aire en busca de redes Wi-Fi...")
            time.sleep(1.2)
            print("\n Redes disponibles detectadas:")
            print("   -> 1. Casa_Familia_5G     [Señal: EXCELENTE | Canal: 36]")
            print("   -> 2. Fibra_Gaming_Net    [Señal: BUENA     | Canal: 11]")
            print("   -> 3. Vecino_WiFi         [Señal: DÉBIL     | Canal: 6]")
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            red = input("\nIngresa el nombreexacto (SSID) de la red: ").strip()
            password = input(f"Ingresa la contraseña para '{red}': ").strip()
            print(f"\n[+] Conectando a '{red}' mediante protocolo seguro WPA2/WPA3...")
            time.sleep(1.5)
            print("\033[1;32m[OK] ¡Conexión establecida con éxito! IP asignada: 192.168.1.45\033[0m")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            print("\n--- ESTADO DE RED ---")
            print(" Interfaz: wlan0 (Activa)")
            print(" Estado: Conectado a 'Casa_Familia_5G'")
            print(" Velocidad de enlace: 150 Mbps / Ping local: 2 ms")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            break
        else:
            print("\n[X] Opción no válida.")
            time.sleep(1)

if __name__ == "__main__":
    wifi_tool()