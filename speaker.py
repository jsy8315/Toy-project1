import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound #라이브러리 불러오기

# 음성 인식 (듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[수영코딩]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패') #음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e)) #API Key 오류, 네트워크 단절 등의 오류

# 대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text: #만약 '안녕'이라는 단어가 input_text안에 포함이 되어있다면
        answer_text = '안녕하세용 반갑습니다.' 
    elif '날씨' in input_text:
        answer_text = '오늘의 철산 기온은 22도입니다. 맑은 하늘과 강한 바람이 예상됩니다.'
    elif '환율' in input_text:
        answer_text = '원 달러 환율은 1410원입니다.'
    elif '고마워' in input_text:
        answer_text = '볼일 다 봤으면 꺼져.'
    elif '종료' in input_text:
        answer_text = '멀리 안나간다'
        stop_listening(wait_for_stop=False) #더이상 듣지 않음
    else:
        answer_text = '다시 한번 말씀해주시겠어요?'
    speak(answer_text) #answer_text 내용을 읽어줌

# 소리내어 읽기 (TTS)
def speak(text):
    print('[인공지능]' +  text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): #voice.mp3 파일 삭제
        os.remove(file_name)


r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?') #프로그램을 실행시키면 일단 말하기
#사람처럼 귀를 계속 열어두고 있음
stop_listening = r.listen_in_background(m, listen) #계속 열어두다가 m이 들어오면(마이크를 통해 소리가 들리면) listen 함수를 불러옴
# stop_listening(wait_for_Stop=False) #더이상 듣지 않을때 호출하면 멈춤

while True: #프로그램 계속 돌리기
    time.sleep(0.1)
