# to know more about the differents families
pywt.families?

# to analyse all the output dimension
wavelet = pywt.Wavelet(families)
pywt.wavedecn_shapes((input_dim, input_dim), wavelet=wavelet, level=2, mode='periodization')

# to have the details level by level
# LEVEL 1 
liste_coeffs = []
for img in liste_img:
    liste_coeffs.append(pywt.dwt2(img, familie, mode='periodization'))
    
liste_coarse = []
liste_detail = []

titles = ['LL : caract globales', 'LH horizontale : transitions rapides de luminances',
          'HL diagonale : transition rapides de contrastes', 'HH diagonale : transition rapide de contours']

for coeffs in liste_coeffs:
    LL, (LH, HL, HH) = coeffs
    liste_coarse.append(LL)
    liste_detail.append((LH, HL, HH))

    fig = plt.figure(figsize=(20, 20))
    for i, a in enumerate([LL, LH, HL, HH]):
        ax = fig.add_subplot(1, 4, i + 1)
        ax.imshow(a)
        ax.set_title(titles[i], fontsize=9)
        ax.axis('off')
        
# LEVEL 2
liste_coeffs2 = []
for img in liste_coarse:
    liste_coeffs2.append(pywt.dwt2(img, familie, mode='periodization'))
    
liste_coarse2 = []
liste_detail2 = []

titles = ['LL : caract globales', 'LH horizontale : transitions rapides de luminances',
          'HL diagonale : transition rapides de contrastes', 'HH diagonale : transition rapide de contours']

for coeffs in liste_coeffs2:
    LL, (LH, HL, HH) = coeffs
    liste_coarse2.append(LL)
    liste_detail2.append((LH, HL, HH))

    fig = plt.figure(figsize=(20, 20))
    for i, a in enumerate([LL, LH, HL, HH]):
        ax = fig.add_subplot(1, 4, i + 1)
        ax.imshow(a)
        ax.set_title(titles[i], fontsize=9)
        ax.axis('off')
        
# to have the wavelet decomposition for a certain level
coeffs = pywt.wavedec2(img, wavelet=families, level=2, mode='periodization')
cA3, (cH3, cV3, cD3), (cH2, cV2, cD2) = coeffs

# to have the reconstruction of the wavelet decomposition
img_reconstruction = pywt.waverec2((coeff_low_frequence, coeff_high_frequence), wavelet = wavelet)
