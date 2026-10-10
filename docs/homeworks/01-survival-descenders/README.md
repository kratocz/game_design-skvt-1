# Domácí úkol č. 1 – survival vrstva pro Descenders

- **Zadání:** [Ukol c.1 - zadani - design dokument.pdf](../Ukol%20c.1%20-%20zadani%20-%20design%20dokument.pdf), varianta *Zadání 1: Survival*
- **Deadline:** čtvrtek 2026-10-15 v 18:00 (začátek lekce), bráno jako tvrdý termín
- **Interní cíl:** víceméně hotovo týden předem (čtvrtek 2026-10-08, prošlo bez draftu); krajně nejpozději úterý 2026-10-13
- **Stav:** pracovní návrh kompletní a prošel oponenturou ([oponentura-2026-10-10.md](oponentura-2026-10-10.md)); zbývá premisa, odevzdávaný one-pager a příloha
- **Branch:** `student-krato-homeworks`

## Co zadání chce

Navrhnout survival systém pro open-world hru dle vlastního výběru. Survival prvky mají hru obohatit, ale nesmí z ní udělat survival hru. Design má zahrnout i to, jak se hráč s překážkami vypořádá. Výstup je menší formát (prezentace nebo one-pager); u vlastní hry nebo vlastního režimu se premisa a setting popisují v separátním dokumentu.

## Upřesnění z Discordu kurzu

Z odpovědí na dotazy studentů v kanálu k úkolu 1 na Discordu kurzu (zprávy z 2026-09-17 až 2026-09-20, přečteno 2026-10-10). Jména z neveřejného serveru sem záměrně nepíšeme, repo je veřejné.

- **Písmo** nejméně 10 bodů, styl je volný, hlavně aby se dalo číst.
- **Prezentace se počítá, ale neznamená hezký vizuál.** One-pager se „nechá někomu na stole“ a čtenář z něj musí vytáhnout všechno bez možnosti dovysvětlení. Rozhoduje, jak dobře informace plynou; i obyčejný Word dokument může být dobrý design.
- **Čtenář hru zná**, takže základy hry do one-pageru nepatří. Co je potřeba vysvětlit navíc (vlastní hra), patří do separátního dokumentu.
- **High-level, bez čísel a hloubkových detailů**, ale víc než jen vize; jako vzor odkazuje na příklad, který studenti dostali.
- **Příloha** se třemi stranami obrázků je v pořádku.

Důsledky pro odevzdávaný one-pager: vynechat vysvětlování Descenders (životy, roguelite struktura), vynechat čísla označená *cíl ladění*, držet logický tok od problému k řešení a písmo nejméně 10 bodů.

## Vzor z kurzu: Valheim – Riding Animals

Vzorový one-pager z kurzu leží lokálně v `docs/homeworks/Valheim Onepager Ride Animals.pdf` (ignorovaný v gitu, repo je veřejné). Co z něj plyne:

- **Jedna strana A4:** velký obrázek nahoře (zhruba dvě pětiny strany), pod ním titulek a asi 400 slov souvislé prózy. Žádné tabulky, žádná čísla.
- **Tok:** problém (jízda na zvířatech neobstojí proti plavbě, běhu a portálům) → kontext ve světě hry → tři konkrétní změny → závěrečná věta, která všechny tři změny přiváže zpět k problému.
- **Každá změna stojí na existujícím prvku hry** (kamenné portály, útok stomp, skok asksvina, láva); hru čtenáři nevysvětluje.
- **Klíčové mechaniky zvýrazněné barvou**, dvě specializace jako odrážky s ikonou a podnadpisem.
- **Vizuál ladí s hrou** (severské ornamenty, runový podtitul).

## Dokumenty

- [odevzdani/one-pager.pdf](odevzdani/one-pager.pdf) – **odevzdávaný one-pager** (A4), zdroj [odevzdani/one-pager.html](odevzdani/one-pager.html); PDF se vyrábí příkazem `weasyprint one-pager.html one-pager.pdf` ve složce `odevzdani`
- [one-pager.md](one-pager.md) – pracovní návrh s podrobnostmi a čísly pro ladění; z něj one-pager vychází
- [premisa-a-setting.md](premisa-a-setting.md) – separátní dokument s premisou a settingem režimu, jak zadání požaduje
- [odlozene-napady.md](odlozene-napady.md) – nápady, které jsme zatím nevybrali, i s důvodem a podmínkou návratu

## Rozhodnutí z brainstormingu (2026-10-06 až 2026-10-10)

- **Téma:** zadání 1 (survival), hra **Descenders** (původní MTB hra, ne Descenders Next).
- **Forma:** nový herní režim *kampaň* – jedna souvislá oblast, kterou kurýr projíždí s volbou trasy. Tím řešíme podmínku open-world, protože základní Descenders stojí na uzlech a procedurálních runech.
- **Jádro dokumentu je survival systém**, příběh je jen rámec v separátním dokumentu.
- **Bez zbraní, bez pronásledování lidským nepřítelem, bez války.** Postapokalyptický svět, ne válečná fronta.
- **Tlak je čas, ne nepřítel.** Měkký termín (odkvět sadů), ne tvrdý odpočet.
- **Náklad jsou včelí královny.** Péče o něco živého, roztomilé, bez medicínských asociací (krev a léky jsme vyřadili, protože při sportu připomínají zranění).
- **Dvě cesty, tam a zpět.** Tam veze kurýr obchodní náklad do horské včelí stanice (solární panely a akumulátory, kterými včelaři v zimě vyhřívají úly). Zpět veze královny, které dostal výměnou, sjezdem do údolí. Původní válečná druhá etapa (ukořistěná data, útěk) zůstává odložená.
- **Zvrat při předání.** Cesta tam má působit jako rutinní zakázka. Jak křehké královny jsou, se hráč dozví až ve včelí stanici, kde je přebírá. Cesta tam tím slouží jako tutoriál (únava, pády) a cesta zpět odemkne teplotu a vitalitu roje.
- **Včely jsou podmínka přežití osady**, ne zisku: bez opylení nesklidí úrodu a nepřečká zimu.
- **Cesta tam je kratší a převážně do kopce**, hráč hodně šlape (Descenders šlapání umí, potvrzeno uživatelem). Cesta zpět je delší a převážně z kopce. Kontrast dělá ze sjezdu odměnu.
- **Z lekce 2026-10-06** ([lesson-game-proposal-2026-10-06.md](../../lesson-game-proposal-2026-10-06.md)) přebíráme katalog terénů, princip „konflikt nutí volit způsob průjezdu“ a překážky vázané na výbavu.

## Rozhodnutí po oponentuře (2026-10-10)

- **Dva ukazatele:** únava jezdce a vitalita roje. Termín je počet dní, ne ukazatel.
- **Hráč rozhoduje jen v safe zóně a na rozcestí**, mezi tím jede. Dovednost survival tlak snižuje.
- **Otevřený svět má vlastní sekci s mapou:** čtyři biomy, safe zóny, tři propojené koridory dolů, volné pořadí, průzkum.
- **Počasí jako pre-luck** (pojem z lekce): předpověď v safe zóně, vyhlídky, události viditelné předem.
- **Životy z kariéry nahrazuje vitalita roje**, pád cestou zpět stojí roj, ne jezdce.
- **Selhání bez ztráty postupu:** únava znamená odpočinek, smrt roje návrat pro náhradní královny, pozdní příjezd skromnější epilog.
- **Výbava:** tři druhy, cestou tam jeden slot, cestou zpět dva.

## Další kroky

1. Zeptat se lektora, zda projde nový open-world režim v Descenders (záloha: Riders Republic).
2. Dopsat premisu a setting.
3. Vygenerovat ilustrace v ChatGPT podle [priloha-prompty.md](priloha-prompty.md).
4. Vytvořit odevzdávaný one-pager (A4, PDF) a přílohu s AI ilustracemi a upozorněním, že jsou mimo hodnocení.
