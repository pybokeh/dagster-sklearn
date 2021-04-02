# A trivial, contrived example of using Dagster to build a scikit-learn pipeline

## PURPOSE
Create a dagster example that is a little more complex than your typical
"hello world" examples, but not too complex that would overwhelm
someone new to workflow management or task orchestration libraries.  Yet,
it is an example that is practical enough where we are extracting data,
transforming data, and then providing an end result.

### Getting Started
Clone this repo.  Then modify the [workspace.yaml](src/workspace.yaml) file and replace the path
to the python executable with the path to your python executable for the environment which has dagster
installed.

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