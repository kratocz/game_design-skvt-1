# Nahrávání hlasu – DÚ č. 2

- **Úkol:** DÚ č. 2 – plížení (video), hlasový komentář k finálnímu videu (nápad z `odlozene-napady.md`, sekce Zvuk)
- **Nástroj:** Audacity
- **Výstup:** `odevzdani/video/hlas/titulek-NN.mp3` (mimo git; `tools/build_video.py` čte hlas přes ffmpeg, takže přijme i WAV)
- **Zapsáno:** 2026-10-28

Hlas čte přesně text titulků, titulky ve videu zůstávají. Agent pak hlas vyčistí (odstranění šumu `afftdn`, hlasitost `loudnorm`, oříznutí ticha), podloží pod záběry a podle délky každého titulku upraví střih v `tools/build_video.py`.

## Nastavení (jednou)

1. Nahoře v liště **Audio Setup** → **Recording Device**: mikrofon (MacBook nebo kabelový/USB, ne AirPods: přes Bluetooth nahrávají v telefonní kvalitě). **Recording Channels**: 1 (Mono).
2. Vlevo dole **Project Rate**: 48000 Hz.
3. Zkušební nahrávka: při běžném hlasu má špička na ukazateli úrovně sahat zhruba na −12 dB, nikdy ne do červené. Když je potichu, přiblížit se k mikrofonu; zesílení přidá agent.

## Nahrávání: jeden titulek = jeden soubor

1. **R** spustí nahrávání: vteřinu počkat, přečíst titulek, vteřinu počkat, **mezerník** zastaví.
2. Přeřeknutí: Cmd+A, Delete a znovu R.
3. Hotový titulek: **Cmd+Shift+E** → formát **MP3**, složka `docs/homeworks/02-plizeni/odevzdani/video/hlas/`, název `titulek-01.mp3` atd.
4. Cmd+A, Delete a další titulek.

## Texty k přečtení

Číslo je název souboru. Úvodní karta (`titulek-00`) je nepovinná.

```
00  Plížení. Ukázka herní mechaniky v Unreal Engine 5. Domácí úkol č. 2 v kurzu Game design pro začátečníky, SKVOT, podzim 2026. Petr Kratochvíl.
01  Plížení: útěk z vesmírné lodi. Chodbu hlídá mimozemšťan, druhá cesta vede ventilací.
02  Dřep se zapíná a vypíná. Ventilací se leze dlouho a držet klávesu by unavovalo.
03  Kamera se v dřepu plynule přiblíží a sníží. Ve ventilaci by do stropu narazila sama; takhle hráč pozná, že se plíží.
04  Pod nízkým stropem vstát nejde. Hra pokyn zahodí, takže z ventilace nevylezeš nečekaně ve stoje.
05  Skok v dřepu je nízký poskok: vejde se pod strop a dostane tě do ventilace. Plný skok až po vstání.
06  V dřepu je postava pomalejší. Plížení je opatrnost, ne útěk.
07  Ve stoje tě mimozemšťan zahlédne zdálky, v dřepu až zblízka.
08  Chodba je rychlá a riskantní, ventilace pomalá a bezpečná.
09  Cílem je teleport ve strojovně. Nabíjí se 4 s, takže s mimozemšťanem v zádech to nestihneš.
10  Co zatím chybí: mimozemšťan hráče, kterého ztratí z dohledu, nehledá, jen se vrátí k hlídce.
11  Použití AI: o návrhu mechaniky jsem rozhodoval v dialogu s AI (Claude). Blueprinty podle něj sestavila AI, stejně jako zvuky, titulky a střih. Hru jsem testoval a ladil sám: výšku kapsle v dřepu, rozměry levelu podle chůze v dřepu a ruční opravy blueprintů. Postavil jsem mříže a teleport, natočil a namluvil všechny záběry.
```

## Přednes a prostředí

- Číst pomaleji, než se zdá přirozené; u dvojtečky a středníku krátká pauza.
- „4 s“ v titulku 9 číst jako „čtyři sekundy“.
- Menší místnost s látkami (záclony, postel, skříň s oblečením) zní líp než prázdná s tvrdými stěnami.
- Od mikrofonu asi 20–30 cm, pořád stejně.

## Po nahrání

Nechat soubory ve složce `odevzdani/video/hlas/` a napsat agentovi.
