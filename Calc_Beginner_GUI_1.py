from tkinter import *
# ======================================SETTINGS=========================================
root = Tk()
root.title("Callculator")
root.geometry('400x400')
root.resizable(width=False, height=False)
color='gray'
root.configure(bg=color)
# ======================================FRAMES==========================================
first_frame=Frame(root,width=400,height=50,bg=color)
first_frame.pack(side=TOP)

second_frame=Frame(root,width=400,height=50,bg=color)
second_frame.pack(side=TOP)

third_frame=Frame(root,width=400,height=50,bg=color)
third_frame.pack(side=TOP)

fourth_frame=Frame(root,width=400,height=50,bg=color)
fourth_frame.pack(side=TOP)
# ======================================BUTTONS============================================
# +
btn_plus = Button(third_frame,text="+",width=5,height=2)
btn_plus.pack(side=LEFT,padx=5,pady=5)
# -
btn_minus = Button(third_frame,text="-",width=5,height=2)
btn_minus.pack(side=LEFT,padx=5,pady=5)
# *
btn_multy = Button(third_frame,text="*",width=5,height=2)
btn_multy.pack(side=LEFT,padx=5,pady=5)
# /
btn_div = Button(third_frame,text="/",width=5,height=2)
btn_div.pack(side=LEFT,padx=5,pady=5)
# ================================ENTRIES AND LABELS========================================================
# label 1
label_first_num=Label(first_frame,text="Input Number 1 :",bg=color)
label_first_num.pack(side=LEFT,pady=5)
# entry 1
first_num = Entry(first_frame,highlightbackground=color)
first_num.pack(side=LEFT)
# ---------------------------------------------------------------------------
# label 2
label_second_num=Label(second_frame,text="Input Number 1 :",bg=color)
label_second_num.pack(side=LEFT,pady=5)
# entry 2
second_num = Entry(second_frame,highlightbackground=color)
second_num.pack(side=LEFT)
# -----------------------------------------------------------------------------
# label 3
label_result=Label(fourth_frame,text="Input Number 2 :",bg=color)
label_result.pack(side=LEFT,pady=5)
# entry 3
result_num = Entry(fourth_frame,highlightbackground=color)
result_num.pack(side=LEFT)
# =======================================================================================
root.mainloop()