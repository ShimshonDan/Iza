from bs4 import BeautifulSoup as bs
import requests
import Error as er

class Parser():
    """Class for parsing https://diletant.media/articles/26249506/ with jokes"""

    __URL_TEMPLATE = "https://diletant.media/articles/26249506/"
    __dictJokes = {}
    
    def __init__(self):
        self.__dictJokes = self.parsing_website()
    
    def parsing_website(self) -> dict:
        requests_get = requests.get(self.__URL_TEMPLATE)
        if requests_get.status_code == 200:
            bs_text = bs(requests_get.text.encode("utf-8"), "lxml")

            jokes = bs_text.find_all("div", class_="publication__content-wrap wysiwyg")
            
            fail_writed = open("medium.txt", 'w', encoding='utf-8')
            jokes = jokes[0].find_all('p')
            joke_string=""
            for j in jokes:
                joke_string+=str(j.text)
            fail_writed.write(joke_string)
            fail_writed.close()
            
            failread = open("medium.txt", 'r', encoding='utf-8')
            s = failread.read()
            failwrited = open("medium.txt", 'w', encoding='utf-8')

            pos_start=pos_end=0
            first_help_dict={}
            index=0
            while pos_end != -1:
                pos_end = s.find("\n", pos_start)
                first_help_dict[index] = s[pos_start:pos_end:]
                index+=1 
                pos_start=pos_end+1

            second_help_dict={}
            for i in range(index-1):   
                string=str(first_help_dict.get(i))
                if len(string) != 0:
                    second_help_dict[i]=(string+"\n").strip()
                if len(string)!=0 and len(str(first_help_dict.get(i+1)))==0:
                    second_help_dict[i+2] = "\n"
            first_help_dict.clear()

            for i in second_help_dict:
                failwrited.write(str(second_help_dict[i]))
            failwrited.close()
            second_help_dict.clear()

            failread = open("medium.txt", "r", encoding="utf-8")
            index = 0
            dictJokes={}
            joke_string = failread.readline()
            while True:
                joke_string = failread.readline()
                if not joke_string:
                    break
                dictJokes[index] = joke_string
                index += 1

            """fail_write = open("answer.txt", "w", encoding="utf-8")
            for i in dictJokes:
                fail_write.write(str(dictJokes.get(i)))"""
            
            return dictJokes
        
        else:
            raise er.MyError("Not Connected")
        
    def getJoke(self) -> dict:
        return self.__dictJokes