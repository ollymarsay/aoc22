with open("02/input.txt", "r") as file:
    cypher = {"A" : ["Y", "Z", "X"], "B" : ["Z", "X", "Y"], "C" : ["X", "Y", "Z"]}
    points = {"X" : 1, "Y" : 2, "Z" : 3}
    win_lose_draw_points = {0 : 6, 1 : 0, 2: 3}
    lose_draw_win = {"X" : 1, "Y": 2, "Z" : 0}
    data = [x.split(" ") for x in file.read().splitlines()]
    score, score2 = 0, 0
    for e, (x, y) in enumerate(data):
        score += points[y] + win_lose_draw_points[cypher[x].index(y)]
        score2 += win_lose_draw_points[lose_draw_win[y]] + points[cypher[x][lose_draw_win[y]]]
    print(score)
    print(score2)