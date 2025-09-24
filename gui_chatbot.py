import tkinter as tk
from tkinter import scrolledtext, messagebox
from agent_setup import agent_executor, parser  
from langchain.schema import HumanMessage, AIMessage

class ExamChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Government Exam Research Assistant")
        self.root.geometry("750x650")
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.user_input = tk.Entry(self.input_frame, font=("Arial", 12))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,5))
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

      
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X, padx=10, pady=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear Chat", command=self.clear_chat)
        self.clear_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.button_frame, text="Save Chat", command=self.save_chat)
        self.save_button.pack(side=tk.RIGHT)

      
        self.chat_history =[]

        self.insert_message("Assistant", "Welcome! I am your Government Exam Research Assistant.\nType your exam query below and press Send.")

    def insert_message(self, sender, message):
        """Insert message into chat area"""
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

 

    def send_message(self, event=None):
        user_msg = self.user_input.get().strip()
        if not user_msg:
            return
        self.insert_message("You", user_msg)
        self.user_input.delete(0, tk.END)

       
        self.chat_history.append(HumanMessage(content=user_msg))

        try:
            raw_response = agent_executor.invoke({
                "query": user_msg,
                "chat_history": self.chat_history
            })

            structured_response = parser.parse(raw_response.get("output")[0]["text"])

            assistant_msg = f"Exam: {structured_response.exam_name}\n\n"
            assistant_msg += "Topics:\n" + "\n".join(f"- {t}" for t in structured_response.topics) + "\n\n"
            assistant_msg += "Questions:\n" + "\n".join(f"- {q}" for q in structured_response.questions) + "\n\n"
            assistant_msg += "Previous Year Summary:\n" + structured_response.previous_year_summary

            self.insert_message("Assistant", assistant_msg)

            
            self.chat_history.append(AIMessage(content=raw_response.get("output")[0]["text"]))

        except Exception as e:
            self.insert_message("Assistant", f"Error parsing response: {e}")

    def clear_chat(self):
        """Clear the chat window and history"""
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state='disabled')
        self.chat_history = ""
        self.insert_message("Assistant", "Chat cleared. You can start a new query now.")

    def save_chat(self):
        """Save the chat history to a file"""
        try:
            with open("chat_history.txt", "a", encoding="utf-8") as f:
                f.write(self.chat_history + "\n\n")
            messagebox.showinfo("Saved", "Chat history saved to chat_history.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save chat: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExamChatbotApp(root)
    root.mainloop()
