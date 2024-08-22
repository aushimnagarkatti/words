#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import font as tkfont
import random
import json

class FlashCard:
    def __init__(self, root, filename= "word_relations.json"):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.filename = filename
        self.root.title("Words")
        self.randk = ""
        self.words = {}
        self.load_words()
        self.word_len = len(self.words)
        self.d_iter=list(self.words.keys())

        # Create widgets
        self.create_widgets()

    def load_words(self):
        """Load json."""
        # Load words from file
        # Read data from file:
        self.words = json.load(open(self.filename))

    def save_words(self):
        """Dump the json output to file."""
        #Save json
        json.dump(self.words, open(self.filename, 'w'))
    
    def add_word(self, word, meaning):
        """Add a word to vocabulary """
        if (self.word_len == 0):
            self.load_words()
        self.words[word]=meaning
        self.word_len = len(self.words)


    def next_word(self):
        """Set the text of the button to a random word."""
        self.T.delete('1.0', tk.END)
        if (self.word_len):
            self.randk=random.choice(self.d_iter) 
            self.T.insert(tk.END, self.randk)

    def quit_app(self):
        """Close the application."""
        self.root.quit()
    
    def show_meaning(self):
        """ Reveal word meaning """
        self.T.delete('1.0', tk.END)
        if (self.randk != ""):
            self.T.insert(tk.END, self.randk + ": " + self.words[self.randk])

    def create_widgets(self):
        """Create and place the widgets on the window."""

        self.T = tk.Text(root, height = 30, width = 90)
        self.T.configure(font = ("Arial", 20, "bold"))
        self.T.pack()

        self.word_button = tk.Button(
            self.root,
            text='Next',
            height=2,
            width=5,
            command=self.next_word,
        )
        self.word_button.pack(side='right')


        self.meaning = tk.Button(
            self.root,
            text='Meaning',
            height=2,
            width=5,
            command=self.show_meaning
        )
        self.meaning.pack(side= 'left')
        
        self.quit_button = tk.Button(
            self.root,
            text='QUIT',
            height=2,
            width=5,
            command=self.quit_app
        )
        self.quit_button.pack(side='bottom')


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashCard(root)
    ### ToDo: Add commandline options
    ### The following will add a word to the database optionally
    # app.add_word("Test Word", "Meaning")
    # app.save_words()
    root.mainloop()
