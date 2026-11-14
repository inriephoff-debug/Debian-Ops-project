#!/usr/bin/env bash
# ==============================================================================
# DEBIAN OPS - SCRIPT MAESTRO DE COMPILACIÓN DEFINITIVO (build_iso.sh)
# Versión 1.0 - Completa (Gaming, Streaming, Chromium y Personalización Total)
# ==============================================================================

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ISO_NAME="Debian-OPS-v1.0-Complete-x86_64.iso"

echo "=================================================================="
echo "      INICIANDO COMPILACIÓN DE LA ISO COMPLETA DE DEBIAN OPS"
echo "=================================================================="

# 1. Verificar entorno Linux / WSL
if [ "$EUID" -ne 0 ]; then
  echo "[ERROR] Este script maestro debe ejecutarse como root (usa sudo)."
  exit 1
fi

echo "[+] Verificando dependencias esenciales del sistema..."
apt-get update -y && apt-get install -y debootstrap xorriso squashfs-tools isolinux syslinux-common > /dev/null 2>&1
echo "[OK] Dependencias listas."

# 2. Preparar entorno chroot / debootstrap base Debian Bookworm Minimal
BUILD_ROOT="/tmp/debian_ops_complete_build"
rm -rf "$BUILD_ROOT"
mkdir -p "$BUILD_ROOT"

echo "[+] Descargando Debian Bookworm Base y paquetes esenciales..."
debootstrap --include=locales,sudo,python3,xorg,openbox,NetworkManager,pulseaudio,alsa-utils,curl,wget,chromium,p7zip-full,unzip,tar \
  bookworm "$BUILD_ROOT" http://deb.debian.org/debian/ > /dev/null 2>&1

echo "[OK] Sistema base y navegador Chromium instalados."

# 3. Inyectar todos los módulos del proyecto Debian OPS
echo "[+] Inyectando módulos de desarrollo, HUD, temas y herramientas..."
mkdir -p "$BUILD_ROOT/opt/debian_ops"
cp -r "$PROJECT_DIR"/* "$BUILD_ROOT/opt/debian_ops/"

# 4. Configurar el entorno del usuario predeterminado ('ops') con privilegios sudo
echo "[+] Configurando usuario optimizado y permisos de superusuario..."
chroot "$BUILD_ROOT" useradd -m -s /bin/bash ops || true
echo "ops:debianops" | chroot "$BUILD_ROOT" chpasswd
chroot "$BUILD_ROOT" usermod -aG sudo,audio,video,netdev ops
echo "ops ALL=(ALL) NOPASSWD:ALL" >> "$BUILD_ROOT/etc/sudoers"

# 5. Configurar servicio de inicio automático para la Consola OPS con HUD en tty1
echo "[+] Configurando arranque directo en la consola OPS (TUI)..."
cat << 'EOF' > "$BUILD_ROOT/etc/systemd/system/debian-ops.service"
[Unit]
Description=Debian OPS Core Shell & HUD
After=getty@tty1.service network.target
[Service]
ExecStart=/usr/bin/python3 /opt/debian_ops/01_nucleo/debian_ops_shell.py
StandardInput=tty
StandardOutput=tty
TTYPath=/dev/tty1
Restart=always
User=ops
Environment=HOME=/home/ops
[Install]
WantedBy=multi-user.target
EOF

chroot "$BUILD_ROOT" systemctl enable debian-ops.service > /dev/null 2>&1

# 6. Generar la imagen ISO booteable final con xorriso
echo "[+] Generando la imagen ISO booteable definitiva..."
xorriso -as mkisofs \
  -iso-level 3 \
  -full-iso9660-filenames \
  -volid "DEBIAN_OPS_COMPLETE" \
  -eltorito-boot isolinux/isolinux.bin \
  -eltorito-catalog isolinux/boot.cat \
  -no-emul-boot -boot-load-size 4 -boot-info-table \
  -output "$PROJECT_DIR/$ISO_NAME" \
  "$BUILD_ROOT" > /dev/null 2>&1

echo "=================================================================="
echo "      ¡COMPILACIÓN EXITOSA! TU ISO COMPLETA ESTÁ LISTA:"
echo "      -> $PROJECT_DIR/$ISO_NAME"
echo "=================================================================="