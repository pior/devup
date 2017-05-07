# DevUp

Command to locally manage your development projects on Github.

> ~ $ de clone devup
> Cloning github.com/pior/devup to ~/src/github.com/pior/devup
> Changing directory to ~/src/github.com/pior/devup
>
> ~/src/github.com/pior/devup $ de up
> * Installing requirements
>
> ~/src/github.com/pior/devup $ de test
> -> py.test devup
> ...
>
> $ de cd kubernetes/charts
> Changing directory to ~/src/github.com/kubernetes/charts
> ...

Commands:

:`de clone`: Clone your project
:`de cd`: Go to your already cloned project
:`de init`: Create `devup.yml`
:`de test`: Run your test suite
:`de lint`: Run your linter
:`de setup`: Create your local devel environment (like creating the DB)
:`de ci`: Run the CI test suite
:`de customcommand`: Run a custom command defined by the project
