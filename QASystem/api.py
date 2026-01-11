from fastapi import APIRouter
from QASystem.schemas import QuestionRequest, AnswerResponse
from QASystem.services.rag import build_rag_chain

router = APIRouter()
rag_chain = build_rag_chain()


@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    result = rag_chain.run(request.question)
    return AnswerResponse(answer=result)
