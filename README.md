<h1>Sending Service</h1>

<h2>Required Libraries for Launch</h2>

<pre><code>pip install fastapi
pip install apscheduler
pip install requests
pip install sqlalchemy
</code></pre>

<h2>Command for Launch</h2>

<pre><code>uvicorn main:app --reload
</code></pre>

<h2>Token</h2>

<p>In the <code>sending_service.py</code>code> file, replace the  <code>token = </code>  with your own token for the mailing service. Please do not hardcode to save token. Use environment variables. </p>

<h2>Documentation</h2>

<p>For local access: <a href="http://127.0.0.1:8000/docs#/">http://127.0.0.1:8000/docs#/</a></p>

<h3>Commands</h3>

<p>For local access: <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> or your server.</p>
<p>Hereafter, the specified address will be denoted by a dot for conciseness.</p>

<h4>POST Requests</h4>

<p>Adding a client to the database:</p>

<pre><code>./client/
</code></pre>

<p>Creating a mailing:</p>

<pre><code>./mailing
</code></pre>

<h4>GET Requests</h4>

<p>Get a mailing by ID:</p>

<pre><code>./mailing/{mailing_id}
</code></pre>

<p>Get all messages by mailing ID:</p>

<pre><code>./message/{mailing_id}
</code></pre>

<h4>DELETE Requests</h4>

<p>Delete a client from the database:</p>

<pre><code>./client/{client_id}
</code></pre>

<p>Delete a mailing:</p>

<pre><code>./mailing/{mailing_id}
</code></pre>

<h4>PATCH Requests</h4>

<p>Update any client data:</p>

<pre><code>./client/{client_id}
</code></pre>

<p>Update mailing attributes:</p>

<pre><code>./mailing/{mailing_id}
</code></pre>

<h3>Additional Tasks</h3>

<p>Task 5 (documentation with Swagger UI).</p>
