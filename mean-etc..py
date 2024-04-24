##1211201118 林優花

# 学生の試験の点数を入力
score1 = int(input("学生1の試験の点数を入力してください: "))
score2 = int(input("学生2の試験の点数を入力してください: "))
score3 = int(input("学生3の試験の点数を入力してください: "))

# 平均点の計算
average = (score1 + score2 + score3) / 3

# 最高点と最低点の計算
max_score = score1
min_score = score1

if score2 > max_score:
    max_score = score2
if score3 > max_score:
    max_score = score3

if score2 < min_score:
    min_score = score2
if score3 < min_score:
    min_score = score3

# 結果の表示
print("平均点:", average)
print("最高点:", max_score)
print("最低点:", min_score)
