# Domácí úkol č. 3 – tábor banditů (living world a level design)

- **Zadání:** slajdy z lekce 2026-11-02 (screenshoty od autora) a prezentace `Domaci_ukol_c._3.pptx` z Discordu kurzu, uložená lokálně v `docs.local/hw03-tabor-banditu/` mimo git; 2026-11-03 už byl úkol i v Labaverse. Hlavní kopie všech materiálů (včetně textu zadání z Labaverse a od 2026-11-04 i celých slajdů lekce 14 „Open world design & design živoucích světů“, s výtahem toho, co se týká úkolu, v tamním `README.md`) je od 2026-11-03 v soukromém repu projektu, `bandit-camp/docs/kurz-du3/`. Doslovné znění sem nedáváme, repo je veřejné.
- **Deadline:** úterý 2026-11-24 23:59 (stránka úkolu v Labaverse, zjištěno 2026-11-03).
- **Interní cíl:** hotovo do úterý 2026-11-17, odevzdat nejpozději v neděli 2026-11-22 (pravidlo: víceméně hotovo týden předem, odevzdat nejpozději dva dny předem).
- **Hodnocení:** maximálně 30 bodů. Lektorka nehodnotí správnost blueprintů, ale design tábora, jeho uvěřitelnost, level design a průchod levelem.
- **Stav:** zadání zapsané 2026-11-02; 2026-11-03 rozhodnuté prostředí (les) a pracovní námět světa; 2026-11-05 layout tábora (útes, řeka s lanem, pláž, jeskyně s lesem na stropě) a plánek v2 se třemi cestami hráče, první verze design dokumentu (3 strany PDF, LW část 1,9 normostrany) hotová v soukromém repu `bandit-camp` (`docs/du3-dokument/`, plánek `docs/navrh-levelu/`). Týž večer založený projekt Unrealu (šablona Third Person, varianta Combat, s MCP na portu 8766) a hotový terén greyboxu (level `L_TaborNaTisine`), ověřený v Play. Ještě týž večer hotový celý greybox: rekvizity tábora, pět banditů jako panáci bez AI (kápo obou variant), neviditelné hranice mapy a Player Start u lodi; autor level prošel v Play bez připomínek. Snímek greyboxu shora s dokreslenými cestami A, B, C a okruhem hlídky je v dokumentu jako čtvrtá strana (příloha) a přiznání AI ke greyboxu je dopsané; dokument má 4 strany, LW část 1,91 normostrany.
- **Branch:** `student-krato-homeworks`

## Co zadání chce

Úkol má dvě designové části a jednoduchou implementaci v Unrealu.

**1. Living world.** V lese neurčené open-world hry se utábořilo pět banditů, kteří se starají o jídlo, o bezpečí a o to, aby jim v táboře nic nechybělo. Úkolem je navrhnout umístění a celkový layout tábora a aktivity banditů nad rámec hlídkování. Popis má nejvýš dvě normostrany. Součástí je plánek s popisky: co kde je, kdo kde hlídkuje a jak dlouho.

**2. Level design.** Hráč má okrást kápa, největšího hrdlořeza z banditů, o cennou věc. Cennost má kápo buď u sebe, nebo v truhle ve svém stanu, a navrhnout se mají obě varianty. Hráč se do tábora plíží ve dne a musí se vyhnout hlídkám; preferovaný způsob hraní je stealth. Průchod levelem vychází z rozmístění banditů a věcí z první části. Zvolené cesty se zakreslí do plánku, nebo do screenshotu z implementace.

**Implementace v UE.** Návrh se postaví v Unrealu, design má proto být jednoduchý. Hodnotí se design tábora, jeho uvěřitelnost, level design a průchod levelem, správnost blueprintů ne.

## Upřesnění z lekce 2026-11-02 a z Discordu kurzu

Z přepisu konce lekce (nahrávka autora v Plaudu, přečteno 2026-11-02) a ze zpráv v kanálu úkolu.

- **Nepřemýšlet to příliš:** jako základ stačí postup ze cvičení level designu na lekcích, tedy přidávat beat po beatu herní prvky.
- **Do popisu patří premisa:** proč zrovna tenhle tábor a proč jsou tam, co je to za lidi, jaké mají role, hierarchii a co dělají. Hlavně rutiny a chování banditů.
- **Implementace bez logiky:** level stačí postavit bez questové logiky a bez blueprintů. Kdo si troufne na skriptování, může, body navíc za to nejsou. Smyslem je vyzkoušet si nástroje na stavbu levelu a práci s prostorem ve 3D: co je vidět a co ne, jak prostor zakrýt, aby se za něco dalo schovat, a jak ho otevřít.
- **Stačí greybox,** nemusí být texturovaný ani barevný. Kdo chce, najde na Fabu balíčky assetů k tématu, i s licencí CC.
- **Plánek** může být screenshot z enginu, do kterého se zakreslí cesty a poklad. Nakreslený plánek tábora navíc pomůže taky.
- **Žánr je volný:** středověcí banditi, fantasy, gang v cyberpunkovém městě; jde o lidi mimo civilizaci, kteří cennost dobrovolně nevydají. Navázat na svět z DÚ č. 1 je výslovně v pořádku.
- **Rutiny nemusí být tak podrobné** jako ve vzorové práci, míru detailu nechává lektorka na studentech.
- **Volitelně video průchodu levelem s komentářem,** jako cvičení, jak předat myšlenku jinému designérovi.

## Vzorová práce

Lektorka na Discordu poslala vzorovou práci z dřívějšího běhu: dokument na tři strany, mapu s vyznačenými trasami hlídek a video implementace. Uložená je lokálně v `docs.local/hw03-tabor-banditu/` (mimo git, repo je veřejné; seznam souborů v tamním `ZDROJE.md`). Pro představu o rozsahu: dokument má části okolí tábora, dispozice tábora, denní a noční rutiny banditů s rozvrhem hlídek, reakce hlídek na hráče, možnosti hráče (přístupy, rizikové body, slabiny) a závěr; mapa je pohled shora s barevnými trasami hlídek a body, kde se NPC zastavují.

## Inspirace z lekce

Lektorka popisovala práci living world designéra na rozmisťování událostí v open worldu: každé místo si projde ze všech úhlů a „režíruje“ ho, aby to, co tam NPC dělají, dávalo smysl (banditi, kteří mají být schovaní, jsou v houští). Bandité, kteří si spolu povídají, musí stát blízko u sebe. Inteligenci NPC hráč pozná z drobností, například z hlášek (barků), kterými NPC komentují dění a hráči tím dávají informace.

## Rozhodnutí (2026-11-02)

- **Level se staví v novém soukromém repu [`kratocz/bandit-camp`](https://github.com/kratocz/bandit-camp)** (`~/IdeaProjects/github.com/kratocz/bandit-camp`, projekt `BanditCamp` na šabloně Third Person), ne v tomhle forku. Z levelu může vzniknout samostatná hra a fork kurzu licenčně čistý být nemůže: obsah kurzu bez licence v něm zůstane i v historii, výchozí mapa projektu je mapa kurzu, zabalená hra obsah kurzu obsahuje a assety z Fabu pod Standard License nesmí do veřejného repa. Dokumentace a odevzdání úkolu zůstávají tady. Dřep z DÚ č. 2 visí na postavě kurzu, v novém projektu se případně postaví znovu na postavě šablony.

## Rozhodnutí (2026-11-03)

- **Prostředí: lesní tábor ze zadání.** Pracovní námět světa je hard sci-fi blízké budoucnosti (rok 2057, rozpadající se, ale stále fungující technologická civilizace); kdo bandité jsou, zatím nerozhodnuto (bývalí technici, vědci, ostraha nebo improvizovaná komunita, která cenné zařízení možná chrání, ne jen drží pro zisk). Námět vznikl 2026-11-03 v hlasové diskusi autora s ChatGPT a leží v soukromém repu `bandit-camp` (`GAME_CONCEPT.md`). Zvažovaná alternativa, loď přepadená bandity (`BANDIT_SHIP_CONCEPT.md` tamtéž), se v úkolu nestaví: mění prostředí i cíl zadání (lesní tábor, cennost u kápa nebo v truhle ve stanu). Svět z DÚ č. 1 ani klasický středověk se nevybraly.
- **Pro úkol stačí z námětu odstavec premisy** (proč tu tábor je, kdo jsou bandité a jejich role); stopy, dilema a víc zakončení patří do případné hry, zadání chce max. dvě normostrany a nic z questové logiky.
- **Házení kamínků** (hráč odláká hlídku zvukem) se v úkolu navrhne, ne implementuje: šablona Combat nemá sluch NPC. Do plánku se zakreslí místa, kam se vyplatí hodit (kotlík, dřevo, plechová bouda), a reakce hlídek se popíšou v textu.

## Rozhodnutí (2026-11-05)

- **Zdroj design dokumentu je v soukromém repu `bandit-camp`** (`docs/du3-dokument/Kratochvil-DU3-tabor-banditu.html`, PDF přes weasyprint), vedle generátoru plánku a pracovních poznámek k levelu (`docs/navrh-levelu/README.md`). Sem do `odevzdani/` přijde při odevzdání hotové PDF. Důvod: dokument, mapa i projekt Unrealu se mění spolu a soukromé repo nemusí hlídat, co smí být veřejné.
- **Layout:** útes na západě přes celou mapu, řeka s lanem pod hladinou (past na lodě), skalnatá pláž u tůně s ohništěm, jeskyně se spaním a truhlou, zalesněná plošina nad jeskyní s okruhem hlídky a komínem (volitelný vstup shora), strážní ostroh kápa na jihu, oka na stezce zvěře na severu jako cíl kamínků, lovec se psem (návrat v 11 a 15) jako časový tlak. Hráč přistává lodí za ostrohem a lodí i uniká. Tři cesty: A přes plošinu, B za zády kápa po okraji pláže, C od severu během siesty. Cennost: podpisový token (varianta A v truhle, B na krku spícího kápa).

## Další kroky

- Oponentura dokumentu proti zadání (subagent v čistém kontextu), potvrzené nálezy zapracovat.
- Den nechat dokument uležet a přečíst celé PDF očima.
- Zvážit plánek bez vestavěné legendy (legenda do textu), aby byl na straně větší a čitelnější v tisku.
- Před odevzdáním: PDF do `odevzdani/`, text odevzdání, kontrola Discordu kurzu.

## Otevřená rozhodnutí

- **Grafika.** Greybox stačí; assety z Fabu jen ty s licencí CC0 nebo CC BY, které smí do veřejného repa (CC BY s uvedením autora), placené a ostatní z Fabu do repa nepatří.
- **Video průchodu s komentářem** je volitelné, rozhodnout podle času.
