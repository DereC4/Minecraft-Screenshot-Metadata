# Minecraft Photo Metadata Setter
<img width="497" height="344" alt="image" src="https://github.com/user-attachments/assets/2cbd8b6d-9807-45f9-9e33-4457f0640af7" />

This tool reads screenshots named like `YYYY-MM-DD_HH.MM.SS.png` and writes consistent metadata (EXIF, XMP, and PNG creation time) based on the timestamp in the filename. Files are copied from an input folder to an output folder and updated there.

## Usage

- Place your screenshots in `input` (the script will create it if missing)
- Run the script

## What gets written

- EXIF: DateTimeOriginal, CreateDate, ModifyDate (UTC)
- XMP: CreateDate, ModifyDate, MetadataDate (UTC, ISO 8601)
- PNG: CreationTime (UTC, ISO 8601)

Files are copied to `output` and modified there.
