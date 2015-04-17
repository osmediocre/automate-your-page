# Updated list HTML generator code to generate slightly different HTML based on the contents
# of each list. Allows for lesson breaks, etc...
def generate_concept_HTML1(lesson,concept_title, concept_description):
    html_text_1 = '''
<div class="lesson">
    <div class="concept-description">
        ''' + '<h2>' + lesson + '</h2>'
    html_text_2 = '''
    </div>
    <div class="concept">
    <div>'''
    html_text_3 = '''
    <div class="concept-title">
    ''' + concept_title
    html_text_4 = '''
    </div>
    <p>''' + concept_description + '''</p>
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text
def generate_concept_HTML2(concept_title, concept_description):
    html_text_1 = '''
    <div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''

    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text
def generate_concept_HTML3(end_lesson):
    html_text = '''
    </div>
    </div>'''
    return html_text

# Generates breaks based on the length of the concept - if it contains the lesson header
# it will break up that box accordingly
def make_HTML(concept):
    if len(concept) == 3:
        lesson = concept[0]
        concept_title = concept[1]
        concept_description = concept[2]
        return generate_concept_HTML1(lesson, concept_title, concept_description)
    if len(concept) == 1:
        end_lesson = concept[0]
        return generate_concept_HTML3(end_lesson)
    else:
        concept_title = concept[0]
        concept_description = concept[1]
        return generate_concept_HTML2(concept_title, concept_description)


SESSION_NOTES =              [ ['Lesson 1: The Basics of the Web and HTML','World Wide Web:','The World Wide Web is made up of a collection of HTML documents. We use <b>H</b>yper<b>T</b>ext <b>T</b>ransfer <b>P</b>rotocol (<b>HTTP</b>) to request and download (view) these <em>web pages</em> from a server to our local machines.'],
                             ['HTML:', '<b>H</b>yper<b>T</b>ext <b>M</b>arkup <b>L</b>anguage is the most common document type on the internet. This is the <em>heart</em> of the web essentially. The documents are made up of text, links and markup language used to change the look and layout of the web page.'],
                             ['HTML Tags:', 'HTML Tags are used to change text formatting (e.g. making certain text bold or italicized), to embed images, to link to other HTML <a href="https://www.youtube.com/watch?v=tntOCGkgt98">pages</a> or other functions. These tags use "&lt;" and "&gt;" to perform these functions as web browsers like Chrome, Firefox or Internet Explorer are programmed to carry out the instructions that the tags indicate. An instruction such as &lt;b&gt;BOLD&lt;/b&gt; would instruct the browser to display the text as <b>BOLD</b>.</p><p><em><b>Inline</b></em> HTML elements such as &lt;br&gt; will simply end a line, while <em><b>Block</b></em> elements essentially draw a box around the text from the beginning of the tag (e.g. &lt;p&gt;) to the end of a tag (e.g. &lt;/p&gt;), affecting all text in between. These "boxes" may have attributes like height or width that will affect how the text is displayed inside.</p><p>Computers are "<em>stupid</em>" in a sense that they need very specific instructions to carry out simple tasks, but when proper <em><b>syntax</b></em> is used the machine can carry out a given task far faster than any human. Incomplete tags such as &lt;b&gt;Text... will affect your entire document if not ended in the proper place by placing a corresponding &lt;/b&gt; tag.'],
                             ['Lesson 2: Creating a Structured Document with HTML','Developer Tools:','Many commercially available browers have a "<b>Developers Tools</b>" option that lets you see behind the curtain to the underlying HTML & CSS code that binds the page together. HTML block elements within elements are seen here as creating a tree structure of the page, making visible drill-downs for you to see the invisible boxes that are created by using the HTML block elements such as &lt;div&gt; or &lt;p&gt;.'],
                             ['HTML "boxes":', 'The invisible "boxes" inserted around indented HTML elements can each have attributes that change the way that they behave based on the type of "class" they are given. Some boxes may contain text formatting attributes while others may change the width of the paragraph - and all of these may be nested in each other to change attributes all the way down the HTML subtree.'],
                             ['Text Editors:','Offline text editing tools such as <b>Sublime Text</b> allow you to switch syntax on the fly from plain text to HTML or CSS in order to better visualize the programming process and keep track of markup.'],
                             ['end lesson'],
                             ['Lesson 3: Adding CSS Style to HTML Structure','CSS:','CSS stands for <b>C</b>ascading <b>S</b>tyle <b>S</b>heets. These are typically separate files referenced in the HTML "head" that give a web page a specific look and layout. "Cascading" refers to the way that the styles will affect all classes of a specific type as definied in the CSS file. For example: all elements under &lt;div class="example"&gt; may have all text in red. This helps to avoid redundancy in programming.'],
                             ['Positioning HTML Boxes:','One of the more difficult aspects of HTML coding is positioning of the invisible content boxes that fill a web page. Normally boxes will fill up the width of a browser but one powerful CSS rule, "<em>display: flex</em>" will allow you to position these content boxes side-by-side to create more flexibility in your design.'],
                             ['Box borders, padding, margins...','The versatility of CSS lets us make endless useful changes to each element box on the screen; adding outer margins to push out surrounding boxes, creating padding around the box contents, changing border attributes (such as "border-radius" to give a round edge to the box) and more!'],
                             ['Code, Test, Refine:','When starting from scratch on a project, you will likely follow the same pattern of Coding, Testing and then Refining the product until it is complete.</p><p>A good place to start is by "boxifying" the elements of the webpage - look for "Natural Boxes" where elements should be divided to present a neat layout. After laying out the obvious boxes, we should look for repeated styles where CSS can help us display all similar types of information in a complementary style. It is here where we can start writing our HTML (or coding) and applying all styles to the page.</p><p>After testing in one web browser, continue to test across platforms to make sure that the layout is as intended - refining as needed until it meets the design criteria.'],
                             ['end lesson'],
                             ['Lesson 4: Introduction to "Serious" Programming','Programming Language:','As we know, computers need a specific set of instructions to carry out a desired function. A computer can do many things, but it is limited in the sense that you need to know how to speak to the machine. Programming languages such as FORTRAN, COBOL, Python, etc act as an interface of sort with the machine - giving users a set of grammer rules that will be translated into a language that the machine can understand.'],
                             ['Python Expressions:','An expression in Python is a statement that will produce an output if the syntax is correct. This can be a simple equation or series of nested calculations that will provide a complex answer, either way Python needs to make sense of it.</p><p>If you were to give Python a command statement such as <span class="code">print 1 + 1</span>, the interpreter would look at the statement, break it down into "expression operator expression" format and it would be determined valid. An open-ended statement such as <span class="code">print 1 +</span> does not follow the "expression operator expression" model, and Python does not know what to do with this.</p><p>Just like we need to use proper grammar to convey our message to other people properly, programming languages have their own grammar rules that need to be followed. Computers are much more strict on the commands than we might be for missed punctuation or spelling errors.'],
                             ['Computer Programs:','Computer programs such as <b>Sublime Text 2</b> or <b>Firefox</b> are created in a programming language and carry out a specific task each time the program is opened. They build upon an existing structure, typically running inside of another computer program such as <b>Windows 7</b> that provides the basic framework within which they can function. It may be a game that needs access to your video card hardware, an office suite that needs access to mouse and keyboard hardware, or just simply any program that needs to output visuals to your monitor. Programs work together to tell the computer what we want to hear, see and do.'],
                             ['end lesson'],
                             ['Lesson 5: Variables and Strings','Variables:','Variables are, as the name suggests, a variable value that can be stored and called upon by the program at a later point. Instead of using the <span class="code">print</span> command to display a lengthy number, perhaps you can assign the value of 99999999980 to a variable called <span class="code">long</span> and help save some typing every time you want to refernce that number.</p><p>Instead of invoking an algebraic expression, in programming the "="(equals) sign tells the interpreter or compiler to assign a value of whatever comes after "=" to the name on the left of the symbol. Thus, <span class="code">long = 99999999980</span> would assign the value of 99999999980 to the variable <span class="code">long</span> to be called upon later.'],
                             ['Strings:','Strings in Python terms are a sequence of characters (letters, numbers, symbols) within closed quotations - single quotes or double quotes - as long as your opening quotation is the same as the closing. "Hello World" is an example of a valid string in Python.</p><p>Because words like <span class="code">long</span> can be used to define and conjure variables in coding, strings must be defined within this quotation system to differentiate from the commands and variables set up in the system. <span class="code">print Hello</span> would therefore have a very different effect than if you typed out <span class="code">print "Hello"</span> for example, as the system expects a variable in the first instance - which may or may not already be defined.'],
                             ['end lesson'],
                             ['Lesson 6: Function -> Output','Functions:','Functions (or procedures) are defineable expressions in programming that let you carry out a sequence of commands when called upon and provided with the appropriate amount of input.</p><p>Example: if I wanted to allow a user to input any number to be added to another number, I might want to make a function that could take these inputs and apply a rule to those in order to get the expected output.</p><p>First we need to <b>make</b> the function by defining it:<br><span class="code">def sum(n1,n2):<br>return n1 + n2<br></span>Then we need to <b>use</b> the function by invoking it with the appropriate amount of inputs:<br><span class="code">print sum(1, 1)</span><br>We should see the output of "2" in this example, but as the function has been defined we can give it any two numbers and it will still be able to give us an output of the sum. As you can imagine, this can cut down greatly on repetition.'],
                             ['Inputs and Outputs:','An Input in function terms is anything that we are giving to the program to help it carry out its task. It may be a static number or string that we are using, or provided via variables affected by a third partys feedback.</p><p>Output is simply anything that is being passed out by a function or expression that may be <span class="code">print</span>ed to the users screen or simply passed through as input to another function or expression.'],
                             ['end lesson'],
                             ['Lesson 7: Decisions and Repetition: If and While','If Statements:','"If" statements in Python (and other languages) allow you to make a test that when found true can trigger other functions or expressions to alter the input and output of your program.</p><p>Example: you may allow 2 inputs and write an "if" statement to test if the first number is larger or not. You may want to test whether a persons name is a specific value and take an action if the output is true. Or you can use "if" along with other nested expressions to perform a series of tests all within a single statement.'],
                             ['Or:','The "or" function will pass through a value of "True" if any of the expressions evaluates to "True". For example, you may want to test if a name starts with an "S" <em>or</em> a "T". <span class="code">return name[0] == "S" or name[0] == "T"</span> - with an input of "Terry", the first part returns "False", but since the second expression is "True" the whole statement returns a "True" value.'],
                             ['While Loops:','While loops allow you to continue testing an expression as long as the expression is true. Thus, you may be able to run an "if" statement indefinitely as long as what passes through is "True" according to the guidelines you established in the loop.</p><p>Example: <span class="code">while i&lt;10:</span> may be established as a rule to continually run the test in the indented block below "while" as long as i is less than 10.</p><p>Loops are at the heart of many complicated programs, and buggy code can lead to crashing systems when the computer cannot find its way out of an "infinite" loop.'],
                             ['end lesson'],
                             ['Lesson 8: Debugging','Bugs:','Bugs are simply problems with your code. They could be inherited problems with copied code that doesnt work properly, simple syntax issues or major systemic problems that affect many processes throughout your program. Since computers are "stupid" in the sense that they need very specific instructions to carry out a function, it could be any number of issues that lead to the bug.</p><p>Thankfully most compilers and interpreters have a robust "debugging" evaluation of where errors were encountered that will help you locate and fix the problem.'],
                             ['Debugging:','If you do encounter a problem with your program, the compiler or interpreter will almost always help you find where the error happened. This is a good place to start when debugging, as you can work your way back through the error logs and pinpoint what is hanging the process.</p><p>If after working and re-working your code you are still having problems running the program, it isnt always a great idea to completely scrap the code altogether. Try hashing out the lines (<span class="code"># symbols will tell Python to ignore the line and skip over to the next line</span>) that dont work and try a different approach. You can always return to that place later or start with a working example that may help you figure out where your code is going wrong.'],
                             ['end lesson'],
                             ['Lesson 9: Structured Data - Lists and For Loops','Lists:','Just as you can assign a single value to a variable, you can also assign a multitude of values (including lists within lists) to a variable that can be indexed and manipulated.</p><p>Referencing <span class="code">list[0]</span> would, for example call out the first value in the list.'],
                             ['For Loops:','For loops allow you to navigate through a list, executing commands or making tests against the contents just like you might do in a <span class="code">while loop</span>.</p><p>You can also search through a list with a <span class="code">for loop</span> like you would with a <span class="code">find</span> command to return the position in the list of the string or value given.'],
                             ['end lesson'],
                             ['Lesson 10: How to Solve Problems','Where to begin:','One of the biggest challenges to writing code from scratch is knowing where to begin. With a fresh, clean slate it may be a daunting task to write code to solve a specific problem, so perhaps the best way to start is to make sure you understand the problem at its core.</p><p>To "understand the problem", we need to be able to define the set of inputs we will be working with as well as their relationship to the desired outputs that we want from our program. Without a solid understanding of what the question/problem is we will not be starting with the best groundwork.'],
                             ['Solving the Problem:','Once we understand what the problem is and what the expected inputs/outputs are, we can start working through some examples to systematically break down our problem into bite-sized pieces.</p><p>Pseudocode is just a logical breakdown of the problem without proper programming syntax that helps us start to form the idea of how we want to tackle the problem. It may not work in any given programming language to produce results, but is often a good general place to start that can be modified into working code when logically sound.</p><p>The first place to start should often be the place that gives you a good estimated result. If you start in a place where you can get an approximated answer, the rest of the elements and fringe examples can be added into the code piecemeal to provide accurate results given any input.'],
                             ['What Should We Do Next?:','With any complex problem any bit of progress is good - so you will want to make sure to break up your big problems into smaller pieces that can be tested, and so that you also know what each small piece of code does as part of the whole.</p><p>With really complex problems sometimes it is a good idea to work on the smaller pieces first. For example if you have a small function that uses a complex function as part of its process, you can work out the code for that smaller function first and it will not (in many cases) need to be changed when you have to work out the complex procedures of the bigger function.</p><p>One thing we do need to realize when breaking up a problem into pieces is that our need for testing each point becomes more critical the more elements we bring into our process. After writing an element we should be actively testing that element as part of the whole.']]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for e in list_of_concepts:
        current = make_HTML(e)
        HTML = HTML + current
    return HTML


print make_HTML_for_many_concepts(SESSION_NOTES)