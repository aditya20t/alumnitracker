import tkinter
from tkinter.ttk import Button
from flask import Flask, render_template, request

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
from tkinter.ttk import *

bot = ChatBot("My Bot")
convo = [
    'hello',
    'hi there',
    'what is your name?',
    'My name is virus, created by @$',
    'how are you?',
    'i m doing great these days',
    'thank you', 'In which city do you live?',
    'i live in bhopal',
    'which is the best college?',
    'lakshmi narain college of technology',
    'In which language you talk?'
    'I mostly talk in english'
]
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer = ListTrainer(bot)

trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot")
# while True:
#   query = input()
#  if query == 'exit':
#     break
#    answer = bot.get_response(query)
#   print("bot :", answer)

main = tkinter.Tk()
main.geometry("300x550")
main.title("My chat bot")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "Bot: " + str(answer_from_bot))
    textF.delete(0, END)


frame = Frame(main)

sc = Scrollbar(frame)

msgs = Listbox(frame, width=40, height=25)
sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text='Ask us',
             command=ask_from_bot)
btn.pack()


def enter_function(event):
    btn.invoke()

    main.bind('<return>', enter_function)


main.mainloop()