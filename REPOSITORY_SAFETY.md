# Repository Safety Policy

## Absolute Rule: Do Not Delete Git Repositories

Deleting a Git repository is forbidden. This applies to every human, automated
agent, script, cleanup task, migration, and synchronization process working in
or around this repository.

The prohibition includes:

- Do not delete a local repository directory.
- Do not delete or replace a repository's `.git` directory.
- Do not delete a remote GitHub repository.
- Do not re-clone over an existing repository.
- Do not use destructive cleanup commands such as `rm -rf`, `git clean -fdx`,
  or `git reset --hard` against a repository or a directory that may contain
  repositories.
- Do not remove a worktree, clone, branch, tag, remote, or Git history as a
  substitute for investigating a synchronization or organization problem.

No current instruction authorizes repository deletion. A future instruction
must explicitly revoke this policy and identify the exact repository and
operation. Ambiguous requests such as "clean up," "start over," "remove the old
copy," or "fix the repo" do not authorize deletion.

## Required Recovery-First Procedure

When an agent finds a duplicate, stale, damaged, disconnected, or misplaced
repository:

1. Stop before deleting, replacing, or moving anything.
2. Record the absolute path, current branch, remotes, status, and latest commit.
3. Preserve all uncommitted and untracked files.
4. Compare local and remote history without destructive commands.
5. Report the condition and propose a non-destructive repair.
6. Ask for explicit, path-specific approval before any cleanup that could remove
   data, metadata, history, branches, tags, remotes, clones, or worktrees.

When uncertain whether a directory is or contains a Git repository, treat it as
a repository and preserve it.

## Open Safety Incidents

Last checked: 2026-07-25

- GitHub Support ticket `4592214` remains open for repeated repository
  deletions and restoration. The support update and deleted-repositories page
  are unresolved handoffs; no repository was deleted, restored, replaced, or
  re-cloned during the email-review pass.
- GitHub reported that a personal access token found in a commit was revoked.
  The token value must never be copied into this repository. Identify the
  affected repository, audit history and dependent integrations for remaining
  exposure, and rotate only the integrations that actually depended on it.
- Until the incident is resolved, every automation and agent must treat Git
  cleanup, repository removal, remote deletion, `.git` replacement, and
  re-cloning over an existing path as forbidden.
