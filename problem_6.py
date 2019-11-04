if __name__ == '__main__':
    score_list = []
    marksheet = []
    n = int(input())
    for _ in range(0,n):
        name = input()
        score = float(input())
        marksheet.append([name,score])
        score_list.append(score)

    score_list = sorted(list(set(score_list)))
    second_score = score_list[1]

    for name, score in sorted(marksheet):
        if score == second_score:
            print(name)
