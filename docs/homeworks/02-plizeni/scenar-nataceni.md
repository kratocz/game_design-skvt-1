# Scénář natáčení – DÚ č. 2

- **Úkol:** DÚ č. 2 – plížení (video), krok T6, kroky 3 a 4 z `postup-editor.md`
- **Level:** `L_Plizeni`
- **Výstup:** samostatné soubory v `docs/homeworks/02-plizeni/odevzdani/video/` (mimo git)

## Nastavení před natáčením

1. V hlavním okně editoru vedle Play klikni na ⋮ a vyber **New Editor Window (PIE)**. Velikost a polohu okna už nastavovat nemusíš (1920 × 1080 na středu 4K televize).
2. Do pole **Cmd** vlevo dole napiš `DisableAllScreenMessages` a dej Enter.
3. Spusť Play. Okno hry se otevře na televizi; klikni do něj, ať chytí myš.
4. Cmd+Shift+5 → **Record Selected Portion** a výběr natáhni přesně na herní plochu, bez titulku okna. macOS si výběr pamatuje, stačí ho nastavit jednou.
5. V Options nastav **Save to** na `/Users/krato/IdeaProjects/github.com/kratocz/game_design-skvt-1/docs/homeworks/02-plizeni/odevzdani/video/`, **Microphone** na None a vypni **Show Mouse Clicks**.

## Ovládání a pravidla

- WASD, myš, mezerník (skok), **C** (dřep), kolečko (zoom).
- Ctrl nepoužívej, Ctrl+mezerník přepíná klávesnici.
- Myš uvolníš Shift+F1.
- Každý záběr nahraj jako samostatný soubor; pořadí se pozná podle času vzniku.
- Mechaniku drž aspoň 7 s a nech kameru ve výchozí vzdálenosti, pokud záběr neříká jinak.

## Záběry v pořadí natáčení

- [x] **1. Dřep a vstání (titulek 2), asi 10 s.** Stůj na startu ve skladu, kamera za zády. C, 3 s počkat, C, 2 s počkat, a celé ještě jednou.
- [x] **2. Detail kamery (titulek 3), asi 10 s.** Na stejném místě otoč myší kameru o 90° na bok postavy. C, 3 s, C, 3 s. Má být vidět, jak kamera přijede blíž a níž a pak zpět.
- [x] **3. Pod stropem nejde vstát (titulek 4), asi 12 s.** Dřepni a jdi ke dveřím na konci skladu pod propadlý strop (pás 3 m před dveřmi). Uprostřed pod ním 2–3× zmáčkni C a nic se nestane. Projdi dveřmi do křižovatky a tam C, postava vstane.
- [x] **4. Chodba versus ventilace (titulek 8), asi 8 s.** V křižovatce dojdi na sever k tyrkysově nasvícenému otvoru ve východní stěně a zastav se. Pomalu otoč kameru z otvoru ventilace doprava na roh, kde se otevírá hlavní chodba.
- [x] **5. Poskok do ventilace (titulek 5), asi 10 s.** Stůj čelem k tyrkysovému otvoru. Ve stoje zkus dojít a skočit dovnitř; nejde to. Pak C a mezerník: poskok na práh a dovnitř.
- [x] **6. Chůze v dřepu (titulek 6), asi 15 s.** Jdi ventilací v dřepu na východ podél mřížek, kterými je vidět chodba, až k výstupu na konci (asi 22 m) a seskoč do chodby. Tam vstaň, kus jdi ve stoje, pak znovu C a pokračuj v dřepu mezi bednami; rozdíl rychlosti má být vidět.
- [x] **7. Úvodní pohled (titulek 1), asi 8 s.** Od dveří strojovny na východním konci se otoč na západ a pomalu projeď kamerou celou chodbu s bednami. Mimozemšťan v ní zatím není; záběr se v T8 přetočí podle postupu.

## Titulky, ke kterým záběry patří

Znění je z `README.md`, sekce Video; titulky do videa přidá agent při sestavení. Před první záběr přijde úvodní karta (název, kurz, autor, krato.cz), ta záběr nepotřebuje.

1. Plížení: útěk z vesmírné lodi. Chodbu hlídá mimozemšťan, druhá cesta vede ventilací.
2. Dřep se zapíná a vypíná. Ventilací se leze dlouho a držet klávesu by unavovalo.
3. Kamera se v dřepu plynule přiblíží a sníží. Ve ventilaci by do stropu narazila sama; takhle hráč pozná, že se plíží.
4. Pod nízkým stropem vstát nejde. Hra pokyn zahodí, takže z ventilace nevylezeš nečekaně ve stoje.
5. Skok v dřepu je nízký poskok: vejde se pod strop a dostane tě do ventilace. Plný skok až po vstání.
6. V dřepu je postava pomalejší. Plížení je opatrnost, ne útěk.
7. Ve stoje tě mimozemšťan zahlédne zdálky, v dřepu až zblízka. (Záběry 8 a 9 z druhého natáčení.)
8. Chodba je rychlá a riskantní, ventilace pomalá a bezpečná.
9. Cílem je teleport ve strojovně. Nabíjí se 4 s, takže s mimozemšťanem v zádech to nestihneš. (Záběry 11 a 12 z druhého natáčení.)
10. Co zatím chybí (zvuky, mimozemšťan hráče po ztrátě z dohledu nehledá).
11. Přiznání použití AI.

## Po natáčení

Záběry jsou natočené 2026-10-26 23:20–23:41 a použité v záložním videu (`tools/build_video.py`, data `odevzdani/video-zalozni.json`). Mají ale starý bílý vzhled, takže se v T8 natáčejí všechny znovu (sekce Druhé natáčení); nové záběry stačí nechat v `odevzdani/video/` a napsat agentovi. Neukládej v editoru nic mimo `Content/Krato/` (hláška „2 Unsaved“ se týká assetů kurzu).

## Druhé natáčení (T8)

Vizuální vylepšení změnila vzhled (panely na stěnách, lampy, ocelové bedny), záběry z prvního natáčení proto nejdou do finálního videa. Nastavení, ovládání a pravidla jsou stejné jako výše.

- [ ] **1.–6.** Záběry 1 až 6 z prvního natáčení znovu, stejně jako tehdy.
- [ ] **7. Úvodní pohled (titulek 1), asi 8 s.** Jako dřív, teď už s hlídajícím mimozemšťanem v chodbě.
- [ ] **8. Zahlédnutí a chycení (titulek 7), asi 12 s.** Ve stoje vyjdi z křižovatky do chodby proti mimozemšťanovi. Světlo nad jeho hlavou zčervená, rozběhne se k postavě, obrazovka ztmavne a postava je zpět na křižovatce.
- [ ] **9. Proplížení za bednami (titulek 7), asi 15 s.** V dřepu jdi chodbou za bednami, zatímco mimozemšťan jde opačným směrem; světlo nad ním zůstane zelené.
- [ ] **10. Pohled mřížkou (titulek 8), asi 8 s.** Ve ventilaci se zastav u mřížky a otoč kameru do chodby, ať je vidět procházející mimozemšťan.
- [ ] **11. Únik teleportem (titulek 9), asi 12 s.** Nezahlédnutý dojdi do strojovny a postav se doprostřed svítící plošiny. Stůj 4 s, světlo nad plošinou sílí, obrazovka zbělá a level začne znovu ve skladu. Záběr ukonči na bílé obrazovce.
- [ ] **12. Chycení na teleportu (titulek 9), asi 10 s.** Ve stoje se nech v chodbě zahlédnout, utíkej do strojovny na plošinu a čekej. Mimozemšťan doběhne dřív, než se teleport nabije, a obrazovka ztmavne.
