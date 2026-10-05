# Pre-registration: crowd presence and referee decisions in the Premier League

**Author:** Szymon Sobiech
**Date:** 2026-10-05. The git commit that adds this file is the timestamp.
**Status:** written **before** any comparison of outcomes between ghost and crowd matches.

This is an informal pre-registration: a private record of the analysis plan. It exists so the specification below cannot be adjusted after seeing the results. Any deviation will be reported in the README as a deviation.

## What had been seen before writing this

- Data cleaning (`notebooks/01_data.ipynb`):
  - row counts; referee name fixes; the 28 low-foul matches;
  - number of matches per crowd category: 1,808 full, 437 ghost and 35 partial in 2017/18–2022/23.
- Team strength (`notebooks/02_elo.ipynb`):
  - ELO ratings;
  - home-win rate and mean `card_diff` by `elo_diff` quintile, pooled over all crowd categories.
- **Not seen:** any outcome (`card_diff`, `cpf_diff`, `foul_diff`) split by ghost / partial / full, or any regression including `ghost`.

## 1. Hypotheses

Sign convention: every difference is **away − home**. Under crowd bias, away teams are treated more harshly with fans, so the `ghost` coefficient is expected to be **negative**.

- **H1 (primary):** `card_diff` (AY − HY) is lower in ghost matches than in full-crowd matches.
- **H1b (secondary):** `cpf_diff` (AY/AF − HY/HF, yellow cards per foul) is lower in ghost matches than in full-crowd matches.
- **Descriptive only:** `foul_diff` (AF − HF). It mixes player behaviour and referee decisions, so it is reported and interpreted but not used as a test.

All tests are two-sided with α = 0.05. A positive or null result is reported the same way as a negative one. For H1 and H1b, both unadjusted and Holm-adjusted p-values are reported.

## 2. Data

- **Source:** football-data.co.uk, Premier League (E0).
- **Analysis sample:** 2017/18–2022/23, 2,280 matches.
- **Crowd classification:** see `data/ghost_matches_sources.md`.
  - `ghost` = 2020-06-17 to 2021-05-23, except the matches listed in `data/partial_matches.csv`;
  - `partial` = the 35 listed matches;
  - every other match is full crowd.
- **Referee name fixes** (verified against match reports):
  - `l Mason` → `L Mason`
  - `A Moss` → `J Moss`
  - `S Scott` → `G Scott`
- **`cpf_diff` exclusion:** matches where either team has **≤ 2 fouls** (28 matches in all seasons) are excluded from `cpf_diff` analyses only. They stay in `card_diff` analyses.
- **Yellow-card definition:** football-data.co.uk's English yellow counts exclude the first yellow when a second yellow becomes a red. Used as is.

## 3. Main model

OLS, one row per match:

```
card_diff ~ ghost + partial + elo_diff + var + trend + C(referee)
cpf_diff  ~ ghost + partial + elo_diff + var + trend + C(referee)      (low_fouls == 0)
```

- **`elo_diff`:** home ELO − away ELO before the match.
  - ELO from results, k = 20, home advantage = 60.
  - Both parameters are fixed: they were chosen on 2011/12–2018/19 only (`notebooks/02_elo.ipynb`).
- **`var`:** 1 from 2019/20. **`trend`:** season number.
- **`C(referee)`:** referee fixed effects. The `ghost` effect is identified by comparing the same referee with and without fans.
- **Coefficient of interest:** `ghost` (ghost vs full crowd). `partial` is reported but not tested as a hypothesis.

## 4. Inference

- **Standard errors:** clustered by referee (33 referees in the sample; 19 of them refereed ghost matches).
- **Primary p-value:** wild cluster bootstrap by referee (`wildboottest`), with these settings:
  - Rademacher weights;
  - 9,999 draws;
  - null hypothesis imposed;
  - seed 2026.

  The conventional clustered p-value is reported alongside.
- **Minimum detectable effect:** MDE = 2.8 × clustered SE of `ghost` (80% power, α = 0.05, two-sided). It is reported next to each main estimate.

## 5. Robustness checks

Each check reports the `ghost` coefficient for both outcomes:

1. **Season fixed effects** instead of `var + trend`. The effect is then identified mainly from the 2019/20 restart, which is stated explicitly.
2. **Partial matches excluded.**
3. **VAR seasons only** (2019/20–2022/23).
4. **2020/21 ghost only:** the 92 ghost matches of the 2019/20 restart are excluded. The restart had different conditions: five substitutes, drinks breaks, a congested schedule.
5. **Poisson cards-per-foul model,** at team-match level with two rows per match:
   `yellows ~ away + away:ghost + away:partial + ghost + partial + team_elo_diff + var + trend + C(referee)`
   - offset = log(fouls); matches with `low_fouls == 1` excluded;
   - SEs clustered by referee;
   - coefficient of interest: `away:ghost`.

## 6. Placebo tests

**Sample:** pre-pandemic seasons 2012/13–2018/19. 2010/11–2011/12 are not used, because they warm up ELO.

**Model:**
`card_diff ~ placebo + elo_diff + trend + C(referee)`, and the same for `cpf_diff`.

1. **Season placebo (as in PLAN.md):** each season from 2014/15 to 2018/19 in turn is coded `placebo = 1`. That gives 5 estimates.
2. **Rolling-window placebo (added):** `placebo = 1` for a block of 437 consecutive matches, the same size as the real ghost group.
   - The block starts at every 10th match of the placebo sample, in date order.
   - Each block lies entirely within the sample.
   - This gives a distribution of roughly 220 estimates.

**Reporting:**
- the real `ghost` estimate is shown against the placebo distribution;
- the share of placebo estimates at least as extreme as the real one, in absolute value, is reported.

5 season placebos alone are too few for a distribution: the smallest possible share is 1/6. That is why the rolling version was added.

## 7. Descriptive statistics

For `card_diff`, `cpf_diff` and `foul_diff`:
- the mean in each crowd category (full / ghost / partial), on the 2017/18–2022/23 sample;
- 95% confidence intervals clustered by referee.
