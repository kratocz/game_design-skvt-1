# Descenders: Kurýr – survival vrstva pro kampaň

- **Hra:** Descenders (MTB, RageSquid / No More Robots)
- **Zadání:** DÚ č. 1, varianta Survival
- **Stav:** pracovní verze po oponentuře 2026-10-10 (všechny opravy zapracované); z ní vznikne zhuštěný odevzdávaný one-pager

> Pracovní dokument, podrobnější než odevzdávaná verze. Fakta o současné hře označená *ověřit* jsou přesvědčení autora, ne ověřený stav. Čísla označená *cíl ladění* jsou výchozí hodnoty návrhu, ne měření.

## 1. Problém, který design řeší

Descenders jsou sled izolovaných sjezdů. Pád stojí život, ale krajina sama hráče nijak neopotřebovává: únava ani teplota neexistují, počasí a noc jsou kulisa. Jízda nemá cíl mimo sebe samu.

Návrh dává cestě důvod a krajině váhu. Biom, počasí a denní doba mají měnit, *kudy* a *kdy* je rozumné jet, ne jen jak rychle.

## 2. Princip: prostředí tlačí stále, hráč rozhoduje občas

Survival tu neznamená, že hráč může umřít. Znamená, že prostředí opotřebovává dva živé tvory: jezdce (únava) a roj včelích královen (vitalita). Tlak působí stále, ale **hráč na něj reaguje jen ve dvou místech:**

- **v safe zóně:** výbava, čas odjezdu podle předpovědi, odpočinek;
- **na rozcestí:** volba trasy.

Mezi nimi hráč prostě jede Descenders. Okamžité volby na trati, třeba přeskočit kmen, nebo ho obejít, jsou volba stopy, kterou hra zná už dnes.

**Dovednost tlak snižuje.** Rychlá a čistá jízda je nejlepší ochrana roje, protože zkracuje dobu v horku i v mrazu. Dobrý jezdec survival vrstvu skoro necítí; kdo jede pomalu nebo padá, cítí ji hned. *Cíl ladění:* aspoň 80 % času kampaně je jízda, ne rozhodování nebo čekání.

## 3. Hranice: proč z toho není survival hra

- Žádný hlad, žádný crafting, žádné stavění základny.
- Jen dva ukazatele a nanejvýš dva kusy výbavy najednou.
- Survival tlak jen mění jízdu a volbu trasy, nemá vlastní herní smyčku.
- Žije jen v nové kampani. Kariéra a bike parky zůstávají, jak jsou. *Volitelně:* počasí a denní doba mohou i v kariéře měnit trakci a viditelnost; náklad a ukazatele zůstávají jen v kampani.

**Descenders dnes survival hra nejsou.** Jsou roguelite: v kariéře hráč začíná se čtyřmi životy a pád stojí život ([Descenders Wiki](https://descenders.fandom.com/wiki/How_to_play_guide_for_Descenders)). To je fail state, ne survival systém. Survival začíná tam, kde krajina opotřebovává, i když nepadáš; to návrh přidává.

**Kampaň a survival jsou různé osy.** Kampaň je struktura (mise, příběh, postup). Survival je vrstva mechanik (prostředí ubírá zdroje, hráč reaguje). Kampaň je nosič: dává cestě důvod, náklad, termín a otevřený svět.

## 4. Otevřený svět

Descenders dnes open-world nejsou: stojí na uzlech a procedurálně generovaných tratích. Kampaň je nový režim s **ručně postavenou souvislou mapou** ze čtyř kariérních biomů hry (Highlands, Forest, Canyon, Peaks; [Descenders Wiki](https://descenders.fandom.com/wiki/Peaks)). Mezi biomy nejsou neviditelné zdi ani nahrávací obrazovky.

**Topologie:**

- **Osada v údolí** (Highlands): start i cíl.
- **Horská včelí stanice** (Peaks): cíl cesty tam, viditelná z osady na obzoru.
- **Safe zóny:** chata nad osadou (Highlands), hájovna (Forest), opuštěná čerpací stanice (Canyon), horská bouda pod Peaks.
- **Tři hlavní koridory dolů ze včelí stanice**, propojené příčnými stezkami, takže je hráč může kombinovat:
  - *Hřebenová zkratka:* nejrychlejší, prudká a kamenitá, nejvíc otřesů, v mrazu.
  - *Přes Canyon:* rychlá, ale v horku.
  - *Přes Forest:* nejdelší, ve stínu, ale tma a kořeny.

**Volnost:** pořadí safe zón ani trasa nejsou předepsané. Pevný je jen cíl.

**Průzkum se vyplácí:** vyhlídky upřesní předpověď počasí pro okolní biom, objevené zkratky zkracují příští průjezd. *Volitelně:* drobné zakázky mezi safe zónami odměňují průzkum výbavou.

## 5. Struktura kampaně

1. **Cesta tam, rutinní zakázka.** Kurýr veze solární panely a akumulátory do horské včelí stanice. Cesta je krátká (*cíl ladění:* asi 15 % kampaně) a vede převážně do kopce, takže hráč hodně šlape (šlapání Descenders umí). Aktivní je jen únava. Hráč se učí mapu a únavu, krátké sjezdy mezi stoupáními fungují jako odměna. Náklad je těžký, takže se vejde jen jeden kus výbavy. Pád stojí jen čas.
2. **Zvrat ve včelí stanici.** Výměnou za panely kurýr přebírá včelí královny. Teprve tady se dozví, jak jsou křehké. Odemkne se ukazatel vitality roje.
3. **Cesta zpět.** Delší, převážně z kopce s krátkými stoupáními, do osady v údolí, dokud kvetou sady. Aktivní jsou oba ukazatele. Box je lehký, takže se vejdou dva kusy výbavy. Po namáhavém stoupání hráč sjezd ocení o to víc, a právě na sjezdu, kde je nejvíc rychlosti a pádů, veze nejcitlivější náklad.

## 6. Dva ukazatele a termín

| Ukazatel | Co ho zhoršuje | Co ho zlepšuje | Následek |
|---|---|---|---|
| Únava jezdce | stoupání, nesení kola, chlad, déšť, teplé oblečení v horku | odpočinek v safe zóně nebo ve stínu | unavený jezdec hůř ovládá kolo a víc padá |
| Vitalita roje | horko i mráz (roj potřebuje mírné pásmo), otřesy, pády | rychlý průjezd extrémem, stín, noc v horku, zahřátí na těle v mrazu | při nule roj hyne |

**Termín není ukazatel.** Je to počet dní do odkvětu, který hráč vidí v safe zóně a na mapě, ne na trati. *Cíl ladění:* pět dní; čistý průjezd zpět zabere zhruba tři.

**Životy z kariéry kampaň nahrazuje vitalitou roje.** Pád cestou zpět neubírá život jezdci, ale roji. Jádro Descenders (pád něco stojí) zůstává, jen má cena tvář.

## 7. Biomy, tlaky a protitahy

| Biom | Tlak | Protitahy a jejich cena |
|---|---|---|
| Highlands | déšť a vítr, bouřková fronta | přečkat v chatě (čas), jet závětrným údolím místo po hřebeni (delší trasa), ujet frontě (riziko pádu) |
| Forest | tma pod korunami, bláto, kořeny | světlo (místo ve výbavě), jet za dne (čekání), přenést kolo přes kořeny (únava). V horku je les úkryt: stín je pro roj bezpečné místo k odpočinku. |
| Canyon | horko | rychlý čistý průjezd (riziko pádu), jet v noci (tma), stinná rokle (delší trasa), chladicí vložka (místo ve výbavě, jednorázová) |
| Peaks | mráz, sníh, led | nést box pod bundou (únava a chlad jezdce), přejet kolem poledne (čekání), hřebenová zkratka (otřesy) |

## 8. Den a noc

Denní doba ve hře existuje (potvrzeno autorem). Kampaň jí dává dopad:

| Biom | Den | Noc |
|---|---|---|
| Highlands | mírný | chladno; v dešti jezdec rychle prochladne |
| Forest | šero pod korunami | téměř tma; bez světla jen pomalu |
| Canyon | horko, pro roj nebezpečné | chladno a pro roj bezpečné, ale tma |
| Peaks | snesitelné, nejlepší kolem poledne | mráz, pro roj i jezdce nejhorší |

**Jak plyne čas:** čas běží s jízdou (*cíl ladění:* herní den zhruba 40 minut). Odpočinek v safe zóně přetočí čas na zvolenou hodinu (úsvit, poledne, soumrak) a ubere tím z termínu. Čekání je tedy volba s cenou, ne pasivní stání.

## 9. Počasí jako náhoda, kterou hráč vidí předem

Počasí je procedurální, ale vždy ohlášené předem (*pre-luck*, pojem z lekce): hráč náhodu vidí dřív, než se rozhoduje.

- **Předpověď v safe zóně** na nejbližší půlden, s pravděpodobností. Je to klíčová informace pro rozhodnutí o odjezdu a výbavě.
- **Vyhlídky** předpověď pro okolní biom zpřesní; průzkum tak dává informaci.
- **Na trati** hráč čte počasí z oblohy: tmavnoucí horizont, vítr v korunách.
- **Události:** bouřková fronta v Highlands, která postupuje k osadě (hráč jí může ujet, nebo ji přečkat), vedro v Canyonu, vánice v Peaks, padlý strom, viditelný z dálky.

## 10. Způsoby průjezdu překážky

Okamžité volby na trati jsou volba stopy, kterou Descenders znají. Nové je, že bezpečná stopa existuje i pro slabšího jezdce, jen něco stojí.

| Způsob | Cena | Dopad na roj |
|---|---|---|
| Projet nebo přeskočit (bunny hop) | riziko pádu | otřes, při pádu velký stres |
| Tlačit nebo přenést kolo | únava, pomalý postup | žádné otřesy |
| Přečkat | čas | roj se stabilizuje, pokud je ve stínu nebo v teple |
| Objet | delší trasa | obvykle bezpečnější |

Příklady z lekce: **padlý kmen** (přeskočit, přenést, objet), **řeka** (přebrodit za cenu chladu jezdce, hledat lávku, v Canyonu vyschlé koryto).

## 11. Výbava v safe zóně

Tři druhy výbavy s funkcí. Dnes má v Descenders vliv na jízdu jen volba kola; dres, helma a doplňky na kole jsou kosmetické (podle autora, který hru zná). Cestou tam se vejde jeden kus, cestou zpět dva, takže jeden vždy chybí. Výbavu jde měnit jen v safe zóně.

| Výbava | Pomáhá | Nevýhoda |
|---|---|---|
| Světlo | noc, tma ve Forestu | zabírá místo |
| Teplá vrstva | mráz v Peaks, noc | v horku zrychluje únavu |
| Chladicí vložka | horko v Canyonu | jednorázová; nová jen v safe zóně |

## 12. Co hráč vidí

Zadání radí zvážit, které informace jsou klíčové. Návrh drží na obrazovce minimum:

- **Na trati:** únava, vitalita roje a šipka, zda teplota boxu stoupá, nebo klesá. Nic dalšího; počasí je vidět na obloze.
- **V safe zóně:** předpověď, dny do odkvětu, mapa s trasami, výbava.

## 13. Selhání

- **Únava na maximu:** jezdec sesedne a musí si odpočinout. Ztratí čas, ne postup.
- **Roj zahyne:** kurýr se vrací do včelí stanice pro náhradní královny. Ztratí čas, ne postup. Stanice má jen dvě náhrady, takže riskovat jde, ale ne donekonečna.
- **Pozdní příjezd po odkvětu:** osada přežije, ale epilog je skromnější. Kampaň jde dohrát vždy.

## 14. Otevřené otázky

- Projde u lektora nový open-world režim v hře, která sama open-world není? Doporučeno zeptat se před odevzdáním. Záloha: přenést návrh na Riders Republic, která open-world je.
