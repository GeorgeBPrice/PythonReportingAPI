import os
import subprocess
import shutil

def generate_asset_report_word(data, output_format="docx", output_dir="temp_reports"):
    """
    Generate a Word file for the asset report using Quarto.

    Args:
        data (dict): The report data to render in the report.
        output_format (str): The desired output format (default: "docx").
        output_dir (str): The directory where the generated file will be stored.

    Returns:
        str: Path to the generated Word file.

    Raises:
        ValueError: If the Quarto command fails or if data is invalid.
        FileNotFoundError: If the template file is missing.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Paths for templates and outputs
    template_path = os.path.join(os.getcwd(), "app/reports/asset_report.qmd")
    temp_template_path = os.path.join(os.getcwd(), "temp_asset_report.qmd")
    temp_output_file = f"temp_asset_report.{output_format}"
    final_output_file = os.path.join(output_dir, f"AssetReport.{output_format}")

    try:
        # Check if the template file exists
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template file not found at {template_path}")

        # Read the template and replace placeholders with actual data
        with open(template_path, "r") as template_file:
            content = template_file.read()

        # Replace placeholders dynamically
        try:
            content = content.replace("{{ asset_data }}", str(data))
        except Exception as e:
            raise ValueError(f"Error replacing placeholders in template: {e}")

        # Write the updated content to a temporary template file
        with open(temp_template_path, "w") as temp_file:
            temp_file.write(content)

        # Render the report using Quarto
        try:
            subprocess.run(
                [
                    "quarto",
                    "render",
                    temp_template_path,
                    "--to",
                    output_format,
                ],
                check=True,
                # stdout=subprocess.PIPE, # Capture the output in terminal
                # stderr=subprocess.PIPE, # Capture the error in terminal
            )
        except subprocess.CalledProcessError as e:
            raise ValueError(
                f"Quarto rendering failed with error: {e.stderr.decode('utf-8')}"
            )

        # Move the generated file to the desired output directory
        if os.path.exists(temp_output_file):
            shutil.move(temp_output_file, final_output_file)
        else:
            raise FileNotFoundError(f"Temporary output file not found: {temp_output_file}")

    finally:
        # Clean up the temporary template file
        if os.path.exists(temp_template_path):
            os.remove(temp_template_path)

    # Ensure the final output file exists
    if not os.path.exists(final_output_file):
        raise FileNotFoundError(f"Final output file not found: {final_output_file}")

    return final_output_file
