galois_row = [1, 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148]
generating_polynomial = [[1, 8], [1, 7], [1, 6], [0, 5], [0, 4], [0, 3], [0, 2], [1, 1], [1, 0]]
generating_polynomial_test_GF8 = [[1, 3], [0, 2], [1, 1], [1, 0]]
coefficients_poly1 = []
coefficients_poly2 = []
degree = []

x = 5
y = 7
bin_x = str(bin(x))[2:]
bin_y = str(bin(y))[2:]

if len(bin_x) < 8:
    bin_x = '0' * (8 - len(bin_x)) + bin_x
for i in range(len(bin_x)):
    degree.append(bin_x[i])
    degree.append(7 - i)
    coefficients_poly1.append(degree)
    degree = []
print(coefficients_poly1)

if len(bin_y) < 8:
    bin_y = '0' * (8 - len(bin_y)) + bin_y
for i in range(len(bin_y)):
    degree.append(bin_y[i])
    degree.append(7 - i)
    coefficients_poly2.append(degree)
    degree = []
print(coefficients_poly2)


#multiplication of polynomials for GF(8)
def polynomials_to_multiply(p1, p2):
    deg = []
    degr = []
    poly = []
    poly_deg = []
    for i in range(8):
        if p1[i][0] != '0':
            for j in range(8):
                if p2[j][0] != '0':
                    deg.append(p1[i][1] + p2[j][1])
    for i in deg:
        cnt = 0
        if i in degr:
            cnt += 1
            x = degr.index(i)
            if cnt % 2 != 0:
                degr.pop(x)
            else:
                degr.append(i)
        else:
            degr.append(i)
    degr.sort(reverse=True)
    print(degr)
    for i in range(degr[0] + 1):
        poly_deg.append(0)
        poly_deg.append(degr[0] - i)
        poly.append(poly_deg)
        poly_deg = []
    for i in range(len(degr)):
        for j in range(degr[0] + 1):
            #print('degr[i] =', degr[i], ' / ',  'poly[j][1] =', poly[j][1], j)
            if degr[i] == poly[j][1]:
                poly[j][0] = 1
    #print(poly)
    poly_bin = ''
    for i in range(len(poly)):
        poly_bin = poly_bin + str(poly[i][0])
    poly_dec = int(poly_bin, 2)
    return poly_bin, poly_dec


print(polynomials_to_multiply(coefficients_poly1, coefficients_poly2))