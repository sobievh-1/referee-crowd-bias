# CLAUDE.md — referee-crowd-bias

## Project
Does crowd presence make Premier League referees penalise away teams more harshly?
Natural experiment: matches without fans during COVID-19 (2019/20 restart, most of 2020/21).
Full plan: see PLAN.md (in Polish). Follow it; if something in the plan looks wrong, say so before changing direction.

## The user
Szymon, SGH student and active football referee. Python level: beginner, learning on this project.
Talk to him in Polish. Code, comments, README and figures in English.

## How to work
- You write the code AND explain it. After each non-trivial block, give a short plain-language explanation in Polish: what it does and why this approach.
- Prefer simple, readable pandas over clever one-liners. No new library without saying why.
- Work in small steps that run. Show the output (head, shape, counts) after each data step.
- Never edit files in data/raw/. Derived data goes to data/processed/.
- Every number that ends up in README must come from a notebook cell that produces it.
- Before running the main ghost-vs-crowd comparison, check whether PREREGISTRATION.md exists; if not, remind the user once.
- When a statistical choice is made (fixed effects, clustering, bootstrap, placebo), add one sentence the user could say in a job interview to justify it.
- If data looks suspicious (missing referees, odd card counts, duplicate matches), stop and flag it instead of silently fixing.

## Data notes
- Source: football-data.co.uk, E0.csv per season. Columns used: Date, HomeTeam, AwayTeam, FTHG, FTAG, Referee, HF, AF, HY, AY, HR, AR.
- English yellow-card counts exclude the first yellow when a second yellow converts to red.
- ghost/partial classification is manual; sources documented in data/ghost_matches_sources.md.
