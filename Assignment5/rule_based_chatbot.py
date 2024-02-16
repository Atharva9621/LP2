from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

qa_pairs = [
    {"question": "What is your name?", "answer": "I am a chatbot."},
    {"question": "What can you do?", "answer": "I can answer questions and provide assistance."},
    {"question": "How does your company provide AI products?", "answer": "We build AI products and provide cloud options to deploy them at scale."},
    {"question": "What kind of AI products does your company build?", "answer": "We build various AI products for different industries."},
    {"question": "Can you explain your data analytics services?", "answer": "We offer data analytics services to help businesses make sense of their data."},
    {"question": "Do you offer cloud deployment options?", "answer": "Yes, we offer cloud options for deploying AI products."},
    {"question": "How can I deploy my AI model at scale?", "answer": "You can use our cloud options to deploy your AI model at scale."},
    {"question": "What technologies do you use for building AI products?", "answer": "We use various technologies such as machine learning, deep learning, and natural language processing."},
    {"question": "Can you provide customer support?", "answer": "Yes, we provide customer support for our products and services."},
    {"question": "How can I get started with your company?", "answer": "You can contact us through our website to get started with our products and services."}
]

class RuleBasedChatbot:
    def __init__(self, qa_context=qa_pairs, model='paraphrase-multilingual-MiniLM-L12-v2', conf_threshold = 0.3):
        self.qa_pairs = qa_context
        self.model = SentenceTransformer(model)
        for item in self.qa_pairs:
            item["embedding"] = self.model.encode(item["question"])

    def answer_qs(self, qs):
        user_embed = self.model.encode(qs)
        max_score , max_answer = -2, "Something went wrong"
        for qa in self.qa_pairs:
            qa_embed = self.model.encode(qa["question"])
            score = cosine_similarity(qa_embed.reshape(1, -1), user_embed.reshape(1, -1))
            if score > max_score:
                max_score = score
                max_answer = qa["answer"]

        return max_answer

    def run_chatbot(self):
        while(True):
            qs = input("Please ask your question ... ")
            response = self.answer_qs(qs)
            print(response)
            print("-------------------------------------")

if __name__ == "__main__":
    rbc = RuleBasedChatbot(qa_pairs)
    rbc.run_chatbot()