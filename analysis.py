# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question3():
    return 'NOT POSSIBLE'
    '''
    The value of epsillon changes the randomness of the exploration. A low epsillon means that there is a low
    chance of the agent doing a random action. A bigger one means a bigger chance of doing a random action.
    So:
    If the agent runs with a low epsillon, it will be prone to perform the safe action, that will be go back to the 
    initial cell and take the reward.
    If it runs with a bigger epsillon, close to 1, it will be prone to perform a random action at each state, 
    exploring more the gird. 
    The problem with the proposed statement is that with a completely random action there is a chance of 1/1024 
    (1/4 actions ** 5 cells) to reach the final cell. With 50 training runs, it's very hard to get there, and once
    it reach it, the q-value of going back can be higher than the one that we get reaching the final cell.
    We can play with the learning factor:
    An alpha close to 0 will make the agent not learn almost anything, one close to 1 will take only the recent values
    into consideration.
    '''
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
