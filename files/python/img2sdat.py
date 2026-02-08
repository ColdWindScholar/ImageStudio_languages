import os
import sys

import blockimgdiff
import sparse_img
import tempfile

DataImage = blockimgdiff.DataImage
def img2sdat(input_image, out_dir='.', version=None, prefix='system'):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    versions = {
        1: "Android Lollipop 5.0",
        2: "Android Lollipop 5.1",
        3: "Android Marshmallow 6.0",
        4: "Android Nougat 7.0/7.1/8.0/8.1"}
    if version not in versions.keys():
        version = 4
    print(f"Img2sdat(1.7):{versions[version]}")
    blockimgdiff.BlockImageDiff(sparse_img.SparseImage(input_image, tempfile.mkstemp()[1], '0'), None, version).Compute(
        f'{out_dir}/{prefix}')

# utils.img2sdat(f"{work}/{name}.img", work, dat_ver, name)
# in mkc, its called like up.
if __name__ == "__main__":
    img2sdat(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])