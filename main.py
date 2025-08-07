import os
import json
import time
import logging
from typing import Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
from pyngrok import ngrok

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI(title="OpenAI OSS Voice Agent", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY")
)

class ChatRequest(BaseModel):
    messages: list[dict]
    model: Optional[str] = "gpt-oss-120b"
    max_completion_tokens: Optional[int] = 65536
    temperature: Optional[float] = 0.5
    top_p: Optional[float] = 1.0
    reasoning_effort: Optional[str] = "low"

@app.post("/chat/completions")
async def chat_completions(request: ChatRequest):
    logger.info(f"Received chat completion request with {len(request.messages)} messages")
    
    try:
        start_time = time.time()
        logger.info("Creating stream with OpenAI OSS model")
        stream = client.chat.completions.create(
            messages=request.messages,
            model=request.model,
            stream=True,
            max_completion_tokens=request.max_completion_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            reasoning_effort=request.reasoning_effort
        )
        
        def generate():
            first_chunk = True
            for chunk in stream:
                if first_chunk:
                    first_chunk = False
                    end_time = time.time()
                    logger.info(f"TTFT: {end_time - start_time:4f} seconds")
                    continue
                json_data = chunk.model_dump_json()
                yield f"data: {json_data}\n\n"
        
        return StreamingResponse(generate(), media_type="text/event-stream")
        
    except Exception as e:
        logger.error(f"Error in chat_completions: {str(e)}")
        logger.error(f"Exception type: {type(e).__name__}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    logger.info("Health check requested")
    return {"status": "healthy", "timestamp": time.time()}

if __name__ == "__main__":
    import uvicorn
    
    # Setup ngrok tunnel
    logger.info("Setting up ngrok tunnel...")
    ngrok_tunnel = ngrok.connect(8000)
    logger.info(f"Public URL: {ngrok_tunnel.public_url}")
    print(f"Public URL: {ngrok_tunnel.public_url}")
    print("Client initialised")
    
    # Run the FastAPI server
    logger.info("Starting FastAPI server...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)