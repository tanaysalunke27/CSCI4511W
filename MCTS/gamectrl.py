# -*- coding: utf-8 -*-
import json
import math
import re
import socket
import time

class BrowserRemoteControl(object):
    ''' Interact with a web browser running the Remote Control extension. '''
    def __init__(self, port):
        self.sock = socket.socket()
        self.sock.connect(('localhost', port))

    def execute(self, cmd):
        msg = cmd.replace('\n', ' ') + '\r\n'
        self.sock.send(msg.encode('utf8'))
        ret = []
        while True:
            chunk = self.sock.recv(4096)
            ret.append(chunk)
            if b'\n' in chunk:
                break
        res = json.loads(b''.join(ret).decode('utf8'))
        if 'error' in res:
            raise Exception(res['error'])
        elif not res:
            return None
        else:
            return res['result']

class Generic2048Control(object):
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.setup()

    def setup():
        raise NotImplementedError()

    def execute(self, cmd):
        return self.ctrl.execute(cmd)

    def get_status(self):
        ''' Check if the game is in an unusual state. '''
        return self.execute('''
            var messageContainer = document.querySelector(".game-message");
            if(messageContainer.className.search(/game-over/) !== -1) {"ended"}
            else if(messageContainer.className.search(/game-won/) !== -1) {"won"}
            else {"running"}
            ''')

    def restart_game(self):
        self.send_key_event('keydown', 82)
        time.sleep(0.1)
        self.send_key_event('keyup', 82)

        self.send_key_event('keydown', 32)
        time.sleep(0.1)
        self.send_key_event('keyup', 32)

    def continue_game(self):
        ''' Continue the game. Only works if the game is in the 'won' state. '''
        self.execute('document.querySelector(".keep-playing-button").click();')

    def send_key_event(self, action, key):
        return self.execute('''
            var keyboardEvent = document.createEvent("KeyboardEvent");
            var initMethod = typeof keyboardEvent.initKeyboardEvent !== 'undefined' ? "initKeyboardEvent" : "initKeyEvent";
            keyboardEvent[initMethod]("%s", true, true, window, false, false, false, false, %d, 0);
            (document.body || document).dispatchEvent(keyboardEvent);
            ''' % (action, key))

class Fast2048Control(Generic2048Control):
    ''' Control 2048 by hooking the GameManager and executing its move() function.

    This is both safer and faster than the keyboard approach, but it is more hackish. '''

    def setup(self):
        # Obtain the GameManager instance by triggering a fake restart.
        self.ctrl.execute(
            '''
            var _func_tmp = GameManager.prototype.isGameTerminated;
            GameManager.prototype.isGameTerminated = function() {
                GameManager._instance = this;
                return true;
            };
            ''')

        # Send an "up" event, which will trigger our replaced isGameTerminated function
        self.send_key_event('keydown', 38)
        time.sleep(0.1)
        self.send_key_event('keyup', 38)

        self.execute('GameManager.prototype.isGameTerminated = _func_tmp;')

    def get_score(self):
        return self.execute('GameManager._instance.score')

    def get_board(self):
        grid = self.execute('GameManager._instance.grid')

        board = [[0]*4 for _ in range(4)]
        for row in grid['cells']:
            for cell in row:
                if cell is None:
                    continue
                pos = cell['x'], cell['y']
                tval = cell['value']
                board[pos[1]][pos[0]] = int(round(math.log(tval, 2)))

        return board

    def execute_move(self, move):
        # We use UDLR ordering; 2048 uses URDL ordering
        move = [0, 2, 3, 1][move]
        self.execute('GameManager._instance.move(%d)' % move)

class Keyboard2048Control(Generic2048Control):
    ''' Control 2048 by accessing the DOM and using key events.
    
    This is relatively slow, and may be prone to race conditions if your
    browser is slow. However, it is more generally compatible with various
    clones of 2048. '''

    def setup(self):
        self.execute(
            '''
            var elems = document.getElementsByTagName('div');
            for(var i in elems)
                if(elems[i].className == 'tile-container') {
                    tileContainer = elems[i];
                    break;
                }
            ''')

    def get_score(self):
        score = self.execute('''
            var scoreContainer = document.querySelector(".score-container");
            var scoreText = '';
            var scoreChildren = scoreContainer.childNodes;
            for(var i = 0; i < scoreChildren.length; ++i) {
                if(scoreChildren[i].nodeType == Node.TEXT_NODE) {
                    scoreText += scoreChildren[i].textContent;
                }
            }
            scoreText;
            ''')

        return int(score)

    def get_board(self):
        res = self.execute(
            '''
            var res = [];
            var tiles = tileContainer.children;
            for(var i=0; i<tiles.length; i++)
                res.push(tiles[i].className);
            res
            ''')
        board = [[0]*4 for _ in range(4)]
        for tile in res:
            tval = pos = None
            for k in tile.split():
                m = re.match(r'^tile-(\d+)$', k)
                if m:
                    tval = int(m.group(1))
                m = re.match(r'^tile-position-(\d+)-(\d+)$', k)
                if m:
                    pos = int(m.group(1)), int(m.group(2))
            board[pos[1]-1][pos[0]-1] = int(round(math.log(tval, 2)))

        return board

    def execute_move(self, move):
        key = [38, 40, 37, 39][move]
        self.send_key_event('keydown', key)
        time.sleep(0.01)
        self.send_key_event('keyup', key)
        time.sleep(0.05)
