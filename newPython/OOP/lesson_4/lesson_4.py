#1mro() ktpi te vor clas@ voric e jarangum D>B>C>A>Object



#2

class AbstractFile:
    def __init__(self):
        raise Exception('This is Abstract class')

    def translate(self):
        raise Exception('translate')

    def write(self):
        with open('file.txt','w') as file:
            file.write(self.writing_text)

class EnglishFile(AbstractFile):

    alphabet = {'a':'а', 'b':'б', 'c':'ц', 'd': 'д', 'e':'е', 'f':'ф', 'g':'г', 'i':'и', 'k':'к','l':'л','m':'м','n':'н','o':'о','p':'п','r':'р','s':'с','t':'т','u':'ю','x':'х','y':'у','z':'з', ' ': ' '}
    writing_text = ''
    def __init__(self):
        pass

    def translate(self,text):
        translated_text = ''
        for char in text:
            if char.lower() in self.alphabet:
                translated_text += self.alphabet[char.lower()]
        self.writing_text = translated_text
        return translated_text



class RussianFile(AbstractFile):
    alphabet = {'а':'a', 'б':'b', 'ц':'c', 'д': 'd', 'е':'e', 'ф':'f', 'г':'g', 'и':'i', 'к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','ю':'u','х':'x','у':'y','з':'z', ' ': ' '}
    writing_text = ''
    def __init__(self):
        pass

    def translate(self,text):
        translated_text = ''
        for char in text:
            if char.lower() in self.alphabet:
                translated_text += self.alphabet[char.lower()]
        self.writing_text = translated_text
        return translated_text


eng = EnglishFile()
rus = RussianFile()
print(eng.translate('Grigor Manukyan'))
print(rus.translate('григор манюкуан'))
rus.write()
eng.write()