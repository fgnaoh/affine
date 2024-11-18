# ham phu dinh
def phu(x): 
    if x[0] == '-':
        return x[1:]
    return '-' + x

[ ] # Hàm chuyển về, đưa các mệnh đề phủ sang về còn lại
def chuyenve(dong):
    vetrai = dong[1][:] 
    vephai = dong[2][:]
    for i in vetrai[:]:
        if 'v' not in i: 
            if i[0] == '-': 
                vetrai.remove(i) 
                vephai.append(phu(i))
    for i in vephai[:]:
        if '^' not in i:
            if i[0] == '-':
                vephai.remove(i)
                vetrai.append(phu(i))
    return [dong[0], vetrai, vephai]

# Hàm chứng minh, kiểm tra tính chứng minh của từng dòng
def chungminh (dong, bien, dich):
    s = bien + "=" + dich
    vetrai = dong[1]
    vephai = dong[2]
    vephai_xet = [i.replace(s, dich) for i in vephai] 
    vetrai_xet = [i.replace(s, dich) for i in vetrai]
    a = set (vephai_xet) & set (vetrai_xet) 
    if a:
        print("\t{}. {} => {} (Thế {}). Mệnh đề được chứng minh. Vì có chung {}".format(dong[0], (', ').join(vetrai), (', ').join(vephai), s, a))
        return 0
    for i in vetrai:
        if 'v' in i:
            return 1
    for i in vephai:
        if '^' in i:
            return 2
    print("\t{}. {} => {} (Thế {}) không thể chứng minh => Mệnh đề không được chứng minh.".format(dong[0], (', ').join(vetrai), (', ').join(vephai), s, a))
    return 3


# @title Hàm tách. Tách 1 dòng thành 2 dòng con
def tach(tap, phep):
    res1 = tap.copy()
    res2 = tap.copy()
    for i in range(len(tap)):
        if phep in tap[i]:
            for j in range(len(tap[i])): 
                if phep== tap[i][j]:
                    res1[i] = tap[i][j]
                    res2[i] = tap[i][j + 1:] 
                    return res1, res2
# return None, None


[ ] # @title Hàm in ra màn hình dòng a được tách thành b và c
def show_tach(dong, dong1, dong2):
    print("Ta tách dòng {} thành dòng {} và dòng {}".format(dong[0], dong1[0], dong2[0])) 
    print('\t{}. {} => {}'.format(dong1[0], ",".join(dong1[1]), ",".join(dong1[2])))
    print('\t{}. {} => {}'.format(dong2[0], ",".join(dong2[1]), ",".join(dong2[2])))
        

# @title Hàm wanghao
def wanghao(GT, KL, bien, dich):
    s = bien + "=" + dich
    GT = GT.replace("", "").split(',')
    GT = [i.replace('(' + bien + ')', '(' + s + ')') for i in GT]
    KL = KL.replace("", "").split(',')
    my_list = []
    dong = chuyenve(['1', GT, KL])
    my_list.append(dong)
    print("Ta có: {}. {} = {}, (Thế {})" .format(dong[0],(', ').join(dong[1]), (', ').join(dong[2]), s))
    while my_list:
        duyet = my_list.pop(0)
        tam = chungminh(duyet, bien, dich) 
        if tam == 3:
            return False
        if tam == 0:
            continue
        if tam == 1:
            tt1, tt2 = tach(duyet[1], 'v') 
            dong1 = [duyet[0] + '.1', tt1, duyet[2]] 
            dong2 = [duyet[0] + '.2', tt2, duyet[2]]
        elif tam == 2:
            tt1, tt2 = tach(duyet[2], '^') 
            dong1 = [duyet[0] + '.1', duyet[1], tt1] 
            dong2 = [duyet[0] + '.2', duyet[2], tt2]
        show_tach(duyet, dong1, dong2, s)
        my_list.extend([chuyenve(dong1), chuyenve(dong2)])
    print("Tất cả đã được chứng minh.")
    print("=> Bài toán đã được chứng minh.")
    return True

# @title Main
GT = 'HocCSDL(x) v HocMangMT(x), -HocCSDL(x) v BietSQL(x), -BietSQL(x) v -ThichExcel (x), ThichExcel (An)'
KL = 'HocMangMT (An)'
print (wanghao(GT, KL, 'x', 'An'))