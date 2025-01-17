from pptx2md import convert, ConversionConfig
from pathlib import Path

# Basic usage
convert(
    ConversionConfig(
        pptx_path=Path(r'C:\Users\21690\Documents\GitHub\Intro2ComputingC\slides.pptx'),
        output_path=Path('README.md'),
        image_dir=Path('img'),
        disable_notes=True
    )
)