class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = [i[0] for i in matches] #collect all winners in one array
        
        losers = [i[1] for i in matches] # collect all loosers in another array
        
        loser_counter = Counter(losers) # count the number of times the player was counted as looser
        
        return [sorted(list(set(winners)-set(losers))),sorted([i for i,j in loser_counter.items() if j == 1])] #using the set differece get the winner and from the counter get the looser