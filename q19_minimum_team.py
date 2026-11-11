"""19. Select the smallest candidate team covering all skills."""


def smallest_team(required, candidates):
    index = {skill: i for i, skill in enumerate(required)}
    full = (1 << len(required)) - 1
    dp = {0: []}
    for person, skills in enumerate(candidates):
        mask = sum(1 << index[s] for s in skills if s in index)
        for covered, team in list(dp.items()):
            new = covered | mask
            if new not in dp or len(dp[new]) > len(team) + 1:
                dp[new] = team + [person]
    return dp[full]


print(smallest_team(["Python", "SQL"], [["Python"], ["SQL"]]))
