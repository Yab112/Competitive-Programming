class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.Ttl = timeToLive
        self.Tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.Tokens[tokenId] = currentTime + self.Ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.Tokens and self.Tokens[tokenId] > currentTime:
            self.Tokens[tokenId] = currentTime + self.Ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = sum(1 for exp_time in self.Tokens.values() if exp_time > currentTime)
        return count
    


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)