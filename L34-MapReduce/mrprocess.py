from mrjob.job import MRJob

class MRProcess(MRJob):
    
    def mapper(self, _, numero):
        n = int(numero)
        if (n%2):
            yield 'DISPARI', n
        else:
            yield 'PARI', n
        
    def reducer(self, chiave, valore):
        yield chiave, sum(valore)
    
if __name__ == '__main__':
    MRProcess.run()