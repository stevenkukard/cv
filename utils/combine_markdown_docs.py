import os

def remove_front_matter(text):
    lines = text.split('\n')
    if lines[0].strip() == '---':
        end_front_matter = lines.index('---', 1)
        return '\n'.join(lines[end_front_matter+1:])
    return text

def remove_slash_in_front_of_assets(text):
    lines = text.split('\n')
    for i in range(len(lines)):
        if lines[i].startswith('/assets'):
            lines[i] = lines[i][1:]
    return '\n'.join(lines)

def combine_markdown_files(list_of_markdown_files, output_file):
    with open(output_file, 'w') as outfile:
        outfile.write("---\nlayout: print\n---\n\n")
        outfile.write("# Steven Kukard's CV \n\n [stevenkukard@gmail.com](mailto:stevenkukard@gmail.com) \n\n **Note** \n\n *This document is a print version of my online CV, which can be viewed at [cv.stevenknightkukard.com](https://cv.stevenknightkukard.com).* \n\n")
        for filename in list_of_markdown_files:
            with open(filename, 'r') as infile:
                content = infile.read()
                cleaned_content = remove_front_matter(content)
                cleaned_content = remove_slash_in_front_of_assets(cleaned_content)
                section_heading = section_headings_dict[filename]
                outfile.write('# ' + section_heading + '\n\n')
                outfile.write(cleaned_content + '\n\n')
                if filename != list_of_markdown_files[-1]:
                    outfile.write('<div style="page-break-after: always"></div>')
                    outfile.write('\n\n')
        outfile.write("\n---\n[stevenkukard@gmail.com](mailto:stevenkukard@gmail.com)")

# Usage
list_of_markdown_files = ['index.markdown', 'experience.markdown', 'projects.markdown', 'skills.markdown', 'education.markdown']
list_of_section_headings = ['Introduction', 'Experience', 'Projects', 'Skills', 'Education']
section_headings_dict = dict(zip(list_of_markdown_files, list_of_section_headings))
output_file = 'combined.markdown'
combine_markdown_files(list_of_markdown_files, output_file)
