from googletrans import LANGUAGES

languages_dict = {code: name for code, name in LANGUAGES.items()}

# Generating HTML code for the dropdown list
html_code = """
<label for="language-select">Select a language:</label>
<select id="language-select">
  <option value="">Select a language</option>
  {options}
</select>
"""

options_html = ""
for code, name in languages_dict.items():
    options_html += f"<option value='{code}'>{name.capitalize()}</option>"

html_code = html_code.format(options=options_html)

# Printing the generated HTML code
print(html_code)
