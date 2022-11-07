import ast

class Vanpham:
    V = []
    T = []
    S = ''
    P = {}
    def taoVanPham(self, data):
        # set V
        self.P = data
        self.V = list(self.P.keys())
        # set T
        value = ''
        for i in range(len(self.V)):
            value = value + self.P.get(self.V[i])
        value1 = list(value)
        value2 = list(value.lower())
        for i in range(len(value1)):
            if(value1[i] in value2):
                self.T.append(value1[i])
        try:
            self.T.remove("|")
        except:
            print('', end='')
        s = set(self.T)
        self.T = list(s)
        self.T.sort()
        # Set S
        self.S = self.V[0]

    def inVanPham(self):
        print("G={" + str(self.V), ","+ str(self.T)+",'"+str(self.S)+"',P}")
        print("     P: " + str(self.P))

    def layListValue(self, key):
        listValue = []
        listValue = (self.P.get(key)).split('|')
        return listValue

    def ktTuyenTinhTrai(self):
        result = True
        print("Kiem tra tuyen tinh trai", end='')
        for i in range(len(self.V)+1):
            listValues = self.layListValue(self.V[i])
            print("\n -Kiem tra luat sinh", self.V[i], "->", listValues, end='')
            for j in range(len(listValues)):
                str1 = ''; str2 = ''; str3 = ''
                lv1 = list(listValues[j])
                lv2 = list((listValues[j]).upper())
                lv3 = list((listValues[j]).lower())
                print("\n   +Luat sinh: ", self.S+"->"+listValues[j])
                if (lv1[0] == lv2[0]):
                    str2 = lv1[0]
                if(str2 != ''):
                    print("   +Bien:", str2)
                else:
                    print("   +Bien: none")
                lv1.reverse()
                lv3.reverse()
                for k in range(len(lv1)):
                    if (lv1[k] == lv3[k]):
                        str3 = lv1[k] + str3
                print("   +Ky hieu ket thuc:", str3)
                str1 = str2 + str3
                print("   +Chuoi kiem tra: ", str1)
                if (str1 != listValues[j]):
                    result = False
                    print("   ->Luat sinh khong thoa tuyen tinh trai!")
                    break
            if (result == False):
                break
        return result

    def ktTuyenTinhPhai(self):
        result = True
        print("Kiem tra tuyen tinh phai", end='')
        for i in range(len(self.V)):
            listValues = self.layListValue(self.V[i])
            print("\n -Kiem tra luat sinh", self.V[i], "->", listValues, end='')
            for j in range(len(listValues)):
                str1 = '';str2 = '';str3 = ''
                lv1 = list(listValues[j])
                lv2 = list((listValues[j]).upper())
                lv3 = list((listValues[j]).lower())
                print("\n   +Luat sinh: ", self.S+"->"+listValues[j])
                if (lv1[-1] == lv2[-1]):
                    str2 = lv1[-1]
                if (str2 != ''):
                    print("   +Bien:", str2)
                else:
                    print("   +Bien: none")
                for k in range(len(lv1)):
                    if (lv1[k] == lv3[k]):
                        str3 = str3 + lv1[k]
                print("   +Ky hieu ket thuc:", str3)
                str1 = str3+str2
                print("   +Chuoi kiem tra: ", str1)
                if (str1 != listValues[j]):
                    result = False
                    print("   ->Luat sinh khong thoa tuyen tinh phai!")
                    break
            if (result == False):
                break
        return result

    def ktVanPhamChinhQuy(self):
        r1 = self.ktTuyenTinhTrai()
        r2 = self.ktTuyenTinhPhai()
        result = ''
        print("\nKET LUAN:")
        if(r1 or r2):
            print("Van pham da cho la van pham chinh quy theo dang:", end='')
            if(r1 == True):
                print("tuyen tinh trai\n")
            if(r2 == True):
                print("tuyen tinh phai\n")
            result = 'YES'
        else:
            print("Van pham da cho KHONG la van pham chinh quy\n")
            result = 'NO'
        return result

def main():
    vp = Vanpham()
    data = {}
    f = open('data.txt', 'r', encoding='UTF-8')
    numLine = f.readline()
    result = []
    for i in range(int(numLine)):
        print("==== VAN PHAM %d ===="%i)
        data = f.readline()
        data = ast.literal_eval(data)
        vp.taoVanPham(data)
        vp.inVanPham()
        tmp = vp.ktVanPhamChinhQuy()
        result.append(tmp)
    for i in range(int(numLine)):
        print("----------------")
        print("VAN PHAM %d: "%i, result[i])
    f.close()

if __name__ == "__main__":
    main()