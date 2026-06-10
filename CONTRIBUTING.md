# Contributing to PYTHONIC

Thank you for your interest in contributing to PYTHONIC! This document provides guidelines and instructions for contributing.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Folder Structure Guidelines](#folder-structure-guidelines)
- [File Naming Conventions](#file-naming-conventions)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing opinions and experiences
- Gracefully accept constructive criticism
- Help and support other community members

---

## How to Contribute

### Report Bugs
- Check if the bug already exists in Issues
- Provide a clear description of the bug
- Include steps to reproduce
- Mention your Python version and OS

### Suggest Enhancements
- Check if similar suggestions exist
- Explain the enhancement clearly
- Provide examples of how it would be used
- List any possible drawbacks

### Add New Content
- Follow the folder structure guidelines (below)
- Ensure code runs without errors
- Add clear comments for complex logic
- Include proper file naming
- Update FILE_INDEX.md

---

## Development Setup

### Prerequisites
- Python 3.6 or higher
- Git
- A text editor or IDE

### Local Setup

1. **Fork the repository**
   ```bash
   Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/PYTHONIC.git
   cd PYTHONIC
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Add new files or modify existing ones
   - Test thoroughly

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add meaningful description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "Compare & pull request"
   - Fill in the PR template

---

## Folder Structure Guidelines

### Category Organization

Files should be placed in appropriate numbered categories (01-12):

```
PYTHONIC_ORGANIZED/
├── 01_Basics/
├── 02_Operators/
├── 03_Control_Flow/
├── 04_Loops/
├── 05_String_Operations/
├── 06_Data_Structures/
├── 07_Functions/
├── 08_File_IO_CSV/
├── 09_Libraries_Modules/
├── 10_Projects_Applications/
├── 11_Testing/
└── 12_Advanced/
```

### When Adding a New File

1. **Identify the correct category** based on primary topic
2. **Place in appropriate subcategory** folder
3. **Follow the naming convention** (see below)
4. **Ensure it fits the learning progression** (not too advanced)

---

## File Naming Conventions

### Python Files
```
[number]_[descriptive_name].py

Examples:
- 01_hello_world.py
- 02_variable_assignment.py
- 03_nested_conditionals.py
```

### Naming Rules
- Use lowercase letters and underscores
- Use descriptive names (not single letters)
- Number sequentially within each folder
- Avoid special characters
- Keep names concise but clear

### Bad Examples ❌
- `solution.py`
- `test-file.py`
- `MyFile.py`
- `file.py`

### Good Examples ✓
- `01_hello_world.py`
- `02_user_input.py`
- `03_type_conversion.py`

---

## Code Quality Guidelines

### General Rules

1. **Code Style**
   - Follow PEP 8 conventions
   - Use 4 spaces for indentation
   - Maximum 79 characters per line

2. **Comments**
   - Add comments for complex logic
   - Use `#` for inline comments
   - Use `"""docstrings"""` for function descriptions
   - Example:
     ```python
     def calculate_area(radius):
         """Calculate circle area using radius."""
         return 3.14 * radius * radius
     ```

3. **Variable Names**
   - Use clear, descriptive names
   - Use snake_case (not camelCase)
   - Example: `user_age` not `userAge`

4. **Avoid**
   - Overly complex logic
   - Magic numbers (use constants)
   - Commented-out code
   - Import statements not used

### Example Good File

```python
# Calculate area of different shapes

def calculate_circle_area(radius):
    """Calculate area of circle: A = π * r²"""
    pi = 3.14159
    area = pi * radius * radius
    return area


def calculate_rectangle_area(length, width):
    """Calculate area of rectangle: A = length * width"""
    return length * width


# Main program
if __name__ == "__main__":
    radius = 5
    area = calculate_circle_area(radius)
    print(f"Circle area: {area}")
```

---

## Commit Guidelines

### Commit Message Format

```
[Type] Brief description

Detailed explanation if needed.
```

### Types
- **Add** - Adding new examples or features
- **Fix** - Fixing bugs or errors
- **Update** - Updating existing content
- **Docs** - Documentation changes
- **Refactor** - Code reorganization

### Examples
```
Add: List comprehension examples to 06_Data_Structures
Fix: Typo in string_slicing.py comments
Update: FILE_INDEX.md with new files
Docs: Improve README with better structure
```

### Commit Rules
- Make one logical change per commit
- Use present tense ("Add" not "Added")
- Reference issues if applicable (#123)
- Keep messages concise but descriptive

---

## Pull Request Process

### Before Submitting

1. **Test your code**
   ```bash
   python your_file.py
   ```

2. **Check for errors**
   - Syntax errors
   - Logic errors
   - Runtime issues

3. **Update documentation**
   - Update FILE_INDEX.md if adding files
   - Update category READMEs if applicable

4. **Verify structure**
   - Files in correct folders
   - Proper naming conventions
   - No unnecessary files

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New content
- [ ] Bug fix
- [ ] Documentation update
- [ ] File reorganization

## Related Issues
Fixes #(issue number)

## Testing
Describe testing performed:
- [ ] Code runs without errors
- [ ] No syntax errors
- [ ] All imports work
- [ ] Output is correct

## Checklist
- [ ] Followed naming conventions
- [ ] Added comments where needed
- [ ] Updated FILE_INDEX.md
- [ ] Tested the code
- [ ] No unnecessary files
```

### Review Process

- Maintainers will review your PR
- May request changes
- Once approved, your PR will be merged
- You'll be added to contributors list

---

## Types of Contributions

### 1. New Examples
- Add new Python examples to appropriate categories
- Ensure examples teach a specific concept
- Include comments and clear variable names

### 2. Improvements
- Fix errors or typos
- Improve code clarity
- Optimize examples
- Add better comments

### 3. Documentation
- Improve README files
- Update guides
- Fix broken links
- Add new learning paths

### 4. Bug Reports
- Report errors in existing files
- Provide steps to reproduce
- Suggest fixes if possible

---

## Questions or Issues?

- **Report bugs**: Open an issue on GitHub
- **Ask questions**: Open a discussion
- **Get help**: Check existing issues first
- **Contact**: Tag a maintainer

---

## Recognition

Contributors will be:
- Listed in the repository README
- Credited in commit messages
- Featured in release notes

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to PYTHONIC! 🎉
