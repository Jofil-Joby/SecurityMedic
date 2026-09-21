from adapters.base import AdapterContract
from agent import SecurityMedic

class OpenAIAdapter(AdapterContract):
    framework="openai"
    def run(self,path):
        return SecurityMedic().inspect(path).to_dict()
    def verify(self,path):
        result=self.run(path)
        return {"framework":self.framework,"mode":"portable","verified":super().verify(path),"result":result}
