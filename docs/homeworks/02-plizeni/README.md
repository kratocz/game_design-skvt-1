# Domácí úkol č. 2 – plížení

- **Zadání:** text na stránce úkolu v Labaverse (kopii poslal uživatel 2026-10-24); doslovné znění sem nedáváme, repo je veřejné
- **Deadline:** čtvrtek 2026-10-29 do 23:59
- **Interní cíl:** odevzdat nejpozději v úterý 2026-10-27; cíl „víceméně hotovo týden předem“ (čtvrtek 2026-10-22) propadl, práce začala v sobotu 2026-10-24
- **Hodnocení:** nejvýš 20 bodů
- **Stav:** design schválen 2026-10-24, postup pro editor (`postup-editor.md`) hotový 2026-10-25, T0 a T1 (postava s dřepem na přepínač, testovací level) hotové 2026-10-25, T2 (póza dřepu; rozměry levelu podle chůze v dřepu, viz Zjištění T2 v `postup-editor.md`) hotové 2026-10-26, T3 (nízký poskok v dřepu) hotové 2026-10-26, T4 (kamera při dřepu) a T5 (blockout levelu) hotové 2026-10-26, T6 (komentáře a screenshoty blueprintů, záložní video s titulky) hotové 2026-10-26 ve 23:52; T7 (mimozemšťan jako blueprint, hlídka, detekce a chycení ověřené v Play přes MCP, ocelové mříže ve ventilaci) uzavřené 2026-10-27 01:31; další krok je T8 (finální video, PDF, odevzdání)
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
| 5 Strojovna | Cíl a oddech. | nízké |

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

### Video

- **Titulky bez hlasu**, zhruba 9 titulků a 130 slov, 2 až 2,5 minuty záznamu ze hry. Hlasový komentář se nenahrává: autor záložní video s titulky po zhlédnutí 2026-10-27 schválil („Je to výborné“). Na titulek o ~100 znacích je potřeba asi 7 s, záběry proto mechaniku chvíli drží.
- **Pracovní znění titulků:**
  1. Plížení: útěk z vesmírné lodi. Chodbu hlídá mimozemšťan, druhá cesta vede ventilací.
  2. Dřep se zapíná a vypíná. Ventilací se leze dlouho a držet klávesu by unavovalo.
  3. Kamera se v dřepu plynule přiblíží a sníží. Ve ventilaci by do stropu narazila sama; takhle hráč pozná, že se plíží.
  4. Pod nízkým stropem vstát nejde. Hra pokyn zahodí, takže z ventilace nevylezeš nečekaně ve stoje.
  5. Skok v dřepu je nízký poskok: vejde se pod strop a dostane tě do ventilace. Plný skok až po vstání.
  6. V dřepu je postava pomalejší. Plížení je opatrnost, ne útěk.
  7. Ve stoje tě mimozemšťan zahlédne zdálky, v dřepu až zblízka.
  8. Chodba je rychlá a riskantní, ventilace pomalá a bezpečná.
  9. Použití AI: návrh mechanik a levelu vznikl v dialogu s AI (Claude), rozhodnutí a testování ve hře jsou moje. Blueprinty a blockout postavila AI v editoru přes MCP plugin, záběry jsem natočil sám, titulky a střih připravila AI. (Znění schválené se záložním videem 2026-10-27; po T7 doplnit mimozemšťana.)
- **Blueprinty ve videu i v PDF** (rozhodnuto 2026-10-24): na konci videa krátký blok s každým klíčovým grafem asi 10 s s titulkem, aby video obstálo samo. K tomu PDF s ostrými screenshoty a krátkým popisem implementace včetně toho, co nefunguje; blueprint ve videu se čte špatně, v PDF si ho lektorka zvětší. PDF se vyrobí přes weasyprint jako u DÚ č. 1. Grafy proto potřebují komentářové bloky, aby se daly číst i bez výkladu.
- **Záložní video** se natočí hned po povinné části, před reakcí mimozemšťana.
- **Titulky vypálit do obrazu:** výchozí `ffmpeg` z Homebrew nemá filtry `subtitles` ani `drawtext`, proto je vedle něj nainstalovaný `ffmpeg-full` (keg-only, `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg`), který je má. Titulky jsou ASS s písmem Arial a pevnou mezerou za jednopísmennými předložkami.
- **Záložní video** (`odevzdani/video/Kratochvil-DU2-zalozni.mp4`, mimo git): 1920 × 1080, 30 fps, 3:56. Obsahuje sedm záběrů s titulky 1–6 a 8 (asi 2 min; titulek 7 chybí, protože mimozemšťan zatím není ve hře), 13 screenshotů blueprintů po 8 s a 9 s přiznání AI. Pokud T7 nevyjde, odevzdává se tohle video.

## Další kroky

Postup krok za krokem je v [postup-editor.md](postup-editor.md) (úkoly T0 až T8, odhad 11–17,5 h, rozhodovací pravidla pro škrtnutí mimozemšťana).

T0–T7 jsou hotové (viz Stav). Zbývá:

1. T8: finální video, PDF a odevzdání v Labaverse nejpozději v úterý 2026-10-27.
