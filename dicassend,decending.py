my_dict={'banana':3,'apple':1,'cherry':6}
print("orginal list:",my_dict)
ass_dict=dict(sorted(my_dict.items()))
print("assending order:",ass_dict)
dis_dict=dict(sorted(my_dict.items(),reverse=True))
print("decenting order:",dis_dict)
