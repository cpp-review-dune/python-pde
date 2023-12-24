# Markdown Files

For more about MyST, see [the MyST Markdown Overview](https://jupyterbook.org/content/myst.html).

Here is a "note" directive:

```{note}
note
```

Here is an inline directive to refer to a document: {doc}`markdown-notebooks`.

## Citations

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.

```{bibliography}
```
