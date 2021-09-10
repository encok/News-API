class News:
    '''
    News class to define news Objects
    '''

    def __init__(self,id,name,description,category,language,url):
        self.id =id
        self.name = name
        self.description = description
        self.url = 'http://www.abc.net.au/news/'+ url
        self.category = category 
        self.language = language
