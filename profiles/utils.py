import cloudinary.uploader

"""
Method to upload profile picture to Cloudinary
"""


def upload_profile_picture(file):
    upload_result = cloudinary.uploader.upload(
        file, transformation={"width": 200, "height": 200, "crop": "fill"}
    )
    return upload_result["secure_url"]
