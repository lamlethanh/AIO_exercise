def cal_md_nre_single(y, y_hat, n, p):
    value = (pow(y, 1/n) - pow(y_hat, 1/n))
    return pow(value, p)

print(cal_md_nre_single(100, 99.5, 2, 1))