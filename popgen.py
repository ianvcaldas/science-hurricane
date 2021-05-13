def next_p(p):
    w1 = p*w11 + w12 - p*w12
    w2 = p*w12 + w22 - p*w22
    wbar = p*w1 + w2 - p*w2
    return p*w1/wbar

p = 0.01
s = 0.01
w11 = 1 + s
w12 = 1 + 0.5*s
w22 = 1

freqs = []
while p < 0.99:
    p = next_p(p)
    freqs.append(p)
    
num_y_bins = 8
y_bin_increment = 1/num_y_bins
num_x_bins = 30
x_bin_increment = len(freqs)/num_x_bins
x_bin_increment = round(x_bin_increment)
if len(freqs) < num_x_bins:
    x_bin_increment = 1

y = 0
print('allele frequency')
while y < num_y_bins:
    upper = 1 - y*(y_bin_increment)
    lower = 1 - (y + 1)*(y_bin_increment)
    line = "    |"
    if y == 0:
        line = "1.0 |"
    if y == num_y_bins - 1:
        line = "0.0 |"
    x_ix = 0
    while x_ix < len(freqs):
        current = freqs[x_ix]
        if current > lower and current < upper:
            line += "x"
        else:
            line += " "
        x_ix += x_bin_increment
    print(line)
    y += 1
print("    " + "-"*num_x_bins)
print("    1" + " "*num_x_bins + str(x_bin_increment*num_x_bins) + " generations")
