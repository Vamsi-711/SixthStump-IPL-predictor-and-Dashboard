# SixthStump 🏏

**IPL 2026 Win Predictor & Dashboard**

> Built by [Vamsi Markandeya](https://yerra-vamsi-markandeya.vercel.app/)

---

## What is SixthStump?

SixthStump is a fully self-contained IPL 2026 cricket web app — no frameworks, no backend, no dependencies. It combines an AI-powered match outcome predictor with a complete IPL 2026 information hub, all wrapped in a bold brutalist editorial UI.

---

## Features

### 🏆 Win Predictor
- Select any two IPL 2026 teams to face off
- Configure match conditions — venue, pitch type, weather, toss outcome, and recent form for both sides
- Venue selection auto-populates the correct pitch type based on real ground characteristics
- Toss dropdown dynamically shows the names of the selected teams
- Probability engine calculates win likelihood using historical win rates, home advantage, toss + pitch interaction, dew factor, and current form
- Results display animated probability bars, a confidence ring meter, key factor chips, and a written AI analysis
- Confetti burst in the winning team's color on prediction

### 📊 Team Analysis Cards
- Appear automatically when a team is selected
- Show official IPL logo, captain, batting/bowling/consistency/experience skill bars (animated)
- IPL titles, win rate, average score, chase win percentage
- Colour-coded strengths and weaknesses tags
- Key player and overseas star callouts

### 📅 Schedule
- All Phase 1 fixtures (Matches 1–20, 28 Mar – 12 Apr 2026)
- Each row shows date, time, team logos, team codes, match number, and venue city
- Phase 2 fixture note included

### 👕 Squads
- Complete post-auction squads for all 10 IPL 2026 teams — 25 players each
- Sourced from the December 2025 Abu Dhabi auction results
- Each player card shows name, role (BAT / WK / AR / BOWL), price/status, and overseas badge
- **Captain card is highlighted** — inverted black background with gold price and ★ CAPTAIN badge
- Filter bar lets you switch between all 10 teams instantly
- Squad header shows team name, captain, coach, player count, and total budget

### 📊 Standings
- Points table shell for all 10 teams with official logos
- Ready to populate from Match 1 (28 March 2026) onwards

### ⚡ Season Stats
- 8 key IPL 2026 edition facts (84 matches, ₹237Cr auction spend, record Cameron Green buy, etc.)
- **Individual Player Stats leaderboards** — toggle between IPL 2025 (reference) and IPL 2026 (live from 28 Mar)
  - 🟠 Orange Cap (most runs)
  - 🟣 Purple Cap (most wickets)
  - 💥 Most Sixes
  - 🎯 Best Economy
  - ⚡ Best Strike Rate
  - 🤲 Most Catches
  - Animated progress bars in each team's brand color
- 6 key IPL 2026 storylines (Jadeja–Samson swap, Cameron Green record, RCB defending, Suryavanshi, expanded format, new venues)

---

## Design

**Style:** Brutalist editorial — inspired by raw newspaper layouts and vintage cricket scorecards

| Element | Detail |
|---|---|
| Background | Cream `#f5f0e4` with graph-paper grid texture |
| Accent | Hard red `#c8371a` |
| Ink | Near-black `#0f0e0a` |
| Borders | 3px solid black, no border-radius anywhere |
| Shadows | Hard 4px/6px offset box-shadows (no blur) |
| Display font | Kanit 900 |
| Mono/data font | IBM Plex Mono |
| Effects | Stamp-in result animation, slide transitions, confetti |

---

## Data

| Dataset | Source |
|---|---|
| Team logos | Official IPL CDN (`documents.iplt20.com`) |
| Squads | December 2025 Abu Dhabi Auction results |
| Schedule | BCCI / IPLT20 Phase 1 fixtures |
| IPL 2025 stats | Final season leaderboards |
| Win rates | IPL all-time records (2008–2025) |

---

## Teams Covered

| Team | Captain | Coach |
|---|---|---|
| Chennai Super Kings | Ruturaj Gaikwad | Stephen Fleming |
| Mumbai Indians | Hardik Pandya | Mark Boucher |
| Royal Challengers Bengaluru | Rajat Patidar | Andy Flower |
| Kolkata Knight Riders | Ajinkya Rahane | Abhishek Nayar |
| Sunrisers Hyderabad | Pat Cummins | Daniel Vettori |
| Delhi Capitals | KL Rahul | DC Staff |
| Punjab Kings | Shreyas Iyer | Ricky Ponting |
| Rajasthan Royals | Riyan Parag | Kumar Sangakkara |
| Gujarat Titans | Shubman Gill | Ashish Nehra |
| Lucknow Super Giants | Rishabh Pant | Justin Langer |

---

## Key Auction Highlights (Dec 2025)

- **Cameron Green** → KKR for ₹25.2Cr *(record overseas buy)*
- **Matheesha Pathirana** → KKR for ₹18Cr
- **Jadeja + Sam Curran** traded to RR; **Sanju Samson** traded to CSK
- **Prashant Veer + Kartik Sharma** → CSK for ₹14.2Cr each *(record uncapped)*
- **Jacob Bethell** → RCB for ₹13Cr
- **Liam Livingstone** → SRH for ₹13Cr
- **Josh Inglis** → LSG for ₹8.6Cr
- **Auqib Nabi Dar** → DC for ₹8.4Cr

---

## Tech Stack

```
HTML5          — Structure and markup
CSS3           — Brutalist styling, animations, grid layout
Vanilla JS     — All interactivity, data rendering, prediction engine
Google Fonts   — Kanit + IBM Plex Mono
IPL CDN        — Official team logos
No frameworks. No bundlers. No build step.
```

---

## How the Prediction Works

The win probability engine is a weighted factor model:

```
Base score     = historical IPL win rate (2008–2025)
Home boost     = ×1.13 if venue belongs to the team
Form weight    = ×(0.65 + form × 0.14)  [form: 1–5 scale]
Toss + pitch   = ×1.07–1.08 if toss decision matches pitch type
Dew penalty    = ×1.10 applied to the team bowling second
```

Both scores are then normalised to 100% and the confidence metric is derived from the margin between them.

---

## Running Locally

No build step needed. Just open the file:

```bash
# Option 1 — direct open
open ipl_brutalist.html

# Option 2 — local server (avoids any CORS issues with logos)
npx serve .
# or
python -m http.server 5500
```

---

## License

Built for personal and educational use. IPL team names, logos, and branding are property of the Board of Control for Cricket in India (BCCI). Player and match data sourced from publicly available records.

---

*SixthStump — Because the best prediction happens before the ball is bowled.*
