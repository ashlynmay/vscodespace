/*
dom stands for document object model
javascript objects allow you to nest other objects inside them.
the document object allows u to organize the entire content of a webpage as an object
this allows you to manipulate the pages elements programmatically

example html:
    <html>
        <head>
            <title>Hello, world</title>
        </head>
        <body>
            <h2>Here's my page</h2>
            <p id="greeting">World, hello</p>
            <a href="test.html">Link</a>
        </body>
    </html>

see DOM:
    open developer console and run console.dir(document), and check children 

major dom properties:
    innerHTML: html inside of tags. ex: <title> would be Hello, world
    nodeName: name of an HTML element, <title> would be title
    id: id attribute of an HTML element. <p id="greeting"> would be greeting
    parentNode: reference to node one level up: <
*/
