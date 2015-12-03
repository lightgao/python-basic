

# https://github.com/nigma/pywt/blob/master/demo/wavedec.py
# http://www.pybytes.com/pywavelets/ref/index.html
# http://www.pybytes.com/pywavelets/ref/signal-extension-modes.html#ref-modes


# > MathLab
# http://cn.mathworks.com/help/wavelet/ref/wavedec.html
# http://cn.mathworks.com/help/wavelet/ref/wrcoef.html
# http://cn.mathworks.com/help/wavelet/ref/dwtmode.html







# http://www.pybytes.com/pywavelets/ref/dwt-discrete-wavelet-transform.html
#
# Wavelet transform has recently become a very popular when it comes to analysis, de-noising and compression of signals and images.
# 通常小波变换被应用在 信号或图像 的 分析／降噪／压缩 上
#
# wavelet reconstruction      小波重构
# wavelet decomposition       小波分解
#
#
# >>>>>>>>> (Forward) Discrete Wavelet Transform (DWT)    离散 小波变换
#
# 1D single level DWT decomposition
#     (cA, cD) = dwt(data, wavelet, mode='sym')
#
# 1D multilevel DWT decomposition and returns ordered list of coefficients arrays
#     [cA_n, cD_n, cD_n-1, ..., cD2, cD1] = pywt.wavedec(data, wavelet, mode='sym', level=None)
#
# ...
#
#
# >>>>>>>>> Inverse Discrete Wavelet Transform  (IDWT)    逆离散 小波变换
#
# single level IDWT reconstruction
#     data = pywt.idwt(cA, cD, wavelet[, mode='sym'[, correct_size=0]])
#
# multilevel IDWT reconstruction
#     data = pywt.waverec(coeffs, wavelet[, mode='sym'])
#
# direct reconstruction
#     data = pywt.upcoef(part, coeffs, wavelet[, level=1[, take=0]])
#         part = ‘a’ - approximations reconstruction is performed
#                ‘d’ - details reconstruction is performed
#
# ...
#
#
# Stationary Wavelet Transform (Undecimated Wavelet Transform)    稳定/平稳 小波变换 (非抽取 小波变换)
#
# Wavelet Packet decomposition and reconstruction     小波包 分解和重构
#
#


