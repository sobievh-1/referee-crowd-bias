"""Simple ELO ratings for Premier League teams, computed from match results only.

How it works:
- Every team starts at 1500 in the first season of the data.
- Before each match, the home team's expected score is
      E = 1 / (1 + 10 ** (-(R_home + HOME_ADVANTAGE - R_away) / 400))
- The actual score S is 1 (home win), 0.5 (draw) or 0 (away win).
- After the match: R_home += K * (S - E), R_away -= K * (S - E).
- Promoted teams (not in the previous Premier League season) enter with the average
  end-of-season rating of the teams that were relegated, since our data only covers
  the Premier League.

We store the ratings *before* each match, so they only use information from earlier matches.
"""

import pandas as pd

START_RATING = 1500


def expected_home_score(home_rating, away_rating, home_advantage):
    """Probability-like expected score for the home team (0 to 1)."""
    return 1 / (1 + 10 ** (-(home_rating + home_advantage - away_rating) / 400))


def actual_home_score(home_goals, away_goals):
    if home_goals > away_goals:
        return 1.0
    if home_goals == away_goals:
        return 0.5
    return 0.0


def compute_elo(matches, k=20, home_advantage=60):
    """Compute ELO ratings through all seasons.

    `matches` needs columns: season_start, Date, HomeTeam, AwayTeam, FTHG, FTAG.

    Returns two tables:
    - a copy of `matches` with pre-match columns home_elo, away_elo, elo_diff and
      expected_home (the model's expected home score),
    - end-of-season ratings: one row per (season_start, team).
    """
    # Play matches in time order; kind="stable" keeps the file order for same-day matches
    matches = matches.sort_values(["season_start", "Date"], kind="stable").copy()

    ratings = {}
    previous_teams = set()
    home_elo, away_elo, expected = [], [], []
    season_end = []

    for season, season_matches in matches.groupby("season_start", sort=True):
        teams = set(season_matches["HomeTeam"]) | set(season_matches["AwayTeam"])

        if not ratings:
            # First season: everyone starts equal
            for team in teams:
                ratings[team] = START_RATING
        else:
            relegated = previous_teams - teams
            promoted = teams - previous_teams
            entry_rating = sum(ratings[t] for t in relegated) / len(relegated)
            for team in promoted:
                ratings[team] = entry_rating

        for row in season_matches.itertuples():
            r_home = ratings[row.HomeTeam]
            r_away = ratings[row.AwayTeam]
            e_home = expected_home_score(r_home, r_away, home_advantage)

            home_elo.append(r_home)
            away_elo.append(r_away)
            expected.append(e_home)

            change = k * (actual_home_score(row.FTHG, row.FTAG) - e_home)
            ratings[row.HomeTeam] = r_home + change
            ratings[row.AwayTeam] = r_away - change

        for team in teams:
            season_end.append({"season_start": season, "team": team, "elo": ratings[team]})
        previous_teams = teams

    matches["home_elo"] = home_elo
    matches["away_elo"] = away_elo
    matches["elo_diff"] = matches["home_elo"] - matches["away_elo"]
    matches["expected_home"] = expected

    season_end = pd.DataFrame(season_end).sort_values(["season_start", "elo"], ascending=[True, False])
    return matches, season_end.reset_index(drop=True)

