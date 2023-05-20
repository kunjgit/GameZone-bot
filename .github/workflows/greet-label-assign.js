const { Octokit } = require("@octokit/rest");

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
});

const issueNumber = process.env.GITHUB_EVENT.issue.number.toString();
const commentBody = "Hello there, thanks for creating this issue!";

octokit.issues.createComment({
  owner: process.env.GITHUB_REPOSITORY_OWNER,
  repo: process.env.GITHUB_REPOSITORY,
  issue_number: issueNumber,
  body: commentBody,
});
