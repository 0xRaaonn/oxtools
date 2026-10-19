# GitHub User Search

Search GitHub users and view their public profiles through GitHub's API. The project is a React web app; it is useful for checking public GitHub accounts, not for searching identities across other social networks.

## Links

- Live app: <https://simonsmith.github.io/github-user-search/#/search>
- Source repository: <https://github.com/simonsmith/github-user-search>
- Upstream README: <https://github.com/simonsmith/github-user-search#readme>

## Install and run locally

The upstream project documents these steps. You need Git, Node.js, and Yarn installed first.

```bash
git clone https://github.com/simonsmith/github-user-search.git
cd github-user-search
yarn
yarnpkg run start
```

Then open <http://localhost:3001/github-user-search/> in a browser. Keep the trailing slash in the URL.

## Example

Open the [live app](https://simonsmith.github.io/github-user-search/#/search), search for a GitHub username such as `octocat`, and inspect the profile returned by GitHub. The app caches requests in session storage to reduce API calls. GitHub applies API rate limits; the upstream README describes using a personal access token for local runs if you need a higher limit.

## Notes

This app uses GitHub's API and shows information available from GitHub profiles. Treat profile details as leads and verify them against other reliable sources.
