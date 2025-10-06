import os
import re
from typing import List, Tuple

ENKKI_ROOT = os.path.join("ENKKI")

def ensure_parent_td_padding(content: str) -> str:
    """
    Ensure outer <td align="center"> has padding: 0 10px for mobile side margins.
    This is the wrapper around the main 600px table.
    """
    # Find the pattern: <td align="center"> that wraps the main table
    # It's usually right after the 100% width table
    pattern = r'(<td\s+align="center"[^>]*?>)'
    
    def add_padding(match):
        tag = match.group(1)
        # Check if already has style with padding
        if 'style=' in tag:
            if 'padding' not in tag.lower():
                # Add padding to existing style
                tag = re.sub(
                    r'style="([^"]*)"',
                    r'style="padding: 0 10px; \1"',
                    tag
                )
        else:
            # Add style attribute
            tag = tag.replace('>', ' style="padding: 0 10px;">')
        return tag
    
    content = re.sub(pattern, add_padding, content, flags=re.IGNORECASE)
    return content

def ensure_container_fluid(content: str) -> str:
    """
    Critical fix: Add max-width: 600px; width: 100%; to the main container table.
    This is what makes emails responsive on mobile.
    """
    # Target the 600px width table (main container, not the outer 100% table)
    pattern = r'(<table\s+width="600"[^>]*?style=")([^"]*?)(")'
    
    def fix_style(match):
        before = match.group(1)
        style = match.group(2)
        after = match.group(3)
        
        # Add max-width if missing
        if 'max-width' not in style.lower():
            style = 'max-width: 600px; ' + style
        
        # Replace any width value with 100%
        if 'width:' in style.lower():
            style = re.sub(r'width:\s*[^;]+;?', '', style, flags=re.IGNORECASE)
        style = 'width: 100%; ' + style
        
        # Clean up extra spaces
        style = re.sub(r'\s+', ' ', style).strip()
        
        return f'{before}{style}{after}'
    
    content = re.sub(pattern, fix_style, content, flags=re.IGNORECASE)
    
    # Handle case where table width="600" has NO style attribute
    pattern_no_style = r'(<table\s+width="600"[^>]*?)(?<!style=")(\s*>)'
    
    def add_style(match):
        before = match.group(1)
        closing = match.group(2)
        
        # Check if style already exists
        if 'style=' not in before:
            return f'{before} style="max-width: 600px; width: 100%;"{closing}'
        return match.group(0)
    
    content = re.sub(pattern_no_style, add_style, content, flags=re.IGNORECASE)
    
    return content

def adjust_paddings_responsive(content: str) -> str:
    """
    Adjust paddings to mobile-friendly values.
    Seminary responsive rules without media queries.
    """
    # Header: 24px 40px -> 24px 20px (keep vertical, reduce horizontal)
    content = re.sub(
        r'(style="[^"]*?)padding:\s*24px\s+40px',
        r'\1padding: 24px 20px',
        content,
        flags=re.IGNORECASE
    )
    
    # Hero/Content: 32px 40px -> 30px 20px
    content = re.sub(
        r'(style="[^"]*?)padding:\s*32px\s+40px',
        r'\1padding: 30px 20px',
        content,
        flags=re.IGNORECASE
    )
    
    # Main content: 40px alone -> 30px 20px
    content = re.sub(
        r'(style="[^"]*?)padding:\s*40px(?=\s*;)',
        r'\1padding: 30px 20px',
        content,
        flags=re.IGNORECASE
    )
    
    # Footer: 20px 40px -> 20px
    content = re.sub(
        r'(style="[^"]*?)padding:\s*20px\s+40px',
        r'\1padding: 20px',
        content,
        flags=re.IGNORECASE
    )
    
    return content

def fix_image_responsiveness(content: str) -> str:
    """
    Make all images responsive with proper inline styles.
    Critical for mobile display.
    """
    pattern = r'<img([^>]*)>'
    
    def fix_img(match):
        img_attrs = match.group(1)
        
        # Check if style attribute exists
        style_match = re.search(r'style="([^"]*)"', img_attrs)
        
        required_styles = {
            'max-width': '100%',
            'height': 'auto',
            'display': 'block'
        }
        
        if style_match:
            existing_style = style_match.group(1)
            style_parts = [s.strip() for s in existing_style.split(';') if s.strip()]
            
            # Parse existing styles
            style_dict = {}
            for part in style_parts:
                if ':' in part:
                    key, value = part.split(':', 1)
                    style_dict[key.strip().lower()] = value.strip()
            
            # Add missing required styles
            for key, value in required_styles.items():
                if key not in style_dict:
                    style_dict[key] = value
            
            # Rebuild style string
            new_style = '; '.join([f'{k}: {v}' for k, v in style_dict.items()])
            img_attrs = img_attrs.replace(f'style="{existing_style}"', f'style="{new_style}"')
        else:
            # No style attribute, add one
            style_string = '; '.join([f'{k}: {v}' for k, v in required_styles.items()])
            img_attrs = f'{img_attrs} style="{style_string}"'
        
        return f'<img{img_attrs}>'
    
    content = re.sub(pattern, fix_img, content, flags=re.IGNORECASE)
    return content

def fix_table_width_attribute(content: str) -> str:
    """
    Important: Keep width="600" attribute but ensure style overrides it for mobile.
    The width attribute is for Outlook, the style is for web/mobile.
    """
    # This function ensures we don't accidentally remove width="600"
    # It's needed for Outlook compatibility
    return content

def process_file(path: str) -> Tuple[bool, List[str]]:
    """
    Process a single HTML file and apply all responsive fixes.
    """
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()
    
    content = original
    changes = []
    
    # 1. Fix outer wrapper padding (critical for mobile margins)
    new_content = ensure_parent_td_padding(content)
    if new_content != content:
        changes.append("✓ Added mobile side margins (padding: 0 10px)")
        content = new_content
    
    # 2. Fix main container width (MOST CRITICAL)
    new_content = ensure_container_fluid(content)
    if new_content != content:
        changes.append("✓ Made container fluid (max-width: 600px; width: 100%)")
        content = new_content
    
    # 3. Adjust all paddings for mobile
    new_content = adjust_paddings_responsive(content)
    if new_content != content:
        changes.append("✓ Adjusted paddings for mobile screens")
        content = new_content
    
    # 4. Make images responsive
    new_content = fix_image_responsiveness(content)
    if new_content != content:
        changes.append("✓ Made all images responsive")
        content = new_content
    
    # Save if any changes were made
    if content != original:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        return True, changes
    
    return False, []

def main() -> None:
    """
    Process all HTML files in ENKKI directory.
    """
    if not os.path.exists(ENKKI_ROOT):
        print(f"❌ Error: Directory '{ENKKI_ROOT}' not found!")
        print(f"   Please ensure ENKKI folder exists at: {os.path.abspath(ENKKI_ROOT)}")
        return
    
    print("🔍 Scanning HTML files in ENKKI directory...")
    print(f"   Path: {os.path.abspath(ENKKI_ROOT)}\n")
    
    updated_files = []
    total_files = 0
    
    for root, _dirs, files in os.walk(ENKKI_ROOT):
        for name in files:
            if name.lower().endswith(".html"):
                total_files += 1
                path = os.path.join(root, name)
                modified, changes = process_file(path)
                
                if modified:
                    updated_files.append((path, changes))
    
    # Display results
    print("=" * 70)
    print(f"📊 Processing Summary")
    print("=" * 70)
    print(f"Total HTML files found: {total_files}")
    print(f"Files updated: {len(updated_files)}")
    print(f"Files already responsive: {total_files - len(updated_files)}\n")
    
    if updated_files:
        print("📝 Detailed Changes:\n")
        for path, changes in updated_files:
            rel_path = os.path.relpath(path, ENKKI_ROOT)
            print(f"📄 {rel_path}")
            for change in changes:
                print(f"   {change}")
            print()
    else:
        print("✅ All files are already responsive!")
        print("   No changes needed.\n")
    
    print("=" * 70)
    print("\n💡 Testing Tips:")
    print("   1. Upload template to Apollo.io")
    print("   2. Send test email to yourself")
    print("   3. Check on mobile device")
    print("   4. Main container should be full-width on mobile")
    print("   5. Images should scale proportionally")
    print("=" * 70)

if __name__ == "__main__":
    main()