import speech_recognition as sr

# 마이크로부터 음성 듣기
r = sr.Recognizer() #객체 만들기
with sr.Microphone() as source: #마이크가 되자
    print('듣고 있으니까 더 말하지 마셈')
    audio = r.listen(source) #마이크로부터 음성 듣기 구글 서버를 통해서 실행

# # 파일로부터 음성 불러오기 (파일 확장자가 한정되어 있음. wav, aiff 가능, mp3는 불가)
# r = sr.Recognizer()
# with sr.AudioFile('sample.wav') as source:
#    audio = r.record(source)
    

try:
    # # 구글 API로 인식(하루 50회 한정)
    # 영어 문장으로 시행
    # text = r.recognize_google(audio, language='en-US')
    # print(text)

    #한국어도 함 해보자
    text = r.recognize_google(audio, language='ko')
    print(text)

except sr.UnknownValueError: #휘파람이나 기타 소리로 음성 인식이 실패하는 경우
    print('인식 실패') #음성 인식이 실패한 경우
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) # API Key 오류, 또는 네트워크 단절 등
