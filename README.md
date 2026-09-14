1. Create README.md file for taking notes
##saving code
1. on the LHS screen, go to source control
client to add files to commit (i.e, stage changes)
Enter a commit message
click commit
click sync changes
check github repository to confirm

##setting up envi in terminal
1. Create virtual environment
>python -m venv .venv
2.Activate virtual environment
>source .venv/bin/activate
3. To install libraries / dependencies, first create a requirements.txt file
4. add openai, streamlit, python-dotenv to requirements text file
5. install dependencies by refering to requirements.txt file
>pip install -r requirements.txt
>pip install --upgrade pip
6. Create a .env file
7. Ensure .env file is grayed out (git ignored) if not edit .gitignore to include .env
8. Add secrets to .env
>OPENAI_API_KEY = "<insert>"

##Create some Code
1. Create a python file - call it whatever you like - home.py by convention
2. run strreamlit, referring to python file i created
>streamlit run home.py

##Create Code in your python file
1. Import streamlit
>import streamlit as st
2. Import openai
3. import python

#control C will stop the server running