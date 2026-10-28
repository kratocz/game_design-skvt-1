# Domácí úkol č. 2 – plížení

- **Zadání:** text na stránce úkolu v Labaverse (kopii poslal uživatel 2026-10-24); doslovné znění sem nedáváme, repo je veřejné
- **Deadline:** neděle 2026-11-01 do půlnoci (prodloužení oznámené na lekci 2026-10-27, potvrzené na Discordu kurzu a podle koordinace upravené i v Labaverse; při odevzdání zkontrolovat na stránce úkolu), původně čtvrtek 2026-10-29 do 23:59
- **Interní cíl:** odevzdat nejpozději ve středu 2026-10-28 ve 23:59; autor ho potvrdil i po prodloužení termínu na neděli (2026-10-27), rezerva jsou tak čtyři dny (posunuto 2026-10-27 z úterý: natáčení až po večerní lekci, středa zůstává na doladění a pozdní nápady, čtvrtek je rezerva). Podmínky posunu: v úterý večer vznikne kompletní odevzdatelný balík (záběry, finální video, PDF) a ve středu se jen dolaďuje; nové nápady do 1 h práce, větší do `odlozene-napady.md`; cíl „víceméně hotovo týden předem“ (čtvrtek 2026-10-22) propadl, práce začala v sobotu 2026-10-24
- **Hodnocení:** nejvýš 20 bodů
- **Stav:** design schválen 2026-10-24, postup pro editor (`postup-editor.md`) hotový 2026-10-25, T0 a T1 (postava s dřepem na přepínač, testovací level) hotové 2026-10-25, T2 (póza dřepu; rozměry levelu podle chůze v dřepu, viz Zjištění T2 v `postup-editor.md`) hotové 2026-10-26, T3 (nízký poskok v dřepu) hotové 2026-10-26, T4 (kamera při dřepu) a T5 (blockout levelu) hotové 2026-10-26, T6 (komentáře a screenshoty blueprintů, záložní video s titulky) hotové 2026-10-26 ve 23:52; T7 (mimozemšťan jako blueprint, hlídka, detekce a chycení ověřené v Play přes MCP, ocelové mříže ve ventilaci) hotové 2026-10-27 02:44 po třech kolech testu autora; vizuální vylepšení (světlo zahlédnutí, lampy, panely na stěnách, ocelové bedny) hotová 2026-10-27 a schválená autorem v Play; teleport s nabíjením uprostřed strojovny (cíl levelu) postavený 2026-10-27 ve 13:50–14:10, ověřený v Play přes MCP; stroje ve strojovně, které teleport napájejí, postavené 17:41; ruční test autora teleportu i strojů prošel 17:56; T8: všech 12 záběrů natočených 2026-10-27 23:23–23:52, finální video (`odevzdani/video-final.json`, 4:38, střih schválený autorem včetně proplížení mezi bednami) sestavené 2026-10-28 po půlnoci; hlas ke všem titulkům 2026-10-28; grafy mimozemšťana, teleportu a úniku přerovnané (polohy uzlů, reroute, komentáře s českými nadpisy, logika beze změny) a nafocené do `odevzdani/blueprinty/14–35` 2026-10-28, šest z nich je ve videu, které má 5:47; grafy dřepu, kamery a animace přerovnané stejným postupem a přefocené pod stejnými jmény (01–12) plus celé grafy jen do PDF (36–40) 2026-10-28; PDF s blueprinty (`odevzdani/Kratochvil-DU2-blueprinty.html`, 32 stran A4 na šířku, weasyprint) sestavené; 2026-10-28 odpoledne: Discord zkontrolovaný (termín ne 1. 11. do půlnoci), záběr s mimozemšťanem ve videu prodloužený na 0:07–0:27 (video 5:56), animace skoku i při skoku v dřepu (snímek 10 přefocený), zvuky ve hře včetně kroků a čistý reset po chycení (viz Video, Zvuky ve hře), všechno vyzkoušené autorem v Play, `tools/build_video.py` umí zvuk hry ze záznamů; ventilace podle autora upravená (výstup 150 cm, dvě šachty vzhůru s odbočkou, kde jde vstát, vyndané mříže u vstupu opřená a před výstupem ležící; commit `3ce5f7b`, autor vyzkoušel); zbývá přetočit všechny záběry se zvukem ze systému, přemluvit titulky 10 a 11, doplnit do PDF odkaz na video a bod „co nefunguje“ podle autora a odevzdat
- **Branch:** `student-krato-homeworks`

## Co zadání chce

Postava se má naučit plížit: v dřepu projde prostory se sníženým stropem, umí skákat a kamera se při dřepnutí plynule přiblíží nebo oddálí, při vstávání obráceně. Odevzdává se video s ukázkou implementace; když je odevzdání odkaz, musí mít povolený přístup. Video má mít 1 až 6 minut. Zadání výslovně připomíná designovou část: jak má plížení fungovat, proč a jaký vliv to bude mít na gameplay.

Technické tipy ze zadání:

- v projektu jsou animace `Crouch_Idle` a `Crouch_Walk` (`Content/Skvt/Characters/Animations/Crouch/`);
- crouch se musí povolit v Character Movement Component;
- skok v dřepu se povolí přetížením funkce `CanJump`;
- funkce `Crouch` a `Uncrouch` má postava k dispozici.

## Upřesnění z lekce 2026-10-15

Z přepisu části lekce, ve které lektorka úkol představila (nahrávka uživatele v Plaudu, přečteno 2026-10-24). LLM souhrn téže nahrávky posouvá data na den nahrání (2026-10-24), proto vycházíme z přepisu.

- **Blueprinty chce vidět:** na videu se dá hodně věcí nafingovat, blueprinty řeknou víc. Můžou být přímo ve videu, nebo zvlášť v dokumentu či prezentaci. Projekt Unrealu neposílat, zdržuje opravování.
- **Video má ukázat všechny body zadání:** dřep, vstání, pohyb, skok a podlézání. Krátký GIF samotného plížení nestačí. Obvykle 1 až 5–6 minut, komentář je volitelný.
- **Přidat, jak jsme přemýšleli a proč:** většina má být vlastní designová rozhodnutí. Uvést i to, co se nepovedlo, protože k tomu může dát zpětnou vazbu; vždy je lepší odevzdat aspoň něco.
- **Otázky, na které má design odpovědět:** s jakým účelem se lidé plíží, jestli by pomohla kamera přiblížená, nebo oddálená, a jak se to má ovládat.
- **Skok z dřepu** podle ní realistický není, herní mechaniky ale realistické být nemusí. Vedle přetížení `CanJump` připustila i jiná řešení.
- **Termín** zmínila jako „přibližně tři týdny“ s tím, že si ho ověří. Platí termín z Labaverse, čtvrtek 2026-10-29 (dva týdny od zadání).

## Výchozí stav projektu

Po merge `upstream/stream10` (2026-10-24). Odvozeno ze jmen v assetech přes `strings`, v editoru ověřeno v T0 2026-10-25 (Zjištění T0 v `postup-editor.md`).

- `BP_SkvtBaseChar` má kameru z první i ze třetí osoby s přepínáním (`IA_SwapCamera`) a zoom kamery přes `TargetArmLength` spring armu (`IA_ZoomCamera`). `BP_SkvtPlayerController` drží `SavedZoomAmount` i přes výměnu postavy.
- `ABP_SkvtCharacter` má state machine se stavy Idle, Jump a Landing. Crouch zatím není v animačním blueprintu ani v postavě.
- Mapování vstupů nepoužívá levý Ctrl ani pravé tlačítko gamepadu; jednopísmenné klávesy se ze `strings` poznat nedají.

## Rozhodnutí (2026-10-24)

- **Úkol řešíme v tomhle projektu, ne v novém.** Animace, postava i cvičení z lekcí jsou tady a aktualizace kurzu se dají dál mergovat.
- **Stavíme na `upstream/stream10`**, kde jsou cvičení letošních lekcí (poslední z 2026-10-22). `upstream/main` se od 2026-09-24 nehýbe.
- **Vlastní assety jen ve složce `Content/Krato/`, assety kurzu needitujeme.** Upstream mění právě `ABP_SkvtCharacter` a `BP_SkvtBaseChar` a binární `.uasset` git neumí sloučit; při konfliktu by šlo jen vybrat jednu stranu. Proto child blueprint postavy kurzu (crouch v Character Movement, `CanJump`, kamera), kopie animačního blueprintu se stavy pro dřep a vlastní testovací level se sníženými stropy. Daň: úpravy animačního blueprintu z dalších lekcí do kopie samy nepřitečou.
- **Video do gitu nepatří** (veřejné repo bez LFS); videa v `docs/homeworks/` ignoruje `.gitignore`.

## Design

Čísla označená *cíl ladění* jsou výchozí odhad, doladí se v editoru.

### Herní kontext: útěk z lodi

Úsek vesmírné lodi ze cvičení na lekci 2026-10-20: hráč se potřebuje dostat ze skladu do strojovny a hlavní chodbu hlídá mimozemšťan. Plížení tu slouží dvěma účelům, které odpovídají na otázku lektorky, proč se lidé plíží: projít tam, kam se ve stoje nevejdeš (spadlá traverza, ventilace), a nebýt vidět. Hráč si mezi nimi vybírá: chodba je rychlá a riskantní, ventilace pomalá a bezpečná.

### Ovládání

- **Dřep je přepínač:** jeden stisk dřep, další stisk vstát. Ventilací se leze dlouho a držet přitom klávesu by unavovalo; stealth hry (Dishonored, Thief) to dělají stejně.
- **Pod nízkým stropem vstát nejde:** hra pokus zahodí a postava zůstane v dřepu, dokud hráč nezkusí vstát znovu na volném místě. Kdyby vstala sama, jakmile je nad ní místo, mohla by se na výstupu z ventilace nečekaně napřímit před mimozemšťanem.
- **Ve vzduchu se dřep nepřepíná** (doplněno 2026-10-24 po kontrole postupu): stisk ve vzduchu se ignoruje. Jinak by se do ventilace dalo dostat i skokem ve stoje a dřepnutím ve vzduchu, protože kapsle se ve vzduchu zmenšuje kolem středu a nohy vyskočí výš, a kamera by při přechodu ve vzduchu škubala.
- **Klávesy:** C a levý Ctrl, na gamepadu pravé tlačítko (B / kolečko). C, levý Ctrl ani to tlačítko gamepadu kurz nepoužívá (ověřeno v T0).

### Pohyb v dřepu

- **Pomalejší:** zhruba poloviční rychlost chůze (*cíl ladění*). Plížení je opatrnost, ne útěk; cenou za bezpečí je čas.
- **Z hrany spadne normálně**, jinak by nešlo seskočit z ventilace, ve které vstát nejde.

### Skok

- **V dřepu jen nízký poskok:** postava zůstane v dřepu a skočí níž, takže se vejde pod nízký strop a dostane se do ventilace, jejíž vstup je ve zdi nad podlahou. Ve vzduchu drží pózu dřepu, protože se standardní animací skoku by hlava prošla stropem.
- **Plný skok až po vstání.** Dřep tak zůstává samostatným tichým režimem a skok z dřepu má v levelu účel, ne jen splněnou položku zadání.

### Kamera

- **Ve třetí osobě se při dřepu plynule přiblíží a sníží**, při vstání se plynule vrátí. Cíl je zhruba 60 % vzdálenosti, kterou si hráč nastavil kolečkem (*cíl ladění*); jde o násobek hráčova zoomu, takže zoom kolečkem v dřepu funguje dál.
- **Proč přiblížit:** ve ventilaci by spring arm stejně narazil do stropu a přitáhl kameru sám, skokově. Řízené přiblížení působí záměrně, dává stísněný pocit a hráč z obrazu pozná, že se plíží.
- **Plynulá musí být i výška:** při dřepu se kapsle postavy zmenší a kamera připojená ke kapsli by bez vyhlazení poskočila dolů (chování Unrealu, *ověřit* v editoru).
- **V první osobě** výška očí jen plynule klesne, bez zoomu.

### Testovací level

```
[1 Sklad] → [2 Křižovatka] ─┬─ hlavní chodba: hlídka, bedny ─┬─→ [5 Strojovna]
 spadlá traverza:           │                                │
 protáhnout se v dřepu      └─ ventilace podél chodby ───────┘
                               vstup ve zdi nad podlahou (poskok),
                               mřížky ve stěně, výstup za zády hlídky (4)
```

| Místo | Co se tam děje | Napětí |
|---|---|---|
| 1 Sklad | Učení v bezpečí: dveře blokuje spadlá traverza, pod ní se projde jen v dřepu. Kamera se přiblíží a pod traverzou nejde vstát. | nízké |
| 2 Křižovatka | Z kolmé chodby je vidět mimozemšťan v osvětlené hlavní chodbě (signposting z lekce 2026-10-20). Nasvícená ventilační mříž ve zdi nabízí druhou cestu. Hráč volí. | střední |
| 3a Chodba | Rychlá a riskantní: hlídka a bedny jako kryt. | vysoké |
| 3b Ventilace | Pomalá a bezpečná: vstup jen poskokem v dřepu, nízký strop, mřížkami ve stěně je vidět hlídka v chodbě. | střední |
| 4 Výstup | Výstup z ventilace do chodby za zády hlídky, pár metrů dřepu kolem konce její trasy. | vysoké |
| 5 Strojovna | Cíl: teleport uprostřed místnosti, kterým hráč z lodi unikne. Musí se na něm 4 s nabíjet, takže kdo přijde nezahlédnutý, má oddech, kdo přiběhne s mimozemšťanem v zádech, nestihne to. | nízké, nebo vrchol při útěku |

Ventilace vede podél chodby za její boční stěnou, ne nad ní (změna 2026-10-24 při psaní postupu pro editor): ze vstupu ve zdi nad podlahou by se do výšky stropu chodby poskokem nedalo dostat.

Rozměry se odvodí z postavy (výška ve stoje a v dřepu včetně pózy animace, výška poskoku), ne od oka:

- traverza a strop ventilace leží mezi výškou postavy v dřepu a ve stoje, aby byl dřep nutný a zároveň stačil;
- vstup do ventilace je výš, než se dá vejít, ale níž, než doskočí poskok v dřepu;
- bedny jsou vyšší než postava v dřepu a nižší než postava ve stoje.

### Mimozemšťan

- **Hlídkuje** po trase v hlavní chodbě.
- **Vidí** jen v zorném kuželu a jen když na hráče přímo dohlédne: ve stoje zdálky, v dřepu až zblízka (zhruba 15 m a 5 m, *cíl ladění*). Viditelnost se měří k temeni postavy, takže kdo se krčí za bednou, je skrytý fyzicky bez zvláštního kódu.
- **Mřížkami ventilace hráče nevidí**, i když hráč jimi vidí ven: v otvorech je neviditelná deska, která blokuje paprsek mimozemšťana. Ventilace tak zůstává bezpečná.
- **Když hráče zahlédne, pronásleduje ho** v hlavní chodbě, na křižovatce až ke dveřím skladu a ve strojovně (rozhodnutí autora 2026-10-27 02:26: na kraji chodby jen marně zíral). Ukrýt se jde jen tam, kam se vejde jen postava v dřepu: pod propadlý strop ve skladu nebo do ventilace. Když k hráči nevede cesta, dojde na nejbližší místo, kam dojít může, chvíli tam stojí a vrátí se k hlídce. Když hráče chytí, obrazovka ztmavne a hráč se vrátí na křižovatku.
- **Pořadí prací:** dokud nejsou hotové povinné mechaniky, level a záložní video, je mimozemšťan jen hlídka bez reakce. Reakce na hráče přijde až potom, aby odevzdání nestálo na AI.

### Teleport ve strojovně (návrh autora, rozhodnuto 2026-10-27)

- **Proč:** od chvíle, kdy mimozemšťan pronásleduje hráče i do strojovny (rozhodnutí 2026-10-27 02:44), neměl level konec: hráč do strojovny došel a nic se nestalo, i když ji tabulka levelu vede jako cíl a oddech. Teleport cíl zhmotní, sedí k příběhu útěku z lodi a dává videu závěr.
- **Nabíjení 4 s** (*cíl ladění*): hráč ve stoje chodí rychlostí 500, mimozemšťan pronásleduje rychlostí 450, ve stoje mu tedy uteče. Okamžitě bezpečné místo by z posledního úseku udělalo závod, ve kterém plížení nemá smysl. Za 4 s mimozemšťan urazí 18 m, takže hráč, kterého zahlédl, unikne jen s velkým náskokem; kdo se doplíží nezahlédnutý, odteleportuje se v klidu. Světlo nad plošinou při nabíjení sílí, aby hráč věděl, že má čekat. Sestoupení z plošiny nabíjení zruší.
- **Únik:** obrazovka zbělá, mimozemšťan hráče přestane vidět i pronásledovat a level začne znovu od skladu. Když mimozemšťan hráče během nabíjení chytí, platí chycení.
- **Zvažovaná a odmítnutá varianta:** okamžitě bezpečné místo bez nabíjení (rychlejší na stavbu, ale ve stoje se k němu dá doběhnout).

### Video

- **Hlas k titulkům (2026-10-28):** autor namluvil všech 11 titulků i úvodní kartu (`nahravani-hlasu.md`, MP3 v `odevzdani/video/hlas/`, mimo git); `tools/build_video.py` hlas ořízne, srovná na −16 LUFS a položí 0,4 s po začátek segmentu, karty prodlouží podle hlasu. Titulky zůstávají. Úvodní kartu autor přemluvil kratším textem (10 s místo 18 s), video s hlasem má 4:59; do limitu 6:00 zbývalo místo na 6 screenshotů blueprintů mimozemšťana a teleportu po 8 s. Ty jsou ve videu od 2026-10-28 (detekce, cíl pohledu, pronásledování, chycení, nabíjení teleportu, únik), video má 5:47; ostatní snímky 14–35 půjdou jen do PDF.
- **Původně titulky bez hlasu**, 11 titulků, 2 až 2,5 minuty záznamu ze hry. Hlasový komentář se nenahrává: autor záložní video s titulky po zhlédnutí 2026-10-27 schválil („Je to výborné“). Na titulek o ~100 znacích je potřeba asi 7 s, záběry proto mechaniku chvíli drží.
- **Úvodní karta** (5 s, klíč `intro` v JSON pro `tools/build_video.py`; schválená autorem 2026-10-27, aby video obstálo i mimo Labaverse): „Plížení – ukázka herní mechaniky v Unreal Engine 5 / Domácí úkol č. 2 v kurzu Game design pro začátečníky / SKVOT, podzim 2026 / Petr Kratochvíl · krato.cz“. Pořadatel kurzu je podle stránky kurzu SKVOT (ne robot_dreams); Labaverse je jen platforma pro odevzdávání.
- **Zveřejnění:** do Labaverse jde odkaz na Google Drive, protože tam „Spravovat verze“ zachová odkaz i po opravě. Na YouTube se nahraje až konečná verze, nejdřív ve středu po doladění, protože YouTube výměnu souboru neumožňuje a každá oprava by měla nový odkaz. Viditelnost nejdřív „Neveřejné“. Zvuk do střihu jen vlastní (syntetizovaný v ffmpeg) nebo s ověřenou licencí, kvůli Content ID.
- **Pracovní znění titulků:**
  1. Plížení: útěk z vesmírné lodi. Chodbu hlídá mimozemšťan, druhá cesta vede ventilací.
  2. Dřep se zapíná a vypíná. Ventilací se leze dlouho a držet klávesu by unavovalo.
  3. Kamera se v dřepu plynule přiblíží a sníží. Ve ventilaci by do stropu narazila sama; takhle hráč pozná, že se plíží.
  4. Pod nízkým stropem vstát nejde. Hra pokyn zahodí, takže z ventilace nevylezeš nečekaně ve stoje.
  5. Skok v dřepu je nízký poskok: vejde se pod strop a dostane tě do ventilace. Plný skok až po vstání.
  6. V dřepu je postava pomalejší. Plížení je opatrnost, ne útěk.
  7. Ve stoje tě mimozemšťan zahlédne zdálky, v dřepu až zblízka.
  8. Chodba je rychlá a riskantní, ventilace pomalá a bezpečná.
  9. Cílem je teleport ve strojovně. Nabíjí se 4 s, takže s mimozemšťanem v zádech to nestihneš.
  10. Co zatím chybí: mimozemšťan hráče, kterého ztratí z dohledu, nehledá, jen se vrátí k hlídce. (Od 2026-10-28 bez zvuků, které jsou ve hře; hlas je potřeba přemluvit.)
  11. Použití AI: o návrhu mechaniky jsem rozhodoval v dialogu s AI (Claude). Blueprinty podle něj sestavila AI, stejně jako zvuky, titulky a střih. Hru jsem testoval a ladil sám: výšku kapsle v dřepu, rozměry levelu podle chůze v dřepu a ruční opravy blueprintů. Postavil jsem mříže a teleport, natočil a namluvil všechny záběry. (Přeformulované 2026-10-28: autor se obával, že „ta postavila blueprinty“ zní, jako by AI udělala skoro všechno; rozdělení práce zůstává poctivé, jen je na prvním místě rozhodování o návrhu. „Stroje“ vypuštěné, protože ve strojovně nejsou poznat. Hlas je potřeba přemluvit.)
- **Blueprinty ve videu i v PDF** (rozhodnuto 2026-10-24): na konci videa krátký blok s každým klíčovým grafem asi 10 s s titulkem, aby video obstálo samo. K tomu PDF s ostrými screenshoty a krátkým popisem implementace včetně toho, co nefunguje; blueprint ve videu se čte špatně, v PDF si ho lektorka zvětší. PDF se vyrobí přes weasyprint jako u DÚ č. 1. Grafy proto potřebují komentářové bloky, aby se daly číst i bez výkladu. Do PDF patří u AI mimozemšťana i věta o architektuře (rozhodnuto 2026-10-28): AI je pro jednoduchost postavená přímo v blueprintu postavy mimozemšťana (hlídka a pronásledování jako události s AI MoveTo, zrak jako vlastní detekce každých 0,2 s); standardní cesta v Unrealu by byla AI Controller s Behavior Tree a AI Perception, viz `odlozene-napady.md`.
- **Zvuky ve hře (2026-10-28, autor schválil v Play):** vlastní syntéza v ffmpeg (krok, úder se stoupajícím tónem a ozvěnou při zahlédnutí, klesající tón při chycení, stoupající tón nabíjení teleportu, šum úniku, hučení strojovny, vítr ve ventilaci jako smyčka z hnědého a růžového šumu). Vítr byl původně ze `Starter_Wind05` a pípnutí byla dvě; 2026-10-28 večer obojí nahrazené (vítr kvůli licenci, viz `AGENTS.md`, Veřejné repo; zvuk zahlédnutí vybral autor ze tří variant); zdrojové WAV leží vedle assetů v `Content/Krato/Audio/`. Kroky počítá `UpdateFootsteps` z Event Tick podle ušlé vzdálenosti: 170 cm ve stoje, 85 cm v dřepu (autor: v dřepu nohy kmitají stejně rychle jako při chůzi, jen kratší krok; odhad 220 cm z délky animace nevyšel), v dřepu tišeji. Ventilace a strojovna jsou `AmbientSound` s útlumem v kvádru přes místnost (ventilace `VolumeMultiplier` 0,4, autor: 0,8 bylo moc). Po chycení `RespawnAtCheckpoint` zastaví pohyb, uvolní držené klávesy (`FlushPlayerInput`) a postava vstane; autor hlásil návrat v dřepu a „drženou“ klávesu W. Kroky mimozemšťana (přidané 2026-10-28 večer na přání autora, „nedává smysl, že hráč dělá kroky a mimozemšťan ne“): `UpdateFootsteps` v `BP_KratoAlien` z Event Tick, krok po 100 cm při hlídce a 160 cm při pronásledování, těžší vlastní zvuk `S_Krato_AlienStep` přes komponentu `StepSound` s prostorovým útlumem 2–15 m (asset `SoundAttenuation` přes MCP vytvořit nejde, `DataAssetTools` bere jen datové assety; útlum na umístěné instanci se nezapsal, proto výměna instance `tools/replace_alien.py`). Dopad po skoku zvuk nemá. Blikání ve svislých šachtách je v PDF v „Co nefunguje“. Záznamy obrazovky z 2026-10-27 zvukovou stopu nemají, záběry se proto přetáčejí se zvukem ze systému; `build_video.py` zvuk hry ze záznamu zachová a pod hlasem ho ztlumí.
- **Záložní video** se natočí hned po povinné části, před reakcí mimozemšťana.
- **Titulky vypálit do obrazu:** výchozí `ffmpeg` z Homebrew nemá filtry `subtitles` ani `drawtext`, proto je vedle něj nainstalovaný `ffmpeg-full` (keg-only, `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg`), který je má. Titulky jsou ASS s písmem Arial a pevnou mezerou za jednopísmennými předložkami.
- **Záložní video** (`odevzdani/video/Kratochvil-DU2-zalozni.mp4`, mimo git): 1920 × 1080, 30 fps, 3:56. Obsahuje sedm záběrů s titulky 1–6 a 8 (asi 2 min; titulek 7 chybí, protože mimozemšťan zatím není ve hře), 13 screenshotů blueprintů po 8 s a 9 s přiznání AI. Pojistka „pokud T7 nevyjde, odevzdává se tohle video“ se nepoužila, T7 je hotové; finální video vznikne v T8. Záběry záložního videa mají starý bílý vzhled, v T8 se proto přetáčejí všechny.

## Další kroky

Postup krok za krokem je v [postup-editor.md](postup-editor.md) (úkoly T0 až T8, odhad 11–17,5 h, rozhodovací pravidla pro škrtnutí mimozemšťana).

T0–T7 a vizuální vylepšení jsou hotové (viz Stav). Zbývá test teleportu (bod 2) a T8 (bod 3); bod 1 zůstává jako záznam:

1. Vizuální vylepšení před natáčením T8 (rozhodnutí autora 2026-10-27 ~02:50; staví agent přes MCP, autor odpovídá na otázky a zkouší v Play průběžně, protože paralelně pracuje na jiných projektech). **Postaveno 2026-10-27 v 03:00–04:20** (commity `bac0ce2`, `3fcb3d7` a `8087c51`), autor výsledek v Play schválil:
   - mimozemšťan má nad hlavou bodové světlo, při hlídce tlumeně zelené (5 cd), při pronásledování červené (60 cd, zbarví okolí). Světlo 20 cd bylo podle autora nenápadné; zkoušela se k němu svítící kulička nad hlavou (stealth hry ukazují stav nepřítele znakem nad hlavou, vykřičník v Metal Gear, ukazatel odhalení v Assassin's Creed), ale autor ji odmítl, „vypadá divně“, a zůstalo jen silnější červené světlo;
   - lampy visí u všech hlavních světel včetně světla u dveří strojovny, jsou zmenšené na 0,75 a ocelové (autor: zlaté byly moc světlé); bez lampy zůstala světla ve ventilaci a reflektor na její vstup;
   - stěny místností mají `M_Krato_TechPanel_World`, kopii `M_Tech_Panel` s texturou podle polohy ve světě (čtvercové panely 2 m, vodorovně se opakují). Autor první pokus s natažením po kostce odmítl kvůli roztaženým šroubům, odraz se mu líbil. Ventilace zůstala bílá (autor): společná stěna s chodbou je jedna kostka, na straně ventilace ji proto kryje 2cm bílé obložení mimo otvory s mřížemi (`Blockout/3b_Ventilace/Oblozeni`). Bedny a traverza ve skladu jsou z `M_Metal_Steel`;
   - pruh na stěně strojovny, který autor viděl problikávat, příčinu nenašel; po výměně materiálu stěn ve snímku není (viz `docs/unreal-mcp.md`, Level a Play).

   Původní plán (světlo, lampy, textury na zkoušku) je splněný. Světlo se od něj liší: je to komponenta `AlertLight` v `BP_KratoAlien` a přepíná ho funkce `UpdateAlertLight` volaná ze `StartChase` a `StopChase`. Po výměně instance mimozemšťana ověřilo Play přes MCP hlídku, zahlédnutí i chycení; skryté desky v mřížích a navigační síť se neměnily. Plán v původním znění:
   1. **Světlo zahlédnutí na mimozemšťanovi** (určitě): malé bodové světlo na hlavě, tlumeně zelené při hlídce, červené při pronásledování (přepíná se v `StartChase` a `StopChase`, světlo najde `GetComponentByClass`). Účel: aby bylo ve videu vidět, kdy hráče zahlédl, což je hodnocená mechanika. Odhad 20–30 min.
   2. **Stropní lampy** (určitě): `/Game/StarterContent/Props/SM_Lamp_Ceiling` u každého bodového světla v chodbě, strojovně a skladu, světlo těsně pod lampou. Odhad 15 min.
   3. **Textury** (vyzkoušet): `M_Tech_Panel` na stěny, `M_Tech_Hex_Tile` nebo `M_Concrete_Tiles` na podlahu, ocel na bedny, vše ze Starter Contentu. Napřed na jedné stěně chodby a snímek autorovi: kostky jsou natažené měřítkem (stěna chodby 25 m), takže se textura může roztáhnout. Pokud ano, vlastní materiál s texturou podle polohy ve světě (world-aligned) za dalších 30–45 min, nebo textury vynechat. Rozhoduje autor podle snímku.
   Změna vzhledu znamená přetočit i sedm záběrů záložního videu (asi 20 min autora), aby finální video nemíchalo bílý blockout s novým vzhledem. Skryté desky v mřížích ventilace a navigační síť se nemění; po úpravách zopakovat test z T7 (chycení ve stoje, křižovatka, strojovna, ventilace).
2. ~~Teleport: ruční test autora v Play.~~ Hotové 2026-10-27 17:56: teleport i stroje prošly, `ChargeTime` zůstává 4 s.
3. T8: přetočit všech sedm záběrů záložního videa (nový vzhled se nemá míchat s bílým blockoutem) a dotočit záběry s mimozemšťanem a teleportem podle `scenar-nataceni.md`, sekce Druhé natáčení; pak finální video a PDF. Natáčení a sestavení v úterý 2026-10-27 večer po lekci, ve středu 2026-10-28 doladění a odevzdání v Labaverse.
