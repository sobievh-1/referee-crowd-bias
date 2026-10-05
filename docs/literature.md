# Literature notes

Short notes on the studies this project builds on. Citations and DOIs were checked against Crossref on 2026-10-05.
Where numbers come from a working-paper version rather than the published article, this is noted.

## Closed-door matches and referee bias

### Reade, Schreyer & Singleton (2022)
**Eliminating supportive crowds reduces referee bias.** *Economic Inquiry* 60(3), 1416–1436. [doi:10.1111/ecin.13063](https://doi.org/10.1111/ecin.13063)

- **Data:** 160 matches played behind closed doors **as a disciplinary punishment, before COVID** (2002/03 – March 2020), compared with 33,796 other matches. Italy, France and UEFA competitions; no English data.
- **Method:** Elo strength controls; fixed effects for home team-season, away team-season and referee; a matched-control design; standard errors clustered by matchup.
- **Findings:**
  - Without a crowd, away teams receive about 20% fewer yellow cards: roughly a third of a card per match, or one card fewer per 22 fouls. Home teams' yellows do not change.
  - **They use the difference in yellow cards per foul as an outcome** (Table 7, about 100 matches).
  - No effect on fouls.
- **Relevance:** the closest paper to this project in measures (cards per foul) and controls (Elo, referee fixed effects).

### Bryson, Dolton, Reade, Schreyer & Singleton (2021)
**Causal effects of an absent crowd on performances and refereeing decisions during Covid-19.** *Economics Letters* 198, 109664. [doi:10.1016/j.econlet.2020.109664](https://doi.org/10.1016/j.econlet.2020.109664)

- **Data:** 2019/20 season, 23 leagues in 17 countries, including the Premier League and Championship. 6,481 matches, 1,498 of them behind closed doors.
- **Method:** fixed effects for home team, away team and referee.
- **Findings** (from the IZA working-paper version):
  - Away yellows −0.22 per match, home yellows +0.10.
  - The home−away yellow difference shifts by about 0.32.
  - No significant effect on results.
  - No fouls analysis.
- **Note:** their yellow counts include second yellows. football-data.co.uk's English counts exclude the first yellow when a second yellow becomes a red, so magnitudes are not directly comparable.

### Endrich & Gesche (2020)
**Home-bias in referee decisions: Evidence from "Ghost Matches" during the Covid19-Pandemic.** *Economics Letters* 197, 109621. [doi:10.1016/j.econlet.2020.109621](https://doi.org/10.1016/j.econlet.2020.109621)

- **Data:** Bundesliga 1 and 2, 2019/20; 612 matches, 165 of them ghost matches. **They use football-data.co.uk, the same source as this project.**
- **Method:** difference-in-differences, with betting-odds strength controls, team and referee fixed effects, and a placebo season.
- **Findings:**
  - In ghost matches home teams are called for relatively more fouls.
  - **Yellow cards with fouls as a control** (i.e. conditional on fouls) also move against the home team. The authors interpret this as "how harshly referees punished given fouls".
  - The effect is concentrated in matches with weak away support.
  - The placebo season shows nothing.

### Fischer & Haucap (2021)
**Does crowd support drive the home advantage in professional football? Evidence from German ghost games during the COVID-19 pandemic.** *Journal of Sports Economics* 22(8), 982–1008. [doi:10.1177/15270025211026552](https://doi.org/10.1177/15270025211026552)

- **Data:** German top three divisions, 2017/18–2019/20; 2,976 matches, 274 ghost games.
- **Findings** (working-paper version):
  - The Bundesliga home-win rate fell from 44.7% to 32.5%. There was no change in the 2nd and 3rd divisions.
  - The decline depends on usual stadium occupancy and fades over time.
  - **No cards or fouls analysis.** The paper is about results, not referees.

## COVID studies covering the Premier League

- **McCarrick, Bilalić, Neave & Wolfson (2021).** *Psychology of Sport and Exercise* 56, 102013. [doi:10.1016/j.psychsport.2021.102013](https://doi.org/10.1016/j.psychsport.2021.102013)
  - 4,844 matches in 15 leagues.
  - Home advantage fell. The home/away difference in fouls and yellows shrank, but less once team dominance (shots, corners) is controlled for.
- **Wunderlich, Weigelt, Rein & Memmert (2021).** *PLOS ONE* 16(3), e0248590. [doi:10.1371/journal.pone.0248590](https://doi.org/10.1371/journal.pone.0248590)
  - 10 leagues, 2010–2020, 1,006 matches without spectators.
  - The away-team excess of fouls and cards disappears. The drop in home advantage in points and goals is not significant.
- **Sors, Grassi, Agostini & Murgia (2021).** *European Journal of Sport Science* 21(12), 1597–1605. [doi:10.1080/17461391.2020.1845814](https://doi.org/10.1080/17461391.2020.1845814)
  - Top two divisions of England, Spain, Germany and Italy.
  - Reduced home advantage and no referee bias behind closed doors.
  - Only the abstract was read.
- **Leitner & Richlan (2021).** *Frontiers in Sports and Active Living* 3, 720488. [doi:10.3389/fspor.2021.720488](https://doi.org/10.3389/fspor.2021.720488)
  - 1,286 matches in eight leagues including the EPL, comparing 2018/19 with the 2019/20 ghost games.
  - Home teams received more **yellow cards for fouls** in ghost games.
  - Group comparisons only (Mann-Whitney tests), no regression.
- **Scoppa (2021).** *Journal of Economic Psychology* 82, 102344.
  - Top two divisions of five leagues including England.
  - In ghost matches the foul difference shifts by about +0.9 and the yellow difference by about +0.5 against the home team.
- **Nevill, Pearson & Webb (2023).** *Journal of Global Sport Management* 9(3), 527–544. [doi:10.1080/24704067.2022.2136102](https://doi.org/10.1080/24704067.2022.2136102)
  - All four English divisions; 2020/21 compared with 2010–2020.
  - The away share of yellows fell from 0.553 to 0.496.
  - **The Premier League shows the smallest effect of the four divisions.** This is relevant for this project's power and MDE analysis.

## Classic pre-COVID evidence

- **Nevill, Balmer & Williams (2002).** *Psychology of Sport and Exercise* 3(4), 261–272. [doi:10.1016/S1469-0292(01)00033-4](https://doi.org/10.1016/S1469-0292(01)00033-4)
  - 40 referees judged video clips with or without crowd noise.
  - With noise they called 15.5% fewer fouls against the home team.
  - This is the experimental basis for the "crowd pressure" mechanism.
- **Dohmen (2008).** *Economic Inquiry* 46(3), 411–424. [doi:10.1111/j.1465-7295.2007.00112.x](https://doi.org/10.1111/j.1465-7295.2007.00112.x)
  - Bundesliga, 1992–2004, with referee fixed effects.
  - More stoppage time when the home team trails.
  - The bias is stronger in stadiums without a running track, where the crowd is closer to the pitch.
- **Garicano, Palacios-Huerta & Prendergast (2005).** *Review of Economics and Statistics* 87(2), 208–216. [doi:10.1162/0034653053970267](https://doi.org/10.1162/0034653053970267)
  - Spanish referees lengthen stoppage time in close games when the home team is behind and shorten it when it is ahead.

## What this means for this project

- **Cards per foul is not a new measure.** Reade et al. (2022) use the same variable, and Endrich & Gesche (2020) use the same idea (yellows conditional on fouls). The project should cite them as the origin of the measure.
- **What is still this project's own:**
  - applying the measure to the Premier League's ghost periods, including almost the whole of 2020/21;
  - careful inference with few referees (wild cluster bootstrap);
  - a full distribution of placebo seasons rather than a single placebo;
  - an explicit minimum detectable effect, which matters because Nevill et al. (2023) find the Premier League effect to be the smallest of the English divisions;
  - a referee's interpretation of the mechanisms.
- **Possible extra robustness check:** a Poisson model of yellow cards with log(fouls) as an offset. This is a third way to condition cards on fouls, next to the ratio (Reade et al.) and fouls as a control (Endrich & Gesche).

## Not verified / caveats

- Numbers for Bryson et al., Fischer & Haucap and McCarrick et al. come from working-paper or preprint versions.
- For Sors et al. only the abstract was read.
- Numbers for Wunderlich et al. and Leitner & Richlan were not checked line by line.
- The search was not exhaustive. Reade et al. counted 39 COVID crowd studies by September 2021. Before publishing, run one more Google Scholar search for "cards per foul" combined with COVID.
