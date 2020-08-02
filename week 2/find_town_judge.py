# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = {}
        for x in trust:
            if x[0] in d:
                d[x[0]].append(x[1])
            else:
                d[x[0]] = [x[1]]
        
        judge = []
        for k,v in d.items():
            judge.append(v)
        if len(judge) > 0:
            possibleContenders = judge[0]
        else:
            if N == 1:
                return 1
            return -1
        for i in range(1, len(judge)):
            possibleContenders = list(set(possibleContenders) & set(judge[i]))
        if len(possibleContenders) == 1:
            return possibleContenders[0]
        return -1