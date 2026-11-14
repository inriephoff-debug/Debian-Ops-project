#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debian OPS - Theme Manager (Gestor de Estética y Paletas)
Permite cambiar dinámicamente los colores TrueColor de la TUI y Openbox.
"""

import os
import json

THEMES_FILE = os.path.expanduser("~/.config/debian_ops/theme.json")

# Definición de Paletas Neón y Retro
PALETTES = {
    "cyber-neon": {
        "name": "Cyber Neon (Por defecto)",
        "bg": "#050505",
        "fg": "#00FF66",
        "accent": "#00E5FF",
        "alert": "#FF0055",
        "border": "pixelated"
    },
    "terraria-pixel": {
        "name": "Pixel Art Naturaleza",
        "bg": "#1A1412",
        "fg": "#4CAF50",
        "accent": "#FFD54F",
        "alert": "#E53935",
        "border": "thin"
    },
    "nord-frost": {
        "name": "Nord Frost Minimalista",
        "bg": "#2E3440",
        "fg": "#ECEFF4",
        "accent": "#88C0D0",
        "alert": "#BF616A",
        "border": "rounded"
    },
    "amber-crt": {
        "name": "Retro Fósforo Ámbar",
        "bg": "#0A0800",
        "fg": "#FFB000",
        "accent": "#FF8C00",
        "alert": "#FF3300",
        "border": "thick"
    }
}

def load_current_theme():
    if os.path.exists(THEMES_FILE):
        try:
            with open(THEMES_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return PALETTES["cyber-neon"]

def save_theme(theme_key):
    if theme_key in PALETTES:
        os.makedirs(os.path.dirname(THEMES_FILE), exist_ok=True)
        with open(THEMES_FILE, "w") as f:
            json.dump(PALETTES[theme_key], f, indent=4)
        print(f"[OK] Tema cambiado exitosamente a: {PALETTES[theme_key]['name']}")
    else:
        print("[ERROR] Tema no encontrado.")

def print_banner():
    current = load_current_theme()
    print("\033[1;36m" + "="*50)
    print(f"   DEBIAN OPS - MEGACENTRO DE PERSONALIZACIÓN VISUAL")
    print(f"   Tema Activo: {current['name']}")
    print("="*50 + "\033[0m")
    print("Paletas disponibles para elegir:")
    for key, data in PALETTES.items():
        print(f" -> {key} : {data['name']}")

if __name__ == "__main__":
    print_banner()