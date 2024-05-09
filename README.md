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

Firstly we deine the app using FastAPI.
Then we difine the model and prompt, add it to the route, so as the generate the api

    app = FastAPI(
      title="Langchain Server",
      version="1.0",
      description="A simple API server"
    )
    model = ChatOpenAI()

    prompt1 = ChatPromptTemplate.from_template("Write me an essay about a {topic} with 100 words")

    add_routes(
      app,
      prompt1|model,
      path="/essay"
    )


    if __name__ == "__main__":
      uvicorn.run(app, host="localhost", port=8000)

You can view the docs after running:

> python app.py

Visit to see api documentation: http://localhost:8000/docs

In the client app, we can invoke the api as below:

    def get_openai_response(input_text):
      response = requests.post("http://localhost:8000/essay/invoke", json={'input': {'topic': input_text}})

      return response.json()['output']['content']

    st.title('Langchain demo with openai & llama2 API')
    input_text_essay = st.text_input('Write an essay on')

    if input_text_essay:
      st.write(get_openai_response(input_text_essay))

Then run:

> streamlit run api/client.py

Visit: http://localhost:8501/
