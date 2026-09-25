from app.phase1.assistant import answer_question

def main():
    print("CURT Inventory Assistant (Phase 1 - Rule Based)")
    print("Type 'exit' to quit.\n")
    while True:
        question = input("You: ")
        if question.strip().lower() == "exit":
            break
        print("Assistant:", answer_question(question), "\n")

if __name__ == "__main__":
    main()