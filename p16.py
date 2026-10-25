
import logging
from pathlib import Path


# Configure error logging
logging.basicConfig(
    filename="file_processor.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Custom exception hierarchy
class FileProcessorError(Exception):
    """Base exception for file processing errors."""
    pass


class InvalidFileFormatError(FileProcessorError):
    """Raised when the file contains invalid data."""
    pass


class EmptyFileError(FileProcessorError):
    """Raised when the file has no data."""
    pass


def process_file(filename):
    file = None

    try:
        print(f"\nOpening file: {filename}")

        file = open(filename, "r", encoding="utf-8")
        contents = file.read()

        if not contents.strip():
            raise EmptyFileError("The file is empty.")

        # Expect one number per line
        numbers = []

        for line_number, line in enumerate(
            contents.splitlines(), start=1
        ):
            try:
                numbers.append(float(line.strip()))
            except ValueError as error:
                raise InvalidFileFormatError(
                    f"Invalid number on line {line_number}: "
                    f"'{line}'"
                ) from error

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        logging.exception("File not found")

    except EmptyFileError:
        print("Error: The file contains no data.")
        logging.exception("Empty file")

    except InvalidFileFormatError:
        print("Error: Invalid file format.")
        logging.exception("Invalid file format")

    except OSError:
        print("Error: A file system error occurred.")
        logging.exception("File system error")

    else:
        # Runs only when no exception occurred
        total = sum(numbers)
        average = total / len(numbers)

        print("File processed successfully!")
        print(f"Numbers: {numbers}")
        print(f"Total: {total:.2f}")
        print(f"Average: {average:.2f}")

    finally:
        # Always runs, even when an exception occurs
        if file is not None:
            file.close()
            print("File closed safely.")
        else:
            print("No file handle to close.")


if __name__ == "__main__":
    print("=" * 45)
    print("       SAFE FILE PROCESSOR")
    print("=" * 45)

    # Create a sample input file for demonstration
    sample_file = Path("numbers.txt")
    sample_file.write_text(
        "10\n20\n30\n40\n",
        encoding="utf-8"
    )

    process_file("numbers.txt")        # Valid input
    process_file("missing.txt")        # Missing file

    # Demonstrate invalid formatting
    Path("invalid_numbers.txt").write_text(
        "10\nhello\n30\n",
        encoding="utf-8"
    )
    process_file("invalid_numbers.txt")

    # Demonstrate empty-file handling
    Path("empty.txt").write_text("", encoding="utf-8")
    process_file("empty.txt")

    print("\nProcessing demonstration completed.")
    print("Check file_processor.log for error details.")
