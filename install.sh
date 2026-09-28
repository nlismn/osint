#!/data/data/com.termux/files/usr/bin/bash

set -e

OSINT_DIR="$HOME/.osint"
BIN_DIR="$HOME/bin"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo
echo "======================================"
echo "        OSINT INSTALLER"
echo "======================================"
echo

echo "[1/5] Termux paketleri kontrol ediliyor..."

if ! command -v pkg >/dev/null 2>&1; then
    echo "HATA: Bu kurulum Termux için hazırlanmıştır."
    exit 1
fi

if ! command -v python >/dev/null 2>&1; then
    echo "Python bulunamadı. Kuruluyor..."
    pkg update -y
    pkg install python -y
else
    echo "✓ Python mevcut"
fi

echo
echo "[2/5] Python bağımlılıkları kontrol ediliyor..."

python -m pip install --upgrade requests

echo
echo "[3/5] OSINT dosyaları kuruluyor..."

mkdir -p "$OSINT_DIR"
mkdir -p "$BIN_DIR"

cp "$SCRIPT_DIR/osint.py" "$OSINT_DIR/osint.py"
cp "$SCRIPT_DIR/osint_help.py" "$OSINT_DIR/osint_help.py"

echo "✓ Dosyalar $OSINT_DIR içine kuruldu"

echo
echo "[4/5] osint komutu kuruluyor..."

cat > "$BIN_DIR/osint" <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash

OSINT_DIR="$HOME/.osint"

if [ "$1" = "help" ]; then
    python "$OSINT_DIR/osint_help.py"
else
    python "$OSINT_DIR/osint.py" "$@"
fi
EOF

chmod +x "$BIN_DIR/osint"

echo "✓ osint komutu oluşturuldu"

echo
echo "[5/5] PATH kontrol ediliyor..."

if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    SHELL_RC="$HOME/.bashrc"

    if [ -n "$ZSH_VERSION" ]; then
        SHELL_RC="$HOME/.zshrc"
    fi

    if ! grep -Fq 'export PATH="$HOME/bin:$PATH"' "$SHELL_RC" 2>/dev/null; then
        echo 'export PATH="$HOME/bin:$PATH"' >> "$SHELL_RC"
    fi

    export PATH="$BIN_DIR:$PATH"

    echo "✓ ~/bin PATH'e eklendi"
else
    echo "✓ ~/bin zaten PATH içinde"
fi

echo
echo "======================================"
echo "       KURULUM TAMAMLANDI"
echo "======================================"
echo
echo "Kullanım:"
echo
echo "  osint"
echo "  osint help"
echo
echo "Kurulum konumu:"
echo "  $OSINT_DIR"
echo
