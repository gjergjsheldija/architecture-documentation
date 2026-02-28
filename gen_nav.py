import os
import yaml

docs_dir = 'docs'
file_list = []

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith('.md'):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, docs_dir)
            file_list.append(rel_path)

file_list.sort()

def build_tree(paths):
    tree = {}
    for path in paths:
        parts = path.split(os.sep)
        current = tree
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = path
    return tree

tree = build_tree(file_list)

def tree_to_nav(tree):
    nav = []
    # Handle index.md first
    if 'index.md' in tree:
        nav.append({'Home': 'index.md'})
        del tree['index.md']
    
    # Sort keys to maintain order (especially with numbers like 01, 02...)
    for key in sorted(tree.keys()):
        val = tree[key]
        if isinstance(val, str):
            # Clean up filename for title
            title = key.replace('.md', '')
            nav.append({title: val})
        else:
            # It's a directory
            # Check if there is a corresponding .md file for this directory
            md_equiv = key + '.md'
            # Look in the parent level for md_equiv
            # This is tricky because the tree structure is nested
            # If the md_equiv exists in the current level's parent, it was already handled or will be.
            # Actually, let's keep it simple.
            nav.append({key: tree_to_nav(val)})
    return nav

nav_structure = tree_to_nav(tree)
print(yaml.dump({'nav': nav_structure}, sort_keys=False, allow_unicode=True))
