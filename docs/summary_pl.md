# Czy tłum wpływa na sędziów? Podsumowanie na jedną stronę

**Szymon Sobiech** · SGH · czynny sędzia piłkarski (ponad 300 meczów)

**Pytanie.** Czy obecność kibiców sprawia, że sędziowie Premier League karzą gości surowiej niż gospodarzy?

**Naturalny eksperyment.** Przez COVID-19 437 meczów Premier League rozegrano bez publiczności: restart w czerwcu i lipcu 2020 oraz prawie cały sezon 2020/21. Ci sami sędziowie i te same drużyny grały z kibicami i bez nich, z powodów niezwiązanych z piłką.

**Dane.** 2280 meczów z sezonów 2017/18–2022/23, źródło: football-data.co.uk. Każdy mecz jest zaklasyfikowany jako: pełne trybuny, ograniczona publiczność albo brak kibiców. Klasyfikację sprawdziłem z oficjalnymi danymi o frekwencji.

**Metoda.**
- **Miary:** różnica „goście − gospodarze” w żółtych kartkach, w żółtych kartkach na faul i w faulach.
- **Kontrole:**
  - efekty stałe sędziego, czyli każdy sędzia porównany sam ze sobą;
  - siła drużyn (ELO liczone z wyników);
  - VAR;
  - trend.
- **Wnioskowanie:** p-wartości z wild cluster bootstrap, bo w próbie jest tylko 33 sędziów.
- **Sprawdzenia:**
  - 223 fikcyjne okresy „bez kibiców” sprzed pandemii (placebo);
  - minimalny wykrywalny efekt.
- **Pre-rejestracja:** całą specyfikację zapisałem w repozytorium, zanim porównałem mecze z kibicami i bez nich.

**Wyniki.**
1. **Żółte kartki.** Przy kibicach goście dostają średnio o ok. 0,16 żółtej kartki na mecz więcej niż gospodarze. Bez kibiców ta różnica znika. Efekt wynosi −0,23 kartki na mecz (95% CI od −0,37 do −0,08, p = 0,009). Wynik trzyma się we wszystkich sprawdzeniach odporności poza wersją z efektami stałymi sezonu: tam ma podobną wielkość, ale jest zbyt mało precyzyjny, żeby był istotny.
2. **To nie przypadek.** Żaden z 223 okresów placebo nie dał tak dużego efektu.
3. **Kartki na faul: brak wyraźnego efektu** (−0,008, p = 0,38). Badanie wykrywa dopiero efekty od 0,024 w górę, a to więcej niż cała różnica w kartkach na faul przy kibicach. Małego efektu nie da się więc wykluczyć. Można natomiast wykluczyć duże efekty, takie jak w badaniach z Włoch i Francji.
4. **Mechanizm (analiza eksploracyjna).** Bez kibiców sędziowie odgwizdują gospodarzom ok. 10% więcej fauli, a liczba fauli gości się nie zmienia. Około 60% spadku różnicy w kartkach wynika ze zmiany w faulach, a ok. 40% z samej decyzji o kartce.

**Perspektywa sędziego.** Sędziowanie to także świadome zarządzanie meczem: czytanie emocji na trybunach i czasem marginalna decyzja na korzyść drużyny pod jej ławką. Dane nie pozwalają odróżnić takiego świadomego zarządzania od nieświadomej presji tłumu. Oba mechanizmy pasują jednak do tego, co widać w faulach.

**Ograniczenia.**
- Jedna liga i tylko 33 sędziów.
- Okres bez kibiców różnił się też innymi rzeczami: pięć zmian w meczu, zagęszczony terminarz.
- Liczba fauli zależy zarówno od decyzji sędziego, jak i od zachowania zawodników.

**Kod i dane:** github.com/sobievh-1/referee-crowd-bias
