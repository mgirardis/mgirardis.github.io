import os
import re

filename = 'D:/Dropbox/p/documentos/curriculum_vitae/template03_overleaf_em_uso/cv_en-US.tex'
f = open(filename,'r',encoding='utf-8')
d = f.readlines()
f.close()

def find_first_line(text,line_list,start_line=0,case_sensitive=True):
    if case_sensitive:
        compare_func = lambda txt,line: txt in line
    else:
        compare_func = lambda txt,line: txt.lower() in line.lower()
    for k,l in enumerate(line_list[start_line:]):
        if compare_func(text,l):
            return start_line + k
    return -1

def get_closing_line(node_type,line_list,start_line=0):
    node_type = node_type.lower()
    all_node_types = [ 'part','chapter','section','subsection','subsubsection' ]
    assert node_type in all_node_types, 'Invalid node_type'
    k = 1 + all_node_types.index(node_type)
    correct_value = lambda v: v if v > -1 else float('inf')
    return int(min([ correct_value(find_first_line('\\' + n,line_list,start_line=start_line+1,case_sensitive=False)) for n in all_node_types[:k] ]))

def get_start_line(node_type,line_list,title=''):
    all_node_types = [ 'part','chapter','section','subsection','subsubsection' ]
    assert node_type in all_node_types, 'Invalid node_type'
    found      = False
    start_line = -1
    while not found:
        start_line = find_first_line('\\' + node_type,line_list,start_line=start_line+1,case_sensitive=False)
        if start_line == -1:
            return -1
        if len(title) > 0:
            if title in line_list[start_line]:
                return start_line
        else:
            return start_line
    return -1

def get_section(title,line_list):
    start_line = get_start_line('section',line_list,title=title)
    if start_line == -1:
        return []
    end_line = get_closing_line('section',line_list,start_line=start_line)
    return line_list[start_line:end_line]

def get_subsection(title,line_list):
    start_line = get_start_line('subsection',line_list,title=title)
    if start_line == -1:
        return []
    end_line = get_closing_line('subsection',line_list,start_line=start_line)
    return line_list[start_line:end_line]


def get_all_node_lines(node_name,line_list):
    nl = []
    for l in line_list:
        if f'\\{node_name}'.lower() in l.lower():
            nl.append(l)
    return nl

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"

def clean_bibstring(text):
    escapes    = ''.join([chr(char) for char in range(1, 32)])
    translator = str.maketrans('', '', escapes)
    return text.replace("{", "").replace("}","").replace("\\","").translate(translator)

def get_latex_url(text):
    try:
        r = text.split(r'\url{')[1].split('}')[0]
    except IndexError:
        r = ''
    return r


is_single_year = lambda s: (len(s) <= 4) and (not ('-' in s))


cventries = get_all_node_lines('cventry', get_subsection('Outreach',d))

loc_dict = {}

talk_month = "01"
talk_day = "01"

talk_type = 'Community outreach and interviews'

for row, cventry in enumerate(cventries):

    item = [ clean_bibstring(s) for s in cventry.split('{')[1:] if len(clean_bibstring(s)) > 0 ]
    # item 0 -> year (or year range)
    # item 1 -> title
    # remaining -> venue
    talk_year  = item[0] if is_single_year(item[0]) else item[0].split('-')[0]
    talk_title = item[1].replace("{", "").replace("}","").replace("\\","")
    talk_venue = ', '.join(item[2:])
    talk_url   = get_latex_url(cventry)

    clean_title = talk_title.replace(" ","-")
    url_slug    = re.sub("[^a-zA-Z0-9_-]", "", clean_title)
    url_slug    = url_slug.replace("--","-")

    talk_date = talk_year+"-"+talk_month+"-"+talk_day

    md_filename   = (str(talk_date) + "-" + url_slug + ".md").replace("--","-")
    html_filename = (str(talk_date) + "-" + url_slug).replace("--","-")
    
    md = "---\ntitle: \""      + talk_title + '"\n'
    md += "collection: talks"  + "\n"
    md += 'type: "'            + talk_type + '"\n'
    md += "permalink: /talks/" + html_filename + "\n"
    md += 'venue: "'           + talk_venue + '"\n'
    md += "date: "             + talk_date + "\n"
    if not is_single_year(item[0]):
        md += 'location: "'    + item[0] + '"\n'   
    md += "---\n"
    
    
    if len(talk_url) > 3:
        md += "\n[See more here](" + talk_url + ")\n" 
        
    md_filename = os.path.basename(md_filename)
    #print(md)
    
    with open("../_talks/" + md_filename, 'w', encoding='utf-8') as f:
        f.write(md)