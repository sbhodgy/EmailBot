<h1>Email Bot</h1>

#### Author:    Scott Hodgins
#### Email:     scottbrianhodgins@yahoo.ca

<h2>Description</h2>

A python codebase to generate automated responses for Google Gmail accounts

<h2>Google Gmail API Configuration</h2>

A precursor to using this code is the configuration of the Google Cloud console to interact with the Gmail API.  This needs to be completed for the Gmail account that will be accessed using this code.  The following link provides the general steps for creating a Google Cloud project, steps specific for this configuration are also included below.

[Develop on Google Workspace](https://developers.google.com/workspace/guides/get-started)

1. Complete Step 1: *Create a Google Cloud project*
2. Complete Step 2: *Enable the APIs you want to use*
    - For this configuration, enable the **Gmail API**
3. Complete Step 4: *Configure the OAuth consent screen*
4. Complete Step 5: *Create access credentials*
    - For this configuration, enable **OAuth client ID** credentials
    - Create as a **Desktop Application**

#### **Storing Credentials**

As part of step 5, the **OAuth 2.0 Client IDs** json file must be downloaded, renamed to *credentials.json* and saved in the root directory of this project.