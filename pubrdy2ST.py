#pubrdy2ST.py ver 001 20240807
import streamlit as st
i = open('./publishready2ST.txt','r')
# i = i.decode('utf-8').encode('ascii', 'replace') 
l = i.readlines()
i.close()

# Define a byte string
# byte_string = b"Hello, world!"
# Convert the byte string to a string using the str() constructor
# string = str(byte_string, encoding='utf-8')
# Print the string
# print(string)

st.title('Experimental Resources News')

for x in range(len(l)):
    if l[x][0:4] == '!STD':
        begin = x
        headline = l[x+1]
        
    if l[x][0:4] == '!END':
        finish = x

        story = l[begin+3:finish-1]
        #sstory = str(story, encoding='utf-8')
        
        #o = open('C:\\tempstore0\\temp' + str(x) +'.txt','w')
        for y in range(len(story)):
                    
            story[y] = str.replace(story[y],'\xa0','')
            story[y] = str.replace(story[y],'\xa02','')
            story[y] = str.replace(story[y],'        ',"\n\n")
            story[y] = str.replace(story[y],'$','USD')
            story[y] = str.replace(story[y],'(RWE)','(RWE)')
            story[y] = '\n\n' + story[y]

        # Using object notation
        add_selectbox = st.sidebar.selectbox(
            "How would you like to be contacted for a short survey?",
            ("Email", "Home phone", "Mobile phone")
        )
        
           
        st.subheader(headline)
        st.markdown('\n'.join(story))
        st.divider()
        #o.close()
            
            

