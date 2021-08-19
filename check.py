from collections import defaultdict

RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Check:
    """
    functions that check what the best hand combination is in a given hand
    """

    def get_rank_counts(self, hand):
        """
        create a dictionary rank_counts that counts how many of each card in hand
        """
        ranks = [card.get_rank() for card in hand]
        rank_counts = defaultdict(lambda: 0)
        for rank in ranks:
            rank_counts[rank] += 1

        return rank_counts

    def one_pairs(self, hand):
        """
        two of the same card

        create a dictionary rank_counts that counts how many of each card in hand
        if there are 2 of any card return True
        """
        rank_counts = self.get_rank_counts(hand)

        if 2 in rank_counts.values():
            return True
        return False

    def two_pairs(self, hand):
        """
        two one pairs

        create a dictionary rank_counts that counts how many of each card in hand
        when the values of this dictionary are sorted, they should be [1, 2, 2] to return True
        """
        rank_counts = self.get_rank_counts(hand)

        if sorted(rank_counts.values()) == [1, 2, 2]:
            return True
        return False

    def three_of_a_kind(self, hand):
        """
        three of one card

        create a dictionary rank_counts that counts how many of each card in hand
        when the values of this dictionary are sorted as a set they should be {3, 1} to return True
        """
        rank_counts = self.get_rank_counts(hand)

        if set(rank_counts.values()) == {3, 1}:
            return True
        return False

    def high_straight(self, hand):
        """
        straight with a high ace
        
        create a dictionary rank_counts that counts how many of each card in hand
        create a list rank_values that is the number equivalent of each card: 10 == 10, J == 11
            Check global RANKS dict - line 3
        
        calculate the range of values
        if set rank_count only contains 1, that means each card only appeared once
            rank_range must also be 4 to indicate an exact difference of 4 between min and max hand
        """
        ranks = [card.get_rank() for card in hand]
        rank_counts = self.get_rank_counts(hand)

        rank_values = [RANKS[rank] for rank in ranks]
        rank_range = max(rank_values) - min(rank_values)

        if len(set(rank_counts.values())) == 1 and (rank_range == 4):
            return True
        return False

    def straight(self, hand):
        """
        all 5 hand must be in consecutive order
        
        if we dont have a high_straight, manually check for the one other case where "A" is low card 1.
        """
        if self.high_straight(hand):
            return True

        # check straight with low Ace
        ranks = [card.get_rank() for card in hand]
        if set(ranks) == {'A', '2', '3', '4', '5'}:
            return True
        return False

    def flush(self, hand):
        """
        the suits of each card in hand should be the same

        create a list of each suit in hand
        when that list is converted to a set it should shrink to length == 1 to verify only 1 suit exists in hand
        """
        suits = [card.get_suit() for card in hand]
        if len(set(suits)) == 1:
            return True
        return False

    def full_house(self, hand):
        """
        one pair AND three of a kind

        create a dictionary rank_counts that counts how many of each card in hand
        when the values of rank_counts is sorted it should be [2,3] to return true
        """
        rank_counts = self.get_rank_counts(hand)

        if sorted(rank_counts.values()) == [2, 3]:
            return True
        return False

    def four_of_a_kind(self, hand):
        """
        four of one card

        create a dictionary rank_counts that counts how many of each card in hand
        when the values of rank_counts are sorted it should be [1,4] to return True
        """
        rank_counts = self.get_rank_counts(hand)

        if sorted(rank_counts.values()) == [1, 4]:
            return True
        return False

    def straight_flush(self, hand):
        if self.straight(hand) and self.flush(hand):
            return True
        return False

    def royal_flush(self, hand):
        if self.high_straight(hand) and self.flush(hand):
            return True
        else:
            return False

    def hand_combinations(self, count, hand):
        """
        call each hand function and increment its count if True
        """
        if self.royal_flush(hand):
            count.royal_flush += 1
        if self.straight_flush(hand):
            count.straight_flush += 1
        if self.four_of_a_kind(hand):
            count.four_of_a_kind += 1
        if self.full_house(hand):
            count.full_house += 1
        if self.flush(hand):
            count.flush += 1
        if self.straight(hand):
            count.straight += 1
        if self.three_of_a_kind(hand):
            count.three_of_a_kind += 1
        if self.two_pairs(hand):
            count.two_pair += 1
        if self.one_pairs(hand):
            count.one_pair += 1