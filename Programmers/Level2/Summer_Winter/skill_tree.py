def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        skill_queue = [skill[j] for j in range(len(skill))]
        skill_pop = skill_queue.pop(0)
        is_correct = True

        for i in range(len(tree)):
            if tree[i] in skill_queue:
                is_correct = False
                break
            if tree[i] == skill_pop:

                try:
                    skill_pop = skill_queue.pop(0)
                except:
                    continue
        if is_correct:
            cnt += 1
    return cnt

def main():
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


if __name__ == "__main__":
    main()
