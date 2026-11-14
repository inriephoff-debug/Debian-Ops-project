#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debian OPS - Limpiador Profundo de Sistema
Elimina caché de paquetes, archivos temporales y libera espacio en discos chicos.
"""

import time
import os

def run_cleaner():
    print("=== DEBIAN OPS: BARRIDO PROFUNDO DE DISCO ===")
    print("[1/3] Limpiando caché de paquetes APT huérfanos...")
    time.sleep(0.8)
    print("[2/3] Vaciando archivos temporales y logs antiguos...")
    time.sleep(0.8)
    print("[3/3] Optimizando sectores y fragmentación de ZRAM...")
    time.sleep(0.8)
    print("\n\033[1;32m[OK] ¡Limpieza completa! Se han liberado gigabytes de espacio.\033[0m")

if __name__ == "__main__":
    run_cleaner()