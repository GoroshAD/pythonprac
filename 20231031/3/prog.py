import sys
from copy import deepcopy

class Maze :
    def __init__(self, N) :
        #self.ways_arr = []
        '''self.maze = [[chr(9608)] * (N * 2  + 1) for i in range(2 * N + 1)]
        for i in range(1, 2 * N + 1, 2) :
            for j in range(1, 2 * N + 1, 2) :
                self.maze[i][j] = '\u2027'''
        self.size = N
        self.maze = set([])
        pass

    def __str__(self) :
        '''tmp = []
        for i in range(len(self.maze)) :
            tmp.append("".join(self.maze[i]))
        return "\n".join(tmp)'''
        s = ["" for i in range(self.size * 2 + 1)]
        for i in range(self.size * 2 + 1) :
            s[i] = []
            for j in range(self.size * 2 + 1) :
                if i * j == 0 or i == self.size * 2 or j == self.size * 2 :
                    s[i].append(chr(9608))
                elif (i, j) in self.maze or all((i % 2 == 1, j % 2 == 1)):
                    s[i].append('\u00B7')
                else :
                    s[i].append(chr(9608))
            s[i] = "".join(s[i])
        return "\n".join(s)

    
    '''def rec_set(self, prev, tmp, fin, tmp_way) :
        if tmp == fin :
            self.ways_arr.append(deepcopy(tmp_way))
            return
        if (tmp[0] + 2, tmp[1]) != prev and (self.maze[tmp[1]][tmp[0] + 1] == chr(183)) :
            tmp_tmp_way = deepcopy(tmp_way)
            tmp_tmp_way.append((tmp[0] + 1, tmp[1]))
            self.rec_set(tmp, (tmp[0] + 2, tmp[1]), fin, deepcopy(tmp_tmp_way))
        if (tmp[0], tmp[1] + 2) != prev and (self.maze[tmp[1] + 1][tmp[0]] == chr(183)) :
            tmp_tmp_way = deepcopy(tmp_way)
            tmp_tmp_way.append((tmp[0], tmp[1] + 1))
            self.rec_set(tmp, (tmp[0], tmp[1] + 2), fin, deepcopy(tmp_tmp_way))
        if (tmp[0] - 2, tmp[1]) != prev and (self.maze[tmp[1]][tmp[0] - 1] == chr(183)) :
            tmp_tmp_way = deepcopy(tmp_way)
            tmp_tmp_way.append((tmp[0] - 1, tmp[1]))
            self.rec_set(tmp, (tmp[0] - 2, tmp[1]), fin, deepcopy(tmp_tmp_way))
        if (tmp[0], tmp[1] - 2) != prev and (self.maze[tmp[1] - 1][tmp[0]] == chr(183)) :
            tmp_tmp_way = deepcopy(tmp_way)
            tmp_tmp_way.append((tmp[0], tmp[1] - 1))
            self.rec_set(tmp, (tmp[0], tmp[1] - 2), fin, deepcopy(tmp_tmp_way))'''

    def __setitem__(self, index, value) :
        y1, x2, useless = index[1].indices(sys.maxsize)
        #if value != chr(9608) :
        fir, sec = (index[0], y1), (x2, index[2])
        if fir[1] == sec[1] :
            for i in range(min(fir[0], sec[0]), max(fir[0], sec[0])) :
                if value == chr(9608) :
                    if (fir[1] * 2 + 1, i * 2 + 2) in self.maze :
                        self.maze.remove((fir[1] * 2 + 1, i * 2 + 2))
                else :
                    self.maze.add((fir[1] * 2 + 1, i * 2 + 2))
                #self.maze[fir[1] * 2 + 1][i * 2 + 2] = value
        elif fir[0] == sec[0] :
            for i in range(min(fir[1], sec[1]), max(fir[1], sec[1])) :
                if value == chr(9608) :
                    if ( i * 2 + 2, fir[0] * 2 + 1) in self.maze :
                        self.maze.remove(( i * 2 + 2, fir[0] * 2 + 1))
                else :
                    self.maze.add(( i * 2 + 2, fir[0] * 2 + 1))
                #self.maze[i * 2 + 2][fir[0] * 2 + 1] = value
        else :
            pass
        '''else :
            fir, sec = (index[0] * 2 + 1, y1 * 2 + 1), (x2 * 2 + 1, index[2] * 2 + 1)
            self.rec_set(None, fir, sec, [])
            for i in self.ways_arr :
                for j in i :
                    self.maze[j[1]][j[0]] = chr(9608)
            self.ways_arr = []'''   #this is if we want to close all the paths from the point to point
    
    '''def rec_get(self, prev, tmp, fin) :
        prev.add(tmp)
        if tmp == fin :
            return True
        if (not (tmp[0] + 2, tmp[1]) in prev) and (self.maze[tmp[1]][tmp[0] + 1] == "\u2027") :
            if self.rec_get(prev, (tmp[0] + 2, tmp[1]), fin) :
                return True
        if (not (tmp[0], tmp[1] + 2) in prev) and (self.maze[tmp[1] + 1][tmp[0]] == '\u2027') :
            if self.rec_get(prev, (tmp[0], tmp[1] + 2), fin) :
                return True
        if (not (tmp[0] - 2, tmp[1]) in prev) and (self.maze[tmp[1]][tmp[0] - 1] == '\u2027') :
            if self.rec_get(prev, (tmp[0] - 2, tmp[1]), fin) :
                return True
        if (not (tmp[0], tmp[1] - 2) in prev) and (self.maze[tmp[1] - 1][tmp[0]] == '\u2027') :
            if self.rec_get(prev, (tmp[0], tmp[1] - 2), fin) :
                return True
        return False'''
    
    def rec_get(self, prev, fir, fin) :
        prev.add(fir)
        rest = set([fir])
        if fir == fin :
            return True
        
        while rest :
            new_rest = set([])
            for tmp in rest :
                if tmp == fin :
                    return True
                if (not (tmp[0] + 2, tmp[1]) in prev) and ((tmp[1], tmp[0] + 1) in self.maze) : #== "\u2027") :
                    new_rest.add((tmp[0] + 2, tmp[1]))
                if (not (tmp[0], tmp[1] + 2) in prev) and ((tmp[1] + 1, tmp[0]) in self.maze) : # == '\u2027') :
                    new_rest.add((tmp[0], tmp[1] + 2))
                if (not (tmp[0] - 2, tmp[1]) in prev) and ((tmp[1], tmp[0] - 1) in self.maze) : # == '\u2027') :
                    new_rest.add((tmp[0] - 2, tmp[1]))
                if (not (tmp[0], tmp[1] - 2) in prev) and ((tmp[1] - 1, tmp[0]) in self.maze) : # == '\u2027') :
                    new_rest.add((tmp[0], tmp[1] - 2))
                prev.add(tmp)
            rest = deepcopy(new_rest)
        return False

    def __getitem__(self, index) :
        y1, x2, useless = index[1].indices(sys.maxsize)
        fir, sec = (index[0] * 2 + 1, y1 * 2 + 1), (x2 * 2 + 1, index[2] * 2 + 1)
        return self.rec_get(set([]), fir, sec)

exec(sys.stdin.read())
