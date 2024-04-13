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
    parentNode: reference to node one level up: <title> would return <head>
    childNodes: array of references to the nodes on level down: <body> would return [h2, p, a]
    attributes: array of attributes of an html elements
    style: object containing the css/html styling of an element.

major dom methods:
    getElementById(id): self explanitory. keep in mind the d in Id is lowercase
    getElementsByTagName(tag): gets all elements with given tag below this point in the dom as an array
    appendChild(node): add the given node ot the dom below this point
    removeChild(node): removes the specified child node from the DOM

jquery:
    a popular open source library that is supposed to simplify client-side scripting (such as dom manipulations and ajax querys)
    document.getElementById('colorDiv).style.backgroundColor = 'green' in pure JS
    $('#colorDiv').css('background-color', 'green'); in jquery


change color of element to purple:
    in js:
        html: <button onclick="turnPurple();">Purple</button>
*/

