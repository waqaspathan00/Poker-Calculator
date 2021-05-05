from collections import defaultdict

RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Check():
    def one_pairs(self, cards):
        ranks = [card.get_rank() for card in cards]
        rank_counts = defaultdict(lambda: 0)
        for v in ranks:
            rank_counts[v] += 1

        if 2 in rank_counts.values():
            return True
        else:
            return False

    def two_pairs(self, cards):
        ranks = [card.get_rank() for card in cards]
        rank_counts = defaultdict(lambda: 0)
        for v in ranks:
            rank_counts[v] += 1
        if sorted(rank_counts.values()) == [1, 2, 2]:
            return True
        else:
            return False

    def three_of_a_kind(self, cards):
        ranks = [card.get_rank() for card in cards]
        rank_counts = defaultdict(lambda: 0)
        for v in ranks:
            rank_counts[v] += 1
        if set(rank_counts.values()) == {3, 1}:
            return True
        else:
            return False

    def high_straight(self, cards):
        ranks = [card.get_rank() for card in cards]
        rank_counts = defaultdict(lambda: 0)
        for rank in ranks:
            rank_counts[rank] += 1
        rank_values = [RANKS[rank] for rank in ranks]
        rank_range = max(rank_values) - min(rank_values)
        if len(set(rank_counts.values())) == 1 and (rank_range == 4):
            return True
        return False

    def straight(self, cards):
        if self.high_straight(cards):
            return True
        else:
            # check straight with low Ace
            ranks = [card.get_rank() for card in cards]
            if set(ranks) == {'A', '2', '3', '4', '5'}:
                return True
            return False

    def flush(self, cards):
        suits = [card.get_suit() for card in cards]
        if len(set(suits)) == 1:
            return True
        else:
            return False

    def full_house(self, cards):
        ranks = [card.get_rank() for card in cards]
        rank_counts = defaultdict(lambda: 0)
        for rank in ranks:
            rank_counts[rank] += 1
        if sorted(rank_counts.values()) == [2, 3]:
            return True
        return False

    def four_of_a_kind(self, cards):
        ranks = [card.get_rank() for card in cards]
        rank_count = defaultdict(lambda: 0)
        for rank in ranks:
            rank_count[rank] += 1
        if sorted(rank_count.values()) == [1, 4]:
            return True
        return False

    def straight_flush(self, cards):
        if self.flush(cards) and self.straight(cards):
            return True
        else:
            return False

    def royal_flush(self, cards):
        if self.high_straight(cards) and self.flush(cards):
            return True
        else:
            return False

    def hand_combinations(self, count, cards):
        if self.royal_flush(cards):
            count.royal_flush += 1
        if self.straight_flush(cards):
            count.straight_flush += 1
        if self.four_of_a_kind(cards):
            count.four_of_a_kind += 1
        if self.full_house(cards):
            count.full_house += 1
        if self.flush(cards):
            count.flush += 1
        if self.straight(cards):
            count.straight += 1
        if self.three_of_a_kind(cards):
            count.three_of_a_kind += 1
        if self.two_pairs(cards):
            count.two_pair += 1
        if self.one_pairs(cards):
            count.one_pair += 1
