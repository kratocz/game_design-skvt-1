# DÚ č. 2 – postup pro editor

- **Datum:** 2026-10-24
- **Spec:** [README.md](README.md), sekce Design (schválená 2026-10-24)
- **Kdo co dělá:** od 2026-10-25 staví blueprinty T1–T4 (a podle možností blockout T5) agent přes MCP plugin editoru (viz `AGENTS.md`); autor je kontroluje, ukládá a testuje v Play. Kroky níže zůstávají jako specifikace a záložní postup, kdyby zápis přes MCP nefungoval. Agent po každém úkolu zkontroluje `git status`, commitne, řeší problémy a dělá titulky, střih a PDF
- **Engine:** Unreal Engine 5.8. Projekt kurzu je z 5.5 a 2026-10-25 se převedl na místě (Convert in-place), protože na Macu je nainstalovaná jen 5.8. Postup a oponentura počítaly s 5.5; kde se editor 5.8 liší, zapíše se to do Zjištění. Hláška o nenalezeném `StarterContent.upack` při otevření je neškodná: `Config/DefaultGame.ini` kurzu chce Starter Content importovat, ten už ale v `Content/StarterContent` je.
- **Kontrola:** 2026-10-24 oponentura v čistém kontextu hledala neplatná tvrzení o UE 5.5: 0 blokujících, 8 zdržujících a 12 kosmetických nálezů, všechny zapracované. Potvrdila, že přetížení Can Jump na skok v dřepu stačí, že postava zůstane v dřepu i ve vzduchu a že vyrovnání výšky kamery sedí. Tvrzení o vnitřku enginu stojí na dokumentaci Epicu a fórech, ne na zdrojovém kódu.

**Cíl:** postava kurzu, která se plíží podle spec, testovací level s mimozemšťanem a podklady pro video i PDF.

**Architektura:** vlastní child blueprint postavy kurzu (`BP_KratoCharacter`) nese ovládání dřepu, skok v dřepu a kameru. Kopie animačního blueprintu kurzu přidává pózu dřepu přes Blend Poses by bool. Vlastní level spouští vlastní GameMode. Mimozemšťan je child NPC kurzu s vlastním AI controllerem a behavior tree. Nic z kurzu se neupravuje.

## Globální pravidla

Platí pro každý úkol.

- **Vlastní assety jen v `Content/Krato/`.** Assety kurzu se jen čtou a odkazují. Neukládat je, ani když je editor po otevření označí jako změněné.
- **Neukládat přes Save All naslepo.** V dialogu ukládání odškrtnout všechno mimo `Content/Krato/`. Před každým commitem musí `git status` ukazovat změny jen v `Content/Krato/` a `docs/`. Když se objeví změna v `Content/Skvt/`, `Config/` nebo jinde, necommitovat a ozvat se.
- **Názvy:** blueprinty `BP_Krato…`, animační blueprint `ABP_Krato…`, mapa `L_Plizeni`, vstupy `IA_…` a `IMC_Krato`.
- **Hodnoty ze spec:** násobek kamery v dřepu 0,6, přechod kamery 0,3 s, rychlost v dřepu zhruba polovina chůze, mimozemšťan vidí stojícího hráče na 15 m a hráče v dřepu na 5 m. Všechno jsou *cíle ladění*.
- **Po každé změně blueprintu Compile a Save** (jen ten asset).
- **Pivot BSP boxu je uprostřed:** Location Z = výška spodní hrany + polovina Z z Brush Settings (strop se spodní hranou 150 a výškou 100 má Z = 200). Platí i pro subtractive boxy. Jednou ověřit, že horní plocha podlahy v levelu Basic je v Z = 0.
- **Prohlížení kolize při Play:** F8 uvolní myš a vrátí editorový viewport, tam Show → Collision (Alt+C); další F8 vrátí ovládání. Nebo v konzoli příkaz `show collision`.
- **Ctrl na Macu:** Ctrl+mezerník přepíná vstupní zdroj (klávesnici). Dřep je přepínač, takže Ctrl stačí stisknout a pustit; poskok testovat raději s C.
- **Commit po každém úkolu:** napiš „commit Tn“, agent zkontroluje `git status`, přidá soubory jednotlivě a commitne.
- **Videa a surové záznamy mimo git:** ukládat do `docs/homeworks/02-plizeni/odevzdani/video/`, které `.gitignore` ignoruje.

## Na co si dát pozor (testy jsou v uvedených úkolech)

1. **Neuložené nebo omylem uložené assety kurzu** po otevření a kompilaci. Řeší kontrola `git status` v každém úkolu.
2. **Child blueprint nesmí přebít logiku kurzu:** zoom a přepnutí kamery jsou vstupní události v `BP_SkvtBaseChar`, mapování vstupů přidává `BP_SkvtPlayerController`. Test v T1: zoom a přepnutí kamery musí fungovat dál.
3. **Rychlé opakované přepínání dřepu nebo zoom kolečkem během přechodu** nesmí rozhodit vzdálenost kamery. Test v T4.
4. **Vstávání na okraji nízkého stropu,** kdy je postava napůl pod ním: vstát nesmí a nesmí ani vstát sama později. Jakmile se `UnCrouch` zavolá a engine ho odmítne, zkouší postavu postavit sám dál a blueprint to zrušit neumí; `CanStandUp` proto musí být aspoň tak přísné jako engine. Test v T1.
5. **Dřep se ve vzduchu nepřepíná:** stisk C ve vzduchu se ignoruje. Jinak by se do ventilace dalo dostat skokem ve stoje a dřepnutím ve vzduchu (kapsle se ve vzduchu zmenšuje kolem středu, nohy vyskočí o 36 cm výš) a kamera by při přechodu ve vzduchu škubala. Test v T1.

## Naměřené hodnoty

Vyplnit v T0 z `BP_SkvtCharacterMale` (Capsule Component a Character Movement); vybraná postava pro video může být i Female, rozměry kapsle by měly být stejné.

| Veličina | Kde v Details | Hodnota |
|---|---|---|
| Stand half height (SHH) | Capsule Component → Capsule Half Height | 90 |
| Poloměr kapsle (R) | Capsule Component → Capsule Radius | 35 |
| Max Walk Speed | Character Movement | 500 |
| Jump Z Velocity | Character Movement | 700 |
| Gravity Scale | Character Movement | 1,75 |
| Max Step Height | Character Movement | 45 (výchozí enginu) |
| Crouched Half Height (CHH) | Character Movement, nastavíme v T2 | 70 (T2: podle hlavy při chůzi v dřepu, viz Zjištění T2; výchozí enginu 40) |

Odvozené rozměry levelu (vzorce platí vždy, příklad počítá s SHH 96, R 42, CHH 60, Max Step Height 45, Gravity Scale 1,75):

| Rozměr | Vzorec | Příklad |
|---|---|---|
| Výška ve stoje H_s | 2 × SHH | 192 cm |
| Výška v dřepu H_c | 2 × CHH | 120 cm |
| Nízký strop L (traverza, ventilace) | H_c + 20 ≤ L ≤ H_s − 30 | 150 cm |
| Šířka ventilace | 2 × R + 30, zaokrouhlit nahoru | 114 → 120 cm |
| Práh vstupu do ventilace S | ≥ Max Step Height + 15 | 65 cm |
| Výška poskoku h_c | ≥ S + 15 a zároveň h_c + H_c ≤ S + L | 80 cm |
| Crouch Jump Z Velocity | √(2 × 980 × Gravity Scale × h_c) | 524 |
| Výška beden C | H_c + 10 ≤ C ≤ H_s − 40 | 140 cm |

## Odhad času

Odhad je pro první setkání s tímhle typem práce v Unrealu, proto široký: T0 0,5–1 h, T1 1–1,5 h, T2 1–1,5 h, T3 0,5 h, T4 1–1,5 h, T5 2–3 h, T6 1–1,5 h, T7 2–4 h, T8 2–3 h; celkem 11–17,5 h.

Skutečnost (podle začátku session a commitů, blueprinty stavěl agent přes MCP): T1 asi 30 min (2026-10-25 23:06–23:35), T2 asi 1 h 35 min (23:35–01:08, včetně měření výšky hlavy a opravy chodidel nad podlahou); dohromady asi 2 h proti odhadu 2–3 h.

**Rozhodovací pravidla (platí předem, ne podle výsledku):**

- Pokud T1 až T6 nejsou hotové v pondělí 2026-10-26 ve 23:59 (hodinu upřesnil autor 2026-10-26), T7 se škrtá a odevzdává se záložní verze (mimozemšťan jen jako hlídka bez reakce, v PDF popsané, co chybí).
- Pokud T7 nefunguje v úterý 2026-10-27 v 18:00, odevzdává se záložní verze a rozpracovaný T7 se popíše v PDF i s blueprinty (lektorka výslovně stojí o to, co se nepovedlo).

---

### T0: Ověřit výchozí stav v editoru

**Výstup:** vyplněná tabulka Naměřené hodnoty a odpovědi na pět otázek níže, zapsané v sekci Zjištění na konci tohoto souboru (zapíše agent podle tvé zprávy).

- [ ] **Krok 1:** Otevřít projekt v UE 5.8 (Project Browser → Browse… → `skvt_projekt.uproject`, u dialogu o jiné verzi More Options → Convert in-place). Při prvním otevření editor dlouho kompiluje shadery.
- [ ] **Krok 2:** Spustit `Content/Skvt/SkvtProjectMap` (Play). Ověřit a poznamenat: funguje zoom kolečkem, přepnutí první/třetí osoby, objeví se po startu menu (cvičení UI)?
- [ ] **Krok 3:** Otevřít `BP_SkvtBaseChar`, Event Graph, najít událost `IA_ZoomCamera` a funkci `SetCamera3rdPerson`. Zjistit a poznamenat:
  - nastavuje zoom `TargetArmLength` jednorázově na vstup, nebo ho průběžně dorovnává (Event Tick, Timeline, FInterp)?
  - počítá novou hodnotu z aktuální `TargetArmLength` (relativně), nebo z proměnné `SavedZoomAmount` (absolutně)?
  - mění `SetCamera3rdPerson` při přepnutí pohledu `TargetArmLength` nebo polohu `CameraBoom`?
  - minimum a maximum zoomu (uzel `FClamp`).

  **Rozhodovací pravidlo:** jednorázové relativní nastavení a přepnutí pohledu, které rameno nepřepisuje → T4 podle plánu. Průběžné dorovnávání, absolutní zoom ze `SavedZoomAmount` nebo přepnutí pohledu, které přepisuje rameno → T4 použije záložní variantu (posun kamery po rameni, krok 6).
- [ ] **Krok 4:** V `BP_SkvtBaseChar`, panel Components: pod čím visí `1stPersonCamera`? Pod meshem (socket hlavy) → v T4 se pro první osobu nic nedělá; pod kapslí → v T4 se vyhlazuje i její výška.
- [ ] **Krok 5:** Otevřít `Content/Skvt/Characters/Input/IMC_Default`, `IMC_SkvtInput` a `IMC_SwapPawn`: je někde použitá klávesa C nebo levý Ctrl? Pokud ano, dřep dostane jen levý Ctrl (a gamepad).
- [ ] **Krok 6:** Otevřít `Content/Skvt/Characters/NPC/BehaviorTrees/BP_NPC_BT_base`: jaký má AI Controller Class, mesh a Anim Class a co dělá jeho Event Graph (útok, pronásledování)? Poznamenat.
- [ ] **Krok 7:** Otevřít `BP_SkvtCharacterMale`, vybrat Capsule Component a Character Movement a vyplnit tabulku Naměřené hodnoty.
- [ ] **Krok 8:** Zavřít editor bez ukládání čehokoli. Agent ověří `git status` (čekáme čistý strom).

---

### T1: Postava, vstup a dřep přepínačem

**Soubory (nové):**
- `Content/Krato/Input/IA_Crouch`
- `Content/Krato/Input/IMC_Krato`
- `Content/Krato/Characters/BP_KratoCharacter` (rodič `BP_SkvtCharacterMale` nebo `BP_SkvtCharacterFemale`)
- `Content/Krato/Characters/BP_KratoGameMode` (rodič `BP_SkvtGameMode`)
- `Content/Krato/Maps/L_Plizeni`

**Rozhraní pro další úkoly:**
- proměnné v `BP_KratoCharacter`: `StandHalfHeight` (float), `StandJumpZVelocity` (float), `BaseBoomZ` (float);
- funkce `CanStandUp` → bool.

- [ ] **Krok 1: Složky.** V Content Browseru vytvořit `Content/Krato/` s podsložkami `Input`, `Characters`, `Animations`, `Maps`, `AI`.
- [ ] **Krok 2: Input Action.** V `Krato/Input`: pravým → Input → Input Action → `IA_Crouch`, Value Type **Digital (bool)**, bez triggerů.
- [ ] **Krok 3: Mapping Context.** Pravým → Input → Input Mapping Context → `IMC_Krato`. Mapování `IA_Crouch` na **C** (pokud je v T0 volné), **Left Ctrl** a **Gamepad Face Button Right**.
- [ ] **Krok 4: Postava.** V `Krato/Characters`: pravým → Blueprint Class → All Classes → `BP_SkvtCharacterMale` (nebo Female) → `BP_KratoCharacter`. Vytvořit přímo tady, ne v kurzu a pak přesouvat (přesun nechá v kurzu redirector).
- [ ] **Krok 5: Character Movement v `BP_KratoCharacter`.** Vybrat komponentu Character Movement, do hledání v Details psát a nastavit:
  - `Can Crouch` ✓ (Nav Movement → Movement Capabilities)
  - `Can Walk Off Ledges When Crouching` ✓ (výchozí je vypnuto; podle spec postava z hrany spadne)
  - `Crouched Half Height` a `Max Walk Speed Crouched` zatím nechat, doladí se v T2.
- [ ] **Krok 6: Proměnné.** V My Blueprint přidat float proměnné `StandHalfHeight`, `StandJumpZVelocity`, `BaseBoomZ`.
- [ ] **Krok 7: Event BeginPlay s voláním rodiče.** Do Event Graphu přidat Event BeginPlay, pravým na něj → **Add Call to Parent Function** a napojit jako první. Postavy kurzu teď vlastní BeginPlay podle jmen v assetech nemají, ale kdyby ho kurz v další lekci přidal, bez volání rodiče by se nespustil.

```
Event BeginPlay
 → Parent: BeginPlay
 → Set StandHalfHeight = CapsuleComponent.Get Unscaled Capsule Half Height
 → Set StandJumpZVelocity = CharacterMovement.Jump Z Velocity
 → Set BaseBoomZ = CameraBoom.Get Relative Location → Break Vector → Z
 → Get Controller → Cast To PlayerController
 → Get Enhanced Input Local Player Subsystem (Player Controller)
 → Add Mapping Context (Mapping Context: IMC_Krato, Priority: 1)
```

- [ ] **Krok 8: Funkce `CanStandUp`.** My Blueprint → Functions → + → `CanStandUp`, výstup Return Value typu bool. Táhne kouli s plným poloměrem kapsle od středu postavy nahoru, až horní okraj koule sahá o 1 cm výš než temeno stojící postavy. Musí být aspoň tak přísná jako engine: když `UnCrouch` zavoláme a engine ho odmítne, postava by pak vstala sama, jakmile bude místo (viz bod 4 nahoře).

```
R      = CapsuleComponent.Get Scaled Capsule Radius
Start  = Get Actor Location
EndZ   = StandHalfHeight × 2 − CapsuleComponent.Get Scaled Capsule Half Height − R + 1
End    = Start + Make Vector(0, 0, EndZ)
Sphere Trace By Channel (Start, End, Radius: R, Trace Channel: Visibility,
                         Ignore Self ✓, Draw Debug Type: For Duration)
Return Value = NOT (Sphere Trace.Return Value)
```

Draw Debug Type nechat na For Duration při testech, před natáčením přepnout na None. Kdyby u stěny nešlo vstát, i když nad hlavou nic není, zmenšit poloměr na R − 0,5, nikdy víc.

- [ ] **Krok 9: Přepínač dřepu.**

```
IA_Crouch (Started)
 → Branch (CharacterMovement.Is Falling)
     True  → (nic – ve vzduchu se dřep nepřepíná)
     False → Branch (Is Crouched)
               False → Crouch
               True  → Branch (CanStandUp)
                         True  → UnCrouch
                         False → (nic – postava zůstane v dřepu)
```

- [ ] **Krok 10: GameMode.** V `Krato/Characters`: Blueprint Class → All Classes → `BP_SkvtGameMode` → `BP_KratoGameMode`, v Class Defaults **Default Pawn Class = `BP_KratoCharacter`**.
- [ ] **Krok 11: Testovací level.** File → New Level → **Basic** → Save As `Content/Krato/Maps/L_Plizeni`. Window → World Settings → **GameMode Override = `BP_KratoGameMode`**. Ve World Outlineru nechat jen jeden Player Start (pokud ho Basic level už má, nepřidávat další, jinak je místo startu náhodné). Přidat jeden „nízký strop“ pro test: Place Actors → Geometry → Box, Brush Settings X 300, Y 300, Z 100, Location Z = 200 (spodní hrana 150 cm nad podlahou, pivot je uprostřed).
- [ ] **Krok 12: Test.** Play v `L_Plizeni`, kolizi zobrazit přes F8 a Show → Collision nebo `show collision` (je vidět kapsle). Očekávání:
  - C / Ctrl přepíná dřep, kapsle se zmenší a zvětší (mesh je zatím ve stoje, póza přijde v T2);
  - pod boxem stisk C / Ctrl nic neudělá, postava zůstane v dřepu; po vylezení ven vstane na další stisk;
  - **okraj stropu (bod 4 v sekci Na co si dát pozor):** postava napůl pod boxem → vstát nejde; po popojití ven vstane až na stisk, ne sama. Projít okraj několikrát s opakovaným mačkáním C;
  - **u stěny:** přitisknout se ke stěně, dřepnout a vstát → musí jít;
  - **ve vzduchu (bod 5):** skočit a během skoku stisknout C → nic se nestane;
  - **logika kurzu (bod 2):** zoom kolečkem a přepnutí první/třetí osoby fungují jako v T0;
  - debug koule `CanStandUp`: celá červená = nad hlavou volno, červená a za místem zásahu zelená = něco je v cestě.
- [ ] **Krok 13: Uložit jen assety z `Content/Krato/`, napsat „commit T1“.** Zpráva commitu: `feat(hw02): postava s dřepem na přepínač`.

---

### T2: Póza dřepu v animacích

**Soubory:**
- nový `Content/Krato/Animations/BS_CrouchMove` (Blend Space 1D)
- nový `Content/Krato/Animations/ABP_KratoCharacter` (kopie `ABP_SkvtCharacter`)
- úprava `Content/Krato/Characters/BP_KratoCharacter`

**Rozhraní:** proměnné v `ABP_KratoCharacter`: `IsCrouching` (bool), `CrouchSpeed` (float).

- [ ] **Krok 1: Blend space.** V `Krato/Animations`: pravým → Animation → Blend Space 1D (v některých verzích pod Animation → Legacy) → skeleton `SK_Mannequin` → `BS_CrouchMove`. Horizontal Axis: název `Speed`, Minimum 0, Maximum 300. Vložit `Crouch_Idle` na 0 a `Crouch_Walk` na 300 (obojí z `Content/Skvt/Characters/Animations/Crouch/`). Uložit.
- [ ] **Krok 2: Kopie animačního blueprintu.** Přetáhnout `Content/Skvt/Characters/Animations/ABP_SkvtCharacter` na složku `Krato/Animations` ve stromu složek → **Copy Here** (ne Move) → přejmenovat na `ABP_KratoCharacter`.
- [ ] **Krok 3: Proměnné v kopii.** V `ABP_KratoCharacter` přidat `IsCrouching` (bool) a `CrouchSpeed` (float). Na konec existujícího Event Blueprint Update Animation, kde se už čte postava a rychlost, doplnit:

```
(existující reference na postavu z Try Get Pawn Owner / Cast)
 → Set IsCrouching = <postava>.Is Crouched
 → Set CrouchSpeed = Select Float (Pick A: IsFalling)
                       True  → 0                       (ve vzduchu držet Crouch_Idle)
                       False → <existující rychlost na zemi>
```

Pokud update neumí „IsFalling“ nebo rychlost, vzít `Character Movement → Is Falling` a `Vector Length XY (Get Velocity)`.

- [ ] **Krok 4: AnimGraph.** Najít, kam vede výstup state machine `Main`. Mezi ni a další uzel vložit **Blend Poses by bool**:

```
Blend Poses by bool
  Active Value     = IsCrouching
  True Pose        = BS_CrouchMove (Speed = CrouchSpeed)
  False Pose       = Main (state machine)
  True Blend Time  = 0.2
  False Blend Time = 0.2
 → (uzel, kam vedl Main dosud, např. Output Pose)
```

Proč ne nový stav ve state machine: přechody by bylo třeba napojit ke každému stavu a skok by se musel blokovat v dřepu zvlášť; blend za state machine drží pózu dřepu i ve vzduchu bez dalšího kódu.

- [ ] **Krok 5: Napojit na postavu.** V `BP_KratoCharacter` vybrat Mesh → Anim Class = `ABP_KratoCharacter`.
- [ ] **Krok 6: Výška dřepu podle pózy.** Play, dřepnout, F8, ve World Outlineru vybrat postavu → Character Movement → `Crouched Half Height`, Show → Collision. Hodnotu měnit (pak F8, vstát a znovu dřepnout), až horní okraj kapsle sedí asi 5 cm nad hlavou v póze `Crouch_Idle`; výchozí 40 bývá málo. Změny na běžící instanci se po Stop ztratí: nalezenou hodnotu zapsat do `BP_KratoCharacter` a do tabulky Naměřené hodnoty.
- [ ] **Krok 7: Rychlost.** Nastavit `Max Walk Speed Crouched` zhruba na polovinu `Max Walk Speed`, stejné číslo dát jako Maximum osy v `BS_CrouchMove` a vzorek `Crouch_Walk` přesunout na nové maximum. Doladit tak, aby nohy při chůzi v dřepu neklouzaly.
- [ ] **Krok 8: Test.** Očekávání: přechod do dřepu a zpět je plynulý (0,2 s), v dřepu stání = `Crouch_Idle`, chůze = `Crouch_Walk`, hlava v dřepu neprochází boxem z T1, ve stoje se nic nezměnilo (běh, skok, dopad jako dřív).
- [ ] **Krok 9: Uložit jen `Content/Krato/`, napsat „commit T2“.** Zpráva: `feat(hw02): póza dřepu v kopii animačního blueprintu`.

---

### T3: Nízký poskok v dřepu

**Soubory:** úprava `Content/Krato/Characters/BP_KratoCharacter`

**Rozhraní:** proměnná `CrouchJumpZVelocity` (float, Instance Editable, výchozí podle tabulky, příklad 524).

- [ ] **Krok 1: Proměnná.** Přidat `CrouchJumpZVelocity` (float), výchozí hodnota z tabulky Odvozené rozměry podle tvé Gravity Scale.
- [ ] **Krok 2: Přetížit Can Jump.** My Blueprint → Functions → Override → **Can Jump** (v C++ `CanJumpInternal`). Výchozí verze v dřepu vrací false.

```
Can Jump
 → Branch (Is Crouched)
     True  → Return (CharacterMovement.Is Moving On Ground)
     False → Return (Parent: Can Jump)
```

- [ ] **Krok 3: Výška skoku podle dřepu.** Přidat Event On Start Crouch a Event On End Crouch (pravým do grafu, hledat „On Start Crouch“). V T4 na ně navážeme kameru, proto zatím jen:

```
Event On Start Crouch → CharacterMovement.Set Jump Z Velocity = CrouchJumpZVelocity
Event On End Crouch   → CharacterMovement.Set Jump Z Velocity = StandJumpZVelocity
```

- [ ] **Krok 4: Test.** Do levelu dočasně přidat Box 200 × 200 × 65 (práh S), Location Z = 32,5. Očekávání:
  - ve stoje skok jako dřív; v dřepu nižší poskok a postava zůstane v dřepu i ve vzduchu (póza drží);
  - z dřepu se poskokem dostane na box výšky S, chůzí ne (Max Step Height je nižší);
  - pod nízkým boxem z T1 poskok narazí hlavou do stropu, ale nevstane;
  - po vstání je skok znovu plný.
- [ ] **Krok 5: Uložit, napsat „commit T3“.** Zpráva: `feat(hw02): nízký poskok v dřepu`.

---

### T4: Kamera při dřepu

**Soubory:** úprava `Content/Krato/Characters/BP_KratoCharacter`

**Rozhraní:** proměnné `CrouchArmFactor` (float, 0.6), `PlayerArm`, `CamFromArm`, `CamToArm`, `CamFromZ` (float), případně `Base1PZ` (float, krok 5); Timeline `TL_CrouchCamera` s float stopou `Alpha`.

Vzdálenost kamery se mění jen během přechodu, takže zoom kolečkem z kurzu v dřepu funguje dál. `PlayerArm` drží vzdálenost, kterou chce hráč ve stoje, a mění se jen mimo přechod; proto ani rychlé přepínání nerozhodí vzdálenost. Výška se vyrovnává o tolik, o kolik se při dřepu posune kapsle (`Scaled Half Height Adjust`), počítáno od aktuálního posunu, takže přechod přerušený v půlce navazuje bez skoku. Dřep se přepíná jen na zemi (T1), kde kapsle drží spodek na podlaze a střed se posouvá právě o tuto hodnotu.

- [ ] **Krok 1: Proměnné a Timeline.** Přidat float proměnné výše (`CrouchArmFactor` výchozí 0.6). Pravým do grafu → Add Timeline → `TL_CrouchCamera`; uvnitř + Float Track `Alpha`, klíče (0, 0) a (0.3, 1), oba klíče pravým → Auto (plynulý průběh), Length 0.3.
- [ ] **Krok 2: Start dřepu.** Navázat za uzel z T3:

```
Event On Start Crouch (Half Height Adjust, Scaled Half Height Adjust)
 → (Set Jump Z Velocity z T3)
 → Branch (NOT TL_CrouchCamera.Is Playing)
     True → Set PlayerArm = CameraBoom.Target Arm Length
 → Set CamFromArm = CameraBoom.Target Arm Length
 → Set CamToArm   = PlayerArm × CrouchArmFactor
 → Set CamFromZ   = (CameraBoom.Relative Location.Z − BaseBoomZ) + Scaled Half Height Adjust
 → TL_CrouchCamera: Play from Start
```

Do `Set CamFromArm` napojit oba výstupy větve: True až za `Set PlayerArm`, False rovnou. Když se napojí jen True, přerušený přechod nic neudělá.

- [ ] **Krok 3: Konec dřepu.** Větev zapojit stejně jako v kroku 2.

```
Event On End Crouch (Half Height Adjust, Scaled Half Height Adjust)
 → (Set Jump Z Velocity z T3)
 → Branch (NOT TL_CrouchCamera.Is Playing)
     True → Set PlayerArm = CameraBoom.Target Arm Length / CrouchArmFactor
 → Set CamFromArm = CameraBoom.Target Arm Length
 → Set CamToArm   = PlayerArm
 → Set CamFromZ   = (CameraBoom.Relative Location.Z − BaseBoomZ) − Scaled Half Height Adjust
 → TL_CrouchCamera: Play from Start
```

- [ ] **Krok 4: Průběh přechodu.**

```
TL_CrouchCamera (Update, Alpha)
 → CameraBoom.Set Target Arm Length = Lerp (CamFromArm, CamToArm, Alpha)
 → CameraBoom.Set Relative Location =
       Make Vector (původní X, původní Y, BaseBoomZ + Lerp (CamFromZ, 0, Alpha))
```

Původní X a Y vzít z Break Vector aktuální relativní polohy CameraBoom.

- [ ] **Krok 5: První osoba (jen pokud v T0 visí `1stPersonCamera` pod kapslí).** V BeginPlay uložit její výchozí relativní Z do `Base1PZ` a v Update stejně nastavovat její relativní Z na `Base1PZ + Lerp (CamFromZ, 0, Alpha)`. Pokud visí pod meshem, nic nedělat: hlava klesá s animací sama.
- [ ] **Krok 6: Záložní varianta (jen pokud pravidlo v T0 kroku 3 ukázalo na ni).** `TargetArmLength` nechat kurzu a místo `Set Target Arm Length` v kroku 4 posouvat kameru po rameni: `3rdPersonCamera.Set Relative Location X = Lerp (FromX, ToX, Alpha)`, kde pro start dřepu FromX = aktuální X a ToX = `CameraBoom.Target Arm Length × (1 − CrouchArmFactor)`, pro konec dřepu ToX = 0. `PlayerArm` se v této variantě nepoužívá. Výška zůstává podle kroků 2–4. Daň: když hráč v dřepu zazoomuje, je vzdálenost „hráčův zoom minus pevný posun“, ne přesně 60 %.
- [ ] **Krok 7: Test.** Očekávání:
  - dřep: kamera za 0,3 s plynule přijede blíž a níž, vstání: plynule zpět, žádný skok výšky;
  - pod nízkým boxem kamera nenaráží do stropu víc, než musí (spring arm ji případně přitáhne, ale bez škubání);
  - **zoom v dřepu (bod 3):** v dřepu odzoomovat kolečkem, vstát → vzdálenost ve stoje odpovídá novému zoomu (dřep × 1/0,6), bez skoku; v záložní variantě jen bez skoku;
  - **rychlé přepínání (bod 3):** desetkrát rychle za sebou C, pak počkat → vzdálenost ve stoje je stejná jako na začátku;
  - **přepnutí pohledu v dřepu:** z třetí osoby do první a zpět → kamera neskočí na vzdálenost ve stoje;
  - **poskok:** v dřepu skočit → kamera drží výšku dřepu, neškubne;
  - první osoba: přepnout pohled, dřepnout → výška očí plynule klesne, žádný zoom.
- [ ] **Krok 8: Uložit, napsat „commit T4“.** Zpráva: `feat(hw02): plynulé přiblížení a snížení kamery při dřepu`.

---

### T5: Testovací level (blockout)

**Soubory:** úprava `Content/Krato/Maps/L_Plizeni`

**Platí od T2 (2026-10-26):** rozměry se berou ze Zjištění T2, ne z příkladu v tabulce Odvozené rozměry ani z čísel níže: strop ventilace a traverzy L = 165 cm, bedny C = 150 cm, šířka ventilace 100 cm, práh S 60 cm. Přes MCP se BSP vytvořit nedá, geometrie se staví z kostek `/Engine/BasicShapes/Cube` (pivot uprostřed, viz `docs/unreal-mcp.md`).

Geometrie z Geometry → Box (BSP, rozměry přesně v Brush Settings), otvory přes Box s Brush Type **Subtractive**. Rozměry z tabulky Odvozené rozměry; čísla níže jsou příklad. Testovací boxy z T1 a T3 smazat.

```
 [1 Sklad 8×6 m] ─dveře─ [2 Křižovatka] ─roh─ [3a Hlavní chodba 25×4 m, hlídka] ─ [5 Strojovna]
   propadlý strop            │ okno do chodby          ║ mřížky ve stěně
   3 m dlouhý, L nad zemí    └─ vstup do ventilace ─ [3b Ventilace podél chodby] ─ výstup (4) do chodby
                                práh S, nasvícený        šířka 120, strop L         za koncem hlídky
```

- [ ] **Krok 1: Sklad.** Místnost 800 × 600 × 400 cm, dveře 200 × 300 cm do křižovatky. Před dveřmi propadlý strop přes celou šířku místnosti, 300 cm dlouhý, spodní hrana ve výšce L, aby se k dveřím dalo jen v dřepu. Player Start na opačném konci skladu.
- [ ] **Krok 2: Křižovatka.** Krátká chodba kolmo k hlavní chodbě. Ve stěně do hlavní chodby okno (subtractive box ve výšce očí), aby byla hlídka vidět dřív, než do chodby hráč vstoupí. Za rohem, odkud hlídka nevidí, Target Point s tagem **`Checkpoint`** (Details → Actor → Tags).
- [ ] **Krok 3: Hlavní chodba.** 2500 × 400 × 400 cm, dobře osvětlená (signposting z lekce 2026-10-20). Bedny výšky C jako kryt, rozestavěné tak, aby se mezi nimi dalo v dřepu proplížit. Na konci dveře do strojovny.
- [ ] **Krok 4: Ventilace.** Vstup z křižovatky: otvor ve stěně s prahem S nad podlahou a výškou L. Uvnitř tunel šířky 120 cm a výšky L, vedený za boční stěnou hlavní chodby, ve stěně směrem do chodby několik mřížek (otvory nebo mezery mezi boxy), skrz které je vidět hlídka. Do každého otvoru dát `Content/StarterContent/Shapes/Shape_Cube` naškálovanou na tenkou desku, Collision Preset **BlockAll** a zaškrtnuté **Actor Hidden In Game**: hráč otvorem vidí, paprsek mimozemšťana ne, takže ventilace zůstane bezpečná, jak chce spec. Výstup do hlavní chodby za koncem hlídkové trasy, kousek před strojovnou.
- [ ] **Krok 5: Strojovna.** Malá místnost; u dveří žluté světlo (podle lekce strojovna jako jediná žlutá místnost na mapě).
- [ ] **Krok 6: Světla.** Hlavní chodba jasně, ventilace šero, nasvícená mříž vstupu do ventilace (barevný Spot Light), žluté světlo u strojovny.
- [ ] **Krok 7: NavMesh a hlídka.** Place Actors → Volumes → **Nav Mesh Bounds Volume** jen přes hlavní chodbu (klávesa P ukáže zelenou navigační síť). Mimozemšťan tak za hráčem nevyjde z chodby a útěk za roh na křižovatku, kde je checkpoint, je bezpečný. Ověřit, že síť nezasahuje do ventilace. Dva Target Pointy pro hlídku na koncích trasy (zhruba 15 m od sebe, konec trasy pár metrů před výstupem z ventilace).
- [ ] **Krok 8: Test průchodu.** Očekávání: ze skladu se ke dveřím dostaneš jen v dřepu; do ventilace jen poskokem v dřepu, ve stoje ani chůzí ne; ventilací se projde až do hlavní chodby; ve ventilaci ani pod propadlým stropem nejde vstát; chodbou se dojde do strojovny. Obě cesty projít celé.
- [ ] **Krok 9: Uložit, napsat „commit T5“.** Zpráva: `feat(hw02): blockout úseku lodi pro plížení`.

---

### T6: Záložní video a screenshoty blueprintů

**Soubory:** `docs/homeworks/02-plizeni/odevzdani/blueprinty/*.png` (v gitu), surové záznamy do `odevzdani/video/` (mimo git)

- [ ] **Krok 1: Komentáře v grafech.** V `BP_KratoCharacter` a `ABP_KratoCharacter` označit logické celky a stisknout C (komentářový blok) s krátkým názvem česky: „Přepínač dřepu“, „Smí vstát?“, „Skok v dřepu“, „Kamera při dřepu“, „Póza dřepu“. `CanStandUp`: Draw Debug Type na None.
- [ ] **Krok 2: Screenshoty.** Každý celek zvlášť: graf přes celou obrazovku, zoom tak, aby byl text čitelný, Cmd+Shift+4. Uložit jako `odevzdani/blueprinty/01-prepinac-drepu.png` atd. (pořadí podle titulků). Plus Details Character Movement s nastavením dřepu.
- [ ] **Krok 3: Nastavit záznam.** Editor Preferences → Level Editor → Play → New Window Size 1920 × 1080, Play in New Editor Window. Před záznamem v konzoli `DisableAllScreenMessages`.
- [ ] **Krok 4: Natočit záběry** (Cmd+Shift+5 → Record Selected Portion na okno hry, bez zvuku), každý záběr zvlášť a mechaniku držet aspoň 7 s:
  1. úvodní pohled na hlavní chodbu s hlídkou;
  2. dřep a vstání ve skladu (titulek 2);
  3. detail kamery při dřepu a vstání (titulek 3);
  4. pokus vstát pod propadlým stropem (titulek 4);
  5. poskok do ventilace (titulek 5);
  6. chůze v dřepu (titulek 6);
  7. chodba versus ventilace z křižovatky (titulek 8).
- [ ] **Krok 5: Agent sestaví záložní video** ze záběrů a screenshotů s titulky (`ffmpeg-full` s libass doinstaluje přes brew) a pošle ho k zhlédnutí.
- [ ] **Krok 6: Rozhodnutí o hlasu.** Po zhlédnutí záložního videa: zůstávají titulky, nebo nahráváš hlasový komentář? Zapsat do README.
- [ ] **Krok 7: Napsat „commit T6“** (screenshoty). Zpráva: `docs(hw02): screenshoty blueprintů a záložní video`.

---

### T7: Mimozemšťan

**Soubory (nové v `Content/Krato/AI/`):** `BB_KratoAlien`, `BT_KratoAlien`, `AIC_KratoAlien`, `BP_KratoAlien` (rodič `BP_NPC_BT_base`), `BTS_DetectPlayer`, `BTT_NextPatrolPoint`, `BTT_CatchPlayer`; úprava `BP_KratoCharacter` (událost `CaughtByAlien`) a `L_Plizeni`.

**Rozhraní:**
- Blackboard klíče: `TargetActor` (Object, Base Class Actor), `PatrolLocation` (Vector);
- `BP_KratoAlien`: `PatrolPoints` (pole Actor, Instance Editable), `PatrolIndex` (int);
- `BP_KratoCharacter`: Custom Event `CaughtByAlien`, proměnná `IsBeingCaught` (bool).

- [ ] **Krok 1: Blackboard a prázdný behavior tree.** Pravým → Artificial Intelligence → Blackboard → `BB_KratoAlien`, klíče `TargetActor` (Object, Base Class Actor) a `PatrolLocation` (Vector). Pak Artificial Intelligence → Behavior Tree → `BT_KratoAlien`, otevřít a v Details nastavit Blackboard Asset = `BB_KratoAlien`. Strom se staví až v kroku 8; teď je potřeba kvůli výběru v kroku 3 a tlačítkům New Task a New Service.
- [ ] **Krok 2: Postava mimozemšťana.** Blueprint Class → All Classes → `BP_NPC_BT_base` → `BP_KratoAlien`. Mesh má dva materiálové sloty: Element 0 = `MI_Manny_01_Green`, Element 1 = `MI_Manny_02_Green` (obojí z kurzu). Proměnné `PatrolPoints` (Actor, pole, Instance Editable) a `PatrolIndex` (int). Character Movement → Max Walk Speed 200. Pokud T0 zjistil v Event Graphu rodiče logiku, která by se bila s hlídkou (útok, vlastní pohyb), ozvat se před dalším krokem.
- [ ] **Krok 3: AI controller.** Blueprint Class → AIController → `AIC_KratoAlien`: `Event On Possess → Run Behavior Tree (BT_KratoAlien)`. V `BP_KratoAlien` Class Defaults: AI Controller Class = `AIC_KratoAlien`, Auto Possess AI = Placed in World or Spawned.
- [ ] **Krok 4: Úkol hlídky `BTT_NextPatrolPoint`** (v editoru behavior tree tlačítko New Task, přejmenovat). Proměnná `PatrolKey` (Blackboard Key Selector, Instance Editable).

```
Event Receive Execute AI (Owner Controller, Controlled Pawn)
 → Cast To BP_KratoAlien (Controlled Pawn) → Alien
 → Set Blackboard Value as Vector (Key: PatrolKey,
       Value: Alien.PatrolPoints[Alien.PatrolIndex].Get Actor Location)
 → Alien.Set PatrolIndex = (Alien.PatrolIndex + 1) % Length (Alien.PatrolPoints)
 → Finish Execute (Success ✓)
```

- [ ] **Krok 5: Detekce `BTS_DetectPlayer`** (New Service). Proměnné (Instance Editable): `TargetKey` (Blackboard Key Selector), `StandRange` 1500, `CrouchRange` 500, `LoseRange` 2250, `HalfAngleCos` 0.64 (kužel ±50°), `EyeHeight` 60, `PatrolSpeed` 200, `ChaseSpeed` 450.

```
Event Receive Tick AI (Owner Controller, Controlled Pawn)
 → Get Player Character (0) → Cast To BP_KratoCharacter → Player
 EyeLoc   = Controlled Pawn.Get Actor Location + (0, 0, EyeHeight)
 HeadLoc  = Player.Get Actor Location
            + (0, 0, Player.CapsuleComponent.Get Scaled Capsule Half Height − 10)
 ToPlayer = HeadLoc − EyeLoc
 Dist     = Vector Length (ToPlayer)
 Range    = Select Float (Player.Is Crouched: True → CrouchRange, False → StandRange)
 InCone   = Dot (Controlled Pawn.Get Actor Forward Vector, Normalize (ToPlayer)) ≥ HalfAngleCos
 Blocked  = Line Trace By Channel (EyeLoc, HeadLoc, Visibility,
                                   Actors to Ignore: [Controlled Pawn, Player])
 Branch (Dist ≤ Range AND InCone AND NOT Blocked AND NOT Player.IsBeingCaught)
   True  → Set Blackboard Value as Object (TargetKey, Player)
   False → Branch (Dist > LoseRange OR Player.IsBeingCaught)
             True → Clear Blackboard Value (TargetKey)
 → (oba konce větví sem)
 → Cast To Character (Controlled Pawn) → Character Movement
   .Set Max Walk Speed = Select Float (Is Valid (Get Blackboard Value as Object (TargetKey)):
                                       True → ChaseSpeed, False → PatrolSpeed)
```

Míří se na temeno kapsle, takže kdo se krčí za bednou vyšší než postava v dřepu, je skrytý bez zvláštního kódu.

- [ ] **Krok 6: Chycení `BTT_CatchPlayer`** (New Task). Proměnná `TargetKey` (Blackboard Key Selector). Move To s neúplnou cestou hlásí úspěch i na okraji navigační sítě, proto se vzdálenost kontroluje ještě tady; jinak by mimozemšťan „chytil“ hráče, který stojí metry daleko za rohem.

```
Event Receive Execute AI (Owner Controller, Controlled Pawn)
 → Get Player Character (0) → Cast To BP_KratoCharacter → Player
 → Branch (Get Distance To (Controlled Pawn, Player) ≤ 200)
     True  → Player.CaughtByAlien
             → Clear Blackboard Value (TargetKey)
             → Finish Execute (Success ✓)
     False → Clear Blackboard Value (TargetKey)
             → Finish Execute (Success ☐)
```

- [ ] **Krok 7: Událost v postavě.** V `BP_KratoCharacter` proměnná `IsBeingCaught` (bool) a Custom Event `CaughtByAlien`. Pojistka `IsBeingCaught` brání tomu, aby se chycení během ztmavnutí spustilo znovu a obraz problikával.

```
CaughtByAlien
 → Branch (NOT IsBeingCaught)
     True → Set IsBeingCaught = true
 → Get Player Camera Manager (0) → Start Camera Fade (From 0, To 1, Duration 0.4,
                                    Color černá, Hold When Finished ✓)
 → Delay 0.5
 → Get All Actors with Tag ("Checkpoint") → Get [0] → Checkpoint
 → Set Actor Location and Rotation (Checkpoint.Location, Checkpoint.Rotation, Teleport ✓)
 → Get Controller → Set Control Rotation (Checkpoint.Rotation)
 → Get Player Camera Manager (0) → Start Camera Fade (From 1, To 0, Duration 0.4)
 → Set IsBeingCaught = false
```

Všechno za `Set IsBeingCaught = true` visí jen na větvi True; větev False nevede nikam.

- [ ] **Krok 8: Behavior tree `BT_KratoAlien`** (Blackboard Asset = `BB_KratoAlien`):

```
Root
 └─ Selector                         [Service: BTS_DetectPlayer, Interval 0.2,
     │                                TargetKey = TargetActor]
     ├─ Sequence „Pronásledování“    [Decorator: Blackboard, TargetActor Is Set,
     │   │                            Observer aborts: Lower Priority]
     │   ├─ Move To (Blackboard Key: TargetActor, Acceptable Radius: 80)
     │   └─ BTT_CatchPlayer (TargetKey = TargetActor)
     └─ Sequence „Hlídka“
         ├─ BTT_NextPatrolPoint (PatrolKey = PatrolLocation)
         ├─ Move To (Blackboard Key: PatrolLocation)
         └─ Wait (1.5 s)
```

- [ ] **Krok 9: Do levelu.** Umístit `BP_KratoAlien` do hlavní chodby, v Details do `PatrolPoints` přidat oba Target Pointy z T5.
- [ ] **Krok 10: Test.** Očekávání:
  - mimozemšťan chodí mezi body a na koncích chvíli stojí;
  - ve stoje v jeho zorném poli do 15 m tě zahlédne, zrychlí a pronásleduje; když tě chytí, obrazovka jednou ztmavne (bez problikávání) a jsi na checkpointu, on se vrátí k hlídce v hlídkové rychlosti;
  - v dřepu tě zahlédne až do 5 m; za bednou v dřepu tě nevidí ani zblízka;
  - za jeho zády tě nevidí;
  - když před ním utečeš z chodby na křižovatku, zastaví se na kraji chodby a nechytí tě přes roh;
  - ventilací projdeš bez odhalení, i když jde kolem mřížky; mřížkami ho vidíš.
- [ ] **Krok 11: Uložit, napsat „commit T7“.** Zpráva: `feat(hw02): mimozemšťan, který v dřepu vidí jen zblízka`.

---

### T8: Finální video, PDF a odevzdání

**Soubory:** `docs/homeworks/02-plizeni/odevzdani/Kratochvil-DU2-blueprinty.html` a `.pdf` (v gitu), finální video `odevzdani/video/Kratochvil-DU2-plizeni.mp4` (mimo git)

- [ ] **Krok 1: Dotočit záběry s mimozemšťanem:** zahlédnutí ve stoje a chycení, proplížení v dřepu za bednami, pohled mřížkou z ventilace (titulek 7); případně přetočit úvodní záběr 1.
- [ ] **Krok 2: Doplnit screenshoty** behavior tree, `BTS_DetectPlayer` a `CaughtByAlien` do `odevzdani/blueprinty/`.
- [ ] **Krok 3: Agent sestaví finální video:** záběry s titulky, na konci blok blueprintů (každý screenshot asi 10 s s titulkem), titulek s přiznáním AI. Délka 2,5–4 min (zadání 1–6 min).
- [ ] **Krok 4: Agent napíše PDF** (weasyprint jako u DÚ č. 1): pro každý blueprint screenshot a dvě tři věty co a proč, nastavení Character Movement, co nefunguje nebo by šlo líp, přiznání AI.
- [ ] **Krok 5: Kontrola** videa a PDF tebou; znění přiznání AI schvaluješ ty.
- [ ] **Krok 6: Odevzdat v Labaverse:** video jako soubor, nebo odkaz na Google Drive s přístupem „kdokoli s odkazem“ (ověřit v anonymním okně), plus PDF.
- [ ] **Krok 7: Agent zapíše stav do README a `AGENTS.md`, napsat „commit T8“.** Zpráva: `docs(hw02): DÚ č. 2 odevzdán`.

## Zjištění

Vyplní agent během T0 a dalších úkolů.

### T0 (2026-10-25)

- **Engine:** UE 5.8, projekt převedený z 5.5 (viz hlavička). Při prvním spuštění hlásil editor chybějící Metal Toolchain, ačkoli byl nainstalovaný (Xcode 27.1); macOS ho připojí až při prvním použití, po zavolání `xcrun metal --version` editor naběhl. Kdyby se chyba vrátila: `xcodebuild -downloadComponent MetalToolchain`.
- **Krok 2:** zoom kolečkem funguje, první a třetí osoba se přepíná klávesou V, menu po startu není, otevírá ho klávesa P.
- **Krok 3:** `IA_ZoomCamera` nastaví jednorázově `Target Arm Length = Clamp(Target Arm Length + Action Value × (−10), 200, 600)`, relativně a jen při aktivní `3rd Person Camera`. `SetCamera3rdPerson` jen přepne aktivní kameru a vypne `Use Controller Rotation Yaw`, rameno nemění. Výchozí `Target Arm Length` je 400. **→ T4 podle plánu**, ne záložní varianta. Okrajový případ k testu T4: když hráč ve stoje přiblíží rameno pod 333, v dřepu bude pod 200 a první otočení kolečkem ho omezení kurzu skokem vrátí na 200; po vstání pak rameno bude 200 / 0,6 = 333.
- **Krok 4:** `1stPersonCamera` visí pod kapslí (Location 40, 0, 50), `CameraBoom` taky (Location Z 8,49). **→ T4 krok 5 se dělá** (vyhladit výšku kamery první osoby). Oči ve stoje SHH + 50 = 140 cm, v dřepu CHH + 50.
- **Krok 5:** žádné mapování (`IMC_Default`, `IMC_SkvtInput`; `IMC_SwapPawn` je jen redirector na `IMC_SkvtInput`) nepoužívá C, levý Ctrl ani Gamepad Face Button Right. Klávesy kurzu: W/A/S/D, šipky, mezerník, myš, V, R, P, Escape, kolečko, D-pad nahoru. Ověřeno z tabulek názvů v `.uasset`, kontrola na mezerníku v `IMC_Default`. **→ dřep dostane C, levý Ctrl i pravé tlačítko gamepadu.**
- **Krok 6:** `BP_NPC_BT_base` (rodič `BP_NPC_base`, mesh `SKM_Manny_Simple`, Anim Class `ABP_Manny`) má jen vypnuté výchozí události. AI Controller `AIC_BT_NPCBase` na BeginPlay spustí `BT_NPCBase`: Root → Sequence → `BTTask_Follow` (Get Player Pawn → AI MoveTo s Acceptance Radius). Blackboard má jen `SelfActor`. NPC kurzu hráče jen následuje, nevidí, nehlídkuje ani neútočí. **→ T7 podle plánu** s vlastním controllerem, blackboardem a stromem; `BTTask_Follow` je vzor pro pronásledování.
- **Krok 7:** hodnoty v tabulce Naměřené hodnoty. Kapsli a pohyb nastavuje `BP_SkvtBaseChar`, `BP_SkvtCharacterMale` je nepřepisuje. Hodnoty bez přepsání jsou výchozí z `CharacterMovementComponent.cpp` UE 5.8: Max Step Height 45, Crouched Half Height 40, Max Walk Speed Crouched 300 (počítá se v konstruktoru z výchozích 600, ne z 500 kurzu), `Can Walk Off Ledges When Crouching` vypnuté, `Can Crouch` vypnuté. Air Control 0,35. Plný skok vyjde 700² / (2 × 980 × 1,75) ≈ 143 cm.
- **Rozměry levelu s naměřenými hodnotami** (CHH 60 jako odhad, přepočítat po T2): H_s 180, H_c 120, L 140–150 → 150, šířka ventilace 2 × 35 + 30 = 100 cm, S ≥ 60 → 60, h_c 75–90 → 80, Crouch Jump Z Velocity √(2 × 980 × 1,75 × 80) ≈ 524, bedny C 130–140 → 135. Rozpětí L je jen 10 cm: kdyby T2 dalo CHH nad 65, L nebude mít řešení a strop se musí zvednout na úkor pravidla H_s − 30.

### T1 (2026-10-25)

- **Postaveno přes MCP:** složky v `Content/Krato/`, `IA_Crouch` (Digital, bez triggerů), `IMC_Krato` (C, Left Ctrl, Gamepad Face Button Right), `BP_KratoCharacter` (rodič `BP_SkvtCharacterMale`) s `Can Crouch` a `Can Walk Off Ledges When Crouching`, proměnnými, BeginPlay podle kroku 7 a funkcí `CanStandUp` podle kroku 8. Kompilace bez chyb i varování, uložení přes `save_assets` funguje, `git status` ukazuje jen nové soubory v `Content/Krato/` a assety kurzu nejsou označené jako změněné.
- **Odchylka od kroku 9:** logika přepínače je ve funkci `ToggleCrouch` a `IA_Crouch (Started)` ji jen volá. DSL nástroje `write_graph_dsl` neumí událost Enhanced Input vytvořit ani napojit na výstup `Started` (napojil by `Triggered`, který u Digital bez triggerů běží každý snímek), takže událost a volání funkce vznikly přes `create_node` a `connect_pins`.
- **Volání rodiče v BeginPlay (krok 7) přes MCP nejde:** uzel „Add Call to Parent Function“ není mezi typy uzlů. Rodiče `BP_SkvtCharacterMale` ani `BP_SkvtBaseChar` BeginPlay neimplementují (`list_events`), takže volání je zatím jen pojistka; doplní se ručně v editoru.
- **Krok 10:** `BP_KratoGameMode` (rodič `BP_SkvtGameMode`) má Default Pawn Class `BP_KratoCharacter`, Player Controller zůstává `BP_SkvtPlayerController` z kurzu.
- **Krok 11:** MCP nemá nástroj na nový level, `L_Plizeni` je proto kopie šablony Basic (`/Engine/Maps/Templates/Template_Default`, podle `TemplateMapInfos` v `BaseEngine.ini`), což je totéž, co dělá New Level → Basic. GameMode Override je `BP_KratoGameMode`, Player Start je jen jeden, v (0, 0, 92). Horní plocha podlahy vychází z bounds v Z = −0,5, tedy prakticky 0. BSP box MCP vytvořit neumí, nízký strop je proto statický mesh `/Engine/BasicShapes/Cube` (kostka 100 cm s pivotem uprostřed) jménem `NizkyStrop_Test`, scale 3 × 3 × 1, Location (600, 0, 200), tedy 300 × 300 × 100 cm se spodní hranou v 150 cm. Kolize je ověřená trace zespodu, zásah v Z = 150. Blockout v T5 přes MCP by tedy stál na kostkách enginu místo BSP, se stejným pravidlem pivotu uprostřed.
- **Test kroku 12 (autor):** dřep, vstávání pod stropem, okraj stropu, skok a logika kurzu prošly. Těsně u boku překážky nad výškou dřepu (bok kostky stropu, který začíná ve 150 cm) šlo dřepnout, ale ne vstát: koule `CanStandUp` s plným poloměrem hlásila zásah na spodní hraně boku. Engine v `UCharacterMovementComponent::UnCrouch` testuje místo statickým překryvem stojící kapsle (`OverlapBlockingTestByChannel`, plný poloměr, výška zvětšená o 0,001), ne pohybem koule, takže těsně podél plochy zásah nenajde. Opraveno podle kroku 8 na poloměr koule R − 0,5; opakovaný test u boku kostky i na okraji stropu prošel. Engine navíc testuje kanálem kapsle (Pawn), `CanStandUp` kanálem Visibility; u kostek enginu blokují oba, u jiných překážek to může rozhodovat.
- **Poznatky k MCP pro další úkoly:** přesunuté do `docs/unreal-mcp.md`.

### T2 (2026-10-25)

- **Postaveno přes MCP:** `BS_CrouchMove` (osa `Speed` 0–250, `Crouch_Idle` na 0, `Crouch_Walk` na 250), `ABP_KratoCharacter` (kopie `ABP_SkvtCharacter`) s proměnnými `IsCrouching` a `CrouchSpeed` na konci Update Animation (`CrouchSpeed` = 0 ve vzduchu, jinak `Speed` kurzu) a s Blend Poses by bool (0,2 s oběma směry) mezi state machine `Main` a slotem `DefaultSlot`. `BP_KratoCharacter` má Anim Class `ABP_KratoCharacter`, `Max Walk Speed Crouched` 250 (polovina 500, krok 7 tím rovnou hotový) a `Crouched Half Height` 60 jako startovní odhad z T0 (výsledná hodnota 70, viz krok 6 níže). Kompilace bez varování, Play přes MCP naběhl bez chyb v logu, assety kurzu nejsou změněné.
- **Odchylky od postupu:** MCP nemá nástroj na nový blend space, `BS_CrouchMove` je proto kopie `MoveForward_Blendspace` z kurzu s přepsanou osou a vzorky. Zápis vlastností přes MCP nepřepočítá vnitřní data blend space (`UBlendSpace::ResampleData` volá jen jeho editor při otevření a úpravách), proto se po úpravě blend space otevřel v editoru (`OpenEditorForAsset`) a pak uložil. Pole `SampleData` nejde přes `set_properties` zároveň zkrátit a změnit; napřed se zkrátilo beze změny prvků, pak se prvky přepsaly.
- **Krok 6 zůstává na autorovi:** dřep v běžící hře přes MCP vyvolat nejde (`bWantsToCrouch` nejde nastavit a stisk klávesy MCP do hry neposílá), `Crouched Half Height` se proto ladí ručně v Play.
- **Blend Poses by bool:** vstup `BlendPose_0` je True Pose, `BlendPose_1` False Pose (`FAnimNode_BlendListByBool::GetActiveChildIndex` vrací pro true index 0).
- **Krok 6, měření výšky hlavy (2026-10-26):** obrysy kapsle a debug koule `CanStandUp` se na screenshotech překrývaly, výška se proto měřila řadou tenkých destiček s kolizí ve známých výškách (po 5 cm) při dočasném `Crouched Half Height` 45, aby kapsle prošla pod všemi a destičky prorážela jen hlava meshe. Temeno hlavy v `Crouch_Idle` je 110–115 cm, v `Crouch_Walk` kolem 135 cm (občas šplhne na destičku 135, pod 140 se vejde). `Crouch_Walk` z kurzu je shrbená chůze s mírně pokrčenými koleny, `Crouch_Idle` hluboký dřep; jiné animace chůze v dřepu projekt nemá. Výška kapsle se proto řídí chůzí: **`Crouched Half Height` 70**, kapsle v dřepu 140 cm. Destičky jsou z levelu zase odstraněné.
- **Rozhodnutí autora 2026-10-26: rozměry levelu podle chůze, ne nižší póza.** S H_c 140 nejdou splnit dvě pravidla z tabulky Odvozené rozměry: strop ventilace (H_c + 20 ≤ L ≤ H_s − 30, tedy 160 ≤ L ≤ 150) a bedny (H_c + 10 ≤ C ≤ H_s − 40, tedy 150 ≤ C ≤ 140). Pro T5 proto platí **strop ventilace a traverzy L = 165 cm** (25 cm nad kapslí v dřepu, stojící kapsle 180 se nevejde) a **bedny C = 150 cm** (hlava v dřepu 135 schovaná, stojící postavě kouká hlava asi 25 cm nad bednu). Poskok platí dál: S 60, h_c 80 splňuje h_c ≥ S + 15 i h_c + H_c ≤ S + L (220 ≤ 225), Crouch Jump Z Velocity 524. Šířka ventilace 100 cm se nemění. Zamítnutá varianta: posunout vzorek `Crouch_Walk` v `BS_CrouchMove`, aby se v plné rychlosti míchal s nižší pózou `Crouch_Idle`; nohy by při plížení klouzaly a na hodnoceném videu by to bylo vidět víc než menší rezervy v levelu.
- **Strop z T1 (spodní hrana 150 cm) zůstává jako test:** v dřepu (140) se pod něj postava vejde s 10 cm rezervou, ve stoje ne.
- **Chodidla nad podlahou (2026-10-26):** ve stoje i v dřepu byla mezera mezi botami a stínem. Naměřeno v Play: horní plocha podlahy Z = −0,5, spodek kapsle Z = 1,65 (Character Movement drží kapsli asi 2 cm nad podlahou), mesh kurzu je na −89 při polovině výšky kapsle 90, chodidla tak byla asi 2,7 cm nad podlahou; nízká kamera s přímým světlem mezeru ve stínu opticky zvětší. Opraveno v `BP_KratoCharacter`: Mesh → Location Z −92 (kurz −89). Engine při dřepu posouvá mesh o rozdíl výšek kapsle, posun proto platí i v dřepu; kamery visí na kapsli a posun je neovlivní.
- **Test kroku 8 (autor, 2026-10-26):** s `Crouched Half Height` 70 a meshem na −92 prošel celý: plynulý přechod, póza v klidu i při chůzi, hlava pod stropem z T1, chodidla na podlaze, pohyb ve stoje beze změny.
- **Vedlejší účinek editoru:** při otevření editoru blend space přepsal editor 5.8 sdílené profily náhledové scény v `Config/DefaultEditor.ini` (přidal profil „Grey Ambient“ a `Version=ApplyNewGridMaterial`). Je to soubor projektu kurzu, necommituje se.
