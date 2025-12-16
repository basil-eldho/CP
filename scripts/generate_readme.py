#!/usr/bin/env python3
"""
Auto-generate README.md for LeetCode repository
Scans problem folders and creates a clean dashboard
"""

import os
import re
from datetime import datetime
from pathlib import Path

def extract_problem_info(folder_name):
    """Extract problem number and name from folder"""
    match = re.match(r'^(\d+)-(.+)$', folder_name)
    if match:
        number = match.group(1)
        name = match.group(2).replace('-', ' ').title()
        return number, name
    return None, None

def get_difficulty_from_readme(readme_path):
    """Extract difficulty from problem README"""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if 'Difficulty-Easy' in content:
                return 'Easy'
            elif 'Difficulty-Medium' in content:
                return 'Medium'
            elif 'Difficulty-Hard' in content:
                return 'Hard'
    except:
        pass
    return 'Unknown'

def get_solution_file(folder_path):
    """Find the solution file in the folder"""
    extensions = ['.cpp', '.java', '.py', '.js', '.ts', '.c', '.go', '.rs']
    for file in os.listdir(folder_path):
        if any(file.endswith(ext) for ext in extensions):
            ext = Path(file).suffix
            lang_map = {
                '.cpp': 'C++',
                '.java': 'Java',
                '.py': 'Python',
                '.js': 'JavaScript',
                '.ts': 'TypeScript',
                '.c': 'C',
                '.go': 'Go',
                '.rs': 'Rust'
            }
            return file, lang_map.get(ext, 'Code')
    return None, None

def scan_problems():
    """Scan repository for problem folders"""
    problems = []
    root = Path('.')
    
    for item in root.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            number, name = extract_problem_info(item.name)
            if number and name:
                readme_path = item / 'README.md'
                difficulty = get_difficulty_from_readme(readme_path)
                solution_file, language = get_solution_file(item)
                
                if solution_file:
                    problems.append({
                        'number': int(number),
                        'name': name,
                        'folder': item.name,
                        'difficulty': difficulty,
                        'solution_file': solution_file,
                        'language': language
                    })
    
    return sorted(problems, key=lambda x: x['number'])

def generate_readme(problems):
    """Generate README content"""
    # Count by difficulty
    easy = sum(1 for p in problems if p['difficulty'] == 'Easy')
    medium = sum(1 for p in problems if p['difficulty'] == 'Medium')
    hard = sum(1 for p in problems if p['difficulty'] == 'Hard')
    total = len(problems)
    
    # Get unique languages
    languages = sorted(set(p['language'] for p in problems))
    languages_str = ', '.join(languages)
    
    # Difficulty badge colors
    diff_colors = {
        'Easy': '5cb85c',
        'Medium': 'f0ad4e',
        'Hard': 'd9534f'
    }
    
    # Generate progress bars
    max_bar = 10
    easy_bar = '█' * min(easy, max_bar) + '░' * (max_bar - min(easy, max_bar))
    medium_bar = '█' * min(medium, max_bar) + '░' * (max_bar - min(medium, max_bar))
    hard_bar = '█' * min(hard, max_bar) + '░' * (max_bar - min(hard, max_bar))
    
    # Build README
    content = f"""# 🚀 LeetCode Progress

![](https://img.shields.io/badge/Problems%20Solved-{total}-brightgreen?style=for-the-badge)
![](https://img.shields.io/badge/Easy-{easy}-5cb85c?style=for-the-badge)
![](https://img.shields.io/badge/Medium-{medium}-f0ad4e?style=for-the-badge)
![](https://img.shields.io/badge/Hard-{hard}-d9534f?style=for-the-badge)

## 📊 Progress Overview

My journey through LeetCode problems, automatically synced from my submissions.

---

## 📝 Solved Problems

| # | Problem | Difficulty | Solution |
|---|---------|------------|----------|
"""
    
    # Add problem rows
    for p in problems:
        prob_url = f"https://leetcode.com/problems/{p['folder'].replace(str(p['number']) + '-', '')}"
        diff_color = diff_colors.get(p['difficulty'], 'lightgrey')
        content += f"| {p['number']} | [{p['name']}]({prob_url}) | ![{p['difficulty']}](https://img.shields.io/badge/{p['difficulty']}-{diff_color}) | [{p['language']}](./{p['folder']}/{p['solution_file']}) |\n"
    
    content += f"""
---

## 🎯 Problem Distribution

```
Easy:     {easy_bar} {easy}
Medium:   {medium_bar} {medium}
Hard:     {hard_bar} {hard}
```

---

## 📈 Stats

- **Total Problems Solved**: {total}
- **Languages Used**: {languages_str}
- **Last Updated**: {datetime.now().strftime('%B %d, %Y')}

---

<div align="center">
  <i>🔄 This repository is automatically updated via LeetCode GitHub Sync</i>
</div>
"""
    
    return content

def main():
    """Main function"""
    print("Scanning for LeetCode problems...")
    problems = scan_problems()
    print(f"Found {len(problems)} problems")
    
    print("Generating README...")
    readme_content = generate_readme(problems)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("README.md updated successfully!")

if __name__ == '__main__':
    main()
