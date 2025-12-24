number = int(input())
counts = {}
for _ in range(number):
    team = input().strip()
    counts[team] = counts.get(team, 0) + 1

sorted_teams = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
for team, counts in sorted_teams:
    print(team)
    break
