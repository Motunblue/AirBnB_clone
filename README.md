<h3>Welcome to the AirBnB clone project!</h3>

<p>Before starting, please read the <strong>AirBnB</strong> concept page.</p>

<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>

<p>This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration&hellip; </p>

<p>Each task is linked and will help you to:</p>

<ul>
<li>put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>&hellip;) that inherit from <code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage. </li>
<li>create all unittests to validate all our classes and storage engine</li>
</ul>

<h3>What&rsquo;s a command interpreter?</h3>

<p>Do you remember the Shell? It&rsquo;s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc&hellip;</li>
<li>Do operations on objects (count, compute stats, etc&hellip;)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>

<h2>More Info</h2>

<h3>Execution</h3>

<p>Your shell should work like this in interactive mode:</p>

<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>

<p>But also in non-interactive mode: (like the Shell project in C)</p>

<pre><code>$ echo &quot;help&quot; | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>

