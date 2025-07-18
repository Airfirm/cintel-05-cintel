# cintel-05-cintel

Your app.py or dashboard/app.py file should have the following sections:

imports (at the top), e.g., shiny, random, datetime
define a reactive calc to fake new data points
define the Shiny Core app_ui
The overall page options
A sidebar
The main section with ui cards, value boxes, and space for grids and charts
Your app should have similar functionality to this basic example before you begin: 

Basic App: https://github.com/denisecase/cintel-05-cintel-basicLinks to an external site.
Once we have live data coming in, we need to want to create temporary storage to hold the "most recent" so we can present that - and analyze it online machine learning algorithms such as predicting a trend line using linear regression. We have a whole course on Streaming Data and another on Machine Learning, so you do NOT need to be able to implement those from scratch. Instead, we want to focus on your skills with presenting and displaying the information that might be available in an accessible and useful manner. 

I will provide an example that includes storing the readings in a deque (of dictionaries) and wrapping that deque in a reactive value as a way to manage our constantly changing state.

Your job is to:

implement the example provided and
propose and implement an enhancement, extension, or variation on the app. 
Options include:

Changing the theme, colors, visuals to be more engaging
Changing the layout to better show the current deque
Changing the chart to not flash on each update
Changing the subject domain from temperatures in Antarctica (so we can add it to our Penguin Dashboards) to an alternate focus using random data appropriate for your chosen domain. 
Integrating live data and continuous intelligence into your own previous interactive app
The goal is to understand the possibilities and challenges of working with live data and consider how you can analyze and present "data in motion" to enhance your analytics projects. 

Some exploration / implemented enhancement is necessary to be eligible for maximum credit. Novel exploration, well presented and explaned, is eligible for up to a 10% bonus. 

Before Beginning
Open the playground to the plotly example at: https://shinylive.io/py/examples/#plotly

Using the content stored in your GitHub project repo cintel-05-cintel.

Customize your requirements.txt
PyShiny Playground already includes all the packages listed below. Please do not add these packages to a requirements.txt running in the Playground - but include them in your requirements.txt that you would use for local development. 

faicons - for Font Awesome free Icons
pandas - for working with tabular data in Python
pyarrow - required by the new pandas
plotly - easy interactive charts
scipy - for the stats linear regression function to build a trend line for our chart
shiny - used to build our web app in Python
shinylive - used to build to our docs folder and host our app on GitHub Pages
shinywidgets - a wrapper for complex widgets like plotly charts
 

Implement the Continuous Intelligence App
Code is not written from the top down like a book. Code is written from the outside in. It is typically organized first - using comment blocks.

Functions are "stubbed in" - returning a basic answer first while getting things connected together. Code is slowly added in, and once connected, we generally fine tune and finish implementing each function - adding error handling, and making sure all the possible special cases are covered (e.g. don't attempt to plot if the Data Frame is empty). 

Start here:

https://github.com/denisecase/cintel-05-cintel-basicLinks to an external site.

Then, implement this slightly fancier version:

https://github.com/denisecase/cintel-05-cintel-fancyLinks to an external site.

Then, implement this version with a deque wrapped in a reactive value, showing the associated datagrid and a plotly chart with online machine learning. 

https://github.com/denisecase/cintel-05-cintelLinks to an external site.

Read the comments. Organize the code. When you get your version implemented, save it - use a good commit message to indicate you've recreated the functionality as requested. 

Then, review the app, and:

Propose a modification / enhancement / extension. 
Plan your work. 
Estimate the time it will take. 
Implement your plan. 
Estimating the time a feature will take is a difficult and valuable skill. 



CC5.1: Orient and Engage (Live Data & Continuous Intelligence)
We learned how to add user interaction and reactive content to static data sources using PyShiny.  We learned a bit of Python by working in the browser, and we briefly explored the process of moving development to our machine for offline work and/or working with confidential data sources and projects. 

In this module, we'll look at integrating live data streams and how "data in motion" is different from "data at rest". You'll see a lot of water analogies when working with modern analytics and data flows. Industry uses data lakes, data pipelines, data warehouses, and data lake houses. In this module, we'll introduce some of those terms, primarily so you can converse in the language of live data and look up information as needed.

Our focus in this course will stay with designing and implementing the user interaction associated with live data streams. To that end, we will introduce a new data structure (called a deque) and approaches for applying machine learning to data in motion so we can enable live, continuous intelligence.

We will work in the browser again while we learn these new aspects.  We will again use a GitHub repo simply to store our code and use README.md files to record notes related to the project. Experienced analysts (e.g. those who have had 44-608 previously) are encouraged to use the local development workflow and publish their apps using GitHub Pages or Shinylive.io (it's good practice) - but it is not required. 

Plan Your Week
Each 7 week course is equivalent to 2 weeks of a typical M-W-F graduate-level course. Expect to invest about 5 hours of "in-class" time, plus 2-3 per contact hour for about 20 hours per week - each course is a half time load. Late penalties may be small (except for Module 7 when no late work is accepted, regardless of reason), but for optimum learning, use the weekend to work ahead and get on track for the rest of the course. 

ACT: We start each week with actions. Like working through this introduction and participating. 
EXPLORE: Take the interactive skill drills as often as you like to learn some key concepts and skills. 
APPLY: Apply your skills in a project. Collaborate and share your work with others and review other submissions. 
 

Action 1: Review Key Terms and Concepts
Review these key terms. Once you've heard of them, you can use your favorite AI or other resources to learn more. 

Data at Rest vs. Data in Motion: Data at rest is stationary, stored data, unchanged until it is accessed or modified. In contrast, data in motion is actively transferring, such as streaming data from IoT devices. Data in motion requires different management, processing, and insight derivation approaches.

Traditional Methods vs. Live Data: Traditional data analysis often relies on batch processing, suited for data at rest. However, live data's continuous and rapid nature requires real-time processing methods, making traditional batch processing ineffective for timely insights and actions.
Data Streams: These are sequences of data generated continuously by different data sources. Understanding data streams is crucial for real-time analytics and decision-making.

Continuous Intelligence (CI): This is the practice of using real-time analytics to process data in motion. CI enables immediate insights and actions based on live data, contrasting with batch processing used for data at rest.

Deque (Double-Ended Queue): A deque (pronounced "deck") is a data structure that allows insertion and removal of elements from both ends efficiently. In the context of live data, deques are useful for holding recent data points for quick analysis without the overhead of processing the entire stream. For example, a deque makes it easy to do analytics on the last, most recent 20 points. It enables continuously updated machine learning models reflecting the current trend. 

Data Lake: A storage repository that holds a vast amount of raw data in its native format. Data lakes are flexible and can store both structured and unstructured data.

Data Warehouse: A system used for reporting and data analysis, storing structured, filtered data that has already been processed for a specific purpose.

Data Pipeline: A set of data processing elements connected in series, where the output of one element is the input of the next. Data pipelines are essential for moving and transforming data in motion.

Data Lakehouse: A newer concept that combines elements of data lakes and data warehouses, offering the scalability and flexibility of lakes with the governance and performance of warehouses.

 

Action 2: Review Available Tools
At work, there are many popular tools that you might encounter that work well with live data and data streams. You should recognize these names and understand where and when they are useful. 

Apache Kafka: An open-source stream-processing software platform designed for handling real-time data feeds. Kafka is widely used for building real-time streaming data pipelines and applications. Example users include LinkedIn and Netflix. 

Apache Flink: An open-source framework and distributed processing engine for stateful computations over data streams. Flink is designed for high throughput and low latency. Example users include Uber,  energy companies, and Alibaba (particularly during their annual Singles' Day (11/11) global shopping festival, processing billions of events in real-time).

Spark Streaming: Part of Apache Spark, this tool enables scalable, high-throughput, fault-tolerant stream processing of live data streams. Example users include Netflix recommendations, Pinterest, eBay, and Amazon analytics. 

RabbitMQ: An open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). RabbitMQ facilitates the efficient handling of messages in a distributed system, making it ideal for scenarios where high-throughput and reliable message delivery are required for data streams. Example users include Instagram and Reddit. 
Python Libraries for Streaming: Libraries like Streamz, Faust, and Pulsar help work with streaming data in Python environments, integrating with common tools.

Streamz is a simple option that works with Pandas

Faust, built on Kafka, is scaleable and enables complex analysis

Pulsar is a distributed system for high-throughput publish/subscribe systems that includes distributed storage and is used by Splunk, Yahoo, and Overstock. 

Python Data Structure for Streaming:  We will use Python's collections.deque class to understand how you can manage recent data efficiently. We'll use the deque class in our project. 
 

Action 3: Create a GitHub Project Repo
Login to GitHub. Click Repositories. Create a new project repo named cintel-05-cintel with a default README.md and a default .gitignore for Python. 

Use the GitHub web interface to add a file named requirements.txt (exactly!) and click commit to save the file. In the most basic version of the Module 5 project, we may only need packages from the Python Standard Library - and those already included in the PyShiny Playground environment. If working in the browser, you likely won't need requirements.txt at all for this project. However, very few real applications do NOT need a requirements.txt file, so I'd say keep it around and use it as needed. If you work on the project locally (on your machine), you will need to requirements.txt and install various packages into your local project virtual environment. This is very common in real-world Python and great practice. 

Use the GitHub web interface to add a new empty file named app.py (exactly!)  and click commit to save the file. 

Verify your project repo has all 4 files:

README.md
.gitignore
requirements.txt
app.py (OR dashboard/app.py if working locally and deploying to GitHub pages - see more below).
If you decide to try the local development, you'll be able to deploy your live date site using GitHub Pages. To make it easy to build our app from a folder and export the app into the docs folder (for Pages), please move your app.py file into a folder. I named my folder "dashboard", so I have a dashboard/app.py file and no app.py in the root folder. This is a more common organization for Python projects. For help adding a folder in VS Code, ask your favorite AI, do a web search, or try this link: https://github.com/orgs/community/discussions/22534Links to an external site.

Aside: To create a file in a folder in GitHub, just name the file with the relative path - for example in GitHub, new File, name it 

dashboard/app.py
And it should work.  Try not to make changes on your machine and in GitHub at the same time - that can create "merge conflicts" which are best avoided. Only edit the repo from one place  at a time. 

Your code is safely stored in the cloud - you can copy from it (and improve it) as you work through this module and complete Project 5.  

Use the README.md to keep your notes as you work. 

Action 4: Learn More About One Topic
After reviewing the sections above, choose one of the topics on data in motion that are new to you or that you want to learn more about.  

Do a web search to find a video, article, or additional example OR 
Ask your favorite AI assistant. 
In your submission, provide:

A clickable link to your resource:
A concise summary of something useful you learned:
What did you need to do to make the information useful: 
Paste the conversation or a helpful excerpt from your resource (include your prompts):
