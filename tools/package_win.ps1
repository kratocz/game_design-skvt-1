# Zabalí hratelnou verzi DÚ č. 2 pro Windows (Shipping, Win64) se startovní mapou L_Plizeni. Obdoba
# tools/package_mac.sh; převzato z tools/package_win.ps1 soukromého repa bandit-camp (DÚ č. 3), kde je postup ověřený
# poprvé 2026-11-14. Z Macu pro Windows zabalit nejde: instalace UE na Macu nemá Engine/Binaries/Win64 a shadery
# DirectX se překládají jen na Windows.
#
# Výchozí herní mapa projektu je mapa kurzu (Config/DefaultEngine.ini, soubor kurzu), proto ji skript na dobu balení
# přepne na L_Plizeni a v bloku finally soubor vrátí ze zálohy. Proces zabitý zvenčí finally nespustí; záloha
# DefaultEngine.ini.package-backup pak zůstane a další běh z ní soubor nejdřív obnoví.
#
# Požadavky na Windows: UE 5.8 z launcheru, Build Tools pro Visual Studio 2022 s MSVC 14.44, Windows SDK a .NET
# Framework 4.8 SDK (podrobnosti a pasti v hlavičce skriptu v bandit-camp). Hra je z blueprintů, ale zapnutý plugin
# GameplayStateTree vynutí překlad vlastního cíle hry, proto překladač C++. Repo je veřejné, klonuje se přes HTTPS.
#
# Spuštění (dlouhý běh, cook překládá shadery DirectX):
#   powershell -NoProfile -ExecutionPolicy Bypass -File tools\package_win.ps1 [cilova-slozka]
# Přes SSH ho spouštět odpojeně (proces vytvořený přes WMI přežije konec SSH relace), s logem do souboru; log
# nesdílet, při chybě do něj nástroje můžou vypsat proměnné prostředí:
#   Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine='cmd /c powershell
#     -NoProfile -ExecutionPolicy Bypass -File C:\Users\krato\skvt_projekt\tools\package_win.ps1
#     > C:\Users\krato\plizeni-package.log 2>&1'}
# STEPS="-build" přeloží jen cíl hry (asi minuta), hodí se jako zkouška před dlouhým cookem.
# Výstup: <cílová složka>\Plizeni (rozbalená hra, spouští se skvt_projekt.exe) a archiv Plizeni-Windows.zip; výchozí
# složka je C:\Users\krato\Plizeni-Windows, mimo Plochu, protože ta je na notebooku autora ve OneDrive.
# První balení 2026-11-15 (odevzdaný stav 5c70038, na notebooku autora s Windows 10): překlad 3 minuty, cook se stagem
# 13 minut (shadery byly v mezipaměti z balení bandit-camp), zip 632 MB, rozbalená hra 1,04 GB, volné místo na C:
# kleslo ze 17 na 11,7 GB (klon repa asi 2 GB). Chyby v logu jen známé GameFeatureData (viz package_mac.sh).
# Hlídání konce: Select-String je bez -CaseSensitive necitlivé na velikost písmen, takže vzor '^end ' najde už
# řádek UAT „End update resource“ uprostřed balení; testovat s -CaseSensitive.
# Hra je nepodepsaná: SmartScreen ji pustí přes „Další informace“ a „Přesto spustit“. -prereqs přibalí instalátor
# knihoven Visual C++, který hra při prvním spuštění sama nabídne, když knihovny chybějí.
#
# Vzdálené příkazy na Windows (kontrola průběhu, hlídání konce) psát do souboru .ps1, přenést scp a spouštět
# `ssh … 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\krato\x.ps1'`, ne jako -Command přímo v ssh:
# výchozí shell SSH na Windows je cmd a svislá čára nebo vnořené uvozovky příkaz rozbijí (2026-11-15 tak Select-String
# s uvozovkami ve vzoru skončil hláškou tar.exe). Chyby vzdáleného příkazu nepotlačovat, z výstupu ssh filtrovat jen
# varování o post-quantum výměně klíčů.
#
# PowerShell 5.1 čte .ps1 bez BOM v kódování systému (cp1250), diakritika proto smí jen do komentářů, kód je v ASCII.
param([string]$Out = (Join-Path $env:USERPROFILE "Plizeni-Windows"))
$ErrorActionPreference = "Stop"

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
  # soubor je ASCII; ReadAllText/WriteAllText zachová konce řádků a nepřidá BOM (Set-Content v PS 5.1 by kódování změnil)
  $Text = [IO.File]::ReadAllText($Ini)
  $New = [regex]::Replace($Text, '(?m)^GameDefaultMap=[^\r\n]*', "GameDefaultMap=$Map.L_Plizeni")
  if ($New -eq $Text) { throw "GameDefaultMap not replaced in $Ini" }
  [IO.File]::WriteAllText($Ini, $New, (New-Object Text.UTF8Encoding $false))

  "start $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
  "map: $Map"
  & "$UE\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun "-project=$Root\$Project.uproject" -noP4 -utf8output `
    -platform=Win64 -clientconfig=Shipping @Steps "-map=$Map" -IgnoreCookErrors -prereqs
  if ($LASTEXITCODE -ne 0) { throw "RunUAT failed with exit code $LASTEXITCODE" }
} finally {
  Move-Item -Force $Backup $Ini
  "DefaultEngine.ini restored"
}
if (($Steps -join ' ') -eq "-build") { "build done $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"; exit 0 }

# hra musí obsahovat uvařená data, jinak se nespustí
$Staged = Join-Path $Root "Saved\StagedBuilds\Windows"
$Pak = Get-ChildItem (Join-Path $Staged "$Project\Content\Paks") -Filter "*.pak"
if (-not $Pak) { throw "no .pak in $Staged" }
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$Game = Join-Path $Out "Plizeni"
$Zip = Join-Path $Out "Plizeni-Windows.zip"
if (Test-Path $Game) { Remove-Item -Recurse -Force $Game }
if (Test-Path $Zip) { Remove-Item -Force $Zip }
Copy-Item -Recurse $Staged $Game
# tar.exe z Windows 10 umí zip (-a podle přípony) a na rozdíl od Compress-Archive zvládne i velké soubory
& tar.exe -a -c -f $Zip -C $Out "Plizeni"
if ($LASTEXITCODE -ne 0) { throw "tar failed with exit code $LASTEXITCODE" }
"end $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Get-ChildItem $Out | Format-Table Name, Length -AutoSize | Out-String
