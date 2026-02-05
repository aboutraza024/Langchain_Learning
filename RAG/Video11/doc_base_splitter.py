from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter,Language

splitter = RecursiveCharacterTextSplitter.from_language(Language.PYTHON,chunk_size=400,chunk_overlap=0)
text="""
class DummyClass:
    def __init__(self, name="dummy", value=0):
        self.name = name
        self.value = value

    def increment(self, amount=1):
        self.value += amount
        return self.value

    def reset(self):
        self.value = 0

    def __repr__(self):
        return f"DummyClass(name={self.name!r}, value={self.value})"


if __name__ == "__main__":
    dummy = DummyClass()
    print(dummy)
    dummy.increment(5)
    print(dummy)
    dummy.reset()
    print(dummy)

"""

docs=splitter.split_text(text)
print(len(docs))
for i in range(len(docs)):
    print(f"Document {i+1}:\n{docs[i]}\n")

