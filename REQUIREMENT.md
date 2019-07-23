# RESTful API Introduction

#### Core

### Introduction

Last project, you discovered about basic web server. That is the first step to become a Full-stack Developer.

In this project, your will learn about **RESTful API principle** and how to design a API follow RESTful API principle with **CRUD operations**.

Besides that, you will understand about what is **HTTP protocol** and how to send and receive data via internet with HTTP protocol.

Enjoy it.

### RESTful API

Before start, many developers **misunderstood** about RESTful API. So, you should careful when learn about RESTful API.

Let start:

### 1. Learn REST, learn RESTful API

You will see that it is not easy to understand what is RESTful API and what is difference between REST API and RESTful API. Don’t so worry, you SHOULD master principle first. It always the key to successful.

But principle is not enough, many related knowledges you should master when you learn principle. They are: **HTTP Protocol, HTTP Request, HTTP Method, HTTP Header and HTTP Status Codes**.

After you are confident with RESTful API principle, you can move to next step.

### 2. Design the first RESTful API

This is the time to prove that you are master of RESTful API principle. In this step, you should try to design a simple RESTful API by yourself first to prove knowledge without any reference because when you had learned principle, you had seen many examples.

When you finish, ask your classmates about your design, compare with some Google results. You will see that your design is good enough or not. (Tip: ensure that you referred to this link during learning)

This time is to enhance your simple RESTful API:  design of all major elements you would need for business applications

- CRUD
- pagination & associated metadata
- sorting
- filtering
- bulk operations
- concurrency control
- error handling

...

When you design an API, you should consider:

- What **headers** need to set?
- What kind of response content type (json, xml, pdf, html, text …)

The best toot for API Design I can recommend: **Swagger**

Finally, you have already your first RESTful API design.



### API Web Services

Now, this time is practices. You will understand RESTful API fully only when you practice frequently. You can use 2 most popular tools: cURL and Postman. You should use both of them to understand how you send and receive data.

First of all, you would to have your API Web Services. You can use **Django framework** to implement your web services based on your design, or use **Flask framework** for simpler.

**Important note:** this project not focus to how many features you created. This focus to **how you understand about RESTful API principle.**

It means that you will have to implement a web services step by step as below:

1. Create a simple web services
2. Configure API route
3. Coding simple CRUD operation API with features: pagination, sorting, filtering and error handling.
4. Deploy your API web services to local
5. Test them with cURL and Postman

Again remind, **don’t focus how to get data and return them** in your API web services. You can return exist data (hard code data) for test.

When you finish, you will confident to do your mission.



### Your mission

Write a Python Application to work with one of API Web Services below:

- Gmail API
- Google Calendar API
- Youtube Data API
- Google Drive API
- Oxford Dictionary API
- Twitter API
- OMDb API
- Slack API

**Acceptance Criteria**

1. Able to choose API, set corresponding parameters (header, parameters/body) without changing source code
2. Able to add new API without changing source code
3. Able to store response data in a file, and file type corresponding with response content type (html, xml, pdf, json, text)
4. Able to store error log when it returned client/server errors.



### REFERENCE

1. **RESTful API principle:** https://restfulapi.net/

2. **RESTful API Design:** https://hackernoon.com/restful-api-design-step-by-step-guide-2f2c9f9fcdbf

3. **Swagger:** https://swagger.io/

4. **cURL:** https://curl.haxx.se/

5. **Postman:** https://www.getpostman.com/

6. **Gmail API:** https://developers.google.com/gmail/api/v1/reference/

7. **Google Calendar API:** https://developers.google.com/calendar/v3/reference/?hl=en_US

8. **Youtube Data API:** https://developers.google.com/youtube/v3/docs/

9. **Google Drive API:** https://developers.google.com/drive/api/v3/reference/

10. **Oxford Dictionary API:** https://developer.oxforddictionaries.com/documentation

11. **Twitter API:** https://developer.twitter.com/en/docs/api-reference-index

12. **OMDb API:** http://www.omdbapi.com/#usage

13. **Slack API:** https://api.slack.com/docs/conversations-api



### BONUS

You have your API Design and you have your API Web Services. And this is your bonus:

1. Simulate the API Web Services which you registered.
2. Create API Design using Swagger. The swagger design must able to test by running cURL.