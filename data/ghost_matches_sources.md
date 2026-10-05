# Ghost / partial match classification — sources

Manual classification of Premier League matches, researched 2026-10-05:

- `ghost`: played behind closed doors
- `partial`: played with limited attendance (2,000 in December 2020; up to 10,000 or 25% of capacity in May 2021)
- otherwise: full stadiums

The partial matches are listed one by one in [`partial_matches.csv`](partial_matches.csv) with their official attendance and match-page source.
The rule used in `notebooks/01_data.ipynb`:

> `ghost = 1` if the match was played between **2020-06-17** and **2021-05-23** and is **not** in `partial_matches.csv`.

## How it was checked

1. **Official Premier League match data.** The premierleague.com match centre (`https://www.premierleague.com/match/<id>`) was checked for the attendance of all 760 matches of 2019/20 and 2020/21.
2. **Wikipedia club-season articles.** All 20 clubs' season pages for 2019/20 to 2022/23 were checked, giving most matches an attendance figure from two pages (home and away club).
3. **Press reports.** Each December 2020 match with fans and each rule change was checked against a news or club source.

Sources 1 and 2 agree on which matches had fans, all 35 of them. They differ only on a few May 2021 head-counts.

Cross-check against football-data.co.uk: all 760 matches matched on season, home team and away team, and all dates were identical.

## Date ranges

| Period | Status | Matches | Source |
|---|---|---|---|
| 2019-08-09 – 2020-03-09 | full crowd | 288 | Official data: every match has attendance > 0. Last match with fans before suspension: Leicester v Aston Villa, 2020-03-09 ([PL](https://www.premierleague.com/match/46889)) |
| 2020-06-17 – 2020-07-26 | **ghost**: all restart matches | 92 | Official data: no attendance; Wikipedia: "0" / "Behind closed doors" |
| 2020-09-12 – 2020-12-01 | **ghost** | 98 | Return of fans planned for 1 Oct 2020 was paused on 22 Sep 2020 ([Jakarta Post / AFP](https://www.thejakartapost.com/news/2020/09/22/plans-to-allow-fans-back-into-stadiums-paused-due-to-virus-spike)); no league pilot events took place |
| 2020-12-02 – 2020-12-30 | **mixed**: 15 partial, 42 ghost | 57 | See below |
| 2020-12-31 – 2021-05-16 | **ghost** | 205 | Liverpool City Region in tier 3 from 31 Dec ([TNT Sports](https://www.tntsports.co.uk/football/premier-league/2020-2021/liverpool-and-everton-to-play-premier-league-games-behind-closed-doors-in-tier-3_sto8049403/story.shtml)), national lockdown from 5 Jan 2021 |
| 2021-05-18 – 2021-05-23 | **partial**: all 20 matches of the last two rounds, home fans only | 20 | Step 3 of the roadmap: up to 10,000 or 25% ([Sports Think Tank](https://www.sportsthinktank.com/news/2021/05/boris-johnson-confirms-up-to-10000-fans-allowed-at-sports-stadiums-from-17-may)); home fans only ([Cyprus Mail / Reuters](https://cyprus-mail.com/2021/05/05/home-fans-only-for-final-two-premier-league-matches)) |
| 2021/22 – 2022/23 | full crowd | – | Season opened with full stadiums on 2021-08-13 ([Cyprus Mail](https://cyprus-mail.com/2021/08/13/5-talking-points-as-premier-league-set-to-return-with-packed-stadiums)); no closed-door matches found |

Seasons 2010/11–2018/19: full crowds (before the pandemic).

### December 2020 in detail

- From 2 Dec 2020, clubs in **tier 2** areas could admit 2,000 fans. That covered Arsenal, Chelsea, Crystal Palace, Fulham, Tottenham, West Ham, Liverpool, Everton, Brighton and Southampton ([The Stadium Business](https://www.thestadiumbusiness.com/2020/11/26/half-of-premier-league-clubs-set-to-welcome-back-fans/)). All other clubs were in tier 3 (no fans).
- London went to tier 3 from 16 Dec 2020. Arsenal v Southampton, Fulham v Brighton and West Ham v Crystal Palace on 16 Dec were behind closed doors ([TNT Sports](https://www.tntsports.co.uk/football/premier-league/2020-2021/london-s-tier-3-move-puts-arsenal-vs-southampton-behind-closed-doors-4-pl-clubs-can-have-fans_sto8033246/story.shtml)).
- Brighton and Southampton went to tier 4 from 26 Dec 2020 ([Sky Sports](https://skysports.com/football/news/11661/12171387/southampton-and-brighton-to-enter-tier-4-from-boxing-day)).
- Every home match of an eligible club, played while it was eligible, had fans.

## Caveats

- **May 2021 head-counts** differ between sources for seven matches. Wikipedia often shows the cap rather than the actual crowd, so the official figures are used. Fulham v Newcastle (2021-05-23) is recorded as 2,000 officially and on ESPN, but as 10,000 on Fulham's Wikipedia page. Fans were present either way, so the classification is unaffected.
- **Away fans in December 2020**: press reports describe home supporters only, but no explicit rule banning away fans was found. For May 2021, home-fans-only is confirmed.
- **December attendance** is officially 2,000 for every match, which is the cap. It may not be an actual turnstile count.
- BBC and Guardian pages could not be accessed during the research. Other outlets were used instead.
