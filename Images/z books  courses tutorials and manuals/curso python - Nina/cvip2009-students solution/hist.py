import Image

def load_image(name):
    img = Image.open("lena_standard.pgm")
    return img

def hist_ef(img):
    mtr = img.load()
    h = [0] * 256
    width, height = img.size
    for i in range(height):
        for j in range(width):
            k = mtr[i, j]
            h[k] = h[k] + 1
    return h

def hist_podre(img):
    mtr = img.load()
    h = [0] * 256
    width, height = img.size
    for v in range(256):
        #print v
        for i in range(height):
            for j in range(width):
                if mtr[i, j] == v:
                    h[v] = h[v] + 1
    return h

def draw_hist(hist):
    h = Image.new("L", (256, 200))
    mtr = h.load()
    wi, he = h.size
    mx = max(hist)
    for j in range(wi):
        px = (1.0 * hist[j] / mx) * he
        px = int(px)
        for i in range(px):
            mtr[j, he - i - 1] = 128
    h.show()

lena = load_image("lena_standard.pgm")
he = hist_ef(lena)

draw_hist(he)
