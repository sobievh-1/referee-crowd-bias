# Czy tłum zmienia decyzje sędziego?
### Premier League: mecze z publicznością i bez niej (pandemia COVID-19)

**Autor:** Szymon Sobiech — student SGH (MIESI), sędzia piłkarski od 2023 r. (200+ meczów)
**Wersja planu:** 2.1 (po przeglądzie literatury, 5.10.2026)
**Tryb:** jeden ciągły sprint, ok. 40 h
**Środowisko:** lokalnie na Macu, Claude Code, repo na GitHubie

---

## 0. Co się zmieniło względem wersji 1

| Było | Jest | Dlaczego |
|---|---|---|
| Plan A: Ekstraklasa, plan B: ligi europejskie | **Tylko Premier League** (football-data.co.uk) | Jedyna pewna liga z sędzią, faulami i kartkami w gotowym CSV; FBref stracił dane Opta w styczniu 2026 |
| H2: doświadczenie sędziego | **Usunięte** | Za mało sędziów (ok. 20–25), problem z liczeniem stażu sprzed okresu danych |
| Główna miara: `card_diff` | `card_diff` **+ kartki na faul** | Kartki na faul lepiej oddzielają decyzję sędziego od zmiany gry zawodników (miara za Reade i in. 2022) |
| Wkład: kartki na faul jako nowa miara | **Kartki na faul przejęte z literatury, wkład gdzie indziej** | Reade, Schreyer, Singleton (2022) używają tej samej zmiennej, Endrich, Gesche (2020) kartek z faulami jako kontrolą; zob. `docs/literature.md` |
| Kontrola siły: pozycja lub kursy | **ELO liczone z wyników** | Kursy z okresu bez kibiców już zawierają brak przewagi gospodarza („zjadają” efekt) |
| Efekty stałe sezonu w modelu głównym | **Zmienna VAR + trend, FE sezonu tylko jako sprawdzenie** | Sezon 2020/21 to prawie w całości mecze bez kibiców, więc FE sezonu wchłonęłoby prawie cały efekt |
| Zasada: AI tylko tłumaczy | **AI pisze i tłumaczy** | Dodany etap „umiem to wyjaśnić” przed publikacją |

**Mój wkład** (skoro Premier League jest dobrze zbadana): kartki na faul (miara za Reade i in. 2022 oraz Endrich, Gesche 2020) zastosowane do Premier League z prawie całym sezonem 2020/21 bez kibiców; wnioskowanie przy małej liczbie sędziów (wild cluster bootstrap); rozkład testów placebo zamiast jednego; jawnie policzona moc (ważne, bo Nevill i in. 2023 pokazują, że w Premier League efekt jest najmniejszy z angielskich lig) oraz perspektywa czynnego sędziego.

---

## 1. Pytanie i hipotezy

**Pytanie:** Czy obecność kibiców sprawia, że sędziowie karzą gości surowiej niż gospodarzy?

- **H1:** W meczach bez publiczności różnica żółtych kartek (goście − gospodarze) jest mniejsza niż w meczach z publicznością.
- **H1b:** W meczach bez publiczności różnica w kartkach na faul (goście − gospodarze) jest mniejsza. To jest test samej decyzji „kartka czy nie”.
- **Opisowo:** `foul_diff`, czyli różnica fauli. Mieszają się w niej zachowanie zawodników i decyzje sędziego, więc tylko interpretuję, nie testuję.

Test dwustronny. Efekt odwrotny lub zerowy też raportuję.

---

## 2. Dane

**Źródło:** football-data.co.uk, pliki `E0.csv` (Premier League) dla sezonów 2010/11–2022/23.
- 2010/11–2016/17: tylko do rozgrzania ELO
- 2017/18–2022/23: próba analityczna
- 2014/15–2018/19: sezony do testów placebo

**Kolumny:** `Date, HomeTeam, AwayTeam, FTHG, FTAG, Referee, HF, AF, HY, AY, HR, AR`

**Uwaga o kartkach:** w danych angielskich żółte kartki nie obejmują pierwszej żółtej, gdy druga zamienia się w czerwoną. Opisać w README.

**Klasyfikacja meczów (ręcznie, z udokumentowanym źródłem):**
- `ghost` = mecze bez kibiców: restart czerwiec–lipiec 2020 i większość sezonu 2020/21
- `partial` = mecze z ograniczoną frekwencją (pojedyncze kolejki w grudniu 2020 i ostatnie kolejki w maju 2021)
- reszta = pełne trybuny

Dokładne daty i listę meczów z częściową frekwencją ustalić na podstawie Wikipedii i doniesień prasowych. Zapisać źródła w `data/ghost_matches_sources.md`.

### Zmienne

| Zmienna | Definicja |
|---|---|
| `card_diff` | AY − HY |
| `cpf_diff` | AY/AF − HY/HF (kartki na faul) |
| `foul_diff` | AF − HF |
| `red_diff` | AR − HR (tylko pomocniczo) |
| `ghost`, `partial` | 0/1 |
| `referee` | z kolumny `Referee` |
| `elo_diff` | ELO gospodarza − ELO gościa przed meczem |
| `var` | 1 od sezonu 2019/20 |
| `trend` | numer sezonu |

---

## 3. Metoda

1. **Opis:** średnie `card_diff`, `cpf_diff` i `foul_diff` w trzech kategoriach meczów, przedziały ufności, pierwszy wykres.
2. **Model główny:**
   `card_diff ~ ghost + partial + elo_diff + var + trend + FE(sędzia)`
   To samo dla `cpf_diff`. Efekty stałe sędziego oznaczają, że porównuję tego samego arbitra z kibicami i bez.
3. **Błędy standardowe:** klastrowane po sędzi. Przy ok. 20–25 klastrach to za mało dla zwykłych SE, więc dodatkowo wild cluster bootstrap (np. pakiet `wildboottest`).
4. **Sprawdzenia odporności:**
   - wersja z FE sezonu (efekt identyfikowany głównie z restartu 2019/20, opisać to wprost),
   - wykluczenie meczów `partial`,
   - tylko sezony z VAR (2019/20–2022/23),
   - trzecia wersja „kartek na faul”: model Poissona dla żółtych kartek z log(faule) jako offsetem (obok różnicy ilorazów jak u Reade i in. i fauli jako kontroli jak u Endrich, Gesche).
5. **Placebo (rozkład):** na danych sprzed pandemii każdy sezon od 2014/15 do 2018/19 kolejno udaje „sezon bez kibiców”. Wynik prawdziwy porównuję z rozkładem efektów placebo.
6. **Moc:** minimalny wykrywalny efekt ≈ 2,8 × SE (moc 80%, α = 0,05). Napisać przy wyniku, jaki efekt byłbym w stanie zobaczyć.

**Specyfikację z punktów 2–5 zapisuję w repo (`PREREGISTRATION.md`) przed porównaniem meczów z kibicami i bez.** Opcjonalne, ale tanie.

---

## 4. Wymiar sędziowski (mój akapit)

Dane nie rozróżnią dwóch mechanizmów, które znam z boiska:
- tłum **przechyla decyzję**, którą sędzia podejmuje (żółta zamiast upomnienia), co powinno być widać w `cpf_diff`,
- tłum sprawia, że przy marginalnym kontakcie sędzia **nie gwiżdże w ogóle**, co powinno być widać w `foul_diff`.

Napisać krótko z własnej perspektywy: co robi presja trybun i czym różni się mecz przy pustych trybunach.

---

## 5. Plan pracy (ok. 40 h)

| # | Etap | Czas | Punkt kontrolny (koniec etapu) |
|---|---|---|---|
| 0 | Setup: repo, venv, struktura folderów, `CLAUDE.md`, pierwszy push | 2 h | Puste repo widoczne na GitHubie, notebook się uruchamia |
| 1 | Dane: skrypt pobierający CSV, łączenie sezonów, czyszczenie, klasyfikacja ghost/partial | 8 h | Jedna tabela mecz po meczu; wypisane liczby meczów w każdej kategorii i liczba sędziów; brak pustych wartości w kluczowych kolumnach |
| 2 | Literatura: 3–4 badania, krótka notatka, co znaleźli | 3 h | `docs/literature.md` z linkami |
| 3 | ELO z wyników | 4 h | Ranking na koniec sezonu 2018/19 wygląda sensownie (mistrz blisko góry) |
| 4 | Pre-rejestracja (opcjonalnie) | 1 h | `PREREGISTRATION.md` w repo z datą commita |
| 5 | Statystyki opisowe i pierwszy wykres | 4 h | Tabela średnich z przedziałami ufności |
| 6 | Model główny i sprawdzenia odporności | 6 h | Tabela wyników: współczynnik `ghost`, SE klastrowane, p-wartość z bootstrapu |
| 7 | Placebo i moc | 4 h | Wykres rozkładu placebo z zaznaczonym wynikiem prawdziwym; MDE w zdaniu |
| 8 | Publikacja: 3 wykresy, README po angielsku, podsumowanie 1 strona PL/EN | 6 h | Osoba spoza piłki rozumie README w 3 minuty |
| 9 | „Umiem to wyjaśnić”: 10 pytań rekrutera i moje odpowiedzi | 2 h | Potrafię bez notatek wyjaśnić FE, klastrowanie, placebo i MDE |

### Kandydaci do literatury (do weryfikacji, czy istnieją i co dokładnie mówią)
- Reade, Schreyer, Singleton — artykuł o ograniczeniu stronniczości sędziów po zniknięciu kibiców (Economic Inquiry, ok. 2022)
- Bryson, Dolton, Reade, Schreyer, Singleton — przyczynowy efekt nieobecności tłumu (Economics Letters, 2021)
- Endrich, Gesche — home bias sędziów w „ghost matches” w Bundeslidze (Economics Letters, 2020)
- Fischer, Haucap — przewaga własnego boiska w niemieckich meczach bez kibiców (Journal of Sports Economics, 2021)

---

## 6. Struktura repo

```
referee-crowd-bias/
├── README.md               # po angielsku, dla rekrutera
├── PLAN.md                 # ten plik
├── PREREGISTRATION.md      # opcjonalnie
├── CLAUDE.md               # zasady pracy z Claude Code
├── data/
│   ├── raw/                # oryginalne CSV, nigdy nie edytowane
│   ├── processed/          # tabela analityczna
│   └── ghost_matches_sources.md
├── src/                    # skrypty: pobieranie, czyszczenie, ELO
├── notebooks/              # 01_data, 02_descriptives, 03_models, 04_placebo
├── figures/
└── docs/                   # literatura, podsumowanie 1 strona
```

---

## 7. Zasady pracy

- AI pisze i tłumaczy. Każdy blok kodu ma krótkie wyjaśnienie, co robi i dlaczego.
- Przed publikacją etap 9: rozumiem każdą liczbę i każdą decyzję metodologiczną.
- Każda liczba w raporcie pochodzi z komórki w notebooku.
- `data/raw` nigdy nie jest edytowane ręcznie.
- Niepewność piszę wprost.
- Najpierw najprostsza wersja, która działa; ulepszenia potem.

---

## 8. Ryzyka

| Ryzyko | Co robię |
|---|---|
| Mało sędziów → niewiarygodne SE | Wild cluster bootstrap, raport mocy |
| `ghost` prawie pokrywa się z sezonem 2020/21 | Model z trendem i VAR zamiast FE sezonu; FE sezonu jako sprawdzenie |
| Restart 2020 miał inne warunki (5 zmian, przerwy na picie, zagęszczony terminarz) | Opisać jako ograniczenie; sprawdzenie tylko na 2020/21 |
| Mało fauli w meczu → zaszumione `cpf_diff` | Opcjonalnie model na poziomie drużyna-mecz: kartki ~ faule × gość × ghost |
| Niepewne daty meczów z częściową frekwencją | Sprawdzenie z wykluczeniem `partial` |
| Premier League dobrze zbadana | Wkład = pełny sezon ghost w Premier League, wnioskowanie przy małej liczbie klastrów, rozkład placebo, moc, perspektywa sędziego; kartki na faul cytowane jako miara z literatury |

---

## 9. Narzędzia

Python 3, pandas, statsmodels (lub linearmodels), wildboottest, matplotlib, JupyterLab lub notebooki w VS Code, git + GitHub, Claude Code.
