# Introduction to DevOps — Notes

## Key Takeaways
- DevOps emphasizes building a culture of shared responsibility, transparency, and embracing failure as a learning opportunity.
- Continuous Integration and Continuous Delivery (CI/CD), Infrastructure as Code, Test Driven Development (TDD), and Behavior Driven Development (BDD) are essential practices for faster, higher-quality software delivery.
- Breaking down silos by organizing developers and operators into cross-functional teams is crucial for successful DevOps adoption.
- Everyone in the team contributes and shares responsibility for the success of the software product.
- Cloud native architecture supports independently deployable microservices that scale horizontally and improve system resilience.
- Designing for failure means accepting that failures will happen and focusing on quick recovery to maintain service reliability.

---
  
## Notes
- DevOps is a cultural change that requires trust, transparency, and discipline across teams.
- In 2009, Patrick Debois coined the term “development operations.” He said, “Development operations is an extension of Agile development environments that aims to enhance the process of software delivery as a whole.” It is an extension of Agile.
- Building a culture of shared responsibility, transparency, and faster feedback is the foundation of every high-performing DevOps team.
- Applications evolved from Waterfall development of monoliths to Agile development of microservices.
- DevOps has three dimensions: culture, method, and tools.
- The essential characteristics of DevOps include cultural change, automated pipelines, infrastructure as code, microservices, containers, and immutable infrastructure.
- Waterfall Method: 
  - Requirement -> Design -> Code -> Integration -> Test -> Deploy (if there's a problem, it's hard to go back)
  - Architects worked for months designing the system -> Devs worked for months on feature (if they had to go back to architects because design was wrong, it was very expensive) -> Testing opened defects and sent the code back to dev -> at some point, code is released to ops -> Ops team took forever to deploy 
- Problems with Waterfall approach:
  - No provisions for changing requirements
  - No idea if it works until the end
  - Each step ends when the next begins
  - Mistakes found later stages are more expensive to fix
  - Usually a long time between software releases
  - Teams work separately, unaware of their impact on each other
  - People who know the least about the code are deploying it into production
- Extreme Programming (XP):
  - Based on an interactive approach to software development
  - Intended to improve software quality and responsiveness to changing customer requirements.
  - One of the first Agile methods
- Don't be afraid to have multiple repos, you want 1 componenet or microservice per repo.
- Create a new branch for every issue that you're working on.
- Lean Manufacturing
  - Working in small batches allows for faster feedback
  - Allows you to experiment more, in order to quickly gain insights.
  - Minimizes waste, don't waste time developing stuff your customer doesn't like.
- Optimally a feature should be small enough to be completed in a week or less. The features you build are one step toward a goal.
- Measuring the size of batches: (how to know if they are small enough)
  - Feature size supports frequent releases
  - Features should be completed in a sprint
  - Features are a step toward a goal, so keep them small
- Minimum Viable Product (MVP)
  - Is an experiment to test your value hypothesis and learn
  - Not phase 1 of a project
  - MVP is focused on learning, not delivery
  - At the end of each MVP, decide whether to pivot or persevere
  - A tool for learning
  - Failure leads to understanding
  - What did you learn from it?
  - What will you do differently?
- Test Driven Development (TDD)
  - You want to write the tests for the code you want to make.
- Basic TDD Workflow:
  1. Write a test case that fails. (RED)
  2. Write just enough code to make it pass. (GREEN)
  3. Refactor code to improve code quality. (REFACTOR)
  - This is known as Red, Green, Refactor.
- Why is TDD important to DevOps?
  - It saves time when developing
  - You can code faster and with more confidence
  - Ensures the code is working as expected
  - Ensures that future changes don't break your code
  - In order to create a DevOps CI/CD pipeline, all testing must be automated
- Behavior Driven Development (BDD)
  - As its name implies, focuses on the behavior of the system as observed from the outside in.
  - Great for integration testing
  - Uses a syntax both developers and stakeholders can easily understand
- TDD is ensuring that you are building the "thing right".
- BDD is ensuring that you are building the "right thing".
- Basic BDD Workflow:
  - Explore problem domain and describe the behavior
  - Document the behavior using Gherkin syntax
  - Use BDD tools to run those scenarios
  - One document that's both the specification and test for software
- Gherkin
  - An easy to read natural language syntax
  - Given.. When.. Then...
  - Understandable by everyone
- How Gherkin is used:
  - Given (some context)
  - When (some event happens)
  - Then (some testable outcome)
  - And (more context, events, or outcomes)
- Gherkin Syntax Example:
```
Feature: Returns go to stock

As a store owner
i need to add items back to stock when they're returned
so that I can keep track of my stock on hand

Scenario 1: Refunded items should be returned to stock
Given that a customer previously bought a black sweater from me
And I have 3 black sweaters in stock
When they return the black sweater for a refund
Then I should have 4 black sweaters in stock
```
- Since failure is inevitable, you must build your software to be resistant to failure and scale horizontally.
  - Embrace failures - they will happen!
  - How to avoid -> How to identify and what to do about it
  - Operational Concern -> developer concern
  - Plan to be throttled
  - Plan to retry (with exponential backoff)
  - Degrade gracefully
  - Cache when appropriate
- Retry pattern enables an application to handle transient failures when it tries to connect to a service or a network resource, by transparently retrying and failing the operation.
- The circuit breaker pattern is similar to the electrical circuit breakers in your home.
- Circuit breaker pattern is used to identify a problem and then do something about it to avoid cascading failures.
- The bulkhead pattern can be used to isolate failing services to limit the scope of a failure.
- Finally, there is chaos engineering, otherwise known as monkey testing.
