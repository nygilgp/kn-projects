# Create Environment

## Using Python command

Create environment for python project

> python -m venv myenv

Activate project

> myenv\Scripts\activate

Install packages in the virtual env, after activation

> pip install numpy

If you need more packages, create a <b>requirements.txt file</b>

## Using virtualenv

Install virtualenv

> pip install virtualenv

Create virtual environment

> virtualenv -p python3 virtual_env

Activate

> viral_env\Scripts\activate

## Using conda

Install conda

Create virtual environment

> conda create -p venv python==3.11 -y

conda create --name <env_name> --file requirements.txt
pip install -r requirements.txt
pip uninstall -r requirements.txt

# Create a chatbot with langchain

1. First we will set the prompt template
2. We will init streamlit and set the input field
3. The llm model is initiated
4. Output parset is initiated
5. Create the chain with prompt, llm and the output parser
6. Finally we create the output writer, which will wait for user input.

# Create a API with langchain
