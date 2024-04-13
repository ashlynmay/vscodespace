/* similar to c Syntax 
runs client side, variables are similar to python with no type selector, can behave like an object-oriented language
var variable = data; 
conditionals: if, elseif, else, switch, ?: are included
loops: while, do-while, for
functions: function name() {}, some functions can be anonymous (no name)
arrays: var nums = [1, 2, 3, 4, 5];
        var mixed = [1, true, 3.333, 'five'];

objects/structs: instead of function(object); do object.function();
        var herbie = {year : 1963, model: 'Beetle'};

loops: 
    var wkArray = ['Monday', 'Tuesday', ... 'Sunday'];

        for (var day in wkArray)
        {
            console.log(day);  (printf)
        }
    output: 
        0,1,2,3,4,5,6

        for (var day of object)
        {
            console.log(day);
        }
    output: Monday, Tuesday, ... Sunday

printing:
        console.lot(wkArrary[day] + ' is day number ' + (parseInt(day) + 1) + ' of the week! ');
    output: Monday is day number 1 of the week!

if adding a variable and a number, use parseInt(var)

arrays:
        array.size();
        array.pop();
        array.push(x);
        array.shift();
        map(); can be used to apply a function to all elements in an array, good time to use anonymous functions

anonymous function:
        var nums = [1,2,3,4,5];
    
    nums = nums.map(function(num) {
        return num * 2;
    });

events:
    an event in HTML and JavaScript is a response to user interaction with the web page.w
    JavaScript has support for event handlers, which are callback functions that respond to HTML events.

    event in html: <button onclick="alertName(event)">Button</button>

    function alertName(event)
    {
        var trigger = event.srcElement;
        alert('You clicked on ' + trigger.innerHTML);
    }
    output: 


<script>include js in html</script>
<link> rel="script" href="script.js"</link>
*/