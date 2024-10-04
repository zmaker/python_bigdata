from mrjob.job import MRJob

class MRProcess(MRJob):
    
    def mapper(self, _, line):
        line = line.upper()
        for ch in line:
            if ch.isalpha():
                yield ch, 1
        
    def reducer(self, chiave, valore):
        yield chiave, sum(valore)

    
if __name__ == '__main__':
    MRProcess.run()
