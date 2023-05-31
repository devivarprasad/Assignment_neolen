import os

class Agent:
    def __init__(self):
        self.file_contents = ""

    def upload_files(self, files):
        for file in files:
            with open(file, 'r') as f:
                self.file_contents += f.read()

    def process_question(self, question):
        
        if question in self.file_contents:
            return self.file_contents[question]
        else:
            return "I'm sorry, I don't have the answer to that question."

agent=Agent()

while True:
    user_input = input("Please enter your command (create/upload/ask/exit): ")

    if user_input == "create":
        agent = Agent()
        print("Agent created successfully!")

    elif user_input == "upload":
        file_list = input("Enter the file names (separated by commas): ").split(",")
        file_list = [f.strip() for f in file_list]
        
        
        valid_files = []
        for file in file_list:
            if os.path.isfile(file):
                valid_files.append(file)
            else:
                print(f"File '{file}' does not exist.")
        
        if valid_files:
            agent.upload_files(valid_files)
            print("Files uploaded successfully!")

    elif user_input == "ask":
        question = input("Enter your question: ")
        answer = agent.process_question(question)
        print("Agent's answer:", answer)

    elif user_input == "exit":
        print("Exiting the program...")
        break

    else:
        print("Invalid command! Please try again.")
