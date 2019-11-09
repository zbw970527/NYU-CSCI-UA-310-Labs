# tabletools.py
# BOWEN ZHANG
# bz896

import tabletools as tt

class LabeledList:
    def __init__(self, data = None, index = None):
        self.values = data
        if index != None:
            self.index = index
        else:
            self.index = range(len(data))
            
    def __str__(self):
        vals_max_len = 0
        idx_max_len = 0
        result = ""
        for i,j in zip(self.values, self.index):
            vals_max_len = max(vals_max_len, len(str(i)))
            idx_max_len = max(idx_max_len, len(str(j)))
        vals_max_len += 1
        idx_max_len += 1
        for i,j in zip(self.values, self.index):
            result += (f"{j:>{idx_max_len}} {str(i):<{vals_max_len}}\n")
        return result
        
    def __repr__(self):
       return self.__str__()
    
    def __getitem__(self, key_list):
        val = []
        key = []
        #input is a ll list
        if isinstance(key_list, LabeledList):
            for i,j in zip(self.values, self.index):
                if j in key_list.values:
                   val.append(i)
                   key.append(j) 
            return tt.LabeledList(val, key)
        #input is a list of string
        if isinstance(key_list, list):
            if(isinstance(key_list[0], str)):
                for i,j in zip(self.values, self.index):
                    if j in key_list:
                        val.append(i)
                        key.append(j)
                if(len(val) == 1):
                    return val[0]
                else:
                    return tt.LabeledList(val, key)
            if(isinstance(key_list[0], bool)):# input is a list of boolean
                for i,j,k in zip(self.values, self.index, key_list):
                    if k == True:
                        val.append(i)
                        key.append(j)
                return tt.LabeledList(val, key)
        if isinstance(key_list, str):
            for i,j in zip(self.values, self.index):
                if j in key_list:
                    val.append(i)
                    key.append(j)
            if(len(val) == 1):
                return val[0]
            else:
                return tt.LabeledList(val, key)

    def __setitem__(self, key, value):
        for index, k in enumerate(self.index):
            if(k == key):
                self.values[index] = value    
                
    def __iter__(self):
         iterator = iter(self.values)
         return iterator
     
    def __eq__(self, scalar):
        val = [True if x == scalar else False for x in self.values]
        return tt.LabeledList(val)
    
    def __ne__(self, scalar):
        val = [True if x != scalar else False for x in self.values]
        return tt.LabeledList(val)
        
    def __gt__(self, scalar):
        val = [True if x > scalar else False for x in self.values]
        return tt.LabeledList(val)
        
    def __lt__(self, scalar):
        val = [True if x < scalar else False for x in self.values]
        return tt.LabeledList(val)
    
    def map(self, f):
        result = []
        result = list(map(f, self.values))
        return tt.LabeledList(result) 
    
    
    
class Table:
    def __init__(self, data, index=None, columns=None):
        self.data = data
        if index == None:
            self.row = range(len(data))
        else:
            self.row = index
        if columns == None:
            self.column = range(len(data[0]))
        else:
            self.column = columns
        
    def __str__(self):
        result = ""
        idx_max_len = 0
        vals_max_len = [0] * len(self.data[0])
        for i in range(len(self.data[0])):# the index of the column
            for j in range(len(self.data)): # the index of the row
                vals_max_len[i] = (max(vals_max_len[i], len(str(self.data[j][i]))))
        for i in self.row: # find largest len in row
            idx_max_len = max(idx_max_len, len(str(i)))
        for i in range(len(self.column)):
            vals_max_len[i] = 1 + (max(vals_max_len[i], len(str(self.column[i]))))
        idx_max_len += 1
        result += (f"{'':>{idx_max_len}}")
        for i in range(len(self.column)):
            result += (f"{self.column[i]:>{vals_max_len[i]}}")
        result += "\n"
        for idx, j in enumerate(self.row):
            result += (f"{j:>{idx_max_len}}")
            for x, val in enumerate(self.data[idx]):
                result += (f"{str(val):>{vals_max_len[x]}}")
            result += "\n"
        return result
            
    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, col_list):
        result = []
        if isinstance(col_list, LabeledList):
            if isinstance(col_list.values[0], bool):
                row = []
                for i,j in enumerate(col_list.values):
                    if j == True:
                        data = []
                        row.append(self.row[i])
                        for k in self.data[i]:
                            data.append(k)
                        result.append(data)
                return Table(result, row, self.column)
            else:
                for i in self.data:
                    row = []
                    for j in col_list:
                        idx = self.column.index(j)
                        row.append(i[idx])
                    result.append(row)    
                return Table(result, self.row, col_list.values)
        if isinstance(col_list, list):
            if(isinstance(col_list[0], str)):
                for i in self.data:
                    row = []
                    for j in col_list:
                        idx = self.column.index(j)
                        row.append(i[idx])
                    result.append(row) 
                return Table(result, self.row, col_list)
            if(isinstance(col_list[0], bool)):
                row = []
                for i,j in enumerate(col_list):
                    if j == True:
                        data = []
                        row.append(self.row[i])
                        for k in self.data[i]:
                            data.append(k)
                        result.append(data)
                return Table(result, row, self.column)
        if isinstance(col_list, str):
            idx = tt.findIdx(self.column, col_list);
            result = []
            if len(idx) > 1:
                for i in range(len(self.data)):
                    result.append([])
                newCol = [col_list] * len(idx)
                for i,j in enumerate(self.data):
                    for val in idx:
                        result[i].append(j[val])
                return Table(result, self.row, newCol)
            if len(idx) == 1:
                for val in self.data:
                    result.append(val[idx[0]])
                return LabeledList(result, self.row)
            
    def __eq__(self, other):
        return self.data == other.data and self.row == other.row and self.column == other.column
    
    def __ne__(self, other):
        return self.data != other.data or self.row != other.row or self.column != other.column
    
    def head(self, n):
        return Table(self.data[:n], self.row[:n], self.column)
            
    def tail(self, n):
        return Table(self.data[-n:], self.row[-n:], self.column)
    
    def shape(self):
        return (len(self.data), len(self.data[0]))
    

def read_csv(fn):
    with open(fn) as f:
        file = f.read()
    file = file.split('\n')
    for i in range(len(file)):
        file[i] = file[i].split(',')
    column = file.pop(0)
    file.pop()
    for i in range(len(file)):
        for j in range(len(file[i])):
            try:
                file[i][j] = file[i][j].strip()
                file[i][j] = float(file[i][j])
            except ValueError:
                pass
    return Table(file, None, column)
        
def findIdx(l, item):
    return [i for i, x in enumerate(l) if x == item];
 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        