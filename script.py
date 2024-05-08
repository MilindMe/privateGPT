from langchain_community.llms.ollama import Ollama
import time

start_time = time.time()
model = Ollama(model="mistral") 
prompt = input("INSERT PROMPT ")
response_text = model.invoke(prompt)
formatted_response = f"Response: {response_text}\n"
print (formatted_response)
print ("%s" % (time.time() - start_time))

