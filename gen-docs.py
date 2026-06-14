import re
import sys
from collections import defaultdict

def parse_comment_blocks(file_path):
    section_pattern = re.compile(r'^.*(?:\/\/|\/\*|\*)\s*@section\s+(.*)$')
    class_pattern = re.compile(r'^.*(?:\/\/|\/\*|\*)\s*@class\s+(.*)$')
    desc_pattern = re.compile(r'^.*(?:\/\/|\/\*|\*)\s*@desc\s+(.*)$')

    entries = []
    current_entry = None

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            section_match = section_pattern.match(line)
            if section_match:
                if current_entry:
                    entries.append(current_entry)
                extracted_section_name = section_match.group(1).replace('*/', '').strip().lower()
                current_entry = {
                    "section": extracted_section_name, 
                    "class": "",
                    "desc": ""
                }
                continue

            if current_entry:
                section_match = section_pattern.match(line)
                class_match = class_pattern.match(line)
                desc_match = desc_pattern.match(line)
                
                if section_match:
                    current_entry["section"] = section_match.group(1).replace('*/', '').strip().lower()
                elif class_match:
                    current_entry["class"] = class_match.group(1).replace('*/', '').strip()
                elif desc_match:
                    current_entry["desc"] = desc_match.group(1).replace('*/', '').strip()

    if current_entry:
        entries.append(current_entry)
    return entries

def generate_classified_docs():
    all_entries = parse_comment_blocks("./src/pre.css")
    
    sections = defaultdict(list)
    for entry in all_entries:
        sections[entry["section"]].append(entry)

    markdown = "# Classes\n\n"

    for section_name, entries in sections.items():
        markdown += f"## {section_name.capitalize()} Utilities\n\n"
        markdown += "| Class | Behavior |\n"
        markdown += "| :--- | :--- |\n"
        
        for entry in entries:
            markdown += f"| `{entry['class']}` | {entry['desc']} |\n"
        
        markdown += "\n"

    output_path = "docs/src/classes.md"
    with open(output_path, 'w', encoding='utf-8') as out_f:
        out_f.write(markdown)
        
    print(f"Classified docs built at {output_path}")

generate_classified_docs()
