Productivity Sprint Setup
Tool versions
The following versions were verified in the Linux setup workspace on 2026-11-13. Record the versions from the machine used for the timed runs if they differ.
Tool	Version	Verification
Visual Studio Code (x64)	1.146.0	code --version
GitHub Copilot (bundled extension)	0.74.0	VS Code reported GitHub.copilot-chat as already installed
Git	2.52.0	git --version


Setup steps
1. Install Visual Studio Code from the official download page and open the holbertonschool-ai4devs repository in the editor.
2. Open Extensions and search for @id:GitHub.copilot-chat. Confirm the GitHub-published extension is enabled, and install it if your VS Code version does not bundle it. Use the extension details page to check the version of a bundled extension.
3. Select Use AI Features from the Copilot icon in the status bar and sign in with a GitHub account that has Copilot access. If Chat: Disable AI Features is enabled in Settings, turn it off.
4. Open Copilot Chat and send Reply with exactly SETUP_OK. A reply of SETUP_OK confirms that Copilot can answer in the editor.
Sprint configuration
- Manual run: Enable Chat: Disable AI Features (chat.disableAIFeatures) and verify that Copilot Chat and inline suggestions are unavailable. Complete the run without using another AI assistant.
- AI-assisted run: Turn off the same setting and confirm Copilot Chat responds. Use the same IDE and testing tools for both runs.
Verification status. VS Code was installed from the official Microsoft Linux package. The bundled Copilot extension version was verified, and the isolated VS Code settings allow AI features. GitHub sign-in and the chat test are pending on the machine used for the sprint.
