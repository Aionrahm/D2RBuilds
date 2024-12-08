import tkinter as tk
from tkinter import filedialog as fd
import json_handler

class GUI():
    def __init__(self):
        self.curr_char = None
        self.data = None
        self.save_char_path = "Saved/"
        self.build_path = "builds/"
        self.filetypes = (
            ('json files', '*.json'),
            ('All files', '*.*')
        )
        self.check_box_data = None

        self.root = tk.Tk()
        self.root.title("D2R Builds")
        self.root.geometry("800x600")
        self.level_frame = tk.Frame(self.root, height=500, width=200, bd=3, highlightbackground="black", highlightthickness=3, bg="red")
        self.quest_frame = tk.Frame(self.root, height=500, width=200, bd=3, highlightbackground="black", highlightthickness=3, bg="blue")
        self.info_frame = tk.Frame(self.root, height=500, width=200, bd=3, highlightbackground="black", highlightthickness=3, bg="green")
        self.char_name_lab = tk.Label(self.info_frame, text="Character Name: ")
        self.char_entry = tk.Entry(self.info_frame)
        self.load_char_button = tk.Button(self.info_frame, text="Load Char", command=self.load_char)
        self.load_guide_button = tk.Button(self.info_frame, text="Load Guide", command=self.load_build)
        
        self.level_frame.grid(row=0, column=0, rowspan=4, sticky=tk.NW, pady=2)
        self.quest_frame.grid(row=0, column=1, rowspan=4, sticky=tk.NW, pady=2)
        self.info_frame.grid(row=0, column=2, rowspan=4, sticky=tk.NW, pady=2)
        self.info_frame.grid_propagate(0)
        self.quest_frame.grid_propagate(0)
        #self.level_frame.grid_propagate(0)
        self.char_name_lab.grid(row=0, column=1, sticky= tk.W, pady=2)
        self.char_entry.grid(row=1, column=1,sticky=tk.W, pady=2)
        self.load_char_button.grid(row=2, column=1, sticky=tk.W, pady=2)
        self.load_guide_button.grid(row=3, column=1, sticky=tk.W, pady=2)
        

        self.root.mainloop()

    def populate_checkbox(self):
        i = 0
        build = "Trap Leveling"
        for d in self.check_box_data[build].keys():
            text = d
            for s in self.check_box_data["Trap Leveling"][d].keys():
                text += f" - {s}: {self.check_box_data[build][d][s]}"

            tk.Checkbutton(self.level_frame, text=str(text), anchor=tk.W).grid(row=i, column=0)
            i += 1
    
    def load_char(self):
        lc = fd.askopenfile(filetypes=self.filetypes, initialdir=self.save_char_path)
        self.read_json(lc)

    def load_build(self):
        lc = fd.askopenfilename(filetypes=self.filetypes, initialdir=self.build_path)
        self.check_box_data = self.read_json(lc)
        self.populate_checkbox()

    def read_json(self, file):
        return json_handler.sort(json_handler.read(file))

    def get_all_saves(self):
        pass

    def save_json(self):
        pass