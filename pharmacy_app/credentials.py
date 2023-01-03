import pandas as pd


#print(df)

def add_new_user(dataframe,user_name,password):
    if user_name not in dataframe['user name'].values:
        new_row = {'user name':user_name, 'password':password}
        dataframe=dataframe.append(new_row, ignore_index=True)
        print(dataframe)
        dataframe.to_csv("login_credentials.csv", index=False)
        print('user added')
        return True
    else:
        print('user already exists')
        return False

def check_credentials(dataframe,user_name,password):
    if user_name in dataframe['user name'].values:
        flag=dataframe.loc[(dataframe[dataframe['user name'] == user_name].index[0]),'password']==password
        print("flag",flag)
        return flag
    else:
         print('User doesnot exist')
         return False


#df = pd.read_csv("login_credentials.csv")
#flag,df=add_new_user(df,"aq","123")

#df.to_csv("login_credentials.csv", index=False)

'''
print(check_credentials(df,'hari','haris123'))
df=add_new_user(df,'chemma','asim123')
print(df)
df.to_csv("login_credentials.csv",index=False)
'''