#!/bin/bash
# Zabalí hratelnou verzi pro macOS (Shipping) se startovní mapou L_Plizeni.
# Výchozí herní mapa projektu je mapa kurzu (Config/DefaultEngine.ini, soubor kurzu), proto ji skript
# na dobu zabalení přepne na L_Plizeni a po skončení (i po chybě nebo Ctrl+C) soubor vrátí.
# Běží desítky minut (kompilace shaderů), pouštět ve vlastním terminálu s logem, editor zavřít:
#   nohup bash tools/package_mac.sh > ~/Desktop/plizeni-package.log 2>&1 &
#   tail -f ~/Desktop/plizeni-package.log
# Výstup: <cílová složka>/Mac/*.app (výchozí ~/Desktop/Plizeni-macOS).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
UE="/Users/Shared/Epic Games/UE_5.8"
OUT="${1:-$HOME/Desktop/Plizeni-macOS}"
INI="$ROOT/Config/DefaultEngine.ini"
MAP="/Game/Krato/Maps/L_Plizeni"

cp "$INI" "$INI.package-backup"
trap 'mv "$INI.package-backup" "$INI"; echo "DefaultEngine.ini vrácen"' EXIT
sed -i '' "s#^GameDefaultMap=.*#GameDefaultMap=$MAP.L_Plizeni#" "$INI"
grep -q "^GameDefaultMap=$MAP.L_Plizeni$" "$INI"

date '+start %Y-%m-%d %H:%M:%S'
"$UE/Engine/Build/BatchFiles/RunUAT.sh" BuildCookRun \
  -project="$ROOT/skvt_projekt.uproject" -noP4 -utf8output \
  -platform=Mac -clientconfig=Shipping \
  -build -cook -map="$MAP" -stage -pak -archive -archivedirectory="$OUT"
date '+konec %Y-%m-%d %H:%M:%S'
ls -la "$OUT"/Mac*/ 2>/dev/null || ls -la "$OUT"
