class Solution(object):
    def findWinners(self, matches):
        winners = set()
        lossers = set()
        lossers2 = set()
        dic = {}

        for match in matches:
            lossers.add(match[1])
            if match[1] in dic:
                dic[match[1]][1] += 1
            else:
                dic[match[1]] = [0, 1]

        for match in matches:
            if match[0] not in lossers:
                winners.add(match[0])

        for key, value in dic.items():
            if value[1] <= 1:
                lossers2.add(key)

        return [sorted(winners), sorted(lossers2)]
