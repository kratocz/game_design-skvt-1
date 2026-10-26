# MCP plugin Unrealu – co jde a co ne

- **Engine:** UE 5.8, oficiální experimentální plugin `ModelContextProtocol` + `AllToolsets` (připojení viz `AGENTS.md`)
- **Ověřeno:** 2026-10-25 a 2026-10-26 při stavbě T1 až T3 DÚ č. 2 (`docs/homeworks/02-plizeni/postup-editor.md`, sekce Zjištění)

Nástroje jsou za meta-nástroji `list_toolsets`, `describe_toolset` a `call_tool`. `call_tool` potřebuje `toolset_name` (plné jméno z `list_toolsets`, např. `editor_toolset.toolsets.blueprint.BlueprintTools`) a `tool_name` jako krátké jméno (`read_graph_dsl`); samotné krátké jméno ani jméno s prefixem toolsetu bez `toolset_name` nástroj nenajde. Volitelné parametry, které schéma vede jako povinné (`find_nodes.title`, `find_node_types.context_pins`), se posílají prázdné (`""`, `[]`). Popis toolsetu `BlueprintTools` je přes 70 tisíc znaků a do odpovědi se nevejde; vyplatí se ho uložit do souboru a vypsat jen názvy a parametry nástrojů.

## Assety

- **Blueprint:** `BlueprintTools.create` s `asset_type` = vygenerovaná třída rodiče (`…/BP_SkvtCharacterMale.BP_SkvtCharacterMale_C`). Vlastnosti komponent se nastavují na CDO přes `ObjectTools.set_properties`, např. `…BP_KratoCharacter.Default__BP_KratoCharacter_C:CharMoveComp` nebo `:CharacterMesh0`.
- **Data assety (Input Action, Mapping Context):** `DataAssetTools.create` s třídou `/Script/EnhancedInput.InputAction` nebo `…InputMappingContext`. Mapování v 5.8 leží ve vlastnosti `DefaultKeyMappings.mappings`.
- **Co vytvořit nejde a čím se to nahradí:** nový level (kopie šablony Basic `/Engine/Maps/Templates/Template_Default` přes `AssetTools.duplicate`), BSP box (kostka `/Engine/BasicShapes/Cube`, 100 cm s pivotem uprostřed), nový blend space (kopie existujícího a přepsání osy a vzorků).
- **Blend space se po zápisu přes MCP nepřepočítá:** vnitřní data (`UBlendSpace::ResampleData`) přepočítává jen jeho editor. Po úpravě ho otevřít (`EditorAppToolset.OpenEditorForAsset`) a pak uložit.
- **Pole nejde zároveň zkrátit a změnit:** `set_properties` to odmítne („elements changed alongside the size change“). Napřed pole zkrátit beze změny prvků, pak prvky přepsat.
- **Ukládání:** `AssetTools.save_assets` s cestami bez přípony objektu; `is_dirty` ukáže neuložené změny. Po uložení ověřit `git status`. Po kompilaci a otevření potomka byl rodič z kurzu (`BP_SkvtBaseChar`) označený jako neuložený (co přesně ho označilo, se nezjišťovalo), proto nikdy `save_assets` s prázdným seznamem (uloží vše). Seznam neuložených assetů dá skript `ProgrammaticToolset.execute_tool_script` s `find_assets` a `is_dirty`.
- **Editor sám přepisuje `Config/DefaultEditor.ini`:** při otevření editoru assetu s náhledem (blend space) převede sdílené profily náhledové scény na formát 5.8. Je to soubor kurzu, necommituje se.

## Grafy blueprintů

- **`write_graph_dsl`** přepíše celou funkci. V Event Graphu přepíše události uvedené v DSL; výchozí neaktivní události (Tick, ActorBeginOverlap) zápis přežily.
- **Události Enhanced Input DSL neumí** (hledá `AddEvent|…` a selže). Uzel události se vytvoří přes `create_node` s typem `Input|EnhancedActionEvents|<IA>`, logika patří do funkce a výstup `Started` (index 1) se napojí `connect_pins` na volání funkce `CallFunction|<Jméno>`. `Triggered` u Digital akce bez triggerů běží každý snímek.
- **„Add Call to Parent Function“** mezi typy uzlů není (ani v přetížené funkci, ověřeno na Can Jump v T3); doplňuje se ručně v editoru. Přes UI toolset `SlateInspectorToolset` to taky nejde: uzly grafu ve stromu widgetů nejsou. Návod pro autora: přetížená funkce je v My Blueprint → Functions pod kategorií rodiče (Can Jump pod „Character“), ne mezi vlastními funkcemi; „Add Call to Parent Function“ je v kontextové nabídce vstupního uzlu funkce nebo uzlu události. Uzel „Parent: …“ může mít exec piny (Can Jump i BeginPlay je mají) a pak se provede jen v exec cestě: zapojit ho do bílé hrany větve, ne jen datovým výstupem, jinak vrací výchozí hodnotu.
- **Přetížení funkce rodiče:** `add_function_graph` s názvem C++ funkce (`CanJumpInternal`, ne zobrazovaný „Can Jump“). Události rodiče přes `add_event` (`K2_OnStartCrouch`), v DSL se pak jmenují `EventOnStartCrouch`.
- **Poziční argumenty u setterů komponent** (`Class|CharacterMovementComponent|SetJumpZVelocity`) jdou v pořadí hodnota, `self`; bezpečnější jsou pojmenované `:self … :JumpZVelocity …`. Pořadí pinů ukáže `get_node_type_pins`.
- **Uzel s několika datovými výstupy** se váže `(bind (outHit hit) …)`, jinak se vezme první výstup. Cesty tříd, enumy a assety v DSL musí být v uvozovkách.
- **`read_graph_dsl`** vypisuje čisté uzly vnořeně, i když jsou v grafu jen jednou; počet uzlů ukáže `find_nodes`. U událostí Enhanced Input vrací jen hlavičku.
- **AnimGraph** se staví přes `create_node`, `connect_pins`, `break_pins` a `set_pin_value`. U Blend Poses by bool je `BlendPose_0` True Pose a `BlendPose_1` False Pose.
- **Uzly z DSL leží v jedné řadě**, `arrange_nodes` je rozloží (kvůli screenshotům blueprintů). Proměnná `float` z `add_variable` je double.

## Level a Play

- **Actory:** `SceneTools.add_to_scene_from_asset`, ověření přes `ActorTools.get_actor_bounds` a `SceneTools.trace_world`. `set_actor_transform` jen s polohou vynuluje měřítko, posílat vždy celý transform.
- **Kolizi nejde přepnout za běhu editoru:** změna `BodyInstance.collisionProfileName` přes `set_properties` se do fyziky propíše až po znovunačtení levelu.
- **Play:** `EditorAppToolset.StartPIE`, `StopPIE`, `IsPIERunning`. Za běhu Play nejde vkládat actory. Objekty běžící hry mají cesty `/Game/…/UEDPIE_0_<Level>.<Level>:PersistentLevel.<Actor>_C_0`, jdou číst přes `ObjectTools.get_properties` a `ActorTools.get_actor_transform`. Log čte `LogsToolset.GetLogEntries` s regexem.
- **Vstup do hry MCP neposílá** a chráněné vlastnosti (`bWantsToCrouch`) nenastaví, takže chování závislé na klávesách testuje autor ručně.
- **Náhled assetu:** `CaptureAssetImage` vrací PNG v base64, odpověď je na výstup nástroje moc velká; uloženou odpověď dekódovat do souboru a ten si prohlédnout.

## Měření v levelu

Výšky ze screenshotů neodhadovat: perspektiva kamery a překrývající se obrysy (kapsle, debug trace, fyzikální tělesa) vedly k chybě o 20 cm. Spolehlivě měří řada tenkých destiček ve známých výškách (kostka se Z měřítkem 0,02, po 5 cm), pod kterou se postava projde a autor řekne, kterou ještě prorazí. Hodnoty z běžící hry (poloha actoru, výška kapsle) dává přímo MCP.
