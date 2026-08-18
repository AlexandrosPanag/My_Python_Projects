#!/usr/bin/env python3
## Created by Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# CC BY-SA 4.0
# Date: 18-08-2026
"""
P5X Tycoon - Full game engine + optimal strategy advisor
Rules: Persona 5 The Phantom X version of Daifugo (大富豪)
"""

import random
import itertools
from copy import deepcopy
from collections import defaultdict

# ─────────────────────────────────────────
# CARD CONSTANTS
# ─────────────────────────────────────────

RANKS = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
SUITS = ['♣','♦','♥','♠']

# Normal strength order (index = strength, higher = stronger)
NORMAL_ORDER = {r: i for i, r in enumerate(RANKS)}
# Jokers sit above everything
JOKER_STRENGTH = 100
# 3♠ beats Joker only in specific context (single Joker on table)

TITLE_NAMES  = ['Tycoon', 'Rich', 'Poor', 'Beggar']
TITLE_POINTS = {'Tycoon': 30, 'Rich': 20, 'Poor': 10, 'Beggar': 0}

# ─────────────────────────────────────────
# CARD REPRESENTATION
# ─────────────────────────────────────────

class Card:
    def __init__(self, rank, suit=None):
        """rank: '3'-'2', 'J','Q','K','A', or 'JOKER'; suit: '♣♦♥♠' or None"""
        self.rank = rank
        self.suit = suit
        self.is_joker = (rank == 'JOKER')

    def strength(self, revolution=False):
        if self.is_joker:
            return JOKER_STRENGTH
        base = NORMAL_ORDER.get(self.rank, -1)
        if revolution:
            # Flip: 3 becomes strongest (12), 2 becomes weakest (0)
            # range 0-12 => reversed
            return (len(RANKS) - 1) - base
        return base

    def is_three_spades(self):
        return self.rank == '3' and self.suit == '♠'

    def is_eight(self):
        return self.rank == '8'

    def is_wonder(self):
        return self.rank == 'WONDER'

    def __repr__(self):
        if self.is_joker:
            return "🃏"
        if self.rank == 'WONDER':
            return "✨WONDER"
        return f"{self.rank}{self.suit}"

    def __eq__(self, other):
        if not isinstance(other, Card): return False
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))

    def short(self):
        if self.is_joker: return "JK"
        if self.rank == 'WONDER': return "WD"
        return f"{self.rank}{self.suit}"


def parse_card(s):
    """Parse a string like '3♠', '10♦', 'JK', 'WD', 'K♥' into a Card."""
    s = s.strip()
    if s.upper() in ('JK', 'JOKER'):
        return Card('JOKER')
    if s.upper() in ('WD', 'WONDER'):
        return Card('WONDER')
    # Try rank + suit
    suit_map = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠',
                '♣': '♣', '♦': '♦', '♥': '♥', '♠': '♠'}
    rank_tokens = ['10','J','Q','K','A','2','3','4','5','6','7','8','9']
    rank = None
    suit = None
    for rt in sorted(rank_tokens, key=len, reverse=True):
        if s.upper().startswith(rt.upper()):
            rank = rt
            rest = s[len(rt):]
            if rest.upper() in suit_map:
                suit = suit_map[rest.upper()]
            break
    if rank is None:
        raise ValueError(f"Cannot parse card: '{s}'")
    return Card(rank, suit)


def parse_hand(s):
    """Parse space-separated card strings into a list of Cards."""
    parts = s.strip().split()
    return [parse_card(p) for p in parts]


def full_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(Card(rank, suit))
    deck.append(Card('JOKER'))
    deck.append(Card('JOKER'))
    return deck


# ─────────────────────────────────────────
# HAND PLAY VALIDATION
# ─────────────────────────────────────────

def effective_rank(play, revolution=False):
    """
    Returns the effective strength of a play (list of Cards).
    For mixed plays (e.g. two 10s + Joker), all non-joker cards define rank;
    Jokers fill in. Returns the numerical strength.
    """
    non_joker = [c for c in play if not c.is_joker and not c.is_wonder()]
    if not non_joker:
        # All jokers – joker pair etc
        return JOKER_STRENGTH
    base_rank = non_joker[0].rank
    return Card(base_rank).strength(revolution)


def is_valid_play(play, table_play, revolution=False):
    """
    Check if `play` (list of Cards) legally beats `table_play` (list of Cards | None).
    Returns (bool, reason_str)
    """
    if not play:
        return False, "Empty play"

    # Wonder: always valid, bypasses all rules
    if any(c.is_wonder() for c in play):
        if len(play) == 1:
            return True, "Wonder"
        return False, "Wonder must be played alone"

    # Must be all same rank (or joker fills)
    non_joker = [c for c in play if not c.is_joker]
    if len(set(c.rank for c in non_joker)) > 1:
        return False, "Cards must all be same rank"

    if table_play is None:
        # Opening play, anything goes
        return True, "Opening"

    # Wonder on table: can't beat wonder (wonder just ends turn)
    if any(c.is_wonder() for c in table_play):
        return False, "Can't beat a Wonder"

    # Must match count
    if len(play) != len(table_play):
        return False, f"Must play {len(table_play)} card(s)"

    table_eff = effective_rank(table_play, revolution)
    play_eff  = effective_rank(play, revolution)

    # 3 of Spades special: beats single Joker
    if (len(table_play) == 1 and table_play[0].is_joker
            and len(play) == 1 and play[0].is_three_spades()):
        return True, "3♠ beats Joker"

    # Joker is always stronger (unless 3♠ rule above)
    if table_play[0].is_joker and not play[0].is_joker:
        return False, "Can't beat Joker"

    if play_eff <= table_eff:
        return False, f"Play strength {play_eff} <= table {table_eff}"

    return True, "Valid"


# ─────────────────────────────────────────
# SPECIAL TRIGGERS
# ─────────────────────────────────────────

def check_8stop(play):
    """Returns True if the play triggers an 8-stop."""
    non_joker = [c for c in play if not c.is_joker]
    eights = [c for c in non_joker if c.is_eight()]
    jokers = [c for c in play if c.is_joker]
    # All cards are 8s or jokers
    return len(eights) + len(jokers) == len(play) and len(eights) > 0


def check_wonder(play):
    return len(play) == 1 and play[0].is_wonder()


def check_revolution(play):
    """4 of a kind (including jokers filling in) = Revolution"""
    return len(play) == 4


def check_counter_revolution(play, table_play, revolution):
    """Counter-revolution: another 4-of-a-kind that beats the revolution 4-of-a-kind."""
    if not revolution:
        return False
    return len(play) == 4 and len(table_play) == 4


def check_8888_or_888joker(play):
    """8888 or 888+Joker = instant revolution counter-revolution (special replay + rev)"""
    if len(play) != 4:
        return False
    eights  = sum(1 for c in play if c.is_eight())
    jokers  = sum(1 for c in play if c.is_joker)
    return eights + jokers == 4 and eights >= 3 and jokers <= 1


def check_triple8(play):
    """888 or 88+Joker = 8-stop AND revolution trigger (per your rules)"""
    # Actually per your spec: "8" or "88" or "888" triggers immediate replay
    # So ANY 8-stop triggers replay. Let's handle 8-stop as replay.
    return check_8stop(play)


# ─────────────────────────────────────────
# GAME STATE
# ─────────────────────────────────────────

class GameState:
    def __init__(self):
        self.round_num    = 0
        self.scores       = [0, 0, 0, 0]   # indexed by seat (0-3)
        self.titles       = [None]*4        # 'Tycoon','Rich','Poor','Beggar'
        self.player_names = ['P1','P2','P3','P4']
        self.user_seat    = 0              # which seat is the human

        # Per-round state
        self.hands        = [[], [], [], []]
        self.has_wonder   = [False]*4
        self.finished     = [False]*4      # finished this round
        self.finish_order = []             # seats in order they emptied hand

        # Turn state
        self.current_player  = 0
        self.table_play      = None        # last played cards
        self.table_player    = None        # who played them
        self.revolution      = False
        self.pass_count      = 0
        self.last_played_by  = None

        # Card tracking
        self.played_cards    = []          # all cards played so far in round
        self.hand_counts     = [13,13,13,13]  # estimated cards per player

    def card_strength(self, card):
        return card.strength(self.revolution)

    def remaining_deck(self):
        """Cards NOT in my hand and NOT played yet."""
        all_cards = set()
        for suit in SUITS:
            for rank in RANKS:
                all_cards.add(Card(rank, suit))
        all_cards.add(Card('JOKER'))
        all_cards.add(Card('JOKER'))
        played_set = self.played_cards[:]
        my_hand    = self.hands[self.user_seat]
        unknown = []
        for c in full_deck():
            if c in my_hand:
                continue
            # Check played
            found = False
            for p in played_set:
                if p.rank == c.rank and p.suit == c.suit:
                    played_set.remove(p)
                    found = True
                    break
            if not found:
                unknown.append(c)
        return unknown


# ─────────────────────────────────────────
# STRATEGY / ADVISOR ENGINE
# ─────────────────────────────────────────

def group_by_rank(hand):
    """Returns dict {rank: [cards]} sorted by strength."""
    groups = defaultdict(list)
    for c in hand:
        if c.is_joker:
            groups['JOKER'].append(c)
        elif c.is_wonder():
            groups['WONDER'].append(c)
        else:
            groups[c.rank].append(c)
    return groups


def get_all_legal_plays(hand, table_play, revolution=False):
    """
    Generate all legal plays from hand given current table state.
    Returns list of plays (each play = list of Cards).
    """
    legal = []
    n = len(table_play) if table_play else None

    # Wonder
    for c in hand:
        if c.is_wonder():
            legal.append([c])

    if n is None:
        # Opening: any single, pair, triple, quad, or wonder
        groups = group_by_rank(hand)
        jokers = groups.get('JOKER', [])
        for rank, cards in groups.items():
            if rank in ('JOKER', 'WONDER'):
                continue
            for size in range(1, min(5, len(cards) + len(jokers) + 1)):
                if size > len(hand):
                    break
                # cards + however many jokers needed
                needed_jokers = max(0, size - len(cards))
                if needed_jokers <= len(jokers):
                    play = cards[:min(size, len(cards))] + jokers[:needed_jokers]
                    if len(play) == size:
                        ok, _ = is_valid_play(play, None, revolution)
                        if ok:
                            legal.append(play)
        # Joker alone or pair
        if len(jokers) >= 1:
            legal.append([jokers[0]])
        if len(jokers) >= 2:
            legal.append(jokers[:2])
        return legal

    # Table has cards
    groups = group_by_rank(hand)
    jokers = groups.get('JOKER', [])

    # Try each rank combo of size n
    for rank, cards in groups.items():
        if rank in ('JOKER', 'WONDER'):
            continue
        for size in range(1, n + 1):
            for combo in itertools.combinations(cards, size):
                jokers_needed = n - size
                if jokers_needed < 0 or jokers_needed > len(jokers):
                    continue
                play = list(combo) + jokers[:jokers_needed]
                if len(play) == n:
                    ok, _ = is_valid_play(play, table_play, revolution)
                    if ok:
                        legal.append(play)

    # All jokers of size n
    if len(jokers) >= n:
        play = jokers[:n]
        ok, _ = is_valid_play(play, table_play, revolution)
        if ok:
            legal.append(play)

    # 3♠ beats single Joker
    if (n == 1 and table_play and len(table_play) == 1 and table_play[0].is_joker):
        for c in hand:
            if c.is_three_spades():
                legal.append([c])

    return legal


def score_play(play, hand, state, opponent_counts):
    """
    Heuristic score for a play. Higher = better.
    Considers:
      - Card value (prefer playing low cards, save high)
      - Special effects (8-stop, revolution, counter-rev)
      - Hand thinning progress
      - Revolution state alignment
      - Whether we need to save a certain number of cards
    """
    score = 0
    rev = state.revolution

    if not play:
        return -9999

    eff = effective_rank(play, rev)
    n   = len(play)

    # Base: penalize using high-value cards wastefully
    # We want to use cards just strong enough to beat the table
    if state.table_play:
        table_eff = effective_rank(state.table_play, rev)
        margin = eff - table_eff
        # Smaller margin = better (efficient use)
        score -= margin * 2

    # Playing more cards at once is good (empties hand faster)
    score += n * 5

    # Hand size after play
    remaining = len(hand) - n
    score += max(0, (13 - remaining))  # bonus for smaller remaining hand

    # Wonder: always great, ends turn and we go next
    if any(c.is_wonder() for c in play):
        score += 50

    # 8-stop: good for controlling turn, especially if hand is good
    if check_8stop(play):
        score += 30
        # Even better if we have many low cards that can now lead
        low_cards = sum(1 for c in hand if not c.is_joker and not c.is_wonder()
                        and c.strength(rev) < 5)
        score += low_cards * 3

    # Revolution via 4-of-a-kind
    if check_revolution(play) or check_counter_revolution(play, state.table_play or [], rev):
        # If currently losing (many cards), revolution can help
        my_cards = len(hand)
        score += 25
        if my_cards > 8:
            score += 20  # big swing needed

    # 8888 / 888Joker (special double trigger)
    if check_8888_or_888joker(play):
        score += 60

    # Penalize using Jokers unless no other option
    jokers_used = sum(1 for c in play if c.is_joker)
    score -= jokers_used * 8

    # Penalize using 2s unless late game
    remaining_after = len(hand) - n
    twos_used = sum(1 for c in play if c.rank == '2')
    if remaining_after > 3:
        score -= twos_used * 10

    # Prefer plays that set us up to empty hand
    if remaining == 0:
        score += 200  # going out!

    # Prefer plays that end with low cards next (don't strand high)
    hand_after = [c for c in hand if c not in play]
    if hand_after:
        avg_str = sum(c.strength(rev) for c in hand_after
                      if not c.is_joker and not c.is_wonder()) / max(1, len(hand_after))
        score -= avg_str * 0.5

    return score


def suggest_play(state):
    """
    Main advisor function. Returns (recommended_play, explanation).
    recommended_play = list of Cards, or [] for PASS.
    """
    hand = state.hands[state.user_seat]
    table = state.table_play
    rev   = state.revolution

    legal = get_all_legal_plays(hand, table, rev)

    if not legal:
        return [], "No legal plays available — must PASS."

    # Estimate opponent card counts (non-finished players)
    opp_counts = {}
    for seat in range(4):
        if seat != state.user_seat and not state.finished[seat]:
            opp_counts[seat] = state.hand_counts[seat]

    # Score each play
    scored = []
    for play in legal:
        s = score_play(play, hand, state, opp_counts)
        scored.append((s, play))

    scored.sort(key=lambda x: x[0], reverse=True)

    best_score, best_play = scored[0]

    # Should we pass instead?
    # Pass is smart when: we have only high-value cards and don't want to waste them
    pass_score = 0  # baseline
    if table is not None:
        table_eff = effective_rank(table, rev)
        # If table is already very high, passing saves cards
        if table_eff > 10:
            pass_score = 5

    if best_score < pass_score and table is not None:
        return [], "Better to PASS — all plays would waste strong cards."

    # Build explanation
    effects = []
    if check_wonder(best_play):
        effects.append("✨ WONDER – ends turn, you lead next")
    if check_8stop(best_play) and not check_8888_or_888joker(best_play):
        effects.append("🛑 8-STOP – ends turn immediately, you lead next")
    if check_8888_or_888joker(best_play):
        effects.append("💥 8888/888JK – 8-stop + counter-revolution triggered!")
    elif check_revolution(best_play) and not check_counter_revolution(best_play, table or [], rev):
        effects.append("🔄 REVOLUTION – card order flipped! 3 becomes strongest")
    elif check_counter_revolution(best_play, table or [], rev):
        effects.append("🔄 COUNTER-REVOLUTION – order restored to normal")

    eff = effective_rank(best_play, rev)
    hand_after = len(hand) - len(best_play)
    explanation = (
        f"Play: {' '.join(str(c) for c in best_play)}\n"
        f"  Effective strength: {eff}  |  Cards remaining after: {hand_after}\n"
        f"  Score: {best_score:.1f}\n"
    )
    if effects:
        explanation += "  Effects: " + ", ".join(effects) + "\n"

    # Show top 3 alternatives
    if len(scored) > 1:
        explanation += "  Alternatives:\n"
        for sc, pl in scored[1:min(4, len(scored))]:
            explanation += f"    {' '.join(str(c) for c in pl)}  (score {sc:.1f})\n"

    return best_play, explanation


# ─────────────────────────────────────────
# UI HELPERS
# ─────────────────────────────────────────

def clear_line():
    print()

def print_banner(text):
    w = 60
    print("=" * w)
    print(f"  {text}")
    print("=" * w)

def print_section(text):
    print(f"\n{'─'*50}")
    print(f"  {text}")
    print('─'*50)

def display_hand(hand, label="Your hand"):
    groups = defaultdict(list)
    for c in hand:
        groups[c.rank].append(c)
    cards_str = "  ".join(str(c) for c in sorted(hand, key=lambda c: c.strength()))
    print(f"{label} [{len(hand)} cards]: {cards_str}")

def display_state(state, players):
    print_section("GAME STATE")
    print(f"Round: {state.round_num+1}/3  |  Revolution: {'🔄 ACTIVE' if state.revolution else 'Normal'}")
    for i, name in enumerate(state.player_names):
        you = " ← YOU" if i == state.user_seat else ""
        fin = " [DONE]" if state.finished[i] else ""
        title = f" ({state.titles[i]})" if state.titles[i] else ""
        cards = len(state.hands[i]) if i == state.user_seat else state.hand_counts[i]
        wonder = " ✨" if state.has_wonder[i] else ""
        print(f"  {name}{you}{title}{fin}{wonder}: {cards} cards | Score: {state.scores[i]}")
    print()
    if state.table_play:
        table_str = " ".join(str(c) for c in state.table_play)
        eff = effective_rank(state.table_play, state.revolution)
        print(f"  Table: {table_str}  (strength {eff})")
    else:
        print("  Table: (empty – opening move)")
    display_hand(state.hands[state.user_seat])
    print()

def prompt_cards(prompt_text, allow_empty=False):
    """Prompt user to enter cards. Returns list of Card objects."""
    while True:
        try:
            raw = input(prompt_text).strip()
            if raw.lower() in ('pass', 'p', ''):
                if allow_empty:
                    return []
                else:
                    print("  (cannot be empty here)")
                    continue
            return parse_hand(raw)
        except ValueError as e:
            print(f"  Parse error: {e}")
            print("  Format: rank+suit, e.g.  3♠ or 3S  10♦ or 10D  JK  WD")
            print("  Ranks: 3 4 5 6 7 8 9 10 J Q K A 2 | Suits: ♣/C ♦/D ♥/H ♠/S | JK=Joker WD=Wonder")


def prompt_yes_no(question):
    while True:
        ans = input(f"{question} (y/n): ").strip().lower()
        if ans in ('y', 'yes'): return True
        if ans in ('n', 'no'): return False


def prompt_seat():
    print("\nWhich seat position are you? (this is random in P5X)")
    print("  Seat order matters for turn order (clockwise).")
    while True:
        try:
            raw = input("Your seat [1/2/3/4]: ").strip()
            seat = int(raw) - 1
            if 0 <= seat <= 3:
                return seat
            print("  Enter 1, 2, 3, or 4.")
        except ValueError:
            print("  Enter a number.")


def prompt_player_names(user_seat):
    print("\nOptional: give names to other players (or press Enter to keep default).")
    names = ['P1', 'P2', 'P3', 'P4']
    names[user_seat] = 'YOU'
    for i in range(4):
        if i == user_seat:
            continue
        raw = input(f"  Name for Seat {i+1} [default {names[i]}]: ").strip()
        if raw:
            names[i] = raw
    return names


# ─────────────────────────────────────────
# ROUND SETUP
# ─────────────────────────────────────────

def setup_round(state):
    """Deal cards and handle trading."""
    state.finished    = [False]*4
    state.finish_order = []
    state.table_play  = None
    state.table_player= None
    state.revolution  = False
    state.pass_count  = 0
    state.played_cards = []

    print_section(f"ROUND {state.round_num+1} SETUP")

    if state.round_num == 0:
        # First round: distribute randomly
        deck = full_deck()
        random.shuffle(deck)
        for seat in range(4):
            state.hands[seat] = deck[seat*13:(seat+1)*13 + (2 if seat == 3 else 0)]
        # Actually deal 13 each, remaining 2 jokers... let's do 13+13+13+13+2joker
        # Proper: 54 cards / 4 = 13 each + 2 remaining -> give to last two
        deck2 = full_deck()
        random.shuffle(deck2)
        per = len(deck2) // 4
        for seat in range(4):
            state.hands[seat] = deck2[seat*per:(seat+1)*per]
        # Leftover
        leftover = deck2[4*per:]
        for i, c in enumerate(leftover):
            state.hands[i % 4].append(c)

        # In P5X you enter YOUR hand manually
        print(f"\nYou are Seat {state.user_seat+1} ({state.player_names[state.user_seat]})")
        print("Enter YOUR hand (the cards you can see in game):")
        print("  Format: 3♠ 10♦ JK WD etc. (space-separated)")
        while True:
            my_hand = prompt_cards("  Your cards: ")
            if my_hand:
                state.hands[state.user_seat] = my_hand
                break
            print("  Hand cannot be empty.")

        # Wonders
        state.has_wonder = [False]*4
        for seat in range(4):
            has_w = any(c.is_wonder() for c in state.hands[seat])
            if seat == state.user_seat:
                state.has_wonder[seat] = has_w
            else:
                ans = prompt_yes_no(f"  Does {state.player_names[seat]} have a WONDER card?")
                state.has_wonder[seat] = ans
                if ans and not any(c.is_wonder() for c in state.hands[seat]):
                    state.hands[seat].append(Card('WONDER'))

        # Estimate other players' hand sizes
        for seat in range(4):
            state.hand_counts[seat] = len(state.hands[seat])

    else:
        # Subsequent rounds: trading
        _do_trading(state)

    # Determine who starts
    if state.round_num == 0:
        # Player with 3♦ starts
        start_seat = state.user_seat  # default
        for seat in range(4):
            if any(c.rank == '3' and c.suit == '♦' for c in state.hands[seat]):
                start_seat = seat
                break
        # If 3♦ is unknown (other players), ask
        has_3d = any(c.rank == '3' and c.suit == '♦' for c in state.hands[state.user_seat])
        if not has_3d:
            print("\n3♦ determines who goes first.")
            while True:
                try:
                    raw = input("  Which seat has the 3♦? [1/2/3/4]: ").strip()
                    start_seat = int(raw) - 1
                    if 0 <= start_seat <= 3:
                        break
                except ValueError:
                    pass
        print(f"\n→ {state.player_names[start_seat]} (Seat {start_seat+1}) goes first (has 3♦)")
        state.current_player = start_seat
    else:
        # Beggar starts subsequent rounds
        beggar_seat = next((i for i, t in enumerate(state.titles) if t == 'Beggar'), 0)
        state.current_player = beggar_seat
        print(f"\n→ {state.player_names[beggar_seat]} (Beggar) starts this round")


def _do_trading(state):
    """Handle card trading at start of rounds 2 and 3."""
    print_section("CARD TRADING")
    tycoon_seat = next((i for i, t in enumerate(state.titles) if t == 'Tycoon'), None)
    rich_seat   = next((i for i, t in enumerate(state.titles) if t == 'Rich'), None)
    poor_seat   = next((i for i, t in enumerate(state.titles) if t == 'Poor'), None)
    beggar_seat = next((i for i, t in enumerate(state.titles) if t == 'Beggar'), None)

    us = state.user_seat

    if tycoon_seat is not None and beggar_seat is not None:
        print(f"  Tycoon ({state.player_names[tycoon_seat]}) ↔ Beggar ({state.player_names[beggar_seat]}): 2 cards")
        if beggar_seat == us:
            # We are beggar: give 2 strongest
            my_hand = sorted(state.hands[us], key=lambda c: c.strength(state.revolution), reverse=True)
            give = my_hand[:2]
            print(f"  You MUST give your 2 strongest cards: {' '.join(str(c) for c in give)}")
            for c in give:
                state.hands[us].remove(c)
            print("  Tycoon gives you 2 cards. Enter them:")
            received = prompt_cards("  Cards received from Tycoon: ")
            state.hands[us].extend(received)
        elif tycoon_seat == us:
            # We are tycoon: receive 2 strongest from beggar
            print("  You are TYCOON. You receive 2 strongest from Beggar.")
            print("  Enter the 2 cards Beggar gave you:")
            received = prompt_cards("  Cards from Beggar: ")
            state.hands[us].extend(received)
            print("  Choose 2 cards to give to Beggar:")
            display_hand(state.hands[us])
            while True:
                give = prompt_cards("  Give (2 cards): ")
                if len(give) == 2 and all(c in state.hands[us] for c in give):
                    for c in give:
                        state.hands[us].remove(c)
                    break
                print("  Must be exactly 2 cards from your hand.")

    if rich_seat is not None and poor_seat is not None:
        print(f"  Rich ({state.player_names[rich_seat]}) ↔ Poor ({state.player_names[poor_seat]}): 1 card")
        if poor_seat == us:
            my_hand = sorted(state.hands[us], key=lambda c: c.strength(state.revolution), reverse=True)
            give = my_hand[:1]
            print(f"  You MUST give your strongest card: {give[0]}")
            state.hands[us].remove(give[0])
            received = prompt_cards("  Card received from Rich: ")
            state.hands[us].extend(received)
        elif rich_seat == us:
            print("  You are RICH. You receive 1 strongest from Poor.")
            received = prompt_cards("  Card from Poor: ")
            state.hands[us].extend(received)
            display_hand(state.hands[us])
            while True:
                give = prompt_cards("  Give 1 card to Poor: ")
                if len(give) == 1 and give[0] in state.hands[us]:
                    state.hands[us].remove(give[0])
                    break
                print("  Must be exactly 1 card from your hand.")

    # Update counts
    for seat in range(4):
        state.hand_counts[seat] = len(state.hands[seat])
        if seat != us:
            print(f"  {state.player_names[seat]} (Seat {seat+1}) — estimated hand size: {state.hand_counts[seat]}")


# ─────────────────────────────────────────
# TURN PROCESSING
# ─────────────────────────────────────────

def process_play(play, seat, state):
    """
    Apply a play to game state. Returns tuple:
    (end_turn: bool, revolution_changed: bool, replay: bool, message: str)
    """
    end_turn = False
    rev_changed = False
    replay = False
    msg = ""

    # Remove cards from hand
    for c in play:
        if c in state.hands[seat]:
            state.hands[seat].remove(c)
        # Don't crash if card not found (opponent hand is estimated)

    state.hand_counts[seat] = len(state.hands[seat])
    state.played_cards.extend(play)
    state.table_play   = play
    state.table_player = seat
    state.last_played_by = seat
    state.pass_count   = 0

    # Check empty hand
    if len(state.hands[seat]) == 0 and not state.finished[seat]:
        state.finished[seat] = True
        state.finish_order.append(seat)
        msg += f"  🏆 {state.player_names[seat]} has gone out! (#{len(state.finish_order)})\n"

    # Wonder
    if check_wonder(play):
        end_turn = True
        replay   = True
        msg += "  ✨ WONDER played! Turn ends, player leads next.\n"
        return end_turn, rev_changed, replay, msg

    # 8888 or 888+Joker: 8-stop + counter-revolution (regardless of revolution state)
    if check_8888_or_888joker(play):
        end_turn   = True
        replay     = True
        state.revolution = not state.revolution  # toggle (counter-rev effect)
        rev_changed = True
        msg += f"  💥 8888/888JK! Counter-revolution! Revolution now: {state.revolution}\n"
        return end_turn, rev_changed, replay, msg

    # 8-stop (includes 8, 88, 888, any combo with joker)
    if check_8stop(play):
        end_turn = True
        replay   = True
        msg += "  🛑 8-STOP! Turn ends, player leads next.\n"
        return end_turn, rev_changed, replay, msg

    # Revolution (4-of-a-kind)
    if check_revolution(play):
        state.revolution = not state.revolution
        rev_changed = True
        if not check_counter_revolution(play, play, not state.revolution):
            msg += f"  🔄 REVOLUTION! Card order flipped. 3 is now {'STRONGEST' if state.revolution else 'weakest'}.\n"

    return end_turn, rev_changed, replay, msg


def run_turn(state, seat):
    """
    Run a single turn for `seat`.
    Returns: (passed: bool, ended_turn: bool, replay: bool)
    """
    is_user = (seat == state.user_seat)
    name    = state.player_names[seat]

    if state.finished[seat]:
        return True, False, False  # skip finished players

    print(f"\n  ── {name}'s turn ──")

    if is_user:
        # Show advisor
        display_hand(state.hands[seat])
        if state.table_play:
            table_str = " ".join(str(c) for c in state.table_play)
            eff = effective_rank(state.table_play, state.revolution)
            print(f"  Table: {table_str} (strength {eff})")
        else:
            print("  Table is empty — you lead.")

        print("\n  🤖 ADVISOR:")
        rec_play, explanation = suggest_play(state)
        print(explanation)

        while True:
            raw = input("  Your play (or 'pass'/'p'): ").strip()
            if raw.lower() in ('pass', 'p'):
                if state.table_play is None:
                    print("  Cannot pass on an opening play.")
                    continue
                print(f"  {name} PASSES.")
                state.pass_count += 1
                return True, False, False
            try:
                play = parse_hand(raw)
                # Validate
                ok, reason = is_valid_play(play, state.table_play, state.revolution)
                if not ok:
                    print(f"  ✗ Invalid: {reason}")
                    continue
                # Check cards are in hand
                hand_copy = list(state.hands[seat])
                valid_cards = True
                for c in play:
                    if c in hand_copy:
                        hand_copy.remove(c)
                    else:
                        print(f"  ✗ You don't have {c} in your hand.")
                        valid_cards = False
                        break
                if not valid_cards:
                    continue
                break
            except ValueError as e:
                print(f"  Parse error: {e}")
                continue

        end_turn, rev_changed, replay, msg = process_play(play, seat, state)
        if msg: print(msg.rstrip())
        if rev_changed:
            print(f"  Revolution status: {'🔄 ACTIVE (3 strongest)' if state.revolution else 'Normal (2 strongest)'}")
        return False, end_turn, replay

    else:
        # Other players — manual entry
        print(f"  Enter what {name} played (or 'pass'/'p'):")
        while True:
            raw = input(f"  {name}: ").strip()
            if raw.lower() in ('pass', 'p', ''):
                if state.table_play is None:
                    print("  Cannot pass on opening. Enter their play.")
                    continue
                print(f"  {name} PASSES.")
                state.pass_count += 1
                state.hand_counts[seat] = max(0, state.hand_counts[seat])
                return True, False, False
            try:
                play = parse_hand(raw)
                ok, reason = is_valid_play(play, state.table_play, state.revolution)
                if not ok:
                    print(f"  ✗ Invalid: {reason} — re-enter or check the play")
                    if not prompt_yes_no("  Override validation and accept anyway?"):
                        continue
                break
            except ValueError as e:
                print(f"  Parse error: {e}")
                continue

        # Update hand count estimate
        state.hand_counts[seat] = max(0, state.hand_counts[seat] - len(play))
        end_turn, rev_changed, replay, msg = process_play(play, seat, state)
        if msg: print(msg.rstrip())
        if rev_changed:
            print(f"  Revolution status: {'🔄 ACTIVE (3 strongest)' if state.revolution else 'Normal (2 strongest)'}")
        return False, end_turn, replay


# ─────────────────────────────────────────
# ROUND LOOP
# ─────────────────────────────────────────

def run_round(state):
    """Run a full round until all but one player is done."""
    print_banner(f"ROUND {state.round_num+1}")
    setup_round(state)

    while True:
        # Check if round is over (at most 1 player left with cards)
        active = [i for i in range(4) if not state.finished[i]]
        if len(active) <= 1:
            if active:
                # Last player automatically becomes Beggar
                last = active[0]
                if not state.finished[last]:
                    state.finished[last] = True
                    state.finish_order.append(last)
                    print(f"\n  {state.player_names[last]} is last — Beggar this round.")
            break

        seat = state.current_player

        if state.finished[seat]:
            state.current_player = (state.current_player + 1) % 4
            continue

        passed, end_turn, replay = run_turn(state, seat)

        if end_turn or replay:
            # Turn ends, current player leads next
            state.table_play   = None
            state.table_player = None
            state.pass_count   = 0
            if replay:
                # Stay on same player (they lead)
                pass
            else:
                state.current_player = (state.current_player + 1) % 4
        elif passed:
            # Check if all others passed = turn ends, last player leads
            active_non_finished = [i for i in range(4) if not state.finished[i]]
            passes_needed = len(active_non_finished) - 1
            if state.pass_count >= passes_needed:
                print(f"\n  All passed. {state.player_names[state.last_played_by]} leads next turn.")
                state.table_play   = None
                state.table_player = None
                state.pass_count   = 0
                state.current_player = state.last_played_by
            else:
                state.current_player = (state.current_player + 1) % 4
        else:
            state.current_player = (state.current_player + 1) % 4

    # Assign titles
    title_map = ['Tycoon', 'Rich', 'Poor', 'Beggar']
    print_section("ROUND RESULTS")
    for i, seat in enumerate(state.finish_order):
        title = title_map[i] if i < len(title_map) else 'Beggar'
        state.titles[seat] = title
        pts = TITLE_POINTS[title]
        state.scores[seat] += pts
        you = " ← YOU" if seat == state.user_seat else ""
        print(f"  #{i+1} {state.player_names[seat]}{you}: {title} (+{pts} pts)")

    print("\n  Scores so far:")
    for seat in range(4):
        you = " ← YOU" if seat == state.user_seat else ""
        print(f"    {state.player_names[seat]}{you}: {state.scores[seat]} pts")


# ─────────────────────────────────────────
# MAIN GAME
# ─────────────────────────────────────────

def run_game():
    print_banner("P5X TYCOON — Game Engine + Strategy Advisor")
    print("""
  Card format:  rank + suit  (e.g. 3♠ or 3S, 10♦ or 10D, J♥ or JH)
  Special:      JK = Joker   WD = Wonder
  Pass:         'pass' or 'p'
  Suits:        ♣/C  ♦/D  ♥/H  ♠/S
  Ranks:        3 4 5 6 7 8 9 10 J Q K A 2
""")

    state = GameState()
    state.user_seat    = prompt_seat()
    state.player_names = prompt_player_names(state.user_seat)

    for r in range(3):
        state.round_num = r
        run_round(state)
        if r < 2:
            input("\n  Press Enter to continue to next round...")

    # Final results
    print_banner("FINAL RESULTS")
    ranked = sorted(range(4), key=lambda s: state.scores[s], reverse=True)
    for rank, seat in enumerate(ranked):
        you = " ← YOU" if seat == state.user_seat else ""
        print(f"  #{rank+1} {state.player_names[seat]}{you}: {state.scores[seat]} pts")

    winner = ranked[0]
    if winner == state.user_seat:
        print("\n  🎉 YOU WIN! Tycoon achieved!")
    else:
        print(f"\n  {state.player_names[winner]} wins this match.")


# ─────────────────────────────────────────
# STANDALONE ADVISOR MODE
# ─────────────────────────────────────────

def run_advisor_only():
    """Quick advisor: enter your hand + table, get recommendation."""
    print_banner("P5X TYCOON — Quick Advisor")
    state = GameState()
    state.user_seat = 0

    print("\nEnter your hand:")
    state.hands[0] = prompt_cards("  Your cards: ")

    print("\nWhat's on the table? (or press Enter if opening move):")
    table_raw = input("  Table cards: ").strip()
    if table_raw.lower() in ('', 'none'):
        state.table_play = None
    else:
        try:
            state.table_play = parse_hand(table_raw)
        except ValueError:
            state.table_play = None

    rev = prompt_yes_no("Revolution active?")
    state.revolution = rev

    print()
    rec, explanation = suggest_play(state)
    if rec:
        print(f"RECOMMENDED PLAY: {' '.join(str(c) for c in rec)}")
    else:
        print("RECOMMENDED: PASS")
    print(explanation)


# ─────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────

if __name__ == '__main__':
    import sys
    print_banner("P5X TYCOON")
    print("\n  [1] Full Game (track all players, full advisor)")
    print("  [2] Quick Advisor (just enter hand + table, get recommendation)")
    while True:
        choice = input("\n  Select mode [1/2]: ").strip()
        if choice == '1':
            run_game()
            break
        elif choice == '2':
            run_advisor_only()
            break
        else:
            print("  Enter 1 or 2.")
