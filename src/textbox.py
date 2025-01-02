import string
import config
import pygame
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

class TextBox:
    def __init__(self, w, h, x, y, font, callback=None):
        self.width = w
        self.height = h
        self.x = x # location
        self.y = y # location
        self.font = font
        self.text = ""  # content in textbox
        self.callback = callback
        self.__surface = pygame.Surface((w, h))
        self.__surface.fill(config.TIMBERWOLF)
 
        self.dagparams = DefaultDagParams()
        self.state = 0 
        self.page = 1  # page index
        self.limit = 5  
        self.pinyin = ''
        self.word_list = []  
        self.word_list_surf = None  
        self.buffer_text = '' 

    def create_word_list_surf(self):
        word_list = [str(index + 1) + '.' + word for index, word in enumerate(self.word_list)]
        text = " ".join(word_list)
        # color
        self.word_list_surf = self.font.render(text, True, config.BLACK)
 
    def draw(self, dest_surf):
        # color
        text_surf = self.font.render(self.text, True, config.BLACK)
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
                       (0, 0, self.width, self.height))
        if self.state == 1:
            dest_surf.blit(self.word_list_surf,
                           (self.x, self.y + (self.height - text_surf.get_height()) - 30),
                           (0, 0, self.width, self.height)
                           )
 
    def key_down(self, event):
        unicode = event.unicode
        key = event.key
 
        if key == 8:
            self.text = self.text[:-1]
            if self.state == 1:
                self.buffer_text = self.buffer_text[:-1]
            return
 
        if key == 301:
            return

        if key == 13:
            if self.callback:
                self.callback(self.text)
            return

        if self.state == 1 and key == 32:
            self.state = 0
            self.text = self.text[:-len(self.buffer_text)] + self.word_list[0]
            self.word_list = []
            self.buffer_text = ''
            self.page = 1
            return
 
        if self.state == 1 and key == 61:
            self.page += 1
            self.word_list = self.py2hz(self.buffer_text)
            if len(self.word_list) == 0:
                self.page -= 1
                self.word_list = self.py2hz(self.buffer_text)
            self.create_word_list_surf()
            return

        if self.state == 1 and key == 45:
            self.page -= 1
            if self.page < 1:
                self.page = 1
            self.word_list = self.py2hz(self.buffer_text)
            self.create_word_list_surf()
            return
 
        if self.state == 1 and key in (49, 50, 51, 52, 53):
            self.state = 0
            if len(self.word_list) <= key - 49:
                return
            self.text = self.text[:-len(self.buffer_text)] + self.word_list[key - 49]
            self.word_list = []
            self.buffer_text = ''
            self.page = 1
            return
 
        if unicode != "":
            char = unicode
        else:
            char = chr(key)
 
        if char in string.ascii_letters:
            self.buffer_text += char
            self.word_list = self.py2hz(self.buffer_text)
            self.create_word_list_surf()
            # print(self.buffer_text)
            self.state = 1
        self.text += char
 
    def safe_key_down(self, event):
        try:
            self.key_down(event)
        except:
            self.reset()
 
    def py2hz(self, pinyin):
        result = dag(self.dagparams, (pinyin,), path_num=self.limit * self.page)[
                 (self.page - 1) * self.limit:self.page * self.limit]
        data = [item.path[0] for item in result]
        return data
 
    def reset(self):
        self.state = 0 
        self.page = 1  
        self.limit = 5  
        self.pinyin = ''
        self.word_list = []  
        self.word_list_surf = None  
        self.buffer_text = ''  