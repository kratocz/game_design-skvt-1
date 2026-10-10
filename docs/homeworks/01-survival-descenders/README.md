# Domácí úkol č. 1 – survival vrstva pro Descenders

- **Zadání:** [Ukol c.1 - zadani - design dokument.pdf](../Ukol%20c.1%20-%20zadani%20-%20design%20dokument.pdf), varianta *Zadání 1: Survival*
- **Deadline:** čtvrtek 2026-10-15 v 18:00 (začátek lekce), bráno jako tvrdý termín
- **Interní cíl:** víceméně hotovo týden předem (čtvrtek 2026-10-08, prošlo bez draftu); krajně nejpozději úterý 2026-10-13
- **Stav:** pracovní návrh kompletní a prošel oponenturou ([oponentura-2026-10-10.md](oponentura-2026-10-10.md)); zbývá premisa, odevzdávaný one-pager a příloha
- **Branch:** `student-krato-homeworks`

## Co zadání chce

Navrhnout survival systém pro open-world hru dle vlastního výběru. Survival prvky mají hru obohatit, ale nesmí z ní udělat survival hru. Design má zahrnout i to, jak se hráč s překážkami vypořádá. Výstup je menší formát (prezentace nebo one-pager); u vlastní hry nebo vlastního režimu se premisa a setting popisují v separátním dokumentu.

## Dokumenty

- [one-pager.md](one-pager.md) – hlavní odevzdávaný výstup: survival systém, biomy, ukazatele, protitahy
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
2. Ověřit ve hře, zda je výbava čistě kosmetická.
3. Dopsat premisu a setting.
4. Vytvořit odevzdávaný one-pager (A4, PDF) a přílohu s AI ilustracemi a upozorněním, že jsou mimo hodnocení.
