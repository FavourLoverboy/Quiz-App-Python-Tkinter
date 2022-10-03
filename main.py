from gui import GUI
from tkinter import ttk


score = 0

question_1 = ["Linus Torvalds created Linux and Git.", "True"]
question_2 = ["The logo for Snapchat is a Bell.", "False"]
question_3 = ["Pointers were not used in the original C programming language; they were added later on in C++.", "False"]
question_4 = ["Ada Lovelace is often considered the first computer programmer.", "True"]
question_5 = ["Time on Computers is measured via the EPOX System.", "False"]

# 1
def question_one(ans):
    c_answer = question_1[1]
    if c_answer == ans:
        global score
        score += 1
        one1.config(text="correct")
    else:
        one1.config(text="wrong")
    one_btn_1.destroy()
    one_btn_2.destroy()
    

def answer_true_one():
    answer = 'True'
    question_one(answer)

def answer_false_one():
    answer = 'False'
    question_one(answer)

# 2
def question_two(ans):
    c_answer = question_2[1]
    if c_answer == ans:
        global score
        score += 1
        two2.config(text="correct")
    else:
        two2.config(text="wrong")
    two_btn_1.destroy()
    two_btn_2.destroy()

def answer_true_two():
    answer = 'True'
    question_two(answer)

def answer_false_two():
    answer = 'False'
    question_two(answer)

# 3
def question_three(ans):
    c_answer = question_3[1]
    if c_answer == ans:
        global score
        score += 1
        three3.config(text="correct")
    else:
        three3.config(text="wrong")
    three_btn_1.destroy()
    three_btn_2.destroy()

def answer_true_three():
    answer = 'True'
    question_three(answer)

def answer_false_three():
    answer = 'False'
    question_three(answer)

# 4
def question_four(ans):
    c_answer = question_4[1]
    if c_answer == ans:
        global score
        score += 1
        four4.config(text="correct")
    else:
        four4.config(text="wrong")
    four_btn_1.destroy()
    four_btn_2.destroy()

def answer_true_four():
    answer = 'True'
    question_four(answer)

def answer_false_four():
    answer = 'False'
    question_four(answer)

# 5
def question_five(ans):
    c_answer = question_5[1]
    if c_answer == ans:
        global score
        score += 1
        five5.config(text="correct")
    else:
        five5.config(text="wrong")
    five_btn_1.destroy()
    five_btn_2.destroy()

    # Tab 4
    tab_4 = ttk.Frame(tab_control)
    tab_control.add(tab_4, text='Score')
    tab_control.grid(row=0, column=0, sticky='w')

    bottom_frame_4 = OBJ.frame(tab_4, b='white', r=1, c=0, s='w', px=240, py=50)
    inner_frame_4 = OBJ.frame(bottom_frame_4, b='#ffe3a9', r=1, c=0, s='w', px=50, py=20)

    s = f"{score} / 5"

    OBJ.label(inner_frame_4, t=s, r=0, c=0, cos=2, b="#ffe3a9", px=30, py=20)

def answer_true_five():
    answer = 'True'
    question_five(answer)

def answer_false_five():
    answer = 'False'
    question_five(answer)


# Calling Objects
OBJ = GUI()

# Creating Window
win_start = OBJ.window('Quiz Game', sz="600x250", b="white")

# Creating Frames
top_frame = OBJ.frame(win_start, b='red', r=0, c=0, s='w', px=5)

# Creating Tabs
tab_control = ttk.Notebook(top_frame) # Create tab control

# Tabs One
tab_1 = ttk.Frame(tab_control)
tab_control.add(tab_1, text='Q1')
tab_control.grid(row=0, column=0, sticky='w')

bottom_frame_1 = OBJ.frame(tab_1, b='white', r=1, c=0, s='w', px=240, py=50)
inner_frame_1 = OBJ.frame(bottom_frame_1, b='#ffe3a9', r=1, c=0, s='w', px=50, py=20)

# Creating Labels
# OBJ.label(top_frame, t="Welcome", r=0, c=0, cos=2, fts=45, b="blue") 
one1 = OBJ.label(inner_frame_1, t=question_1[0], r=0, c=0, cos=2, b="#ffe3a9", px=30, py=20) 

# Creating Buttons
one_btn_1 =  OBJ.button(inner_frame_1, t="True", b="#14c38f", cm=answer_true_one, h=4, w=25, r=1, c=0, px=58, py=45)
one_btn_2 =  OBJ.button(inner_frame_1, t="False", b="#ff5d5d", cm=answer_false_one, h=4, w=25, r=1, c=1, px=58, py=45)

# Tabs Two
tab_2 = ttk.Frame(tab_control)
tab_control.add(tab_2, text='Q2')
tab_control.grid(row=0, column=1, sticky='w')

bottom_frame_2 = OBJ.frame(tab_2, b='white', r=1, c=0, s='w', px=240, py=50)
inner_frame_2 = OBJ.frame(bottom_frame_2, b='#ffe3a9', r=1, c=0, s='w', px=50, py=20)

# Creating Labels
# OBJ.label(top_frame, t="Welcome", r=0, c=0, cos=2, fts=45, b="blue") 
two2 = OBJ.label(inner_frame_2, t=question_2[0], r=0, c=0, cos=2, b="#ffe3a9", px=30, py=20) 

# Creating Buttons
two_btn_1 = OBJ.button(inner_frame_2, t="True", b="#14c38f", cm=answer_true_two, h=4, w=25, r=1, c=0, px=58, py=45)
two_btn_2 = OBJ.button(inner_frame_2, t="False", b="#ff5d5d", cm=answer_false_two, h=4, w=25, r=1, c=1, px=58, py=45)

# Tab Three
tab_3 = ttk.Frame(tab_control)
tab_control.add(tab_3, text='Q3')
tab_control.grid(row=0, column=1, sticky='w')

bottom_frame_3 = OBJ.frame(tab_3, b='white', r=1, c=0, s='w', px=240, py=50)
inner_frame_3 = OBJ.frame(bottom_frame_3, b='#ffe3a9', r=1, c=0, s='w', px=50, py=20)

# Creating Labels
# OBJ.label(top_frame, t="Welcome", r=0, c=0, cos=2, fts=45, b="blue") 
three3 = OBJ.label(inner_frame_3, t=question_3[0], r=0, c=0, cos=2, b="#ffe3a9", px=30, py=20) 

# Creating Buttons
three_btn_1 = OBJ.button(inner_frame_3, t="True", b="#14c38f", cm=answer_true_three, h=4, w=25, r=1, c=0, px=58, py=45)
three_btn_2 = OBJ.button(inner_frame_3, t="False", b="#ff5d5d", cm=answer_false_three, h=4, w=25, r=1, c=1, px=58, py=45)

# Tab Four
tab_4 = ttk.Frame(tab_control)
tab_control.add(tab_4, text='Q4')
tab_control.grid(row=0, column=1, sticky='w')

bottom_frame_4 = OBJ.frame(tab_4, b='white', r=1, c=0, s='w', px=240, py=50)
inner_frame_4 = OBJ.frame(bottom_frame_4, b='#ffe3a9', r=1, c=0, s='w', px=50, py=20)

# Creating Labels
# OBJ.label(top_frame, t="Welcome", r=0, c=0, cos=2, fts=45, b="blue") 
four4 = OBJ.label(inner_frame_4, t=question_4[0], r=0, c=0, cos=2, b="#ffe3a9", px=30, py=20) 

# Creating Buttons
four_btn_1 = OBJ.button(inner_frame_4, t="True", b="#14c38f", cm=answer_true_four, h=4, w=25, r=1, c=0, px=58, py=45)
four_btn_2 = OBJ.button(inner_frame_4, t="False", b="#ff5d5d", cm=answer_false_four, h=4, w=25, r=1, c=1, px=58, py=45)

# Tab Five
tab_5 = ttk.Frame(tab_control)
tab_control.add(tab_5, text='Q5')
tab_control.grid(row=0, column=1, sticky='w')

bottom_frame_5 = OBJ.frame(tab_5, b='white', r=1, c=0, s='w', px=240, py=50)
inner_frame_5 = OBJ.frame(bottom_frame_5, b='#ffe3a9', r=1, c=0, s='w', px=50, py=20)

# Creating Labels
# OBJ.label(top_frame, t="Welcome", r=0, c=0, cos=2, fts=45, b="blue") 
five5 = OBJ.label(inner_frame_5, t=question_5[0], r=0, c=0, cos=2, b="#ffe3a9", px=30, py=20) 

# Creating Buttons
five_btn_1 = OBJ.button(inner_frame_5, t="True", b="#14c38f", cm=answer_true_five, h=4, w=25, r=1, c=0, px=58, py=45)
five_btn_2 = OBJ.button(inner_frame_5, t="False", b="#ff5d5d", cm=answer_false_five, h=4, w=25, r=1, c=1, px=58, py=45)

OBJ.mainloop(win_start)
