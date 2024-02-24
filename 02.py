height = 100
total = 100 #第一次的反彈
bounce_height = height

for i in range(1,10):
    bounce_height /= 2
    total += 2 * bounce_height

final_bounce_height = bounce_height / 2

print(f'總共經歷:{total}')
print(f'第10次反彈高度:{final_bounce_height}')
