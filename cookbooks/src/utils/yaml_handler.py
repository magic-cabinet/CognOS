import yaml

def clean_yaml(text):
    """
    Remove markdown code fence markers from YAML text.
    Handles both ```yaml and ``` markers.
    """
    lines = text.strip().split('\n')
    
    # Remove first line if it starts with ```
    if lines and lines[0].strip().startswith('```'):
        lines = lines[1:]
    
    # Remove last line if it's just ```
    if lines and lines[-1].strip() == '```':
        lines = lines[:-1]
    
    return '\n'.join(lines)

def parse_yaml_to_dict(yaml_text):
    """
    Parse YAML text into a Python dictionary.
    Automatically cleans markdown code fences if present.
    """
    # Clean the text first
    cleaned_text = clean_yaml(yaml_text)
    
    # Parse YAML to dictionary
    data = yaml.safe_load(cleaned_text)
    
    return data


# Example usage
input_text = """```yaml
Street:
  - Via dei Fori Imperiali
  - Via del Corso
  - Ponte Palatino
  - Via della Lungara
Transport:
  - train
  - metro
  - bus
  - walk
  - taxi
  - private transfer
```"""

cleaned_yaml = clean_yaml(input_text)
print(cleaned_yaml)

# Parse to dictionary
result = parse_yaml_to_dict(input_text)

print("Parsed dictionary:")
print(result)
print("\nAccessing data:")
print(f"Streets: {result['Street']}")
print(f"First street: {result['Street'][0]}")
print(f"Transport methods: {result['Transport']}")