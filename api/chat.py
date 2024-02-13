from fastapi import APIRouter, HTTPException, Depends, Body
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate  

load_dotenv()
router = APIRouter()
template = """Context: You are Cyklops, an information retrieval agent who knows about {context}. You should store all the necessary information and when needed provide exact details "
                   f"and stick only with {context}. The AI provides specific details from its context. "
                   f"If the AI does not know the answer to a question, it truthfully says it does not know. "

Question: {question}  

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])

@router.post("/create_conversation")
async def create_conversation(data: dict = Body({"context":"some context","question":"Your Question?"})):
    try:
        user_context = data.get('context')
        user_question = data.get('question')

        if not user_context or not user_question:
            raise HTTPException(status_code=400, detail="Context and question must be provided in the request body.")

        formatted_prompt = prompt.format(context=user_context, question=user_question)

        llm = ChatGoogleGenerativeAI(model="gemini-pro", max_output_tokens=1000)

        # Use the formatted prompt from the previous step
        result = llm.invoke(formatted_prompt)

        # Return the result
        return {"response": result.content}

    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))