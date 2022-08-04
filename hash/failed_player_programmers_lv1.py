def solution(participant, completion):
    if len(participant) == 1:
        return participant[0]
    participant.sort()
    completion.sort()
    while participant:
        x = participant.pop()
        if len(completion) == 0 or x != completion[-1]:
            return x
        else:
            completion.pop()


