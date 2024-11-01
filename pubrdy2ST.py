#pubrdy2ST.py ver 001 20240807
import streamlit as st
i = open('./publishready.txt','r')
l = i.readlines()
i.close()

for x in range(len(l)):
    if l[x][0:4] == '!STD':
        begin = x
        headline = l[x+1]
        
    if l[x][0:4] == '!END':
        finish = x
        #print(str(x))

        story = l[begin+3:finish-1]
        #story = str(story.encode('utf-8'))
        
        #o = open('C:\\tempstore0\\temp' + str(x) +'.txt','w')
        for y in range(len(story)):
            
            story[y] = str.replace(story[y],'\xa0','')
            story[y] = str.replace(story[y],'\xa02','')
            story[y] = str.replace(story[y],'        ',"\n\n")
            story[y] = str.replace(story[y],'$','USD')
            #story[y] = str.replace(story[y],'(RWE)','(RWE)')
            story[y] = '\n\n' + story[y]

            #o.write(story[y])
            
            
        #hline = ("**" + str(headline) + "**")    
        #st.markdown("<b>Your bold text here</b>", unsafe_allow_html=True)
        #st.markdown("<b>" + headline + "</b>", unsafe_allow_html=True)
        st.subheader(headline)
        st.markdown('\n'.join(story))
        st.divider()
        #o.close()
            
            
