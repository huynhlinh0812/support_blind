from translate import Translator
translator= Translator(to_lang="vi")

def process(lst, lang):
	lst_name = []
	lst_count = []
	text_ob_of = "Have"
	while len(lst) != 0:
		Count = lst.count(lst[0])
		lst_name.append(lst[0])
		lst_count.append(Count)
		delet = lst[0]
		for i in range(Count):
			lst.remove(delet)

	for i in range(len(lst_count)):
		if len(lst_count) == 1:
			text_ob_of += ' ' + str(lst_count[i]) +' ' + lst_name[i]
		else:
			if i == len(lst_count) - 1:
				text_ob_of += ' ' + "and" + ' ' + str(lst_count[i]) +' ' + lst_name[i]
			elif i == len(lst_count) - 2:
				text_ob_of += ' ' + str(lst_count[i]) +' ' + lst_name[i]
			else:
				text_ob_of += ' ' + str(lst_count[i]) +' ' + lst_name[i] + ','

	if (lang == 'vi-VN'):
		translation = translator.translate(text_ob_of)
		return translation


	return text_ob_of