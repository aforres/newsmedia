#pubrdy2ST.py ver 001 20240807
import streamlit as st
i = open('./publishready2ST.txt','r')
i = i.decode('utf-8').encode('ascii', 'replace') 
l = i.readlines()
i.close()

for x in range(len(l)):
    if l[x][0:4] == '!STD':
        begin = x
        headline = l[x+1]
        
    if l[x][0:4] == '!END':
        finish = x

        story = l[begin+3:finish-1]
        
        
        #o = open('C:\\tempstore0\\temp' + str(x) +'.txt','w')
        for y in range(len(story)):
            # story[y] = story[y].decode('utf-8').encode('ascii', 'replace')            
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
            
            

# ────────────────────── Traceback (most recent call last) ───────────────────────

#   /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

#   nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

#   /home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptru  

#   nner/script_runner.py:579 in code_to_exec                                     

                                                                                

#   /mount/src/newsmedia/pubrdy2ST.py:16 in <module>                              

                                                                                

#     13 │   │   finish = x                                                       

#     14 │   │                                                                    

#     15 │   │   story = l[begin+3:finish-1]                                      

#   ❱ 16 │   │   story = story.decode('utf-8').encode('ascii', 'replace')         

#     17 │   │                                                                    

#     18 │   │   #o = open('C:\\tempstore0\\temp' + str(x) +'.txt','w')           

#     19 │   │   for y in range(len(story)):                                      

# ────────────────────────────────────────────────────────────────────────────────

# AttributeError: 'list' object has no attribute 'decode'

# 2024-11-01 07:51:19.198 503 
