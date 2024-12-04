# text="vipinkumar@gmail.com"



# print(text[0:text.index("@")])




text="hello python"


o_index=text.index("o")

reversed_sub_str=text[o_index-1::-1]


balance_sub_str=text[o_index:]

result=reversed_sub_str+balance_sub_str

print(result)