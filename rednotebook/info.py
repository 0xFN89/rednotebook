from __future__ import with_statement
import os
from rednotebook.util import filesystem

version = '0.5.2'
author = 'Jendrik Seipp'
authorMail = 'jendrikseipp@web.de'
url = "http://rednotebook.sourceforge.net"
developers = 	['Jendrik Seipp <jendrikseipp@web.de>',
				'Alexandre Cucumel <superkiouk@gmail.com>',
				]
comments = '''\
RedNotebook is a graphical diary and journal to keep track of notes and \
thoughts throughout the day. It includes a calendar navigation, customizable \ 
templates for each day, export functionality and a keyword search and cloud. \
'''

licenseText = '''\
Copyright (C) 2008  Jendrik Seipp

RedNotebook is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

RedNotebook is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with RedNotebook; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
            
completeWelcomeText = '''\
Hello, 
this is the RedNotebook, a desktop diary. Thank you very much for giving it a try.
The text field containing this text is the container for your normal diary entries like this one: 

Today I went to a //pet shop// and bought a **tiger**. Then we went to the --pool-- park and had a nice time playing \
ultimate frisbee. Afterwards we watched "__Life of Brian__".

=== Format ===
As you can see you can format your text **bold**, //italic//, --stricken-- and __underlined__. \
To see the results, just click on the "Preview" tab.

=== Extra Content ===
On the right there is space for extra content, things that can easily be sorted into categories. \
For example you could add the category Ideas and then add your ideas \
of that day to it. On the right you can see what that looks like.

=== Templates ===
RedNotebook supports a template system: In the directory "''' + filesystem.templateDir + '''" you find seven \
text files. One for each day of the week. You can edit those files \
with your favourite text editor and the text for a given weekday will be inserted when you press the button \
"Insert Template".

=== Tags ===
Tagging an entry (e.g. with the tag "Work") is also easy: On the right, click on "New Entry" and insert "Tags" \
and "Work" into the dialog. 

=== Search ===
On the left you find the fancy search field. You can search for text, display a \
category's content or show all days with a given tag.

=== Save and Export ===
Everything you enter will be saved automatically when you exit the program. If you want to double check you can save \
pressing "Strg-S" or using the menu entry under "File" in the top left corner. "Backup" saves all your entered data in a \
zip file. In the same menu you also find an "Export"-Button. \
Click on it and export your diary to Plain Text, HTML, Latex or PDF (Linux only, see Help for instructions).

=== Help ===
Now you can erase this help text and enter e.g. what you have done today. To read the instructions again, \
go to "Help -> Help" in the menu bar.

There are many features I have planned to add in the future so stay tuned.
I hope you enjoy the program!'''
            
welcomeHelpText = '''\
Hello, 
this is the RedNotebook, a desktop diary. This program helps you to keep track of your activities and thoughts. \
Thank you very much for giving it a try.
'''

dayEntryHelpText1 = '''\
The text field in the middle is the container for your normal diary entries like this one: 

'''

dayEntryHelpText2 = '''\
Today I went to a pet shop and bought a tiger. 
Then we went to the park and had a nice time playing ultimate frisbee. 
Afterwards we watched "Life of Brian".'''

dayEntryHelpText = dayEntryHelpText1 + dayEntryHelpText2

categoriesHelpText1 = '''\
On the right there is space for extra content, things that can easily be sorted into categories. \
Those entries are shown in a tree. For example you could add the category Ideas and then add an \
entry which reminds you of what your idea was about:'''

categoriesHelpText2 = '''\
> Ideas
  Invent Anti-Hangover-Machine
  
In addition you could add

> Cool Stuff
  Went to see the pope
'''

categoriesHelpText3 = '''
for the really cool things you did that day. On the right panel you control everything with right-clicks. Click either \
on the white space or on existing categories.'''

categoriesHelpText = categoriesHelpText1 + '\n\n' + categoriesHelpText2 + '\n' + categoriesHelpText3

templateHelpText = '''\
RedNotebook supports a template system: In the directory "''' \
        + filesystem.templateDir + '''" you find seven text files. One for each day of the week. You can edit those files \
with your favourite text editor and the text for a given weekday will be inserted when you press the button \
"Insert Template".'''

automaticSavingHelpText = '''\
Everything you enter will be saved automatically when you exit the program. If you want to double check you can save \
pressing "Strg-S" or using the menu entry under "File" in the top left corner. "Backup" saves all your entered data in a \
zip file. After pressing the button you can select a location for that.'''

goodbyeHelpText = '''\
Now you can erase this help text and enter what you have done today. To read the instructions again, press "F1" or \
go to "Help -> Show Help" in the menu bar.

There are many features I have planned to add in the future so stay tuned.
I hope you enjoy the program!'''

#completeWelcomeText = welcomeHelpText + '\n' + dayEntryHelpText + '\n\n' + categoriesHelpText + '\n\n' + templateHelpText + \
#                        '\n\n' + automaticSavingHelpText + '\n\n' + goodbyeHelpText
                        
exportHelpText = '''\
To export your entries click on Export in the File Menu. Then you can select a format and the range of dates to export.
Available formats are: Plain Text, HTML and Latex.

<p><b>Linux</b></p>

<p>If you are on Linux, you can also export your diary directly to PDF. All you have to do is to install the packages \
texlive-latex-base and texlive-latex-recommended. Those contain the pdflatex program and are available in the \
repositories of most Linux distros.</p>

<p>However there are some pitfalls: Not all characters can be exported to pdf. E.g. problems occur when exporting \
the euro sign or other "non-standard" characters to pdf.</br>
When you export to PDF, RedNotebook will create a Latex file (.tex) and then make an attempt to convert that file to pdf \
using pdflatex. If the .tex file contains odd characters this might or might not fail. Most of the time a pdf is created \
even if RedNotebook tells you that an error occured.</p>

<p><b>Windows</b></p>

<p>Windows users cannot export directly to pdf as of now. However you can open an exported \
Latex file with Texniccenter and MikTex and export it to pdf (Look over at www.toolscenter.org and www.miktex.org \
for programs and instructions).</p>
'''

headerType = 'h4'

htmlHelp = '''\
<html>

<body bgcolor="#ababab">
<h3>Table of Contents</h3>

<ul>
<li><a href="#dayEntries">Day Entries</a></li>
<li><a href="#categories">Category Entries</a></li>
<li><a href="#templates">Templates</a></li>
<li><a href="#saving">Automatic Saving</a></li>
<li><a href="#saving">Export</a></li>
</ul>

<p>
<a name="dayEntries">
<'''+headerType+'''>Day Entries</'''+headerType+'''>''' + dayEntryHelpText1 + '''<pre>''' + dayEntryHelpText2 + '''</pre>''' + '''\
</a>
</p>

<p>
<a name="categories">
<'''+headerType+'''>Category Entries</'''+headerType+'''>''' + categoriesHelpText1 + \
'''<pre>''' + categoriesHelpText2 + '''</pre>'''+ categoriesHelpText3 + '''\
</a>
</p>

<p>
<a name="templates">
<'''+headerType+'''>Templates</'''+headerType+'''>''' + templateHelpText + '''\
</a>
</p>

<p>
<a name="saving">
<'''+headerType+'''>Automatic Saving</'''+headerType+'''>''' + automaticSavingHelpText + '''\
</a>
</p>

<p>
<a name="saving">
<'''+headerType+'''>Export</'''+headerType+'''>''' + exportHelpText + '''\
</a>
</p>

</body>
</html>
'''