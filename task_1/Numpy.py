
class Array:
    def __init__(self, data):
        if isinstance(data, list):
            if all(isinstance(row, list) for row in data):
                # 2D array
                self.data = data
                
            elif all(isinstance(item, (int, float)) for item in data):
                # 1D array
                self.data = data
                
            else:
                raise TypeError("Les données entrées doivent être une liste de nombre")
        else:
            raise TypeError("Les données entrées doivent être une liste")

    #def __repr__(self):
        #return f"Array({self.data})"

    def __str__(self):
        return str(self.data)

    @property
    def shape(self):
        if len(self.data) == 0:
            return (0,)
        elif isinstance(self.data[0], list):
            return (len(self.data), len(self.data[0]))
        else:
            return (len(self.data),)

    def __len__(self):
        return len(self.data)        

    def __getitem__(self, key):
        if isinstance(key, tuple):
            i, j = key
            return self.data[i][j]
        else:
            return self.data[key]

    def __contenir__(self, item):
        for row in self.data:
            if item in row:
                return True
        return False

    def _get_dimensions(self):
        if isinstance(self.data[0], list):
            return 2
        else:
            return 1

    def _valider_dimensions(self, other):
        if isinstance(other, Array):
            if self._get_dimensions() != other._get_dimensions():
                raise ValueError("Ne peux pas opérer sur des arrays de dimensions différentes.")
            if self._get_dimensions() == 1:
                if len(self.data) != len(other.data):
                    raise ValueError("Les dimensions ne correspondent pas")
            elif self._get_dimensions()== 2:
                if len(self.data) != len(other.data) or any(len(row) != len(other.data[i]) for i, row in enumerate(self.data)):
                
                    raise ValueError("Les dimensions ne correspondent pas")
        elif isinstance(other, (int, float)):
            pass
        else:
            raise ValueError("Ne prend pas en charge ce typr d'opération avec Array")
    

    def _apply_operation(self, other, operation):
        
        self._valider_dimensions(other)
        if isinstance(other, Array):
            if self._get_dimensions()== 1:
                return Array([operation(x,y) for x, y in zip(self.data, other.data)])
            elif self._get_dimensions()== 2:
                return Array([[operation(x,y) for  x, y in zip(row_self, row_other)] for row_self, row_other in zip(self.data, other.data)])
        elif isinstance(other, (int, float)):
            if self._get_dimensions() == 1:
                return Array([operation(x, other) for x in self.data])
            elif self._get_dimensions() == 2:
                return Array([[operation(x, other) for x in row] for row in self.data])

    def __add__(self, other):
        return self._apply_operation(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self._apply_operation(other, lambda x, y: x - y)

    def __mul__(self, other):
        return self._apply_operation(other, lambda x, y: x * y)

    def __truediv__(self, other):
        return self._apply_operation(other, lambda x, y: x / y)
    
        
    def __matmul__(self, other):
        if not isinstance(other, Array):
            raise TypeError("Unsupported operand type(s) for @: '{type(self)}' and '{type(other)}'")
        if self.shape != other.shape:
            raise ValueError("Les dimensions ne correspondent pas")
        if len(self.shape) != 1 or self.shape[0] != len(other.data):
            raise ValueError("Matrix multiplication (@) is only supported between 1D arrays of the same shape")

        result = sum(self.data[i] * other.data[i] for i in range(len(self.data)))
        return result
    
     
    def __getitem__(self, key):
        if isinstance(key, tuple):
            row, col= key
            return self.data[row][col]
        else:
            return self.data[key]
                
            
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            row, col= key
            self.data[row][col]= value

        else:
            self.data[key]= value
            
                

    def __iter__(self):
        return iter(self.data)



