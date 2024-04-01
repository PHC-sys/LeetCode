class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dicz = {'z','x','c','v','b','n','m'};
        dica = {'a','s','d','f','g','h','j','k','l'};
        dicq = {'q','w','e','r','t','y','u','i','o','p'};
        re = [];
        for Word in words:
            countz = 0;
            counta = 0;
            countq = 0;
            word = Word.lower()
            for dic in dicz:
                countz = countz + word.count(dic);   
            for dic in dica:        
                counta = counta + word.count(dic);  
            for dic in dicq:        
                countq = countq + word.count(dic);
            if countz == len(word) or counta == len(word) or countq == len(word):
                re.append(Word)
        return re 