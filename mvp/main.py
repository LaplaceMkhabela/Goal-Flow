from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from keys.keys import API_KEY


def ai(goal):
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key= API_KEY
    )

    result = model.invoke(f"Break the following goal into tasks, goal: {goal}")

    return result.content

def html(tasks):
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key= API_KEY
    )

    result = model.invoke(f"Create an html page from the following {tasks}")

    return result.content

tasks = ai('I want learn python')
page = html(tasks)



with open('goals.html','w') as file:
    file.write(page)
    print('done')


print(page)