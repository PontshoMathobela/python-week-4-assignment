def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        # Modify each line by adding line numbers
        modified_lines = [f"{i + 1}: {line}" for i, line in enumerate(lines)]

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"✅ Successfully wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


# Ask the user for a filename
input_filename = input("📄 Enter the filename to read: ").strip()

# You can set a default name for the output
output_filename = "modified_output.txt"

# Run the function
modify_file(input_filename, output_filename)
