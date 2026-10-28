#!/bin/bash
# Zabalí hratelnou verzi pro macOS (Shipping, Apple Silicon) se startovní mapou L_Plizeni.
# Výchozí herní mapa projektu je mapa kurzu (Config/DefaultEngine.ini, soubor kurzu), proto ji skript
# na dobu zabalení přepne na L_Plizeni a po skončení (i po chybě nebo Ctrl+C) soubor vrátí.
# Pouštět ve vlastním terminálu s logem (poprvé desítky minut, pak pár minut):
#   nohup bash tools/package_mac.sh > ~/Desktop/plizeni-package.log 2>&1 &
#   tail -f ~/Desktop/plizeni-package.log
# Výstup: <cílová složka>/Plizeni.app a Plizeni-macOS.zip (výchozí ~/Desktop/Plizeni-macOS).
#
# Pasti UE 5.8 na tomhle projektu (2026-10-29):
# - UBT po překladu volá xcodebuild „PostBuildSync“ a ten při volání z UAT padá („Failed to finalize the .app
#   with Xcode“, ruční xcodebuild se stejnými parametry projde). UE_BUILD_FROM_XCODE=1 ten krok přeskočí
#   (AppleToolChain.cs, PostBuildSync); aplikaci s daty pak sestaví xcodebuild ve fázi Stage.
# - Archiv (-archive) by zkopíroval aplikaci z Binaries/Mac bez dat, proto se bere Saved/StagedBuilds/Mac.
# - Cook hlásí jen chybějící pravidlo Asset Manageru pro GameFeatureData (pluginy nepoužíváme), proto
#   -IgnoreCookErrors; souhrn chyb zůstává v logu.
# - Při chybě Xcode vypíše do logu všechny proměnné prostředí včetně tokenů a API klíčů: log nesdílet.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
UE="/Users/Shared/Epic Games/UE_5.8"
OUT="${1:-$HOME/Desktop/Plizeni-macOS}"
INI="$ROOT/Config/DefaultEngine.ini"
MAP="/Game/Krato/Maps/L_Plizeni"
STAGED="$ROOT/Saved/StagedBuilds/Mac/skvt_projekt-Mac-Shipping.app"
export UE_BUILD_FROM_XCODE=1

cp "$INI" "$INI.package-backup"
trap 'mv "$INI.package-backup" "$INI"; echo "DefaultEngine.ini vrácen"' EXIT
sed -i '' "s#^GameDefaultMap=.*#GameDefaultMap=$MAP.L_Plizeni#" "$INI"
grep -q "^GameDefaultMap=$MAP.L_Plizeni$" "$INI"

date '+start %Y-%m-%d %H:%M:%S'
"$UE/Engine/Build/BatchFiles/RunUAT.sh" BuildCookRun \
  -project="$ROOT/skvt_projekt.uproject" -noP4 -utf8output \
  -platform=Mac -clientconfig=Shipping \
  -build -cook -map="$MAP" -stage -pak -IgnoreCookErrors

# aplikace musí obsahovat uvařená data, jinak se nespustí
ls "$STAGED/Contents/UE/skvt_projekt/Content/Paks/"*.pak > /dev/null
mkdir -p "$OUT"
rm -rf "${OUT:?}/Plizeni.app" "${OUT:?}/Plizeni-macOS.zip"
ditto "$STAGED" "$OUT/Plizeni.app"
codesign -v "$OUT/Plizeni.app"
(cd "$OUT" && ditto -c -k --keepParent Plizeni.app Plizeni-macOS.zip)
date '+konec %Y-%m-%d %H:%M:%S'
ls -la "$OUT"
