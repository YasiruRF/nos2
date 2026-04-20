
with open(r'D:\Praxis\NOS\ros2_dsl_architecture.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(550, 560):
    if i < len(lines):
        print(f"Line {i+1}: {repr(lines[i])}")
        if 'â' in lines[i]:
            for char in lines[i]:
                if ord(char) > 127:
                    print(f"  Non-ASCII Char: {char}, Ord: {ord(char)}")
