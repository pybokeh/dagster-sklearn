# A trivial, contrived example of using Dagster to build a scikit-learn pipeline
## *UPDATED FOR 1.1.14, WORKING AS OF January 28, 2023*
Though not an ETL newbie, I'm making a basically cold start on data and workflow orchestration frameworks.  There's a lot of excitement around Dagster, but the documentation and scant tutorials alone aren't answering my questions.  This project was mentioned on Reddit as being a course in itself.  I appreciate that it tackles a problem beginning to end, but `solids` (ops) and `pipelines` (jobs) aren't part of the Dagster vernacular anymore, and a few other changes had popped up.  Updating this project and viewing how it uses the framework to address a problem has been immensely helpful in developing my understanding and confidence.  I hope it helps others.  More to come. . .
Oh, and instructions below were followed more or less as is.  Transition and execution done locally.  Docker not attempted or updated in any way.

## PURPOSE
Create a dagster example that is a little more complex than your typical
"hello world" examples, but not too complex that would overwhelm
someone new to workflow management or task orchestration libraries.  Yet,
it is an example that is practical enough where we are extracting data,
transforming data, and then providing an end result.  I personally found the 
examples in the official tutorial a bit overwhelming or hard to follow. 
It was not readily apparent to me how the pieces of the various dagster abstractions
come together due to not seeing all the example code structured in a cohesive manner or 
not being able to see see all the code in one place.  I think just seeing a portion of the 
code at a time in the examples make it difficult to follow or causes you to have to scroll up or down to see the rest of the code.

### Getting Started
With this repo, you can run the example with Docker or without.  Clone this repo.  Then modify the [workspace.yaml](src/workspace.yaml) file and replace the path to the python executable with the path to your python executable for the environment which has dagster installed.  There is also a `workspace_docker.yaml` file that you can use if using Docker.  Otherwise, you can ignore it.

Then create a `DAGSTER_HOME` environment variable.  A sensible location could be:<br>
`export DAGSTER_HOME=$HOME/.dagster` for Linux/Mac<br>
`set DAGSTER_HOME=%USERPROFILE%\.dagster` for Windows

Then save the `dagster.yaml` file into your `.dagster` folder per your `DAGSTER_HOME` location.  By default, when
you execute your job, sqlite databases will be saved in the `.dagster` folder.  These 
sqlite databases will save your job logs, runs, and event statuses.  You can also use a different
database such as Postgres or MySQL, instead of sqlite.  If you don't specify a `DAGSTER_HOME` environment variable,
then logs, runs, and event statuses will be saved in-memory, instead of the filesystem storage.
See [documentation](https://docs.dagster.io/deployment/dagster-instance) for information about default
dagster behavior and how to configure it.

### Development workflow
In dagster, you define tasks with [ops](src/ops/sklearn_ops.py).  Then you define dependencies between ops in a 
[job](src/jobs/sklearn_job.py) definition.  Then you can group one or more jobs in a 
[repository](src/repositories/sklearn_repository.py) definition.  With the [workspace.yaml](src/workspace.yaml) file, you can tie a 
repository to a specific Python executable.  You can schedule execution of your job by creating a [schedule](src/schedules/sklearn_schedule.py) definition which you then refer to it in the [repository](src/repositories/sklearn_repository.py) definition (lines 12 through 14).  These are the most basic abstractions and features of dagster.  There are many more such as
sensors for event-based triggering, resources and modes, integration with jupyter notebooks, etc.

### Code Organization
For me at least, it makes sense to place ops, jobs, schedules, and respositories in 
their own folder for better code organization.  Then we can just import them accordingly.  Then
place the workspace.yaml at the top level above them where you would call the `dagit` command.

Folder tree:

src<br>
├── jobs<br>
│       └── sklearn_job.py<br>
├── repositories<br>
│       └── sklearn_repository.py<br>
├── schedules<br>
│       └── sklearn_schedule.py<br>
├── ops<br>
│       └── sklearn_ops.py<br>
├── workspace_docker.yaml<br>
└── workspace.yaml<br>

### Next Steps
- ~~Dockerize the application without Docker Compose - make use of Docker network and Docker volume~~
- ~~Dockerize using Docker Compose~~