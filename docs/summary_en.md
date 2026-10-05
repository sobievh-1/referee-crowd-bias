# Do crowds bias referees? — one-page summary

**Szymon Sobiech** · SGH Warsaw School of Economics · active football referee (200+ matches)

**Question.** Does the crowd make Premier League referees treat away teams more harshly?

**Natural experiment.** COVID-19 forced 437 Premier League matches to be played behind closed doors: the June–July 2020 restart and almost all of 2020/21. The same referees and teams played with and without fans, for reasons unrelated to football.

**Data.** 2,280 matches, 2017/18–2022/23, from football-data.co.uk. Every match was classified as full crowd, limited crowd or no crowd, and the classification was checked against official attendance figures.

**Method.**
- **Outcome:** the away-minus-home difference in yellow cards, yellow cards per foul and fouls.
- **Controls:** referee fixed effects (each referee compared with themselves), team strength (ELO from results), VAR and a time trend.
- **Inference:** p-values from a wild cluster bootstrap, because there are only 33 referees.
- **Checks:** 223 placebo "no-crowd" periods before the pandemic, and the smallest detectable effect.
- **Pre-registration:** the whole specification was committed before any comparison of crowd and no-crowd matches.

**Results.**
1. **Yellow cards.** With fans, away teams get about 0.16 more yellows per match than home teams. Without fans, the gap disappears: −0.23 yellows per match, 95% CI −0.37 to −0.08, p = 0.009. The result holds in all robustness checks except season fixed effects, where it is similar in size but too imprecise to be significant.
2. **Chance can be ruled out.** None of the 223 placebo periods produced an effect this large.
3. **Cards per foul: no clear effect.** The estimate is −0.008, p = 0.38. The design can only detect effects of 0.024 or more, larger than the whole cards-per-foul gap with fans, so a small effect cannot be ruled out. Large effects like those found in Italy and France can.
4. **Mechanism (exploratory).** Without fans, home teams are called for about 10% more fouls, while away fouls do not change. Roughly 60% of the drop in the card gap comes through fouls, and about 40% through the card decision itself.

**A referee's view.** Refereeing involves deliberate game management: reading the emotions in the stadium and sometimes giving the marginal call to a team near its own bench. The data cannot separate this deliberate management from unconscious crowd pressure, but both fit the pattern in the fouls.

**Limitations.**
- One league and 33 referees.
- The no-crowd period was unusual in other ways too (five substitutes, a congested schedule).
- Foul counts mix referee decisions with player behaviour.

**Code and data:** github.com/sobievh-1/referee-crowd-bias
