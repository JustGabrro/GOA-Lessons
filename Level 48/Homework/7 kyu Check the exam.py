def check_exam(arr1,arr2):
    score = 0 
    for correct, x in zip(arr1, arr2):
        if x == "":
            continue
        elif x == correct:
            score += 4
        else:
            score -= 1
    return max(score, 0)