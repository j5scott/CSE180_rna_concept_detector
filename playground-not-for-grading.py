
class sex:
    gender = ''
    def __init__(self,gender):
        gender = self.gender

m1 = sex('man')
m2 = sex('man')

print id(m1) #57079248
print id(m2) #57079328
