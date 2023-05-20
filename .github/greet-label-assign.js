const { Octokit } = require('@octokit/rest');

async function run() {
  try {
    const octokit = new Octokit({
      auth: process.env.GITHUB_TOKEN
    });

    const greeting = 'Hello there, thanks for creating this issue!';
    const [owner, repo] = process.env.GITHUB_REPOSITORY.split('/');
    const issue_number = process.env.GITHUB_EVENT.issue.number;

    await octokit.issues.createComment({
      owner,
      repo,
      issue_number,
      body: greeting
    });

    const labelName = 'GSSoC23';
    const { data: issue } = await octokit.issues.get({
      owner,
      repo,
      issue_number
    });

    if (issue.body.includes(labelName)) {
      await octokit.issues.addLabels({
        owner,
        repo,
        issue_number,
        labels: [labelName]
      });
    }

    const { data: comments } = await octokit.issues.listComments({
      owner,
      repo,
      issue_number
    });

    const lastComment = comments[comments.length - 1];
    const assignCommand = '/assign';

    if (lastComment && lastComment.body.includes(assignCommand)) {
      await octokit.issues.addAssignees({
        owner,
        repo,
        issue_number,
        assignees: [process.env.GITHUB_ACTOR]
      });
    }
  } catch (error) {
    console.error(error);
    process.exit(1);
  }
}

run();
