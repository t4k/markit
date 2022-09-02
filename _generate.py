import os
import subprocess
import sys


def main(file):
    print(f"🐞 file: {file}")
    # TODO think through handling of _closed files
    if file.startswith("web/"):
        # file_segments[1] will be component_id
        file_segments = file.split("/")
        if os.path.isfile(f"build/{file_segments[1]}/{file_segments[1]}.html"):
            print(f"🐞 file exists: build/{file_segments[1]}/{file_segments[1]}.html")
            return
        os.mkdir(file_segments[1])
        subprocess.run(
            [
                "pandoc",
                "--from=markdown",
                "--to=html",
                f"--output=build/{file_segments[1]}/{file_segments[1]}.html",
                f"web/{file_segments[1]}/{file_segments[1]}.md",
            ]
        )
        print(f"🐞 file generated: build/{file_segments[1]}/{file_segments[1]}.html")


if __name__ == "__main__":
    main(sys.argv[1])
