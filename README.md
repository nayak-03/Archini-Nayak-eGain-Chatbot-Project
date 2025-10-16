# eGain-Chatbot-Project
A simple chatbot to help you track your lost packages.

---

### Setup Instructions:
Setup assumes the user has Python installed on their computer. Any version of Python 3 is acceptable.  
Library Dependencies (should all come with a basic Python installation): 
- re (regex)
- json (for .json file parsing)  

Click the green "code" button, and then click "download as .zip". Once downloaded, please unzip the folder into the desired location. Open the terminal to access your command line interface. Navigate to the folder into where you unzipped the download. Type the following into the command line:  

`python .\chatbot.py`    

The chatbot should greet you. Type your answers to the chatbot's questions into the command line interface. 

---

### Overall Approach

I chose to build a package tracking chatbot that balances helpfulness with security. If given a tracking number, the chatbot is able to look it up in a database of packages. If not, the chatbot is able to file a service request on the user's behalf.

---

### Technical Approach

For security reasons, the chatbot only retrieves and displays package information when a valid tracking number is provided.

Each user scenario is contained in its own function, which manages both logic and exception handling internally. The main flow function contains only high-level conversation logic (following the chatbot flowchart) and does not handle user messages or exceptions explicitly. This isolation makes for clean, modular code flow that is easy to maintain and add to. 

The modular functionality also allows for the user to enter the "escalate issue" branch of the tree at a variety of places.

Additionally, I chose descriptive variable names even when they were slightly long, to improve readability.

---

### Error Handling

Since users can often provide invalid or incomplete inputs, I wanted robust error handling. Examples include:

- Accepting only “yes” or “no” responses for "yes or no" questions.
- Identifying correctly formatted tracking numbers, and allowing retries for mistyped numbers.
- Validating names to exclude numeric characters.
- Verifying that email addresses follow standard email address formatting.

This prevents confusing or broken user interactions; the bot will only exit when the conversation is completed.

---

### Challenges

One of the main challenges was creating a natural-sounding conversation without bloating the flowchart with edge cases. This was resolved very nicely by abstracting every scenario into independent, callable functions that returned descriptive values. 

Another challenge was implementing correct input validation. I found that using primarily yes/no questions worked well, while still collecting necessary information. 

---

### Potential Improvements

If given more time, I would focus on two main enhancements:

1. Secure email/phone number access:
   In my initial brainstorm, I briefly considered a way for users to retrieve package information using additional identifiers such as an email or a phone number. However I realized that this functionality was insecure and could be abused, so I decided against including it in the prototype. In the future, I would want to implement one-time passwords or two-factor auth, to allow users without their tracking numbers to access updates using the bot as well.

2. Complaint submission system:
   Adding a system for the complaint data to be properly stored. Currently, the chatbot collects information, but doesn't store it anywhere. 



