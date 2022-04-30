smoking = input('你抽過菸嗎? ')
if smoking !='有' and smoking !='沒有':
	print('只能輸入 有 或 沒有 ')
	raise SystemExit
age = input('你幾歲? ')
age = int(age)
if smoking == '有':
	if age >= 18:
		print('行!你可以抽菸')
	else: 
		print('你不可以抽菸吧...?')
if smoking == '沒有':
	if age >= 18:
		print('很好，你是健康的人')
	else:
		print('請繼續保持')

