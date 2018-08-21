def sum(pos):

    def ds(step):
        new_pos = pos + step
        pos = new_pos
        return new_pos
        
    ds()

r = sum()
print(r)