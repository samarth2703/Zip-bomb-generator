# ZIP Bomb Generator

A Python-based cybersecurity research project demonstrating ZIP compression, extreme compression ratios, and the security risks associated with archives that expand to exceptionally large sizes.

> **⚠️ WARNING:** This project demonstrates a potentially disruptive file format technique. The configured target size is 20 TiB (approximately 22 TB in decimal units). Do not run the generator on your primary system or extract generated archives on systems without strict resource limits.

## Overview

The ZIP Bomb Generator demonstrates how highly repetitive data can be compressed into a comparatively small ZIP archive using Python's built-in `zipfile` module and DEFLATE compression.

The provided script generates a file named `bomb_20tb.zip`, containing an entry named `bomb_file.txt`. The intended uncompressed size is approximately 20 TiB.

The actual compressed size and successful completion depend on the Python implementation, compression performance, available resources, and ZIP format limitations.

## Features

- **Python implementation:** Uses standard-library modules for archive creation and file handling.
- **DEFLATE compression:** Demonstrates high-level compression using `ZIP_DEFLATED`.
- **Repetitive data pattern:** Uses repeated byte values to illustrate compression efficiency.
- **Incremental writing:** Processes data in blocks rather than allocating the entire intended payload in memory.
- **Compression analysis:** Reports the final archive size and an estimated compression ratio.
- **Cybersecurity education:** Illustrates why archive extraction limits are important when processing untrusted files.

## Requirements

- Python 3.8 or later recommended.
- Standard-library modules:
  - `zipfile`
  - `os`
  - `sys` (imported but unused in the provided script)
- Adequate CPU resources and storage for the selected workload.

No third-party Python packages are required.

## How It Works

1. Calculates the intended uncompressed size using a binary unit conversion.
2. Creates a 1 MiB block of repeated `A` characters.
3. Calculates the number of blocks and any remaining bytes.
4. Opens a ZIP archive using DEFLATE compression.
5. Writes the repetitive data incrementally into `bomb_file.txt`.
6. Closes the archive and reports its actual compressed size and estimated compression ratio.

## Configuration

The provided script uses the following configuration:

| Parameter | Value |
|---|---|
| Output filename | `bomb_20tb.zip` |
| Target uncompressed size | 20 TiB |
| Repeating pattern | `A` characters |
| Pattern block size | 1 MiB |
| Compression method | DEFLATE |
| Compression level | 9 |
| Archive entry | `bomb_file.txt` |

**Note:** The script uses \(1024^4\) bytes per target unit, so its `target_size_tb=20` setting represents 20 tebibytes (TiB), not 20 decimal terabytes (TB).

## Execution

The script's entry point invokes the generator with a target size of 20 TiB.

Running this configuration may require substantial processing time and can create an archive that consumes significant storage. Review the source code before execution and avoid running the full-size configuration on a production or personal system.

## Security Considerations

Archives with extreme expansion ratios can cause denial-of-service conditions when software extracts or scans them without sufficient resource controls.

Potential consequences include:

- Exhaustion of available disk space.
- Excessive CPU usage during compression, extraction, or scanning.
- Resource exhaustion in archive-processing applications.
- Application failures caused by oversized decompressed content.

For defensive testing, use small, controlled test inputs in a disposable virtual machine.

When building software that accepts ZIP files, consider enforcing:

- Maximum total extracted size.
- Maximum individual file size.
- Maximum archive nesting depth.
- Maximum compression ratio, where appropriate.
- Extraction timeouts and resource quotas.
- Safe handling of paths and archive entries.

## Limitations

- The reported compression ratio is an estimate based on the target size and final archive size.
- The generated archive's actual size is not predetermined.
- Successful archive creation is not guaranteed.
- ZIP readers and security scanners may reject oversized or suspicious archives.
- The script does not automatically extract the generated archive.

## Disclaimer 

This project is intended for cybersecurity education, compression research, and defensive testing in authorized, isolated environments.

The author is not responsible for data loss, service disruption, storage exhaustion, or other damage resulting from unsafe execution or extraction of generated archives.

Use responsibly and only on systems you own or have explicit authorization to test.
</span>
