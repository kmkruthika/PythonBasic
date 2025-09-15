qa=[
  {
    "question":"What is the capital of Karnataka?",
    "answer":"BENGALURU"
  },
  {
    "question":"What is CPU",
    "answer":"CENTRAL PROCESSING UNIT"
  }
]
score=0
for q in qa:
  print(q["question"])
  
  ans=input("Enter the answer").upper()

  if ans==q["answer"]:
    print("Correct answer")
    score+=1
  else:
    print("the answer was:",q["answer"])
    
print("Quiz completed")
print(f"Total score is {score}/{len(qa)}")


if score==len(qa):
  print("perfect answers all correct")
elif score>0:
  print("Good Job!")
else:
  print("Keep practicing")