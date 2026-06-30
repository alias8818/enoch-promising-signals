# Real-agent evidence-ledger replay under forced restart

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `real-agent-evidence-ledger-replay-under-forced-restart-58dae06556`
Run ID: `real-agent-evidence-ledger-replay-under-forced-restart-58dae06556-20260604T042405598038+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real local-agent evidence ledger with nondeterministic tools: enoch://control-plane/projects/real-local-agent-evidence-ledger-with-nondeterministic-too-5629f0c008/runs/real-local-agent-evidence-ledger-with-nondeterministic-too-5629f0c008-20260604T003530948280+0000
- Parent run decision: Persistent real-tool evidence ledger replay after agent restart: enoch://control-plane/projects/persistent-real-tool-evidence-ledger-replay-after-agent-re-e7cf00ba94/runs/persistent-real-tool-evidence-ledger-replay-after-agent-re-e7cf00ba94-20260604T022701707122+0000

## What looked useful

Across 540 forced-restart trials, all modes reached correct final digests. Ledger trials had 0.0 mean redundant operations versus 12.667 for a fair checkpoint snapshot baseline and 130.0 for no-state restart, but ledger mean elapsed time was slower at 0.489 s versus checkpoint at 0.322 s.

## Boundaries and scale limits

The worker is synthetic and deterministic rather than a production LLM/tool agent; tasks are small/medium local file operations; ledger persistence uses per-operation fsync, which increased wall-clock time versus a fair coarse checkpoint snapshot baseline.

## Claim scope

In a bounded local forced-restart benchmark with deterministic file-operation subprocess agents, append-only evidence-ledger replay recovered exact final state after SIGKILL and eliminated redundant operations relative to coarse checkpoint and no-state baselines.

## Why it stopped

Mechanism support is clear under the local benchmark, but practical superiority is mixed because the ledger removes redundant work while increasing wall-clock time versus a fair checkpoint baseline; this is not paper-positive direct evidence for real agents.

## Recommended next action

Stop this run as no-paper useful systems evidence; next bounded test should evaluate batched/group-commit evidence ledgers inside an actual tool-agent loop to see whether zero-loss recovery can retain lower redundant work without the measured per-operation fsync overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Group-commit evidence ledger replay in a real tool-agent forced-restart loop
- Success threshold: At least 100 forced-restart real-agent trials with 100% final correctness for group-commit ledger, mean redundant tool work at least 80% lower than checkpoint, and mean wall-clock time no more than 10% slower than checkpoint.
- Stop condition: Stop if group-commit ledger loses replay correctness in any reproducible crash case or remains more than 25% slower than checkpoint after one bounded implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-replay-under-forced-restart-58dae06556`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
