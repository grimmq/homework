students = {"德瑞克": 33, "尚恩": 73, "傑夫": 63, "馬基": 39}

for name, score in students.items():
    new_score = round(score / 5) * 5
    
    if new_score < 40:
        print(name,score)
    else:
        print(name, new_score)
