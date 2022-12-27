class vector:
    def __init__(self):
        self.X=int
        self.Y=int
        self.Z=int
    def sum(self,vect1,vect2):
        vect3=vector()
        vect3.X=vect1.X+vect2.X
        vect3.Y=vect1.Y+vect2.Y
        vect3.Z=vect1.Z+vect2.Z
        return vect3.X,vect3.Y,vect3.Z
    def sc_multiply(self,vect1,vect2):
        scalar=vect1.X*vect2.X+vect1.Y*vect2.Y+vect1.Z*vect2.Z
        return scalar
    def multiply(self,vect1):
        a=int(input('Введите число: '))
        vect3=vector()
        vect3.X=vect1.X*a
        vect3.Y=vect1.Y*a
        vect3.Z=vect1.Z*a
        return vect3.X,vect3.Y,vect3.Z
    def substraction(self,vect1,vect2):
        vect3=vector()
        vect3.X=vect1.X-vect2.X
        vect3.Y=vect1.Y-vect2.Y
        vect3.Z=vect1.Z-vect2.Z
        return vect3.X,vect3.Y,vect3.Z
def main():
    global vect1,vect2
    vect3=vector()
    vect1=vector()
    print('Введите координаты первого вектора (X,Y,Z): ')
    vect1.X=int(input())
    vect1.Y=int(input())
    vect1.Z=int(input())
    answer=int(input(('Выберите операцию: \n1 - сложение,\n2 - скалярное умножение,\n3 - умножение на скаляр,\n4 - вычитание\n')))
    while answer !=1 and answer !=2 and answer !=3 and answer !=4:
        answer=int(input('Введите цифру, соответствующую операции: '))
    else:
        if answer==3:
            print('Координаты результирующего вектора: ',vect3.multiply(vect1))
        else:
            vect2=vector()
            print('Введите координаты второго вектора (X,Y,Z): ')
            vect2.X=int(input())
            vect2.Y=int(input())
            vect2.Z=int(input())
        if answer==1:
            print('Координаты результирующего вектора: ',vect3.sum(vect1,vect2))
        elif answer==2:
            print('Скалярное произведение: ',vect3.sc_multiply(vect1,vect2))
        elif answer==4:
            print('Координаты результирующего вектора: ', vect3.substraction(vect1,vect2))
main()



