# List Azure DevOps Account IDs

Quickly find the Azure DevOps account IDs (a.k.a. hostId) using this Python snippet.

## Why do I need the account ID?

To specify the issuer of Azure DevOps OIDC tokens: `https://vstoken.dev.azure.com/<accountId>`.

## Can't I find the account ID on the UI?

Nope :-(

## Run

1. Configure your Azure credentials

```bash
az login
```

2. Run the snippet

```bash
make run
```