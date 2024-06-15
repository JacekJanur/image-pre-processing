# Image Pre-processing
This project automates image pre-processing for my art Instagram [@ciekawa_sztuka](https://www.instagram.com/ciekawa_sztuka/).

## Usage
Add images you want to pre-process to the */images* folder. The title will be generated from the image name. Then, simply run:

```bash
python main.py
```

## Pre-processing
Python will:
- Resize the image to 1080x1080 pixels.
- Add a colored triangle.
- Add a title.
- Save the new image.

## Example

<div style="display: flex; flex-direction: row;">
    <img src="example\forests.jpg" alt="Image Before" style="width: 45%; margin-right: 5%;" />
    <img src="example\changed_forests.jpg" alt="Image After" style="width: 45%;" />
</div>

## License

[MIT](https://choosealicense.com/licenses/mit/)