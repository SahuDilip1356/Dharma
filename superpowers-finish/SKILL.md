---
name: superpowers-finish
description: |
  Complete a development branch — verify tests, present merge/PR/keep/discard options, execute
  the choice, and clean up the worktree. Triggers when:
  - All tasks in a plan are complete and verified
  - User says "ship it", "finish the branch", "merge", "create a PR", "done with this feature"
  - superpowers-execute reports all tasks complete
  - Ready to close out a development session

  Never skip test verification before presenting options.
  Always present exactly 4 options — no variations.
  This is Phase 6 of the Superpowers methodology.
license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/superpowers
  version: "1.0.0"
---

# Superpowers: Finish Development Branch

**Purpose:** Close out a feature branch correctly — tests verified, options presented, clean commit history, worktree cleaned up.

---

## Step 1: Verify Tests (Non-Negotiable)

Run the full test suite before anything else.

```
Command: [project test command]
```

If tests fail: **Stop.** Do not present completion options. Fix the failures first (`superpowers-debug`). Return here after they pass.

Report:
```
Test suite: [N] passed, [M] failed
Status: [PASS / FAIL — must be PASS to continue]
```

---

## Step 2: Identify the Base Branch

```bash
git log --oneline --decorate | head -20
```

Identify which branch (typically `main` or `master`) this work branched from.

---

## Step 3: Present 4 Options (Exactly These, No Variations)

Present this to the user without additional explanation:

---
**Development complete. Tests passing. Choose how to proceed:**

1. **Merge to `[base-branch]` locally** — merge this branch into [base] on your machine
2. **Push and create a Pull Request** — push to remote and open a PR for review
3. **Keep the branch as-is** — save work without merging (continue later)
4. **Discard this work** — delete the branch and remove the worktree

Reply with 1, 2, 3, or 4.

---

Wait for the user's choice before doing anything.

---

## Step 4: Execute the Chosen Option

### Option 1: Merge Locally
```bash
git checkout [base-branch]
git merge --no-ff [feature-branch] -m "feat: [feature description]"
git log --oneline -3
```
Verify: the merge commit appears in the log.

### Option 2: Push and Create PR
```bash
git push -u origin [feature-branch]
gh pr create --title "[feature title]" --body "[summary of changes]" --base [base-branch]
```
Report: the PR URL.

### Option 3: Keep As-Is
No git commands. Confirm: "Branch preserved at `[branch-name]`. Worktree kept intact."

### Option 4: Discard
**Require typed confirmation before proceeding:**
> "To confirm: type 'discard' to permanently delete this work."

If confirmed:
```bash
git checkout [base-branch]
git branch -D [feature-branch]
```

---

## Step 5: Clean Up Worktree

Only for Options 1, 2, and 4 (NOT Option 3):

```bash
# Check if currently in a worktree
git worktree list

# If in a worktree, remove it
git worktree remove [worktree-path]
```

Confirm: worktree removed.

---

## After Completion

Prompt the user:
> "Branch complete. Run `/memory-sync` to capture this session's decisions and learnings."

If a significant architectural or product decision was made during this branch, remind the user to log it in `memory/decisions.md`.
