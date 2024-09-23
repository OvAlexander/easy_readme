import customtkinter
import markdown
from markdown2 import Markdown
from tkhtmlview import HTMLLabel

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
APPEARANCE_MODE = ["system", "dark", "light"]

class TextBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.label = customtkinter.CTkLabel(self, text=title, fg_color="transparent", justify="center", anchor = "center")
        self.label.grid(row=0, column=0, sticky="NSEW")
        self.text_box = customtkinter.CTkTextbox(self)
        self.text_box.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")
        self.raw_markdown = "tEST"
        self.html = "<h1>test</h1>"
        self.title = title.lower().replace(" ", "_")
        print(self.title)

        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.add("raw")
        self.tabview.add("markdown")
        self.tabview.set("markdown")

        self.raw_text_box = customtkinter.CTkTextbox(master=self.tabview.tab("raw"), fg_color="transparent", bg_color="white")
        self.raw_text_box.insert("0.0", self.raw_markdown)
        self.raw_text_box.grid(row=0, column=0)

        self.html_label = HTMLLabel(master=self.tabview.tab("markdown"))
        self.html_label.set_html(self.html)
        self.html_label.grid(row=0, column=0)

        self.tabview.grid(row=1,column=1, sticky="NSEW")

        self.update_button = customtkinter.CTkButton(self, text="Update", command=self.update)
        self.update_button.grid(row=2,column=0, columnspan=1, sticky="NSEW")

        self.push_button = customtkinter.CTkButton(self, text="Push", command=self.push(self.title))
        self.push_button.grid(row=2,column=1, columnspan=1, sticky="NSEW")
        self.fetch_readme(self.title)
        
        
    def update(self):
        self.raw_markdown = self.text_box.get("0.0", "end")
        self.html = Markdown().convert(self.raw_markdown)
        self.raw_text_box.configure(state="normal")
        self.raw_text_box.delete("0.0", "end")
        self.raw_text_box.insert("0.0", self.raw_markdown)
        self.raw_text_box.configure(state="disabled")
        self.html_label.set_html(self.html)
    
    def push(self, file_name):
        self.output_text = self.text_box.get("0.0", "end")
        file_path = f"./output/{file_name}.md"
        file = open(file_path, "w")
        print(f"Writing\n{self.output_text}")
        file.write(self.output_text)
        file.close()

    def fetch_readme(self, file: str):
        file = f"./templates/{file}.md"
        md_file = open(file, "r")
        md_text = md_file.readlines()
        md_file.close()
        parsed_text = ""
        for text in md_text:
            parsed_text += text
        self.text_box.insert("0.0", parsed_text)
        self.update()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EASY README")
        self.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self._set_appearance_mode(APPEARANCE_MODE[1])

        self.label = customtkinter.CTkLabel(self, text="EASY README", fg_color="transparent")
        self.label.grid(row=0, column=0, sticky = "NSEW", columnspan=2)

        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.add("Acknowledgements")
        self.tabview.add("Contributing")
        self.tabview.add("Getting Started")
        self.tabview.add("License")
        self.tabview.set("Acknowledgements")
        self.ack_frame = TextBoxFrame(self.tabview.tab("Acknowledgements"), title="Acknowledgements")
        self.ack_frame.grid(row=1,column=0,sticky="NSWE")
        self.ack_frame = TextBoxFrame(self.tabview.tab("Contributing"), title="Contributing")
        self.ack_frame.grid(row=1,column=1,sticky="NSWE")
        self.ack_frame = TextBoxFrame(self.tabview.tab("Getting Started"), title="Getting Started")
        self.ack_frame.grid(row=1,column=1,sticky="NSWE")
        self.ack_frame = TextBoxFrame(self.tabview.tab("License"), title="License")
        self.ack_frame.grid(row=1,column=1,sticky="NSWE")
        self.tabview.grid(row=1,column=0, columnspan=2, sticky="NSEW")

        

if __name__ == "__main__":
    app = App()
    app.mainloop()
