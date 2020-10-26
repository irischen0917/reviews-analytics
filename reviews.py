#reviews
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sume_len + len(d)

print('平均留言長度為：', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有' , len(new), '筆資料長度小於100')
print(new[0])
print(new[1])

good = [d for d in data if 'good' in d]
print(good[0])


#增加計數功能
wc = {} # = word_count
for line in data:
	words = line.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1


for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])

print(len(wc))
print(wc['Iris'])

while True:
	word = input('請輸入您要查找的字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過', wc[word], '次')
	else:
		print('這個字沒有出現過喔！')

print('感謝使用本查詢功能')









