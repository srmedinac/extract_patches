from histoprep import SlideReader
import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

slides_path = "/path/to/slide/.svs"
masks_path = "/path/to/mask/.png"
save_path = "/path/for/saving/patches"
mask_save_path = "/path/for/saving/masks"
level = 1
overlap = 0
max_background = 0.5
patch_size = 512

reader = SlideReader(slides_path)
downsample = reader.level_downsamples[level][1]
downsampled_patch_size = int(patch_size * downsample)
mask_reader = SlideReader(masks_path, backend="PILLOW")
threshold, tissue_mask = reader.get_tissue_mask(level=1)
tile_coordinates = reader.get_tile_coordinates(
    tissue_mask,
    width=downsampled_patch_size,
    overlap=overlap * downsample,
    max_background=max_background,
)

tile_metadata = reader.save_regions(
    save_path,
    tile_coordinates,
    level=level,
    threshold=threshold,
    save_metrics=False,
    overwrite=True,
)
mask_metadata = mask_reader.save_regions(
    mask_save_path,
    tile_coordinates,
    level=level,
    threshold=threshold,
    save_metrics=False,
    overwrite=True,
)
