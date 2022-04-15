num_to_word = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
              '6':'six', '7':'seven', '8':'eight', '9':'nine'}
word_to_num = dict(map(reversed, num_to_word.items()))

def solution(s):
    answer = ''
    word = ''
    for i in s:
        if i in num_to_word.keys():
            answer = answer + i
        else:
            word = word + i
            if word in word_to_num.keys():
                answer = answer + word_to_num[word]
                word = ''
    return answer

print(solution("one4seveneight"))