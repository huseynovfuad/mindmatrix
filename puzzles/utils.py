from .models import PuzzleImage
from PIL import Image
from django.core.files import File
from django.core.files.images import ImageFile
from .models import upload_to_puzzle_images
from django.utils.text import slugify



def create_puzzle_pieces(puzzle):
    original_image = Image.open(puzzle.image)
    width, height = original_image.size

    # Calculate the size of each piece
    piece_width = width // puzzle.row
    piece_height = height // puzzle.column

    # Loop through the image and cut it into pieces
    for i in range(puzzle.row):
        for j in range(puzzle.column):

            # Define the region to crop
            left = j * piece_width
            upper = i * piece_height
            right = left + piece_width
            lower = upper + piece_height

            # Save the piece to the PuzzlePiece model
            piece_obj = PuzzleImage.objects.create(
                puzzle=puzzle,
                image=ImageFile(puzzle.image),
                row=i,
                col=j,
            )

            # Crop the image
            piece_image = original_image.crop((left, upper, right, lower))
            piece_image.save(piece_obj.image.path)
            # piece_image.show()

    # Close the original image to free up resources
    original_image.close()
