# A trivial, contrived example of using Dagster to build a scikit-learn pipeline

## PURPOSE
Create a dagster example that is a little more complex than your typical
"hello world" examples, but not too complex that would overwhelm
someone new to workflow management or task orchestration libraries.  Yet,
it is an example that is practical enough where we are extracting data,
transforming data, and then providing an end result.  I personally find the 
examples in the official tutorial a bit overwhelming.  It took me several attempts of 
re-reading the tutorial to really "get" how dagster works.  Part of the reason is, 
it isn't readily apparent to me when I see boilerplate code inside dagster's
various different function decorators, if the boilderplate is mandatory or not or why
this boilerplate is needed.  It turns out that most of the boilerplate is not needed or 
is optional.  Also, a lot of the boilerplate is directly proportional to how much metadata
you want shown on dagit or stored in a database backend.  However, I think in most production 
use cases, a moderate amount of boilerplate probably can not be avoided.  Recently, they
have re-vamped the documentation and have added much needed scenario based examples.

### Getting Started
Clone this repo.  Then modify the [workspace.yaml](src/workspace.yaml) file and replace the path
to the python executable with the path to your python executable for the environment which has dagster
installed.  There is also a `workspace_docker.yaml` file that you can ignore if you're not using Docker.

Then create a `DAGSTER_HOME` environment variable.  A sensible location could be:<br>
`export DAGSTER_HOME=$HOME/.dagster` for Linux/Mac<br>
`set DAGSTER_HOME=%USERPROFILE%\.dagster` for Windows

Then save the `dagster.yaml` file into your `.dagster` folder per your `DAGSTER_HOME` location.  By default, when
you execute your pipeline, sqlite databases will be saved in the `.dagster` folder.  These 
sqlite databases will save your pipeline logs, runs, and event statuses.  You can also use a different
database such as Postgres or MySQL, instead of sqlite.  If you don't specify a `DAGSTER_HOME` environment variable,
then logs, runs, and event statuses will be saved in-memory, instead of the filesystem storage.
See [documentatiion](https://docs.dagster.io/deployment/dagster-instance) for information about default
dagster behavior and how to configure it.

### Development workflow
In dagster, you define tasks with [solids](src/solids/sklearn_solids.py).  Then you define dependencies between solids in a 
[pipeline](src/pipelines/sklearn_pipeline.py) definition.  Then you can group one or more pipelines in a 
[repository](src/repositories/sklearn_repository.py) definition.  With the [workspace.yaml](src/workspace.yaml) file, you can tie a 
repository to a specific Python executable.  You can schedule execution of your pipeline by creating a [schedule](src/schedules/sklearn_schedule.py) definition which you then refer to it in the [repository](src/repositories/sklearn_repository.py) definition (lines 12 through 14).  These are the most basic abstractions and features of dagster.  There are many more such as
sensors for event-based triggering, resources and modes, integration with jupyter notebooks, etc.

### Next Steps
- ~~Dockerize the application without Docker Compose - make use of Docker network and docker volume~~
- Dockerize using Docker Compose