import glob
import cv2
from stitching import Stitcher

def resize_img(orig_img, width = None, height = None, interp=cv2.INTER_LINEAR):
    (h, w) = orig_img.shape[:2]

    if width is None and height is None:
        # i.e. if neither width and height are given
        return orig_img
    elif width is None and height is not None:
        # i.e. if height is given
        ratio = height / float(h)
        resized_dim = (int(w * ratio), height)
    elif height is None and width is not None:
        # i.e. if width is given
        ratio = width / float(w)
        resized_dim = (width, int(h * height))
    else:
        # i.e. if neither width and height are given
        resized_dim = (width, height)

    return cv2.resize(orig_img, resized_dim, interpolation=interp)

def main():
    UNSTITCHED_IMAGES_FOLDER = "unstitchedImages/*.jpg"
    DO_STITCH_VERBOSE = False
    VERBOSE_OUTPUT_DIR = "stitcher_brisk_050"

    img_paths = glob.glob(UNSTITCHED_IMAGES_FOLDER)

    # Load images into memory
    all_imgs = []
    for path in img_paths:
        cv_img = cv2.imread(path)
        cv_resize_img = resize_img(cv_img, height = 600)
        all_imgs += [cv_resize_img]

    # Create panorama stitching object
    stitcher = Stitcher(
        #py detector="sift",
        # confidence_threshold=0.5,
    )

    # Create panorama
    if DO_STITCH_VERBOSE:
        panorama = stitcher.stitch_verbose(all_imgs, verbose_dir=VERBOSE_OUTPUT_DIR)
    else:
        panorama = stitcher.stitch(all_imgs)

    # Save panorama to disk
    cv2.imwrite("panorama.jpg", panorama)