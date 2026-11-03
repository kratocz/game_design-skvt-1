# Domácí úkol č. 3 – tábor banditů (living world a level design)

- **Zadání:** slajdy z lekce 2026-11-02 (screenshoty od autora) a prezentace `Domaci_ukol_c._3.pptx` z Discordu kurzu, uložená lokálně v `docs.local/hw03-tabor-banditu/` mimo git; v Labaverse zatím úkol není (stav 2026-11-02). Doslovné znění sem nedáváme, repo je veřejné.
- **Deadline:** zatím neznámý. Na lekci zaznělo „minimálně tři týdny, možná měsíc“ s tím, že ho lektorka napíše na Discord; závazný bude termín na stránce úkolu v Labaverse. Odhad: kolem 2026-11-23 až 2026-11-30.
- **Interní cíl:** stanovit, až bude termín v Labaverse (pravidlo: víceméně hotovo týden předem, odevzdat nejpozději dva dny předem).
- **Hodnocení:** zatím neznámé.
- **Stav:** zadání zapsané 2026-11-02; 2026-11-03 rozhodnuté prostředí (les) a pracovní námět světa, design dokument nezačal.
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

- **Prostředí: lesní tábor ze zadání.** Pracovní námět světa je hard sci-fi blízké budoucnosti (rok 2057, rozpadající se, ale stále fungující technologická civilizace); bandité jsou skupina bývalých techniků a jejich ochránců s cenným zařízením, které chrání. Námět vznikl 2026-11-03 v hlasové diskusi autora s ChatGPT a leží v soukromém repu `bandit-camp` (`GAME_CONCEPT.md`). Zvažovaná alternativa, loď přepadená bandity (`BANDIT_SHIP_CONCEPT.md` tamtéž), se v úkolu nestaví: mění prostředí i cíl zadání (lesní tábor, cennost u kápa nebo v truhle ve stanu). Svět z DÚ č. 1 ani klasický středověk se nevybraly.
- **Pro úkol stačí z námětu odstavec premisy** (proč tu tábor je, kdo jsou bandité a jejich role); stopy, dilema a víc zakončení patří do případné hry, zadání chce max. dvě normostrany a nic z questové logiky.
- **Házení kamínků** (hráč odláká hlídku zvukem) se v úkolu navrhne, ne implementuje: šablona Combat nemá sluch NPC. Do plánku se zakreslí místa, kam se vyplatí hodit (kotlík, dřevo, plechová bouda), a reakce hlídek se popíšou v textu.

## Další kroky

Námět vůči zadání zatím nepokrývá:

- **obě varianty cennosti:** kdy ji kápo nosí u sebe, kdy leží v truhle ve stanu, a jak se podle toho mění cesta hráče;
- **rozvrh hlídek:** kdo kde hlídkuje a jak dlouho; námět má jediného hlídače, pět lidí potřebuje střídání (např. hlídač s průzkumníkem);
- **layout tábora:** stany, ohniště, generátor, přístupové cesty a krytí.

## Otevřená rozhodnutí

- **Grafika.** Greybox stačí; assety z Fabu jen ty s licencí CC0 nebo CC BY, které smí do veřejného repa (CC BY s uvedením autora), placené a ostatní z Fabu do repa nepatří.
- **Video průchodu s komentářem** je volitelné, rozhodnout podle času.
