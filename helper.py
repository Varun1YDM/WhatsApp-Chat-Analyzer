from urlextract import URLExtract
extractor = URLExtract()
from wordcloud import WordCloud

def fetch_stats(selected_user,df):
    
    if(selected_user != 'Overall'):
        df = df[df['users'] == selected_user]
    num_messages = df.shape[0]
    words = []
    for mess in df['messages']:
        words.extend(mess.split())
    
    number_media_messages = df[ df['messages'] == '<Media omitted>\n'].shape[0]
    
    #fetch number of links
    
    links = []
    for message in df['messages']:
        links.extend(extractor.find_urls(message))
    
    return num_messages,len(words),number_media_messages,len(links)


def most_busy_users(df):
    x = df['users'].value_counts().head()
    df = round(( df['users'].value_counts() / df.shape[0] ) *  100, 2).reset_index().rename(columns={'index':'name','users':'percentage'})
    return x,df

def create_wordcloud(selected_user,df):
    if(selected_user != 'Overall'):
        df = df[df['users'] == selected_user]
    
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['messages'].str.cat(sep=" "))
    return df_wc










    '''if selected_user == "Overall":
        #1. fetch number of messages
        num_messages = df.shape[0]
        #2. number of words
        words = []
        for mess in df['messages']:
            words.extend(mess.split())
        return num_messages,len(words)
    else:
        new_df = df[df['users'] == selected_user]
        num_messages = new_df.shape[0]
        words = []
        for mess in new_df['messages']:
            words.extend(mess.split())
        return num_messages,len(words)
         '''