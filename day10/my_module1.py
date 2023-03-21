import pandas as pd
data = pd.read_excel("ss.xlsx")
def group_data(modeldata,sub_msg):

    df = pd.DataFrame()
    cinema_code_len_ls = []
    modeldata = modeldata.drop(columns=['total_sales','tickets_sold'])
    for ii, jj in modeldata.groupby(sub_msg):
        cinema_code_len = len(set(jj['cinema_code']))##一共多少家电影院上映
        datat = jj.mean()
        datat = pd.DataFrame(datat.values,index=datat.index).T
        df = pd.concat([df,datat],axis=0)##合并电影数据
        cinema_code_len_ls.append(cinema_code_len)
    df['cinema_num'] = cinema_code_len_ls
    df = df.set_index('film_code')
    df = df.drop(columns=['cinema_code'])
    return df

group_data_res = group_data(data,'film_code')
print(group_data_res)