# Descenders: Kurýr – survival vrstva pro kampaň

- **Hra:** Descenders (MTB, RageSquid / No More Robots)
- **Zadání:** DÚ č. 1, varianta Survival
- **Stav:** kostra

> Pracovní verze. Fakta o současné hře označená *ověřit* jsou moje přesvědčení, ne ověřený stav; před odevzdáním je potvrdit ve hře.

## 1. Problém, který design řeší

*K dopsání.* Descenders jsou sled izolovaných jízd. Jízda nemá cíl mimo sebe samu a krajina je jen kulisa sjezdu. Survival vrstva dává cestě důvod a krajině váhu: biom, počasí a denní doba mění, *jak* a *kdy* je rozumné jet, ne jen jak rychle.

## 2. Hranice: proč z toho není survival hra

*K dopsání.* Žádný hlad, žádný crafting, žádné stavění základny. Survival tlak je vždy modifikátor jízdy a volby trasy, nikdy samostatná herní smyčka. Hráč, který jede dobře, se survival systémem skoro nezabývá; hráč, který riskuje, ho cítí.

## 2a. Proč je to pořád survival

*K dopsání a obhajobě.* Survival tu neznamená „hráč může umřít“, ale „prostředí neustále ohrožuje něco živého a hráč s tím hospodaří“. Ohrožení jsou dva: roj (horko, mráz, otřesy) a jezdec (únava, chlad). Oba jsou provázané: unavený nebo prochladlý jezdec hůř ovládá kolo, víc padá a pády stresují roj. Jezdcovo přežití je tak nástrojem přežití roje. Pozor na riziko, že bez té vazby by z návrhu byla jen eskortní mise s nákladem, ne survival systém.

*K dopsání a obhajobě.* **Descenders dnes survival hra nejsou.** Jsou roguelite: pády ubírají zdraví a jeho ztráta ukončí run (*ověřit* přesnou mechaniku). To je fail state, ne survival systém, protože hra nemá zdroj, který by krajina ubírala v čase. Únava ani teplota neexistují, počasí a noc jsou kulisa. Survival začíná tam, kde tě krajina opotřebovává, i když nepadáš; to návrh přidává.

**Kampaň a survival jsou různé osy.** Kampaň je struktura (mise, příběh, postup), survival je vrstva mechanik (prostředí ubírá zdroje, hráč hospodaří). Kampaň je nosič: dává důvod k cestě, náklad, termín a otevřený svět s volbou trasy. Survival vrstva žije jen v ní; kariéra a bike parky zůstávají beze změny.

## 3. Režim a struktura

- Jedna souvislá oblast se čtyřmi biomy, mezi nimi safe zóny (vesnice, chaty).
- Mezi safe zónami víc tras s různým profilem: rychlá a exponovaná vs. delší a chráněná.
- **Cesta tam:** obchodní zakázka, panely a akumulátory do horské včelí stanice. Těžký a křehký náklad, sázka nízká. Aktivní je jen únava jezdce a citlivost nákladu na pády; učí základ systému. Cesta je kratší a vede převážně do kopce, takže hráč hodně šlape (šlapání Descenders umí). Únava je tu hlavní téma a krátké sjezdy mezi stoupáními působí jako odměna.
- **Kontrast směrů:** cesta zpět vede převážně z kopce. Po namáhavém stoupání hráč sjezd ocení o to víc, a právě na sjezdu, kde je nejvíc rychlosti a pádů, veze nejcitlivější náklad.
- **Zvrat ve včelí stanici:** hráč přebírá královny a teprve tady se dozví, jak jsou citlivé na teplotu a otřesy. UI odemkne ukazatel vitality roje.
- **Cesta zpět:** sjezd do osady v údolí, dokud kvetou sady. Aktivní jsou všechny tři ukazatele. Stejná krajina klade jiné otázky: Canyon v poledne je pro panely jen horká jízda, pro královny smrt.

## 4. Tři ukazatele

| Ukazatel | Co ho zhoršuje | Co ho zlepšuje |
|---|---|---|
| Únava jezdce | dlouhá jízda, stoupání, tlačení a nesení kola, chlad, nesení boxu pod bundou | odpočinek v safe zóně nebo ve stínu |
| Vitalita roje | horko, mráz (pásmo, ne jeden směr), otřesy a pády | stín, noc v horku, zahřátí na těle v mrazu, chladicí náplně |
| Čas do odkvětu | čekání, objížďky, odpočinek | rychlost, kratší trasa |

*K rozhodnutí:* přesná podoba UI a zda je vitalita jedno číslo, nebo dva podukazatele (teplota a stres).

## 5. Biomy, tlaky a protitahy

| Biom | Hlavní tlak | Terén (z lekce) | Protitahy | Cena protitahu |
|---|---|---|---|---|
| Highlands | déšť (kluzký povrch, promoknutí, chlad pro jezdce i roj), vítr (protivítr do kopce, boční poryvy na hřebeni) | hladká cesta, stoupání | přečkat déšť v chatě nebo pod převisem, jet závětrnou stranou údolím místo po hřebeni, nepromokavý obal na náklad, krýt se za skalami | čas, delší trasa, místo v nosnosti, pomalejší jízda |
| Forest | tma (pod korunami i ve dne horší viditelnost), bláto (trakce, únava), kořeny (otřesy stresují roj) | kořeny, říčka | světlo, projet za dne, technicky pomalu přes kořeny, nést kolo přes nejhorší úsek, objet po lesní cestě, přebrodit říčku nebo hledat lávku | místo v nosnosti, čekání, čas, únava, delší trasa, mokro a chlad po brodu |
| Canyon | horko | kameny, řeka, klesání | rychlost, jízda v noci, stinná rokle, chladicí náplně, odpočinek ve stínu | riziko pádu, tma, delší trasa, omezené náplně, čas |
| Peaks | mráz, sníh, výška | led, stoupání | nést box pod bundou, krátká trasa přes hřeben | vlastní teplo a únava, exponovanost |

Forest je i úkryt: ve stínu korun je chladno, takže v horku je les pro roj bezpečnějším místem k odpočinku než otevřený Canyon. Stejný biom tak jednou škodí a jindy pomáhá, podle toho, odkud hráč přijíždí.

*Ověřit:* názvy a počet kariérních biomů v Descenders.

## 6. Klíčové napětí: rychlost vs. opatrnost

Rychlost chrání před horkem a šetří čas, ale zvyšuje riziko pádu a pád stresuje roj. Survival vrstva tak přidává k risk/reward jádru Descenders druhou osu, nevymýšlí nové.

## 7. Způsoby průjezdu překážky

*K dopsání.* Jet, tlačit, nést kolo, brodit, přečkat, objet. Každý stojí něco jiného (únavu, čas, vitalitu roje). Překážky z lekce: padlý kmen, řeka.

## 8. Den a noc

Denní doba ve hře existuje (potvrzeno uživatelem). Návrh přidává její vliv: noc v Canyonu je chladná a pro roj dobrá, ale tmavá; noc v Peaks je mráz. *K dopsání:* světlo jako výbava.

## 9. Výbava v safe zóně

*K dopsání.* Nová vrstva (výbava v Descenders je podle mě kosmetická, *ověřit*): pláště podle povrchu, světlo, teplé oblečení, chladicí náplně. Omezená nosnost, takže výběr je volba.

## 10. Otevřené otázky

- Co se stane, když roj zahyne? Konec kampaně, nebo návrat do poslední safe zóny pro nové královny?
- Co přesně znamená pozdní příjezd po odkvětu – snížená odměna, horší konec, nebo prodloužení o další rok?
- Bouřková fronta jako „pronásledovatel“ – patří do Highlands, nebo vynechat?
- Jak udělat, aby cesta tam *působila* rutinně, ale nebyla pro hráče nudná? Jízda sama je zábavná; rutinní má být jen zakázka, ne zážitek.
