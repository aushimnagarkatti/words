# A crowd-sourced repository for students

## words: A python application to run vocabulary building flashcards

### Clone repository:
`git clone https://github.com/aushimnagarkatti/words.git`

### Dependencies:
tkinter
python3.12.4+ (required for ARM OSx)

If you use conda to manage environments,
`conda update python`
before running the app

If button clicks do not always register, your python3
needs to update its tk package
On macOS:
`brew install python-tk`


### Usage:

`cd words`

`python3 words.py`

To add a word to database,
Uncomment the following lines in words.py:
```
app.add_word("Insert Word", "Meaning")
app.save_words()
```

## LEARNINGS.md:

A repository of links to navigate grad school
