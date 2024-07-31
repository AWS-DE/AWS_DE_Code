def re_encode_file(input_file, output_file="unknown"):
  """
  Re-encodes a file to UTF-8.

  Args:
      input_file (str): Path to the file to be re-encoded.
      output_file (str, optional): Path to save the re-encoded file. (Optional, defaults to appending "_utf8" to input filename)
  """
  # Open the input file in binary mode for broader compatibility
  with open(input_file, "rb") as f:
    content = f.read()

  # Try to detect encoding using chardet (assuming it's installed)
  try:
    from chardet import UniversalDetector
    detector = UniversalDetector()
    detector.feed(content)
    detector.close()
    original_encoding = detector.result["encoding"]
  except ImportError:
    original_encoding = "unknown"
    print("Warning: chardet library not found. Using 'unknown' encoding.")

  # Open the output file with UTF-8 encoding
  if output_file == "unknown":
    output_file = f"{input_file[:-4]}_utf8.txt"

  with open(output_file, "w", encoding="utf-8") as f:
    try:
      # Decode content using original encoding and write directly as string
      f.write(content.decode(original_encoding, errors="replace"))
      print(f"File re-encoded successfully: {output_file}")
    except UnicodeDecodeError:
      print(f"Error: Unable to decode using {original_encoding}. Trying generic UTF-8 encoding...")
      f.write(content.decode("utf-8", errors="replace").encode("utf-8").decode("utf-8"))  # Only for specific needs
      print(f"File re-encoded with generic UTF-8 (may have character replacements): {output_file}")

# Example usage 
input_file = "C:\\Users\\Chinna\\Downloads\\archive (2)\\sales_data_sample.csv" 

re_encode_file(input_file)  # Uses "unknown" encoding and appends "_utf8"
# re_encode_file(input_file, "renamed_utf8.txt")  # Specify output filename
