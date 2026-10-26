# AGENTS.md

## Projekt

Fork repozitáře kurzu [Game Design pro začátečníky](https://skvt.cz/course/122-game-design-pro-zacatecniky) (SKVT, podzim 2026). Unreal Engine projekt kurzu je v kořeni (`Config/`, `Content/`, `skvt_projekt.uproject`). Remote `upstream` je repozitář kurzu, `origin` je fork studenta; do `origin` se commituje a pushuje bez ptaní (fork je jen studentův, na GitHubu ale veřejný), do `upstream` nikdy. Cvičení z lekcí letošního běhu kurzu jsou ve větvi `upstream/stream10` (dřívější běhy mají `Stream6` až `Stream9`); `upstream/main` se od 2026-09-24 nehýbe.

## Domácí úkoly

- Domácí úkoly se řeší v branch `student-krato-homeworks`; `main` sleduje `upstream/main`. Novinky z lekcí se do branch úkolů dostávají merge `upstream/stream10`.
- Commity úkolů mají tvar Conventional Commits se scope úkolu, např. `docs(hw02): …`.
- Vlastní assety v Unrealu patří do `Content/Krato/`, assety kurzu se needitují: binární `.uasset` git neumí sloučit s dalšími změnami z kurzu. Změny chování se dělají v child blueprintech, upravovaný asset kurzu se zkopíruje. Před commitem práce z editoru se ověří `git status`: změny smí být jen v `Content/Krato/` a `docs/`, změna jinde v `Content/` znamená upravený asset kurzu. Výjimka: `Config/DefaultEditor.ini` přepisuje editor 5.8 sám při otevření editoru assetu (profily náhledové scény); necommituje se a vrací se `git checkout` při zavřeném editoru.
- Projekt běží v UE 5.8 (převedený z 5.5). Agent se k editoru připojuje přes oficiální experimentální MCP plugin (`ModelContextProtocol` + `AllToolsets` v `.uproject`) na `http://127.0.0.1:8765/mcp`, v Claude Code zaregistrovaný lokálně pro projekt jako `unreal`. Port je v uživatelském nastavení projektu (`Saved/`, sekce Model Context Protocol); když server neběží, spustí ho v konzoli editoru `ModelContextProtocol.StartServer 8765`. Nástroje jsou za meta-nástroji `list_toolsets`, `describe_toolset` a `call_tool` (`tool_name` je krátké jméno, např. `read_graph_dsl`). Co přes MCP jde, co ne a čím se to nahrazuje, je v `docs/unreal-mcp.md`; číst před prací v editoru. Hodnoty z `.uasset` jdou bez editoru vyčíst i z tabulky názvů a tagů vlastností (`tools/uasset_names.py <asset>`, `tools/uasset_props.py <asset> <Vlastnost>…`, heuristika ověřená na kapsli `BP_SkvtBaseChar` a na proměnné blueprintu `CrouchJumpZVelocity`); jméno v tabulce názvů ale neznamená, že objekt v assetu je (`K2Node_CallParentFunction` v ní byl i bez uzlu), existenci uzlu ověřuje MCP (`find_nodes`); co blueprint nepřepisuje, je výchozí hodnota ze zdrojáků v `/Users/Shared/Epic Games/UE_5.8/Engine/Source`.
- Zadání (PDF z lekcí) leží v `docs/homeworks/`, každý úkol má vlastní složku `docs/homeworks/NN-<téma>/` s `README.md` (zadání, deadline, rozhodnutí, další kroky).
- Odevzdávané soubory leží v `odevzdani/` ve složce úkolu a jmenují se `Kratochvil-DU<N>-…`, u více dokumentů s pořadím čtení (`Kratochvil-DU1-1-one-pager`). Dokumenty se píšou jako HTML a do PDF se převádějí přes weasyprint. Videa a surové záznamy zůstávají mimo git (`odevzdani/video/`, `*.mov` a `*.mp4` jsou v `.gitignore`).
- Zápisy z cvičení na lekcích jsou v `docs/lesson-*.md`.
- Otázky k úkolům se řeší na Discordu kurzu (server „Game design pro začátečníky“ s číslem běhu), v kategorii Úkoly-otázky má každý úkol vlastní kanál; dál stojí za kontrolu kanály s důležitými informacemi a k Unreal Engine. Agent je čte přes Discord MCP před plánováním a před odevzdáním úkolu. Do repa z nich jdou jen vlastní závěry pro plán, ne jména ani obsah zpráv (viz Veřejné repo).
- Nevybrané nápady se nemažou, ukládají se do `odlozene-napady.md` v dané složce i s podmínkou návratu.
- Použití AI je v kurzu povolené, pokud student uvede, co vytvořil s pomocí AI a co sám. Odevzdávané výstupy proto obsahují krátké věcné přiznání použití AI, ne omluvu ani žádost o vyřazení z hodnocení.

### Termíny

Úkoly se odevzdávají v Labaverse a závazný je termín na stránce úkolu tam, i s hodinou. Ústní údaj z lekce bývá přibližný: DÚ č. 1 platil do konce čtvrtka, ne do začátku lekce, a u DÚ č. 2 zaznělo „asi tři týdny“, kdežto Labaverse uvádí dva.

| Úkol | Deadline | Interní cíl | Stav |
|---|---|---|---|
| DÚ č. 1 – survival vrstva pro Descenders | čt 2026-10-15 23:59:59 | týden předem; krajně út 2026-10-13 | odevzdáno út 2026-10-13, čeká na hodnocení |
| DÚ č. 2 – plížení (video) | čt 2026-10-29 23:59 | odevzdat nejpozději út 2026-10-27 (týden předem propadl, začátek so 2026-10-24) | design schválen 2026-10-24, postup pro editor, T0 a T1 hotové 2026-10-25, T2 hotové 2026-10-26, T3 hotové 2026-10-26, T4 hotové 2026-10-26, T5 hotové 2026-10-26, následuje T6 (blueprinty staví agent přes MCP) |

## Psaní dokumentů

- Česky, s plnou diakritikou a českými uvozovkami „takto“.
- Odstavec je jeden řádek, žádné pevné zalomení uprostřed věty.
- Metadata na začátku dokumentu jako odrážkový seznam (`- **Klíč:** hodnota`).
- Tvrzení o současném stavu existující hry, která nejsou ověřená ve hře, označit *ověřit*.

## Veřejné repo

**Otevřené (2026-10-26):** zadání DÚ č. 1 (`docs/homeworks/Ukol c.1 - zadani - design dokument.pdf`) je v gitu od 2026-10-10, protože se přidalo dřív než pravidlo v `.gitignore`, které na sledované soubory nepůsobí; a README obou úkolů podle auditu parafrázují zprávy z Discordu kurzu, vzorovou práci a zadání. Autor rozhodne sám; do té doby nic z toho neodebírat ani nepřepisovat bez jeho pokynu.

Fork i repozitář kurzu jsou na GitHubu **veřejné**. Do gitu proto nepatří studijní materiály kurzu (zadání, vzorové práce; `docs/homeworks/*.pdf` je v `.gitignore`), jména ani obsah zpráv z neveřejného Discordu kurzu, ani nic, co by student nepublikoval sám.
