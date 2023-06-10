import pandas as pd
filepath = 'D:\python\chatbot\ChatbotData.csv'

data = pd.read_csv(filepath) # 경로 지정
questions = data['Q'].tolist()  # 질문열 리스트 저장
answers = data['A'].tolist()   # 답변열 리스트 저장

def calc_distance(a, b): # 레벤슈타인 거리 계산(8~31)
    if a == b: return 0 # 같으면 0을 반환
    a_len = len(a) # a 길이
    b_len = len(b) # b 길이
    if a == "": return b_len #a가 공백일때 b의 길이 반환
    if b == "": return a_len #b가 공백일때 a의 길이 반환
    matrix = [[] for i in range(a_len+1)]
    for i in range(a_len+1):
        matrix[i] = [0 for j in range(b_len+1)]    
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    for i in range(1, a_len+1):
        ac = a[i-1]        
        for j in range(1, b_len+1):
            bc = b[j-1] 
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1,
                matrix[i][j-1] + 1,
                matrix[i-1][j-1] + cost
            ])
    return matrix[a_len][b_len]

input_sentence = input('You: ')
bigbox=[] # 입력값과 파일 1~11824 질문값 비교 리스트 생성
for distance in range(len(questions)):
    bigbox.append(calc_distance(input_sentence,questions[distance-1]))
index = bigbox.index(min(bigbox))-1 # 레벤슈타인 거리가 최소인 값의 인덱스 반환, 인덱스는 0부터 시작하므로 -1

print(answers[index])