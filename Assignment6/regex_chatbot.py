import re
from typing import List

qa_pairs = [
    {"question": "Do you have specific store hours?", "answer": "Yes, we provide our services from 8:00 AM to 10:00 PM every day.", 
        "keywords": ["hour", "timing", "time"]},
    {"question": "Can I request home delivery?", "answer": "Yes, we provide home delivery services for orders placed online or over the phone.",
        "keywords": ["home", "delivery"]},
    {"question": "Are there discounts for bulk purchases?", "answer": "Yes, we offer discounts on bulk purchases, especially for items like rice, pasta, and canned goods.",
        "keywords": ["discount", "offer", "bulk"]},
    {"question": "Is there a section dedicated to organic produce?", "answer": "Yes, we have a dedicated section for organic fruits and vegetables.",
        "keywords": ["green", "organic"]},
    {"question": "Can I find a variety of international foods?", "answer": "Yes, we carry a diverse range of international foods, from Asian spices to European cheeses.",
        "keywords": ["international", "global"]},
    {"question": "Are there options for gluten-free products?", "answer": "Yes, we stock a selection of gluten-free products, including bread, pasta, and snacks.",
        "keywords": ["fat", "gluten"]},
    {"question": "What payment methods do you accept?", "answer": "We accept cash, credit cards, debit cards, and mobile payments like Apple Pay and Google Pay.",
        "keywords": ["payment", "pay", "bill"]},
    {"question": "Do you offer a loyalty program?", "answer": "Yes, we have a loyalty program where customers can earn points on purchases and redeem them for discounts or free items.",
        "keywords": ["rewards", "loyalty"]},
    {"question": "Are there dairy-free alternatives like almond milk or coconut yogurt available?", "answer": "Yes, we carry a variety of dairy-free alternatives, including almond milk, coconut yogurt, and soy cheese.",
        "keywords": ["dairy", "milk"]},
]

class RegexChatbot:
    def __init__(self, qa_pairs: List=qa_pairs) -> None:
        self.qa_pairs = qa_pairs 
        self.default_response = "Sorry, I was unable to get that ... "
        for i, item in enumerate(self.qa_pairs):
            self.qa_pairs[i]["pattern"]=self.__generate_pattern(item["keywords"])

    def __generate_pattern(self, keywords: List[str])->re.Pattern:
        return r"\b("+"|".join(keywords)+r")\b"
    
    def answer_qs(self, qs: str)->str:
        for item in self.qa_pairs:
            if re.search(item["pattern"], qs):
                return item["answer"]
        return self.default_response
    
    def run_chatbot(self)->None:
        while(True):
            qs = input("Please ask your question ... ")
            response = self.answer_qs(qs)
            print(response)
            print("-------------------------------------")

if __name__ == "__main__":
    rbc = RegexChatbot(qa_pairs)
    rbc.run_chatbot()