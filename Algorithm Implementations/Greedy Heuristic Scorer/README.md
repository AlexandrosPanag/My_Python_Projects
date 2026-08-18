# Persona Tycoon — Game Engine & Strategy Advisor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 👤 Author

**Alexandros Panagiotakopoulos**

---

## 📖 Overview

**P5X Tycoon** is a fully-featured Python implementation of Tycoon — the card game variant of Daifugo (大富豪) featured in *Persona 5: The Phantom X*. It ships with three distinct modes:

- **Full Game** — Play a live 3-round match where you manually enter your cards and your opponents' plays, assisted by a real-time strategy advisor.
- **Quick Advisor** — Instantly analyze any hand and table state and get an optimal play recommendation.
- **AI Simulation** — Watch four ruthless AI archetypes battle it out across a full match, with live play-by-play output and optional bulk statistical analysis across hundreds of games.

The engine enforces the complete P5X ruleset including Revolution, Counter-Revolution, 8-stops, Wonder cards, the 3♠ exception, Joker wildcards, and the full card trading system between rounds.

---

## ✨ Features

- **Full Rules Implementation** — Every P5X mechanic is enforced: rank order, set matching, Joker wildcards, 3♠ beats single Joker, Revolution via 4-of-a-kind, Counter-Revolution, 8-stop triggers (8 / 88 / 888), 8888 / 888+Joker double-trigger, Wonder card override, and card trading between rounds
- **Real-Time Strategy Advisor** — Scores every legal play using a multi-factor heuristic covering card efficiency, hand thinning, special effect bonuses, Joker conservation, and going-out priority
- **Four AI Archetypes** — Aggressive, Conservative, Opportunist, and Gambler — each with distinct scoring weights and playstyle logic
- **Bulk Simulation** — Run 10–1000 silent games and get aggregate win rates, Tycoon%, Beggar%, and average scores per archetype
- **Flexible Card Input** — Accepts suit symbols (♣♦♥♠) or letter shortcuts (C D H S), supports JK for Joker and WD for Wonder
- **Validation with Override** — Opponent plays are validated against the rules, with an option to force-accept if you observed something unusual
- **3-Round Match with Trading** — Full Tycoon/Rich → Beggar/Poor card trading between rounds

---

## 🎮 Mode Guide

### Mode 1 — Full Game

A live 3-round match where you are one of the four players.

**What you do:**
- Choose your seat position (1–4, assigned randomly in P5X)
- Enter your hand at the start of each round
- On your turn: type your play or `pass`
- On opponents' turns: type what they played or `pass`
- The advisor shows you the best play and top alternatives before each of your turns

**What the program tracks:**
- Revolution state
- All played cards (for hand estimation)
- Opponent hand size estimates
- Round scores and titles
- Card trading between rounds

---

### Mode 2 — Quick Advisor

No game tracking. Just enter your current hand and what's on the table, and get an instant recommendation.

**Useful for:** Mid-game consultation, testing play ideas, or learning which plays score well in a given situation.

---

### Mode 3 — AI Simulation

Four AI players battle through a full 3-round match. You watch.

**Speed options:**
- `Fast` — Instant output, no delays
- `Normal` — Short pauses for readability
- `Slow` — Dramatic per-play pauses, cinematic feel
- `Multi` — Run N silent games (10–1000) and print aggregate stats

**Multi-game output example:**
```
Archetype         Wins    Win%   AvgScore   Tycoon%   Beggar%
────────────────────────────────────────────────────────────
Conservative        27   27.0%       46.3      52.8%      12.5%
Gambler             25   25.0%       46.2      35.4%      23.1%
Aggressive          24   24.0%       42.1      37.5%      18.8%
Opportunist         24   24.0%       45.4      31.7%      22.2%
```

---

## 🃏 Card Input Format

| Card | Input Options |
|------|---------------|
| 3 of Spades | `3♠` or `3S` |
| 10 of Diamonds | `10♦` or `10D` |
| Jack of Hearts | `J♥` or `JH` |
| King of Clubs | `K♣` or `KC` |
| Joker | `JK` or `JOKER` |
| Wonder | `WD` or `WONDER` |

**Ranks:** `3 4 5 6 7 8 9 10 J Q K A 2`

**Suits:** `♣/C  ♦/D  ♥/H  ♠/S`

Multiple cards are space-separated:
```
3♠ 10♦ JH KC JK
```

To pass a turn, type `pass` or `p`.

---

## 📋 Rules Reference

### Card Strength (Normal Order)
```
Weakest → Strongest
3  4  5  6  7  8  9  10  J  Q  K  A  2  Joker
```

### Basic Rules
- You must play the **same number of cards** as the current table play
- Your play must **beat the table** in strength
- All non-Joker cards in a play must be the **same rank**
- Jokers act as **wildcards** to fill sets (e.g. two 10s + Joker = triple 10s)
- If you cannot or choose not to beat the table, **pass**
- When all other active players pass, the table clears and the last player leads

### Special Rules

| Trigger | Effect |
|---------|--------|
| **3♠** played on a single Joker | 3♠ wins — beats the Joker |
| **Wonder** (any table state) | Always valid, ends turn, you lead next |
| **8 / 88 / 888 / 8+Joker combos** | 8-stop — turn ends immediately, you lead next |
| **4-of-a-kind** | Revolution — card order flips (3 becomes strongest) |
| **4-of-a-kind during Revolution** | Counter-Revolution — order restored to normal |
| **8888 or 888+Joker** | 8-stop AND Counter-Revolution triggered simultaneously |

### Revolution
When Revolution is active, the strength order **reverses**:
```
Strongest → Weakest
3  4  5  6  7  8  9  10  J  Q  K  A  2  Joker
```
Joker remains above everything. Playing another 4-of-a-kind flips it back.

### Card Trading (Rounds 2 & 3)

| Trade | Cards |
|-------|-------|
| Beggar → Tycoon | 2 strongest cards |
| Tycoon → Beggar | 2 cards of their choice |
| Poor → Rich | 1 strongest card |
| Rich → Poor | 1 card of their choice |

---

## 🤖 Strategy Advisor

The advisor runs before every one of your turns in Mode 1, and on demand in Mode 2.

### How It Scores Plays

Each legal play receives a score based on:

- **Margin efficiency** — plays that barely beat the table score better than ones that massively overkill it
- **Hand thinning** — playing more cards at once is generally preferred
- **Going-out bonus** — plays that empty your hand score +200
- **Special effect bonuses** — 8-stop, Wonder, Revolution, 8888 all receive significant score bumps
- **Joker conservation** — Jokers are penalized unless no better option exists
- **High-card preservation** — 2s and Aces are penalized if the hand is still large
- **Pass threshold** — if the best play scores below the pass threshold, the advisor recommends passing instead

### Output Format

```
🤖 ADVISOR:
Play: 7♣ 7♥ 7♦
  Effective strength: 4  |  Cards remaining after: 10
  Score: 47.5
  Effects: 🔄 REVOLUTION – card order flipped! 3 becomes strongest
  Alternatives:
    7♣ 7♥ 🃏  (score 41.0)
    7♣ 7♦    (score 28.5)
```

---

## 🧠 AI Archetypes (Mode 3)

| Archetype | Description |
|-----------|-------------|
| **Aggressive** | Burns cards fast, loves triggering Revolutions, almost never passes, light on Joker conservation |
| **Conservative** | Hoards 2s and Jokers, passes readily, only strikes when the play is efficient |
| **Opportunist** | 8-stop specialist — heavily rewards blocking a player who's close to going out |
| **Gambler** | Adds random noise to every decision, high-variance chaos agent |

In Multi mode, archetypes are reshuffled randomly each game so seat position doesn't bias results.

---

## 🔍 Troubleshooting

### "Cannot parse card: '...'"

Check your input format. Common mistakes:

```
❌ 10 of Diamonds     (spaces not supported within a card)
✓  10D or 10♦

❌ Joker              (use JK or JOKER)
✓  JK

❌ 3s                 (lowercase suit)
✓  3S or 3♠
```

### "Invalid: Must play N card(s)"

You're trying to play a different number of cards than what's on the table. Match the count exactly or pass.

### "Invalid: Play strength X <= table Y"

Your play doesn't beat the current table. Either play stronger cards, use a Joker, or pass.

### Advisor recommends passing but I want to play

The advisor is a suggestion, not a command. Type your preferred play directly — it will be validated and executed if legal.

### Opponent play fails validation

The program will ask if you want to override. If you observed the play in-game and it was accepted, choose yes. This can happen with edge cases or unusual plugin interactions.

### Simulation hits safety limit

If a round hits 3000 iterations without finishing (extremely rare), it aborts and marks remaining players. This is a guard against degenerate game states and should not occur in normal play.

---

## 📊 Scoring System

At the end of each round, players are assigned titles based on finish order:

| Finish Position | Title | Points |
|-----------------|-------|--------|
| 1st | Tycoon | 30 |
| 2nd | Rich | 20 |
| 3rd | Poor | 10 |
| 4th | Beggar | 0 |

The player with the highest total points after 3 rounds wins the match.

---

## 💡 Tips & Strategy Notes

- **Low cards are your friends early.** Lead with your weakest singles and pairs to thin your hand before opponents establish control.
- **Save your Joker.** It wins almost any single or set, and as a wildcard it completes sets you'd otherwise miss. Don't burn it casually.
- **Revolution timing matters.** If you have a lot of low cards, triggering Revolution turns them into your strongest plays. If opponents are low on cards, it might not be worth the risk.
- **8-stops are control tools.** An 8-stop doesn't just end the turn — it hands you the lead. Use them to break dangerous momentum.
- **Wonder is always worth playing.** It bypasses the table entirely and gives you the next lead. Never pass when you hold a Wonder.
- **Track opponent hand counts.** The program shows estimated counts — when someone drops to 3–4 cards, prioritize disruption (8-stops, Wonder) over efficiency.
- **Trading is deterministic for Beggar/Poor.** As Beggar you must give your 2 strongest — plan your Round 2/3 strategy knowing this.

---

## ⚖️ License

**Copyright © 2026 Alexandros Panagiotakopoulos. All Rights Reserved.**

Licensed under the MIT License. You are free to use, modify, and distribute this software for any purpose with attribution.
