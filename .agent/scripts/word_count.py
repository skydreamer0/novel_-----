import os
import re
import sys

def count_chars(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Total characters (excluding whitespace)
        total_chars = len(re.sub(r'\s+', '', content))
        
        # Chinese characters (Hanzi)
        chinese_chars = len(re.findall(r'[\u4e00-\u9fa5]', content))
        
        # Punctuation (roughly, if we want to be specific, we could, but let's stick to these two for now)
        # Or just return everything not whitespace
        
        return total_chars, chinese_chars
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0, 0

import csv

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    csv_output = sys.argv[3] if len(sys.argv) > 3 else None
    
    results = []
    
    if os.path.isfile(path):
        files = [path]
    else:
        files = []
        for root, _, filenames in os.walk(path):
            if '.agent' in root: continue
            for filename in filenames:
                if filename.endswith('.md'):
                    files.append(os.path.join(root, filename))
    
    files.sort()
    
    print(f"{'File Name':<45} | {'Total':>8} | {'Chinese':>8} | {'Status'}")
    print("-" * 80)
    
    grand_total = 0
    grand_chinese = 0
    short_chapters = 0
    csv_data = []
    
    for file in files:
        total, chinese = count_chars(file)
        rel_path = os.path.relpath(file, path) if os.path.isdir(path) else os.path.basename(file)
        
        status = ""
        if threshold > 0:
            if total < threshold:
                status = f"SHORT (min {threshold})"
                short_chapters += 1
            else:
                status = "OK"
        
        print(f"{rel_path:<45} | {total:>8,} | {chinese:>8,} | {status}")
        grand_total += total
        grand_chinese += chinese
        csv_data.append([rel_path, total, chinese, status])
        
    print("-" * 80)
    print(f"{'GRAND TOTAL':<45} | {grand_total:>8,} | {grand_chinese:>8,}")
    
    if threshold > 0:
        print(f"\nSummary: {len(files)} chapters total, {short_chapters} chapters below threshold.")

    if csv_output:
        try:
            with open(csv_output, 'w', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['File Path', 'Total Characters', 'Chinese Characters', 'Status'])
                writer.writerows(csv_data)
                writer.writerow(['GRAND TOTAL', grand_total, grand_chinese, ''])
            print(f"\nResults saved to: {csv_output}")
        except Exception as e:
            print(f"Error saving CSV: {e}")

if __name__ == "__main__":
    main()
