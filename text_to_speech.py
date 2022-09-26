# TTS (Text To Speech)
# STT (Speech To Text)

from gtts import gTTS
from playsound import playsound
file_name = 'sample.mp3'

#영어 문장
# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
# #영어로 인식한 결과를 text로 받아옴
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# #mp3 파일 여는 것 귀찮으니까 바로 mp3파일재생해버리기
# from playsound import playsound
# playsound(file_name)


# #한글 문장
# text = '배소리는 흐엉흐엉, 개지섭은 아르릉아르릉'
# tts_ko = gTTS(text = text, lang='ko')
# tts_ko.save(file_name)

# #mp3 파일 여는 것 귀찮으니까 바로 mp3파일재생해버리기
# playsound(file_name)

# 긴 문장 (파일에서 불러와서 처리)
with open('sample.txt', 'r', encoding='utf8') as f: #sample.txt를 열어서
    text = f.read() #파일에 있는 모든 내용을 text로 저장

tts_ko = gTTS(text = text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)





