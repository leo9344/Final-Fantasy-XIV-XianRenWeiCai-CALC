import numpy as np
from itertools import permutations

class Calculator():
    def __init__(self):
        self._results = np.zeros(8,dtype='uint64')
        self._weight = [10000,36,720,360,80,252,108,72,54,180,72,180,119,36,306,1080,144,1800,3600]
        self.elem = [1,2,3,4,5,6,7,8,9]

    def cal(self,_map=np.zeros((3,3),dtype='uint8')):
        '''
        @param: _map is a 3*3 uint8 numpy array which contains 0.
        '''
        self._results = np.zeros(8,dtype='uint64') # init
        self.elem = [1,2,3,4,5,6,7,8,9] # init

        tmp_map = _map.copy()
        for i in range(3):
            for j in range(3):
                if tmp_map[i,j] != 0:
                    self.elem.remove(tmp_map[i,j])
        print("self.elem")
        print(self.elem)



        perm = permutations(self.elem)
        for it in perm:
            tmp_map = _map.copy()
            it_i = 0
            for i in range(0,3):
                for j in range(0,3):
                    if tmp_map[i,j] == 0:
                        tmp_map[i,j] = it[it_i]
                        it_i += 1
            print("tmp_map")
            print(tmp_map)
            self._results += self.cal_once(tmp_map)
            
        return self._results
    def cal_once(self,_map=np.zeros((3,3),dtype='uint8')):
        '''
        @param: _map is a 3*3 uint8 numpy array which cannot contain 0.
        '''
        row1 = self._weight[(_map[0,0] + _map[0,1] + _map[0,2] -6)]
        row2 = self._weight[(_map[1,0] + _map[1,1] + _map[1,2] -6)]
        row3 = self._weight[(_map[2,0] + _map[2,1] + _map[2,2] -6)]
        col1 = self._weight[(_map[0,0] + _map[1,0] + _map[2,0] -6)]
        col2 = self._weight[(_map[0,1] + _map[1,1] + _map[2,1] -6)]
        col3 = self._weight[(_map[0,2] + _map[1,2] + _map[2,2] -6)]
        diag1 = self._weight[(_map[0,0] + _map[1,1] + _map[2,2] -6)]
        diag2 = self._weight[(_map[0,2] + _map[1,1] + _map[2,0] -6)]

        tmp_result = np.array([row1,row2,row3,col1,col2,col3,diag1,diag2],dtype='uint64')
        print("tmp_result")
        print(tmp_result) 

        return tmp_result
