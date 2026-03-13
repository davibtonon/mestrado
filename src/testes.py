from tools import load_log_file

doc = load_log_file('C:\\Users\\Tiago Tonon\\Documents\\Orion\\mestrado\\data\\raw\\sh_binary_padding_dd_2020-11-10081941.log')
print(len(doc))
print(doc[0].page_content)
print(doc[0].metadata)