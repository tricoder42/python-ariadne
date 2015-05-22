Writing scenarios
=================

Let's start with testing simple story -- user wants to log in:

  1. User come to login page
  2. They fill in the username and password and submit the form

Actions
-------

The most atomic part of stories are actions. In this case, each line is one
action:

  1. :py:class:`actions.Visit` -- go to page specified by URL
  2. :py:class:`actions.FillForm` -- fill in form and submit it

We can use predefined actions (see :doc:`Reference </reference/actions>`) and
initialize them with custom parameters:

.. code-block:: python

  from ariadne import actions

  visit_login = actions.Visit(url='/login')

  credentials = {
    'username': 'admin',
    'password': 'secret',
  }
  fill_credentials = actions.FillForm(data=credentials, submit='#btn-submit')


Stories
-------

Once we have ``actions`` defined, we can groups them into stories and specify
in which order these actions should be executed:

.. code-block:: python

  from ariadne import stories

  login_process = stories.Simple([
    visit_login,
    fill_credentials
  ])

:py:class:`stories.Simple` is just wrapper around set of actions, which
executes them serially one after another.

Scenarios
---------

The last step is to define scenarios. It usually consists of several stories,
but sometimes is scenario as simple as story itself. We can use simple shortcut
in such case:

.. code-block:: python

  user_login = login_process.as_scenario()

The main difference between scenario and stories is context. Each scenario
is executed with isolated context, while stories pass context from one to
another. In unittest scenario would be single test case.

Context and config
------------------

Now we are ready to run our scenario in browser.

We mentioned context in previous section. Context is basically a dictionary
of data which is passed through scenario and contains *persistent* object.
Web browser is example of such object -- we need to keep state of our browser
during whole scenario.

Context are constructed using *context preprocessors* at the beginning of
each scenario. *Context preprocessors* are simple functions which modify
context, eg. add key ``browser`` with instantiated web browser.

We use config to define used *context preprocessors*:

.. code-block:: python

  from ariadne.config import BaseConfig
  from ariadne.context import browsers

  class ExampleConfig(BaseConfig):
      def context_preprocessors(self):
          return [
              browsers.Splinter('firefox')
          ]

Let's run it already!
---------------------

Alright. Enough talk, let's fight. We have scenarios and basic configuration,
the last thing we need is a runner. In this case we can use very simple one:

.. code-block:: python

  from ariadne.runners import SimpleRunner


  runner = SimpleRunner(config=ExampleConfig)
  runner.add(user_login)

  if __name__ == '__main__':
      runner.run()

As simple as it could be, it only run one scenario and output results to stdout.

Try this file execute in Python, you should see following output:

.. code-block:: shell

  $ python example.py
  Scenario 1 of 1: login_process
  - visit http://localhost/login … OK
  - fill form … OK

That's it. You might have noticed that we haven't tested anything and you're
100% right. We've just opened browser and filled form. If we want to test
something, we need to write *checks*.
