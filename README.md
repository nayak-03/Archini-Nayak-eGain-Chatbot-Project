# eGain-Chatbot-Project
A simple chatbot to help you track your lost packages.

---

### Setup Instructions:
Setup assumes the user has Python installed on their computer. Any version of Python 3 is acceptable.  
Library Dependencies (should all come with a basic Python installation): 
- re (regex)
- json (for .json file parsing)  

To download, click the green "code" button, and then click "Download ZIP." Once downloaded, please unzip the folder into the desired location. Open the terminal to access your command line interface. In your command line interface, navigate to the folder where you unzipped the download. Type the following into the command line:  

`python .\chatbot\chatbot.py`    

The chatbot should greet you. Type your answers to the chatbot's questions into the command line interface. 

---

### Overall Approach

I chose to build a package tracking chatbot that balances helpfulness, security, and exception-safety. The conversation flow for the chatbot is given below:

<img width="936" height="451" alt="eGain_Chatbot_Flowchart drawio" src="https://github.com/user-attachments/assets/4692b4d7-b9c5-4137-8104-aaf81f974d24" />


My main focuses were:  
**Security:** The chatbot only reveals package information upon receiving a valid tracking number.   
**Helpfulness:** Bot gives helpful reminders, and collects information to make service requests on the customer's behalf.  
**Exception-safety:** A smooth and error-free user experience reflects well on the company – the customer should never have a broken or buggy interface.   

---

### Technical Approach

Each user scenario is contained in its own function, which manages both logic and exception handling internally. This isolation makes for clean, modular code flow that is easy to maintain and add to. 

<img width="423" height="60" alt="Screenshot 2025-10-16 013339" src="https://github.com/user-attachments/assets/0b9f1b7c-dcab-4abf-8658-77221419e7ef" />

<img width="433" height="73" alt="Screenshot 2025-10-16 013416" src="https://github.com/user-attachments/assets/2c985818-482a-4aea-a8e5-fac8b0e976f7" />

Additionally, I prioritized human-readability. I chose descriptive variable and function names even when they were slightly long. The main flow function contains only high-level conversation logic (following the chatbot flowchart) and does not handle user messages or exceptions, making it easy to understand and maintain. 

---

### Exception Safety
  
I wanted the user experience to be smooth and error-free. Since users can often provide invalid or incomplete inputs, I wanted robust error handling. Examples include:

- Accepting only “yes” or “no” responses for "yes or no" questions.
- Identifying correctly formatted tracking numbers, and allowing retries for mistyped numbers.
- Validating names to exclude numeric characters.
- Verifying that email addresses follow standard email address formatting.

This prevents confusing or broken user interactions; the bot will only exit when the conversation is completed.

<img width="1089" height="265" alt="Screenshot 2025-10-16 020538" src="https://github.com/user-attachments/assets/107b482a-27d5-4fad-be7e-b1c708987cbe" />

---

### Challenges

One of the main challenges was creating a natural-sounding conversation without bloating the flowchart with edge cases. This was resolved very nicely by abstracting every scenario into independent, callable functions that returned descriptive values.

Another challenge was implementing correct input validation. I found that using primarily yes/no questions worked well, while still collecting necessary information. I also used outside libraries to help validate common data types (name, email, etc).

<img width="1074" height="441" alt="Screenshot 2025-10-16 020814" src="https://github.com/user-attachments/assets/27c647f8-ad1c-40e8-acce-d73e35dff056" />

---

### Potential Improvements

If given more time, I would focus on two main enhancements:

1. **Secure email/phone number access:**   
   In my initial brainstorm, I briefly considered a way for users to retrieve package information using additional identifiers such as an email or a phone number. However I realized that this functionality was insecure and could be abused, so I decided against including it in the prototype. In the future, I would want to implement one-time passwords or two-factor auth, to allow users without their tracking numbers to access updates using the bot as well.

2. **Common issue descriptions:**
   I would analyze customer data to determine the top N most common problems ("delivered" but not received, delayed for more than 2 weeks, etc). Then, I would add the problems as options to be included with the filed service request. Later on in the process, this would help us sort the requests by urgency based on the issue.


