# Python3

import random

dna_sequence = ('A', 'T', 'C', 'G')
rna_sequence = ('A', 'U', 'C', 'G')
human_weights = [0.295, 0.295, 0.205, 0.205]
whnumber = 0

def other_weights(sequence_type):
	if sequence_type == 'DNA':
		custom_sequence = dna_sequence
	else:
		custom_sequence = rna_sequence
	user_weight = []
	for rk in custom_sequence:
		weight = float(input(f"请输入 {rk} 的权重(0~1):"))
		if 0 <= weight <= 1:
			user_weight.append(weight)
		else:
			print("只能是（0～1）之间的数！")
	total = sum(user_weight)
	if total == 1:
		user_weight = [w / total for w in user_weight]
	return user_weight

def one_sequence(custom_na):
	if custom_na == 'dna':
		all_acids = ''
		couple_sequence = ''
		for i in range(number):
			all_acids += random.choices(dna_sequence, weights = human_weights, k = 1)[0]
			if all_acids[i] == 'A':
				couple_sequence += 'T'
			elif all_acids[i] == 'T':
				couple_sequence += 'A'
			elif all_acids[i] == 'C':
				couple_sequence += 'G'
			elif all_acids[i] == 'G':
				couple_sequence += 'C'
		return all_acids, couple_sequence
	elif custom_na == 'rna':
		all_acids = ''
		for j in range(number):
			all_acids += random.choice(rna_sequence)
		return all_acids


while whnumber == 0:
	print("------------------------------Menu------------------------------\n\
	   dna.成对DNA的序列.    \n\
	   RNA.RNA的序列.    \n\
	   [输入其它退出].退出")
	judgment = input('请输入:')
	if judgment == 'dna':
		number = int(input('请输入脱氧核糖核苷酸的个数(输入0回主菜单):'))
		if number == 0:
			continue
		else:
			custom = input("是否自行选择含氮碱基的概率？（同意输入y 拒绝输入n）(如果拒绝将会使用默认人类的含氮碱基权重):")
			if custom == 'y':
				user_weight = other_weights("DNA")
			else:
				user_weight = human_weights
			single, couple = one_sequence(judgment)
			print(single)
			print(couple)

	elif judgment == 'rna':
		number = int(input('请输入核糖核苷酸的个数(输入0回主菜单):'))
		if number == 0:
			continue
		else:
			srna = one_sequence(judgment)
			print(srna)

	else:
		break