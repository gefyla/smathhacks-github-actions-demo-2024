
# GitHub Actions & CI/CD Pipelines Demo

Repository for showing what GitHub Actions can do.

March 3, 2024 @ SmathHacks  

By: Geoffrey Fylak

## CI/CD Badges

[![Lint](https://github.com/gefyla/smathhacks-github-actions-demo-2024/actions/workflows/lint.yaml/badge.svg?branch-main)](https://github.com/gefyla/smathhacks-github-actions-demo-2024/actions/workflows/lint.yaml)

[![Test](https://github.com/gefyla/smathhacks-github-actions-demo-2024/actions/workflows/test.yaml/badge.svg?branch-main)](https://github.com/gefyla/smathhacks-github-actions-demo-2024/actions/workflows/test.yaml)

## Workflows

### Github Actions Demo Workflows

A workflow that I found on GitHub's website and it seemed like a pretty good starting point 🤷‍♂️

### Input Output Workflow

A side piece to show how GitHub Actions can:
- have manual triggers
- accept user input
- produce output
- output colorful logs
- read secrets from the repository

#### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|     INPUT      |  TYPE   | REQUIRED | DEFAULT |             DESCRIPTION             |
|----------------|---------|----------|---------|-------------------------------------|
|      name      | string  |   true   |         |             Your name.              |
| secret-message | boolean |  false   | `false` | I wonder what enabling this does... |

<!-- AUTO-DOC-INPUT:END -->

#### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

|      OUTPUT      |           DESCRIPTION           |
|------------------|---------------------------------|
| name-char-length | Character length of name input. |

<!-- AUTO-DOC-OUTPUT:END -->

### Lint Workflow

A workflow that makes sure the code is clean by running:
- pylint
- flake8
- doctoc
- actionlint
- markdownlint

### Test Workflow

A workflow that makes sure tests continue passing so that the code base does not regress.

## More Resources

- [Pre-commit](https://pre-commit.com)
- [GitHub Markdown Emojis](https://gist.github.com/rxaviers/7360908)
- [Colorized Bash Echo](https://gist.github.com/stevewithington/b1b620b5bc9252e2c32e2cad35efbf83)
- [auto-doc](https://github.com/tj-actions/auto-doc)


## Connect

Feel free to connect and reach out to me on [LinkedIn](www.linkedin.com/in/geoffrey-fylak-01885b156)!
