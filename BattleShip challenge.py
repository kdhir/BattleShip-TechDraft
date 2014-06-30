import urllib2
import json
from pprint import pprint

rows = ['A','B','C','D','E','F','G','H','I','J']
cols = ['1','2','3','4','5','6','7','8','9','10']
def singleBoard(board):
    url = 'https://student.people.co/api/challenge/battleship/e53f110c8332/boards/'+board
    response = urllib2.urlopen(url).read()
    print(response)

def boardCollection():
    url = 'https://student.people.co/api/challenge/battleship/e53f110c8332/boards'
    response = urllib2.urlopen(url).read()
    print(response)

def singleShot(board,location):
    url = 'https://student.people.co/api/challenge/battleship/e53f110c8332/boards/'+board+'/'+location
    response = urllib2.urlopen(url).read()
    return(response)

def killShip(r,c):
    #first check down (col+1)
    rTemp = r
    cTemp = c+1
    loc= rows[r]+cols[cTemp]
    res = json.loads(singleShot('live_board_1',loc))
    #if it is a hit, continue going down
    if (str(res['is_hit']) == 'True'):
         while((str(res['is_hit']) == 'False' )|| (cTemp > 9)):
            cTemp+=1
            loc= rows[r]+cols[cTemp]
            res = json.loads(singleShot('live_board_1',loc))
         if ( c > 0)
             loc= rows[r]+cols[c - 1]
             res = json.loads(singleShot('live_board_1',loc))                          
         else
             return
    #otherwise go right
         
#singleBoard('test_board_1');
#singleShot('test_board_1','A1')
def randomShots():
    for r in range(0,9):
        for c in range(0,9):
            loc= rows[r]+cols[c]
            res = json.loads(singleShot('live_board_1',loc))
            if (str(res['is_hit']) == 'True'):
                print(res['location'])
                
            
#singleBoard('test_board_1')
#res = json.loads(singleBoard('test_board_1'))
#while (str(res['is_finished']) == 'False'):
randomShots()
