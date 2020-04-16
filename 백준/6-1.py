# 완주하지 못한 선수

import collections


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


# for in zip 함수는 보통 여러 List를 slice할때 사용
# 즉 두개의 인덱스 동시에 반복되어야 할 때 사용

###


# def solution(participant, completion):
#    answer = collections.Counter(participant) - collections.Counter(completion)
#    return list(answer.keys())[0]
###

# collections 모듈 => Counter : hash가능한 객체를 카운트하는 dict
