
def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:]) 
    return words


def evaluate(text, segs):

    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words)))) 
    return text_size + lexicon_size

from random import randint

def flip(segs, pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n): 
    for i in range(n):
        segs = flip(segs, randint(0,len(segs)-1)) 
    return segs

def anneal(text, segs, iterations, rate): 
    temperature = float(len(segs))
    while temperature > 0.1:
        best_segs, best = segs, evaluate(text, segs) 
        
        for i in range(iterations):
            guess = flip_n(segs, int(round(temperature))) 
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess 
            
        score, segs = best, best_segs
        temperature = temperature / rate
        print evaluate(text, segs), segment(text, segs)
    return score, segs
    
text = "dienthoaiiphonex256gbhangnhapkhaudienthoaiiphone8plus64gbhangchinhhangfptdienthoaihtc10hangchinhhang"
# Strategy 1
seg1 = "0000000000000000000000000000000010000000000000000000000000000000000000001000000000000000000000000001"
score, final_seg = anneal(text, seg1, 10000, 1.1)
# Stategy 2
#seg1 = "0000000010000010000000000000000010000000010000010000000010000000000001001000000001000010000000000001"
#score, final_seg = anneal(text, seg1, 10000, 1.1)
