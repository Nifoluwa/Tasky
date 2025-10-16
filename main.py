from fastapi import FastAPI
from datetime import datetime
import httpx

app = FastAPI()
url = "https://catfact.ninja/fact"
time = datetime.now().isoformat()

@app.get("/me")
async def say_hello():
    timeout = httpx.Timeout(5.0, connect=2.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            fact = response.json()["fact"]
        except httpx.RequestError as e:
            return {"Message": "Apologies, Cats have gone extinct now. Sorry",
                    "Error": e}
        return {
              "status": "success",
              "user": {
                "email": "<your email>",
                "name": "<your full name>",
                "stack": "<your backend stack>"
              },
              "timestamp": time,
              "fact": f"{fact}"
            }




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)