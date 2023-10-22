import dotenv
import requests
import streamlit as st
from humanloop import Humanloop

from webscraper import call_nhs_search

dotenv.load_dotenv()
import os

# Constants
HUMAN_LOOP_API_KEY = os.getenv("HUMAN_LOOP_API_KEY")  # add Humanloop API Key
PROJECT_ID = os.getenv("PROJECT_ID")  # add project ID
hl = Humanloop(api_key=HUMAN_LOOP_API_KEY)


def search_papers(search_term, page=1):
    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    url = f'{base_url}?db=pubmed&term={search_term}&retmode=json&retstart={((page - 1) * 3)}&retmax=3'
    try:
        response = requests.get(url)
        data = response.json()
        pubmed_ids = data['esearchresult']['idlist']

        results = []

        for pubmed_id in pubmed_ids:
            summary_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pubmed_id}&retmode=json'
            summary_response = requests.get(summary_url)
            summary_data = summary_response.json()
            article_title = summary_data['result'][pubmed_id]['title']
            article_url = f'https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/'
            authors = summary_data['result'][pubmed_id]['authors']
            author_names = [author['name'] for author in authors]
            final_response = f"<a href='{article_url}' target='_blank'>{article_title}</a> by {', '.join(author_names)}"
            results.append(final_response)

        for result in results:
            print(result)

        return results

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")


def run_conversation(content):
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": content}]
    response = hl.chat_deployed(
        project_id=PROJECT_ID,
        messages=messages,
    )

    response = response.body["data"][0]  # first response
    print(response, messages)
    print(response["output"])

    if response.get("output") != None:
        # Step 2: call the function
        tool_name = response["output"]
        # TODO: pubMed needs to return search arguments

        if tool_name.startswith('pubMed'):
            print("selected pubmed")
            pubmed_args = response["output"].split("-")[1:]
            tool_result = search_papers(search_term=pubmed_args)
        elif tool_name.startswith('nhs'):
            print("selected nhs")
            # tool_result = "query_wolfram_alpha(query=tool_args.get('query'))"
            nhs_args = response["output"].split("-")[1:]
            tool_result = "The following links are treatment options from the nhs, highlight that they are not a substitute for a physician's advice\t" + str(
                call_nhs_search(query=" ".join(
                    nhs_args)))
        elif tool_name == 'pdf':
            print("selected pdf")
            tool_result = "query_wolfram_alpha(query=tool_args.get('query'))"
        else:
            raise NotImplementedError("My code does not know about this tool!")

        # Step 3: send the response back to the model
        messages.append(
            {
                "role": "assistant",
                # "name": tool_name,
                "content": str(tool_result),
            }
        )
        # messages.append(
        #     {"role": "assistant", "content": "", "tool_call": response["tool_call"]}
        # )
        second_response = hl.chat_deployed(
            project_id=PROJECT_ID,
            messages=messages,
        )
        return second_response.body["data"][0]
    else:
        return response
    # if response.get("tool_call"):
    #     # Step 2: call the function
    #     tool_name = response["tool_call"]["name"]
    #     tool_args = json.loads(response["tool_call"]["arguments"])
    #
    #     if tool_name == 'get_pub_med_paper':
    #         tool_result = search_papers(search_term=tool_args.get("search_term"))
    #     elif tool_name == 'nhs':
    #         print("selected nhs")
    #         tool_result = "query_wolfram_alpha(query=tool_args.get('query'))"
    #     else:
    #         raise NotImplementedError("My code does not know about this tool!")
    #
    #     # Step 3: send the response back to the model
    #     messages.append(
    #         {"role": "assistant", "content": "", "tool_call": response["tool_call"]}
    #     )
    #     messages.append(
    #         {
    #             "role": "tool",
    #             "name": tool_name,
    #             "content": json.dumps(tool_result),
    #         }
    #     )
    #     second_response = hl.chat_deployed(
    #         project_id=PROJECT_ID,
    #         messages=messages,
    #     )
    #     return second_response.body["data"][0]


# Streamlit app - run if you want to use Streamlit

def run_app():
    st.title("Med-Xplain")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What can I help with?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Call your run_conversation function
        response_data = run_conversation(prompt)

        # Extract the desired message from the response_data
        response_content = response_data["output"] if response_data else f"Error processing request: {prompt}"

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response_content)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_content})


# Actually run the app
if __name__ == "__main__":
    run_app()
