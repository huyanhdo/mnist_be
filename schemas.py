from pydantic import BaseModel

class Models(BaseModel):
    name: str
    # @abstractmethod
    def predict(self,x):
        pass



