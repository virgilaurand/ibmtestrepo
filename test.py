In this video we will discuss Application
Programming Interfaces, or APIs. Specifically, we will discuss: What an API is, API Libraries,
REST APIs, including: Request and Response. An API lets two pieces
of software talk to each other. For example you have your program, you have some data,
you have other software components. You use the API to communicate with the other software
components.You don’t have to know how the API works, you just need to know its inputs
and outputs. Remember, the API only refers to the interface, or the part of the library
that you see. The “library” refers to the whole thing. Consider the pandas library.
Pandas is actually a set of software components, many of which are not even written in Python.
You have some data. You have a set of software components.
We use the pandas API to process the data by communicating with the other software components.
There can be a single software component at the back end, but there can be a separate
API for different languages. Consider TensorFlow, written in C++.
There are separate APIs in Python, JavaScript, C++
Java, and Go. The API is simply the interface. There are also multiple volunteer-developed
APIs for TensorFlow; for example Julia, MATLAB, R, Scala, and many more. REST APIs are another
popular type of API. They enable you to communicate using the internet, taking advantage of storage,
greater data access, artificial intelligence algorithms,
and many other resources. The RE stands for “Representational,” the S stands for “State,”
the T stand for “Transfer.” In rest APIs, your program is called the “client.” The
API communicates with a web service that you call through the internet. A set of rules
governs Communication, Input or Request, and Output or Response. Here are some common API-related
terms. You or your code can be thought of as a client. The web service is referred to
as a resource. The client finds the service through an endpoint. The client sends the
request to the resource and the response to the client. HTTP methods are a way of transmitting
data over the internet We tell the REST APIs what to do by sending a request. The request
is usually communicated through an HTTP message. The HTTP message usually contains a JSON file,
which contains instructions for the operation that we would like the service to perform.
This operation is transmitted to the web service over the internet. The service performs the
operation. Similarly, the web service returns a response through an HTTP message, where
the information is usually returned using a JSON file.
This information is transmitted back to the client.
The Watson Speech to Text API is an example of a REST API. This API converts speech to
text. In the API call, you send a copy of the audio file to the API; this process is
called a post request. The API then sends the text transcription of what the individual
is saying. The API is making a get request. The Watson Language-Translator API provides
another example. You send the text you would like to translate into the API, the API translates
the text and sends the translation back to you. In this case we translate English to
Spanish. In this video, we’ve discussed what an API is, API Libraries, REST APIs,
including Request and Response. Thank you for watching this video.