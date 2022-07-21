import pandas as pd

chatbot_data = pd.read_excel("C:\make_Project\chatbot_data.xlsx")

chat_dic={}
row=0
for rule in chatbot_data['rule']:
    chat_dic[row]=rule.split(',')
    row += 1
    
print(chat_dic)