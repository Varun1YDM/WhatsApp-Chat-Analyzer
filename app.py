import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    #st.text(data)
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    #fetch unique users
    user_list = df['users'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user =  st.sidebar.selectbox("Show analysis : ",user_list)
 
    if st.sidebar.button("Show Analysis"):
        
       num_messages,words,number_media_messages,num_links = helper.fetch_stats(selected_user,df)   #
       
       col1,col2,col3,col4 = st.columns(4)  # ,col4
       
       with col1:
           st.header("Total Messages")
           st.title(num_messages)
           
       with col2:
           st.header("Total Words")
           st.title(words)
       with col3:
           st.header("Media Shared")
           st.title(number_media_messages)
       with col4:
          st.header("Links Shared")
          st.title(num_links)
          
        #find busiset user in group(Group level)
       if selected_user == 'Overall':
            st.title("Most Busy Users ")
            x,new_df = helper.most_busy_users(df)
            
            fig, ax = plt.subplots()
            
            col1,col2 = st.columns(2)
            
            with col1:
                 ax.bar(x.index,x.values,color='red')
                 plt.xticks(rotation='vertical')
                 st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
                
       #wordclound
       st.title('WordCloud')
       df_wc = helper.create_wordcloud(selected_user,df)
       fig,ax = plt.subplots()
       ax.imshow(df_wc)
       st.pyplot(fig)
                
      
