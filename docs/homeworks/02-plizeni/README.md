# Domácí úkol č. 2 – plížení

- **Zadání:** text na stránce úkolu v Labaverse (kopii poslal uživatel 2026-10-24); doslovné znění sem nedáváme, repo je veřejné
- **Deadline:** čtvrtek 2026-10-29 do 23:59
- **Interní cíl:** odevzdat nejpozději v úterý 2026-10-27; cíl „víceméně hotovo týden předem“ (čtvrtek 2026-10-22) propadl, práce začala v sobotu 2026-10-24
- **Hodnocení:** nejvýš 20 bodů
- **Stav:** brainstorming designu
- **Branch:** `student-krato-homeworks`

## Co zadání chce

Postava se má naučit plížit: v dřepu projde prostory se sníženým stropem, umí skákat a kamera se při dřepnutí plynule přiblíží nebo oddálí, při vstávání obráceně. Odevzdává se video s ukázkou implementace; když je odevzdání odkaz, musí mít povolený přístup. Zadání výslovně připomíná designovou část: jak má plížení fungovat, proč a jaký vliv to bude mít na gameplay.

Technické tipy ze zadání:

- v projektu jsou animace `Crouch_Idle` a `Crouch_Walk` (`Content/Skvt/Characters/Animations/Crouch/`);
- crouch se musí povolit v Character Movement Component;
- skok v dřepu se povolí přetížením funkce `CanJump`;
- funkce `Crouch` a `Uncrouch` má postava k dispozici.

## Výchozí stav projektu

Po merge `upstream/stream10` (2026-10-24). Odvozeno ze jmen v assetech přes `strings`, v editoru zatím *ověřit*.

- `BP_SkvtBaseChar` má kameru z první i ze třetí osoby s přepínáním (`IA_SwapCamera`) a zoom kamery přes `TargetArmLength` spring armu (`IA_ZoomCamera`). `BP_SkvtPlayerController` drží `SavedZoomAmount` i přes výměnu postavy.
- `ABP_SkvtCharacter` má state machine se stavy Idle, Jump a Landing. Crouch zatím není v animačním blueprintu ani v postavě.

## Rozhodnutí (2026-10-24)

- **Úkol řešíme v tomhle projektu, ne v novém.** Animace, postava i cvičení z lekcí jsou tady a aktualizace kurzu se dají dál mergovat.
- **Stavíme na `upstream/stream10`**, kde jsou cvičení letošních lekcí (poslední z 2026-10-22). `upstream/main` se od 2026-09-24 nehýbe.
- **Vlastní assety jen ve složce `Content/Krato/`, assety kurzu needitujeme.** Upstream mění právě `ABP_SkvtCharacter` a `BP_SkvtBaseChar` a binární `.uasset` git neumí sloučit; při konfliktu by šlo jen vybrat jednu stranu. Proto child blueprint postavy kurzu (crouch v Character Movement, `CanJump`, kamera), kopie animačního blueprintu se stavy pro dřep a vlastní testovací level se sníženými stropy. Daň: úpravy animačního blueprintu z dalších lekcí do kopie samy nepřitečou.
- **Video do gitu nepatří** (veřejné repo bez LFS); videa v `docs/homeworks/` ignoruje `.gitignore`.

## Další kroky

1. Brainstorming designu: herní kontext, ovládání, skok v dřepu, kamera, testovací level.
2. Postup krok za krokem pro editor.
3. Implementace v `Content/Krato/`.
4. Scénář a natočení videa včetně přiznání použití AI.
5. Odevzdat v Labaverse nejpozději v úterý 2026-10-27.
