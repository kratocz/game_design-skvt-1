# Odložené nápady

- **Účel:** nápady k DÚ č. 2, které se do odevzdání nevešly; mohou se hodit u dalších úkolů
- **Zapsáno:** 2026-10-27

Ke každému je důvod odložení a podmínka, za které by se vyplatilo se k němu vrátit.

## Zvuk

- **Zvuky ve hře: kroky, běh, seskok, chycení.** Projekt nemá žádné zvuky kroků ani dopadů (Starter Content má jen vítr, oheň, výbuchy, páru, ptáky a hudbu), takže by se zvuky musely stáhnout (např. CC0 od Kenneyho) a importovat ručně, protože MCP plugin import neumí. Kroky potřebují anim notify v animacích chůze a běhu z kurzu, tedy jejich kopie a přepojení v animačním blueprintu. Záznam přes Cmd+Shift+5 navíc zvuk z Macu nenahrává, záběry by se musely přetočit jiným nahrávačem (OBS). Odhad 2–4 h, většinou poprvé. *Odloženo:* odevzdání v den nápadu a zadání hodnotí plížení, ne zvuk. *Návrat:* zadání nebo lektorka zvuk chtějí, nebo se natáčí přes OBS. Nejlevnější varianta je zvuk až ve střihu přes ffmpeg: ambientní hukot lodi pod celé video a krátký zvuk při chycení, jen ze stažených souborů bez zásahu do Unrealu, asi 30–45 min.
- **Hlasový komentář ve videu (zapsáno 2026-10-28; nakonec realizováno týž den po půlnoci, autor ho chtěl hned, postup v `nahravani-hlasu.md`).** Autor namluví přesně text titulků, titulky zůstanou: kdo nečte, poslouchá a dívá se na hru, titulky dál slouží pro přístupnost a přehrávání bez zvuku. Samotný hlas bez titulků ne, protože lektorka si text nemůže zastavit a přečíst a část diváků pouští video potichu. Práce: namluvení 11 titulků s opakováním 30–45 min autora, pak střih záběrů podle délky hlasu, vyrovnání hlasitosti a hlasová stopa místo ticha v `tools/build_video.py` asi 30 min agenta, celkem 1–1,5 h. *Odloženo:* zadání komentář uvádí jako volitelný, video s titulky autor schválil a středa před odevzdáním patří screenshotům blueprintů, přerovnání uzlů a PDF; nápad přesahuje hodinovou hranici pro pozdní nápady. *Návrat:* YouTube verze po odevzdání, nebo když se ve středu vše ostatní stihne do odpoledne a autor bude chtít.

## Vydání hry

- **Hratelná verze pro spolužáky a kamarády (nápad autora 2026-10-27).** Z Macu jde zabalit verze pro macOS (`.app`); bez podpisu a notarizace ji Gatekeeper u ostatních zablokuje a otevře se až přes pravé tlačítko → Otevřít. Verzi pro Windows Unreal z Macu nezabalí, potřebuje Windows s nainstalovaným Unrealem; Linux se křížově kompiluje jen z Windows. Android z Macu jde, ale s instalací Android SDK a NDK a bez dotykového ovládání, protože hra počítá s klávesnicí a myší. Hru hratelnou v prohlížeči jako u Godotu UE 5 oficiálně neumí (export HTML5 skončil v UE 4.24); Pixel Streaming hru jen streamuje ze serveru s grafickou kartou. Před zveřejněním ověřit licenci assetů kurzu. *Odloženo:* odevzdání má přednost. *Návrat:* po odevzdání, nejdřív verze pro macOS (odhad 1–2 h, poprvé). Tvrzení o podpoře platforem jsou z obecné znalosti UE, *ověřit* v dokumentaci UE 5.8.
