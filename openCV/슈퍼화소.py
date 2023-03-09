import skimage
import numpy as np
import cv2 as cv
import time

img=skimage.data.coffee()
cv.imshow('Coffee image', cv.cvtColor(img, cv.COLOR_RGB2BGR))

start=time.time()
slic=skimage.segmentation.slic(img, compactness=20, n_segments=600, start_label=1)
g=skimage.future.graph.rag_mean_color(img, slic, mode='similarity')
ncut=skimage.future.graph.cut_normalized(slic, g)
print(img.shape, '영상분할에 ', time.time()-start, '초 소요')

marking=skimage.segmentation.mark_boundaries(img, ncut)
ncut_img=np.uint8(marking*255.0)

cv.imshow('Normalized cut', cv.cvtColor(ncut_img, cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()
