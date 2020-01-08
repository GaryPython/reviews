data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print('檔案讀取完成,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每筆留言平均是', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言資料小於100')
print(new[0])

good = []
for d in data:
	if 'good' in d :
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])
