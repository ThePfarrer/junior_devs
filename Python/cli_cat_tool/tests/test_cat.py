import pytest
from click.testing import CliRunner

from cat_tool.cli import main


@pytest.fixture
def runner():
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_read_regular_file(runner):
    """Test reading from a regular file."""
    test_content = '"Thinking is the capital, Enterprise is the way, Hard Work is the solution."\n"If You Can\'T Make It Good, At Least Make It Look Good."\n'

    with runner.isolated_filesystem():
        with open("test.txt", "w") as f:
            f.write(test_content)

        result = runner.invoke(main, ["test.txt"])

        assert result.output == test_content


def test_read_multiple_files(runner):
    """Test reading from multiple files."""
    file1_content = "File 1 Line 1\nFile 1 Line 2\n"
    file2_content = "File 2 Line 1\nFile 2 Line 2\nFile 2 Line 3\n"

    with runner.isolated_filesystem():
        # Create test files
        with open("file1.txt", "w") as f:
            f.write(file1_content)
        with open("file2.txt", "w") as f:
            f.write(file2_content)

        # Run the command
        result = runner.invoke(main, ["file1.txt", "file2.txt"])

        assert result.output == file1_content + file2_content


def test_read_empty_file(runner):
    """Test reading from an empty file."""
    with runner.isolated_filesystem():
        with open("empty.txt", "w") as f:
            pass

        result = runner.invoke(main, ["empty.txt"])

        assert result.output == ""


def test_read_from_stdin(runner):
    """Test reading from stdin when '-' is provided."""
    test_input = "Input from pipe\n"

    result = runner.invoke(main, ["-"], input=test_input)

    assert result.output == test_input


def test_read_from_empty_stdin(runner):
    """Test reading from stdin when empty input is provided."""
    result = runner.invoke(main, ["-"], input="")

    assert result.output == ""


def test_number_all_lines_from_file(runner):
    """Test the '-n' option with text file."""
    test_input = "Line 1 from stdin\nLine 2 from stdin\n"
    expected_output = "     1  Line 1 from stdin\n     2  Line 2 from stdin\n"

    with runner.isolated_filesystem():
        with open("test.txt", "w") as f:
            f.write(test_input)

        result = runner.invoke(main, ["-n", "test.txt"])

        assert result.output == expected_output


def test_number_all_lines_from_stdin(runner):
    """Test the '-n' option with stdin input."""
    test_input = "Line 1 from stdin\nLine 2 from stdin\n"
    expected_output = "     1  Line 1 from stdin\n     2  Line 2 from stdin\n"

    result = runner.invoke(main, ["-n"], test_input)

    assert result.output == expected_output


def test_number_all_non_blank_lines_from_file(runner):
    """Test the '-b' option text file."""
    test_input = "Line 1\n\nLine 3\n"
    expected_output = "     1  Line 1\n\n     2  Line 3\n"

    with runner.isolated_filesystem():
        with open("test.txt", "w") as f:
            f.write(test_input)

        result = runner.invoke(main, ["-b", "test.txt"])

        assert result.output == expected_output


def test_number_all_non_blank_lines_from_stdin(runner):
    """Test the '-b' option with stdin input."""
    test_input = "Line 1\n\nLine 3\n"
    expected_output = "     1  Line 1\n\n     2  Line 3\n"

    result = runner.invoke(main, ["-b"], input=test_input)

    assert result.output == expected_output


def test_file_not_found(runner):
    """Test behavior when file is not found."""
    result = runner.invoke(main, ["non_existent_file.txt"])

    assert "Error" in result.output or "No such file" in result.output


def test_read_large_file(runner):
    """Test reading a large file."""
    large_file_content = "Line {}\n" * 1000000

    with runner.isolated_filesystem():
        with open("large.txt", "w") as f:
            f.write(large_file_content)

        result = runner.invoke(main, ["large.txt"])

        assert result.output == large_file_content
