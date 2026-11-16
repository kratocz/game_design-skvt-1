# Zabalí hratelnou verzi DÚ č. 2 pro Linux (Shipping, x86_64) křížovým překladem na notebooku autora s Windows,
# se startovní mapou L_Plizeni. Obdoba tools/package_win.ps1 (stejný stroj, klon, přepnutí GameDefaultMap a pasti
# v jeho hlavičce: odpojené spuštění přes WMI, vzdálené příkazy v souboru .ps1, kód jen v ASCII); převzato
# z tools/package_linux.ps1 soukromého repa bandit-camp (DÚ č. 3), kde se pro Linux balilo poprvé 2026-11-16.
# Z Macu pro Linux zabalit nejde.
#
# Co je potřeba (na notebooku autora od 2026-11-16 nainstalované, postup v hlavičce skriptu v bandit-camp):
# - cílová platforma Linux v instalaci UE 5.8 z launcheru;
# - toolchain přesně podle Engine\Config\Linux\Linux_SDK.json (UE 5.8: v26_clang-20.1.8-rockylinux8 od Epicu
#   v C:\UnrealToolchains\) a proměnná prostředí LINUX_MULTIARCH_ROOT; bez ní skript hned skončí chybou.
#
# Spuštění odpojeně s logem jako package_win.ps1, jen s tímto skriptem a logem plizeni-package-linux.log.
# Výstup: <cílová složka>\Plizeni (spouští se skvt_projekt.sh) a archiv Plizeni-Linux.zip, výchozí složka
# C:\Users\krato\Plizeni-Linux. Prereqs (Visual C++) se pro Linux nepřidávají. Hra pro Linux potřebuje grafiku
# s Vulkanem. Zip z tar.exe na Windows nemá spustitelný bit, proto po rozbalení na Linuxu
# chmod +x skvt_projekt.sh skvt_projekt/Binaries/Linux/skvt_projekt-Linux-Shipping.
# První balení 2026-11-16 (odevzdaný stav 5c70038): překlad 41 s (zkouška STEPS=-build předtím 2 min 17 s), cook
# 1 h 48 min (shadery Vulkan; bandit-camp bez mezipaměti 3 h 53 min, globální shadery enginu ze sdílené mezipaměti
# Zen v LOCALAPPDATA se zřejmě použily znovu), stage 63 s; zip 888 MB, rozbalená hra 2,61 GB (staging přibalí
# i .debug a .sym binárky), volné místo na C: kleslo z 13,46 na 11,15 GB. Chyby v logu jen známé GameFeatureData.
# Hru pro Linux zatím nikdo nespustil.
param([string]$Out = (Join-Path $env:USERPROFILE "Plizeni-Linux"))
$ErrorActionPreference = "Stop"

$Tc = $env:LINUX_MULTIARCH_ROOT
if (-not $Tc) { $Tc = [Environment]::GetEnvironmentVariable("LINUX_MULTIARCH_ROOT", "Machine") }
if (-not $Tc) { $Tc = [Environment]::GetEnvironmentVariable("LINUX_MULTIARCH_ROOT", "User") }
if (-not $Tc -or -not (Test-Path $Tc)) { throw "LINUX_MULTIARCH_ROOT not set or missing (install the cross toolchain from Engine\Config\Linux\Linux_SDK.json)" }
$env:LINUX_MULTIARCH_ROOT = $Tc

$Root = Split-Path -Parent $PSScriptRoot
$UE = "C:\Program Files\Epic Games\UE_5.8"
$Project = "skvt_projekt"
$Map = "/Game/Krato/Maps/L_Plizeni"
$Ini = Join-Path $Root "Config\DefaultEngine.ini"
$Backup = "$Ini.package-backup"
# @() je nutné: if vrátí jednoprvkové pole jako řetězec a splatting @Steps by ho předal po znacích
$Steps = @(if ($env:STEPS) { $env:STEPS -split ' ' } else { "-build", "-cook", "-stage", "-pak" })

if (Test-Path $Backup) { Move-Item -Force $Backup $Ini; "DefaultEngine.ini restored from previous run" }
Copy-Item $Ini $Backup
try {
  # soubor je ASCII; ReadAllText/WriteAllText zachová konce řádků a nepřidá BOM
  $Text = [IO.File]::ReadAllText($Ini)
  $New = [regex]::Replace($Text, '(?m)^GameDefaultMap=[^\r\n]*', "GameDefaultMap=$Map.L_Plizeni")
  if ($New -eq $Text) { throw "GameDefaultMap not replaced in $Ini" }
  [IO.File]::WriteAllText($Ini, $New, (New-Object Text.UTF8Encoding $false))

  "start $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
  "map: $Map  toolchain: $Tc"
  & "$UE\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun "-project=$Root\$Project.uproject" -noP4 -utf8output `
    -platform=Linux -clientconfig=Shipping @Steps "-map=$Map" -IgnoreCookErrors
  if ($LASTEXITCODE -ne 0) { throw "RunUAT failed with exit code $LASTEXITCODE" }
} finally {
  Move-Item -Force $Backup $Ini
  "DefaultEngine.ini restored"
}
if (($Steps -join ' ') -eq "-build") { "build done $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"; exit 0 }

# hra musí obsahovat uvařená data, jinak se nespustí
$Staged = Join-Path $Root "Saved\StagedBuilds\Linux"
$Pak = Get-ChildItem (Join-Path $Staged "$Project\Content\Paks") -Filter "*.pak"
if (-not $Pak) { throw "no .pak in $Staged" }
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$Game = Join-Path $Out "Plizeni"
$Zip = Join-Path $Out "Plizeni-Linux.zip"
if (Test-Path $Game) { Remove-Item -Recurse -Force $Game }
if (Test-Path $Zip) { Remove-Item -Force $Zip }
Copy-Item -Recurse $Staged $Game
& tar.exe -a -c -f $Zip -C $Out "Plizeni"
if ($LASTEXITCODE -ne 0) { throw "tar failed with exit code $LASTEXITCODE" }
"end $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Get-ChildItem $Out | Format-Table Name, Length -AutoSize | Out-String
