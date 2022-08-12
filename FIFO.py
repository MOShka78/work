import time
import collections
#Ver. 1.0

class Fifo:
    def __init__(self, maxSize):  
        self.put = 0       # Указатель на последнее значение
        self.maxSize = maxSize      # Максимальное количество переменных в очереди
        self.data = [None] * maxSize   # Очередь
        self.out = 0 #  указатель на первое значение 

    def write(self, object):        # Записываем значение в буфер, если в ячейке было первое значение оно заменится
        if self.put < self.maxSize:
            if self.data[self.put] != 0:
                self.data[self.put] = object
                self.put += 1
        else: 
            self.put = 0
            self.data[self.put] = object
    
    def delat(self):           # Первое значение в очереди обнуляется
        self.out = abs(self.put - self.maxSize)
        while self.data[self.out] == None:
            print(self.out)
            if self.out < self.maxSize-1:
                self.out += 1
            else: self.out = 0

        self.data[self.out] = None

test_Fifo = Fifo(100)
i = 0
start_time = time.time()
while(i<10000):
    test_Fifo.write(i+1)
    i+=1
print("--- %s seconds Ver. 1 ---" % (time.time() - start_time))
# 1 Вариант выполнения циклического буфера FIFO представлено в классе Fifo. 
# Плюс данной реализации вижу в том, что не используются никакие дополнительные модули


#Ver. 2.0
class FIFO_DEQUE(object):

    def __init__(self, buffer_size):
        self.content = None
        self.size = buffer_size

    def write(self, scalar):
        try:
            self.content.append(scalar)
        except AttributeError:
            self.content = collections.deque([0.] * self.size, maxlen=self.size)

test_Deque = FIFO_DEQUE(100)
i = 0
start_time = time.time()
while(i<10000):
    test_Deque.write(i+1)
    i+=1
print("--- %s seconds Ver. 2 ---" % (time.time() - start_time))

# Почитав документацию deque понял, что он будет хорошим конструктором для создания буфера FIFO


# Ver. 3.0
class Fifo_2(object):

    def __init__(self, buffer_size):
        self.content = None
        self.size = buffer_size

    def write(self, scalar):
        try:
            self.content.append(scalar)
            self.content.pop(0)
        except AttributeError:
            self.content = [0.] * self.size


test_3 = Fifo_2(100)
i = 0
start_time = time.time()
while(i<10000):
    test_Deque.write(i+1)
    i+=1
print("--- %s seconds Ver. 3 ---" % (time.time() - start_time))

#Реализация на основе методов списков

#Вывод по поводу быстродействия: Самая быстра Ver. 3. Самая медленная Ver. 2
