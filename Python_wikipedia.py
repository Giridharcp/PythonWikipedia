import wikipedia

def wiki():# Retuns a sentence of article about the user-specified subject from Wikipedia.
    try:
        response=input('What do you want me to search: ')
        result = wikipedia.summary(response, sentences=2)
        url = "http://en.wikipedia.org/w/index.php?title="
        #webbrowser.open_new_tab(url+str)
        print("\n\nThese are the result's i've got\n\n")
        print(result)
    except wikipedia.exceptions.PageError:
        url1 = "http://www.google.com/?#q="
        webbrowser.open_new_tab(url1+str)
        print( "I did not find any information regarding that query, here the related search results")
        
    except wikipedia.exceptions.DisambiguationError:
        print('can you please be more specific')
        
wiki()
